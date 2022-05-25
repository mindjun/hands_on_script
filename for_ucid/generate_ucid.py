import pandas as pd

# data_source
# mer_id
# mer_name 商户号
# member_type
# unified_code 统一社会信用代码
# license_code 营业执照号
# tax_code 税号
# legal_cert_no_mask

class UCIDGenerator(object):
    def __init__(self, file_path):
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        self.file_path = file_path
        self.excel_data = None
        self.ucids = list()
        self.ucid_count = 0

    def data_from_xlsx(self):
        self.excel_data = pd.read_excel(self.file_path)
        # 将空的数据填充
        self.excel_data['unified_code'].fillna(-1, inplace=True)
        self.excel_data['license_code'].fillna(-2, inplace=True)
        self.excel_data['tax_code'].fillna(-3, inplace=True)
        result = pd.DataFrame()
        # 统一社会信用代码
        unified_code_groups = self.excel_data.groupby(by='unified_code')
        for unified_code in unified_code_groups:
            # 没有社会信用代码，根据营业执照进行判断
            if unified_code[0] == -1:
                result = self.contact_by_license_code(unified_code[1], result, True)
            # 社会信用代码不为空，使用营业执照进行判断
            else:
                result = self.contact_by_license_code(unified_code[1], result, False)
        result = result.replace(-1, '')
        result = result.replace(-2, '')
        result = result.replace(-3, '')
        return result

    def contact_by_license_code(self, unified_code_group, result, nan_flag):
        license_codes = unified_code_group.groupby(by='license_code')
        # 社会信用代码不是空，但是有多组的营业执照，冲突
        if nan_flag is False and len(license_codes) > 1:
            self.fill_ucid(unified_code_group, conflict=True)
            result = pd.concat([result, unified_code_group])
            return result
        # 社会信用代码是空，使用营业执照分组，再进行判断
        for license_code in license_codes:
            # 营业执照也为空，根据税号进行判断
            if license_code[0] == -2:
                result = self.contact_by_tax_code(license_code[1], result, True)
                continue
            # 营业执照不为空，使用税号进行判断
            else:
                result = self.contact_by_tax_code(license_code[1], result, False)
        return result

    def contact_by_tax_code(self, license_code, result, nan_flag):
        tax_codes = license_code.groupby(by='tax_code')
        if nan_flag is False:
            if len(tax_codes) > 1:
                self.fill_ucid(license_code, conflict=True)
                result = pd.concat([result, license_code])
                return result
            for tax_code in tax_codes:
                self.fill_ucid(tax_code[1], conflict=False)
                result = pd.concat([result, tax_code[1]])
            return result

        self.fill_ucid(license_code, conflict=False)
        result = pd.concat([result, license_code])
        return result

    def fill_ucid(self, df, conflict=False):
        if conflict is False:
            self.ucid_count += 1
        df['UCID'] = df['member_type'].transform(self.ucid_helper, conflict=conflict)

    def ucid_helper(self, member_type, conflict=False):
        if conflict:
            ucid = 'X'
            # self.ucid_count += 1
        else:
            ucid = '1'
        if member_type.startswith('个人'):
            ucid_str = ucid + '0000-' + str(self.ucid_count).zfill(10)
        else:
            ucid_str = ucid + '1000-' + str(self.ucid_count).zfill(10)
        return ucid_str

    def ucid_to_xlsx(self):
        self.excel_data['UCID'] = [str(i) + '_' for i in self.excel_data['mer_id']]
        self.excel_data.to_excel('./out.xlsx', index=False, header=True)

    def generate_ucid(self):
        result = self.data_from_xlsx()
        result.to_excel('./out.xlsx', index=False, header=True)


# 思路就是根据关键字去 groupby，如果是空的，那么就再根据下一个去 groupby，最后勇 transform 函数去填充 UCID

if __name__ == '__main__':
    ucid = UCIDGenerator('./test.xlsx')
    ucid.generate_ucid()
