import pandas as pd


# data_source
# mer_id
# mer_name 商户号
# member_type
# unified_code 统一社会信用代码
# license_code 营业执照号
# tax_code 税号
# legal_cert_no_mask

# groupby 之后的结果是一个生成器，需要遍历里面的结果

class UCIDGenerator(object):
    def __init__(self, file_path):
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        self.file_path = file_path
        self.excel_data = None
        self.ucids = list()
        self.ucid_count = 0
        self.result = pd.DataFrame()

    def data_from_xlsx(self):
        self.excel_data = pd.read_excel(self.file_path)
        # 将空的数据填充
        self.excel_data['unified_code'].fillna(-1, inplace=True)
        self.excel_data['license_code'].fillna(-2, inplace=True)
        self.excel_data['tax_code'].fillna(-3, inplace=True)
        # 统一社会信用代码
        unified_code_groups = self.excel_data.groupby(by='unified_code')
        for unified_code in unified_code_groups:
            if unified_code[0] == -1:
                # 社会信用代码为空   unified_code[1] 为参数
                self.unified_code_is_nan(unified_code[1])
            else:
                self.unified_code_is_not_nan(unified_code[1])
        # 将空值中的 -1，-2，-3 替换回来
        self.result = self.result.replace([-1, -2, -3], '')
        # 禁用科学计数法
        self.result['mer_id'] = self.result['mer_id'].astype('str')

    def unified_code_is_nan(self, unified_code):
        license_codes = unified_code.groupby(by='license_code')
        # 只有一组营业执照且为空
        if len(license_codes) == 1 and license_codes[0][0] == -2:
            self.contact_by_tax_code_nan(license_codes[0][1])
        # 有两组营业执照且一组为空
        elif len(license_codes) == 2 and -2 in [i[0] for i in license_codes]:
            concat_license_codes = pd.concat([license_codes[0][1], license_codes[1][1]])
            self.contact_by_tax_code(concat_license_codes)
        else:
            for license_code in license_codes:
                self.contact_by_tax_code(license_code[1])

    def unified_code_is_not_nan(self, unified_code):
        license_codes = unified_code.groupby(by='license_code')
        # 只有一组营业执照，根据税号来判断
        if len(license_codes) == 1:
            # self.contact_by_tax_code(license_codes[0][1])
            self.contact_by_tax_code([i for i in license_codes][0][1])
        # 有两组营业执照且一组为空
        elif len(license_codes) == 2 and -2 in [i[0] for i in license_codes]:
            license_code_groups = [i for i in license_codes]
            concat_license_codes = pd.concat([license_code_groups[0][1], license_code_groups[1][1]])
            self.contact_by_tax_code(concat_license_codes)
        # 每个信用代码有多组营业执照，全部冲突
        else:
            self.fill_ucid(unified_code)
            self.result = pd.concat([self.result, unified_code])

    def contact_by_tax_code(self, license_code):
        tax_codes = license_code.groupby(by='tax_code')
        if len(tax_codes) == 1:
            # 只有一组，不冲突
            self.fill_ucid(license_code)
            self.result = pd.concat([self.result, license_code])
        elif len(tax_codes) == 2 and -3 in [i[0] for i in tax_codes]:
            # 有两组，且有一组为空
            self.fill_ucid(license_code)
            self.result = pd.concat([self.result, license_code])
        else:
            # len(tax_codes) > 2 有多组，直接冲突
            self.fill_ucid(license_code, conflict=True)
            self.result = pd.concat([self.result, license_code])

    def contact_by_tax_code_nan(self, license_code):
        tax_codes = license_code.groupby(by='tax_code')
        if len(tax_codes) == 1:
            # 只有一组，不冲突
            self.fill_ucid(license_code)
            self.result = pd.concat([self.result, license_code])
        elif len(tax_codes) == 2 and -3 in [i[0] for i in tax_codes]:
            # 有两组，且有一组为空
            self.fill_ucid(license_code)
            self.result = pd.concat([self.result, license_code])
        else:
            # len(tax_codes) > 2:
            # 多组，不冲突，但是他们的编码不一样
            self.fill_ucid(license_code, increase_count=True)
            self.result = pd.concat([self.result, license_code])

    def fill_ucid(self, df, conflict=False, increase_count=False):
        if conflict is False:
            self.ucid_count += 1
        df['UCID'] = df['member_type'].transform(self.ucid_helper, conflict=conflict,
                                                 increase_count=increase_count)

    def ucid_helper(self, member_type, conflict=False, increase_count=False):
        ucid_prefix = 'X' if conflict else '1'
        member_type_str = '0000' if member_type.startswith('个人') else '1000'
        if increase_count:
            self.ucid_count += 1

        ucid_str = "{}{}-{}".format(ucid_prefix, member_type_str, str(self.ucid_count).zfill(10))
        return ucid_str

    def generate_ucid(self):
        self.data_from_xlsx()
        self.result.to_excel('./out.xlsx', index=False, header=True)


# 思路就是根据关键字去 groupby，如果是空的，那么就再根据下一个去 groupby，最后用 transform 函数去填充 UCID

if __name__ == '__main__':
    ucid = UCIDGenerator('./test.xlsx')
    ucid.generate_ucid()
