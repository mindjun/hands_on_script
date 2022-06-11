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
        self.excel_data['UCID'] = None
        self.excel_data = self.excel_data.fillna('')
        self.excel_data['member_type'] = self.excel_data['member_type'].map(lambda x: '个人' if x.startswith('个人') else '企业')
        groups = self.excel_data.groupby(by='member_type')
        company_df = groups.get_group('企业')
        # company_df['unified_code'] = company_df['unified_code'].map(lambda x: str(x))
        # company_df['license_code'] = company_df['license_code'].map(lambda x: str(x))
        # company_df['tax_code'] = company_df['tax_code'].map(lambda x: str(x))

        company_df['unified_code'] = company_df['unified_code'].astype('str')
        company_df['license_code'] = company_df['license_code'].astype('str')
        company_df['tax_code'] = company_df['tax_code'].astype('str')

        company_df['contact'] = company_df['unified_code'].str.cat([company_df['license_code'],
                                                                    company_df['tax_code']], sep='_')
        company_df.sort_values('contact', inplace=True)
        print(company_df)
        person_df = groups.get_group('个人')
        person_df.sort_values('legal_cert_no_mask', inplace=True)
        print(person_df)

    def contact_columns(self, member_type):
        if member_type == '个人':
            return ''

    def generate_ucid(self):
        result = self.data_from_xlsx()
        result.to_excel('./out.xlsx', index=False, header=True)


if __name__ == '__main__':
    ucid = UCIDGenerator('./test.xlsx')
    ucid.generate_ucid()
