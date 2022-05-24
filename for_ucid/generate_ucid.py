import pandas as pd

# data_source
# mer_id
# mer_name 商户号
# member_type
# unified_code 社会编码
# license_code 营业执照号
# tax_code 税号
# legal_cert_no_mask

class UCIDGenerator(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.excel_data = None
        self.ucids = list()

    def data_from_xlsx(self):
        self.excel_data = pd.read_excel(self.file_path)
        print(self.excel_data)

    def ucid_to_xlsx(self):
        self.excel_data['UCID'] = [str(i) + '_' for i in self.excel_data['mer_id']]
        self.excel_data.to_excel('./out.xlsx', index=False, header=True)

    def generate_ucid(self):
        self.data_from_xlsx()
        self.ucid_to_xlsx()


if __name__ == '__main__':
    ucid = UCIDGenerator('./test.xlsx')
    ucid.generate_ucid()
