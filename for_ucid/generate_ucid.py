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
        self.ids = [
            -1,  # formal company
            -1,  # formal person
            -1,  # tmp company
            -1,  # tmp person
        ]

    def get_id(self, mtype, is_formal):
        type_prefix = {
            '企业': '1',
            '个人': '0',
        }.get(mtype)

        level_prefix = '1' if is_formal else 'X'

        current = {
            '10': 0,
            '11': 1,
            'X0': 2,
            'X1': 3,
        }.get(f'{level_prefix}{type_prefix}')

        self.ids[current] += 1

        return "{level_prefix}{type_prefix}-{id}".format(
            level_prefix=level_prefix,
            type_prefix=type_prefix,
            id=str(self.ids[current]).zfill(10)
        )

    def data_from_xlsx(self):
        self.excel_data = pd.read_excel(self.file_path)
        # 将空的数据填充
        self.excel_data['UCID'] = None
        self.excel_data = self.excel_data.fillna('')
        self.excel_data['member_type'] = self.excel_data['member_type'].map(lambda x: '个人' if x.startswith('个人') else '企业')
        groups = self.excel_data.groupby(by='member_type')
        company_df = groups.get_group('企业')

        company_df['unified_code'] = company_df['unified_code'].astype('str')
        company_df['license_code'] = company_df['license_code'].astype('str')
        company_df['tax_code'] = company_df['tax_code'].astype('str')
        company_df['contact'] = company_df['unified_code'].str.cat([company_df['license_code'],
                                                                    company_df['tax_code']], sep='_')
        company_df.sort_values('contact', inplace=True)
        candidate_idx, license_code_set, tax_code_set = list(), set(), set()
        temp_unified_code, only_tax_code_prefix = None, None
        index = -1

        for name, row in company_df['contact'].iteritems():
            index += 1
            # 全部为空的情况
            if row == '___':
                self.excel_data.loc[name, "UCID"] = self.get_id('企业', False)
                continue

            # 前两个为空的情况
            if row.startswith('__'):
                only_tax_code_prefix = '__'
                tax_code_set.add(company_df.iloc[index]['tax_code'])
                candidate_idx.append(name)
                continue
            if only_tax_code_prefix == '__':
                self.handle_only_tax_code(tax_code_set, candidate_idx)
                only_tax_code_prefix = None

            if temp_unified_code is None:
                temp_unified_code = company_df.iloc[index]['unified_code']
                self.update_container(name, license_code_set, tax_code_set, candidate_idx)
                continue

            if company_df.iloc[index]['unified_code'] == temp_unified_code:
                self.update_container(name, license_code_set, tax_code_set, candidate_idx)
                continue
            # unified_code 不一样，说明已经进入下一个分组，进行判断以及清理
            self.handle_full_condition(license_code_set, tax_code_set, candidate_idx)
            temp_unified_code = company_df.iloc[index]['unified_code']
            self.update_container(name, license_code_set, tax_code_set, candidate_idx)

        person_df = groups.get_group('个人')
        person_df.sort_values('legal_cert_no_mask', inplace=True)
        legal_cert_no_mask, candidate_idx, person_index = None, list(), -1
        for name, row in person_df['legal_cert_no_mask'].iteritems():
            person_index += 1
            if legal_cert_no_mask is None:
                legal_cert_no_mask = person_df.iloc[person_index]['legal_cert_no_mask']
                candidate_idx.append(name)
                continue
            if person_df.iloc[person_index]['legal_cert_no_mask'] == legal_cert_no_mask:
                candidate_idx.append(name)
                continue
            self.excel_data.loc[candidate_idx, 'UCID'] = self.get_id('个人', True)
            candidate_idx.clear()

    def update_container(self, name, license_code_set, tax_code_set, candidate_idx):
        license_code_set.add(self.excel_data.iloc[name]['license_code'])
        tax_code_set.add(self.excel_data.iloc[name]['tax_code'])
        candidate_idx.append(name)

    # 处理只有税号的情况
    def handle_only_tax_code(self, tax_code_set, candidate_idx):
        if len(tax_code_set) > 2 or (len(tax_code_set) == 2 and '' not in tax_code_set):
            self.set_conflict_ucid_by_candidate_idx(candidate_idx, '企业')
        else:
            self.excel_data.loc[candidate_idx, "UCID"] = self.get_id('企业', True)
        # 清空
        candidate_idx.clear()
        tax_code_set.clear()

    # 多个冲突的 ucid，需要一个一个设置
    def set_conflict_ucid_by_candidate_idx(self, candidate_idx, member_type):
        for idx in candidate_idx:
            self.excel_data.loc[idx, 'UCID'] = self.get_id(member_type, False)

    def handle_full_condition(self, license_code_set, tax_code_set, candidate_idx):
        if len(license_code_set) > 2 or (len(license_code_set) == 2 and '' not in license_code_set):
            self.set_conflict_ucid_by_candidate_idx(candidate_idx, '企业')
        elif len(tax_code_set) > 2 and (len(tax_code_set) == 2 and '' not in tax_code_set):
            self.set_conflict_ucid_by_candidate_idx(candidate_idx, '企业')
        else:
            # 不冲突
            self.excel_data.loc[candidate_idx, 'UCID'] = self.get_id('企业', True)
        candidate_idx.clear()
        license_code_set.clear()
        tax_code_set.clear()

    def generate_ucid(self):
        self.data_from_xlsx()
        self.excel_data.sort_values('UCID', inplace=True)
        self.excel_data.to_excel('./out.xlsx', index=False, header=True)


if __name__ == '__main__':
    ucid = UCIDGenerator('./test.xlsx')
    ucid.generate_ucid()
