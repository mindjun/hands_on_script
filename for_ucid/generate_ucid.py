import time
from collections import defaultdict

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
        start = int(time.time())
        print('group_by start at: {}'.format(start))
        groups = self.excel_data.groupby(by='member_type')
        print('group_by cost: {}'.format(int(time.time()) - start))
        # 企业
        company_df = groups.get_group('企业')
        self.company_group(company_df)
        # 个人
        person_df = groups.get_group('个人')
        self.person_group(person_df)

    def person_group(self, person_df):
        start = int(time.time())
        print('person sorting start at: {}'.format(start))
        person_df.sort_values('legal_cert_no_mask', inplace=True)
        print('person sorting cost: {}'.format(int(time.time()) - start))

        legal_cert_no_mask_set, candidate_idx, index = set(), list(), -1
        last_prefix = person_df['legal_cert_no_mask'][0]
        for name, row in person_df['legal_cert_no_mask'].iteritems():
            index += 1
            if index == 0:
                self.update_person_container(legal_cert_no_mask_set, candidate_idx, name)
                continue
            if row == last_prefix:
                self.update_person_container(legal_cert_no_mask_set, candidate_idx, name)
            else:
                self.person_group_ucid(legal_cert_no_mask_set, candidate_idx)
                last_prefix = row
                self.update_person_container(legal_cert_no_mask_set, candidate_idx, name)
            # 最后一组
            if index == len(person_df) - 1:
                self.person_group_ucid(legal_cert_no_mask_set, candidate_idx)

    def update_person_container(self, legal_cert_no_mask_set, candidate_idx, name):
        legal_cert_no_mask_set.add(self.excel_data.iloc[name]['legal_cert_no_mask'])
        candidate_idx.append(name)

    def person_group_ucid(self, legal_cert_no_mask_set, candidate_idx):
        if len(legal_cert_no_mask_set) > 1:
            self.set_conflict_ucid_by_candidate_idx(candidate_idx, '个人')
        elif '' in legal_cert_no_mask_set:
            self.excel_data.loc[candidate_idx, 'UCID'] = self.get_id('个人', False)
        else:
            self.excel_data.loc[candidate_idx, 'UCID'] = self.get_id('个人', True)
        legal_cert_no_mask_set.clear()
        candidate_idx.clear()

    def company_group(self, company_df):
        company_df['unified_code'] = company_df['unified_code'].astype('str')
        company_df['license_code'] = company_df['license_code'].astype('str')
        company_df['tax_code'] = company_df['tax_code'].astype('str')
        company_df['contact'] = company_df['unified_code'].str.cat([company_df['license_code'],
                                                                    company_df['tax_code']], sep='_')
        start = int(time.time())
        print('company sorting start at: {}'.format(start))
        company_df.sort_values('contact', inplace=True)
        print('company sorting cost: {}'.format(int(time.time()) - start))
        candidate_idx, license_code_set, tax_code_set, only_tax_code = list(), set(), set(), defaultdict(list)
        last_prefix = self.set_last_prefix(company_df, 0)
        index = -1

        for name, row in company_df['contact'].iteritems():
            index += 1
            # 信用代码，营业执照，税号全部为空的情况
            if row == '__':
                if len(license_code_set) != 0:
                    self.company_group_ucid(license_code_set, tax_code_set, candidate_idx)
                self.excel_data.loc[name, "UCID"] = self.get_id('企业', False)
                last_prefix = '___'
                continue

            if index == 0:
                self.update_container(name, license_code_set, tax_code_set, candidate_idx, last_prefix)
                continue

            # 只有税号的情况
            if row.startswith('__'):
                last_prefix = '__'
                only_tax_code[self.excel_data.iloc[name]['tax_code']].append(name)
            elif len(only_tax_code) > 0:
                self.handle_only_tax_code(only_tax_code)
                last_prefix = self.set_last_prefix(company_df, index)

            if last_prefix != '__':
                if row.startswith(last_prefix):
                    self.update_container(name, license_code_set, tax_code_set, candidate_idx, last_prefix)
                else:
                    self.company_group_ucid(license_code_set, tax_code_set, candidate_idx)
                    last_prefix = self.set_last_prefix(company_df, index)
                    self.update_container(name, license_code_set, tax_code_set, candidate_idx, last_prefix)

            # 最后一组数据
            if index == len(company_df) - 1:
                self.company_group_ucid(license_code_set, tax_code_set, candidate_idx)
                self.handle_only_tax_code(only_tax_code)

    def handle_only_tax_code(self, only_tax_code):
        # 每一个 value 都设置相同的 ucid
        for tax_code, names in only_tax_code.items():
            self.excel_data.loc[names, 'UCID'] = self.get_id('企业', True)
        only_tax_code.clear()

    def update_container(self, name, license_code_set, tax_code_set, candidate_idx, last_prefix):
        tax_code_set.add(self.excel_data.iloc[name]['tax_code'])
        if last_prefix != '__':
            license_code_set.add(self.excel_data.iloc[name]['license_code'])
        candidate_idx.append(name)

    @staticmethod
    def set_last_prefix(company_df, index):
        last_prefix = '{}_'.format(company_df.iloc[index]['unified_code'])
        return last_prefix

    def company_group_ucid(self, license_code_set, tax_code_set, candidate_idx):
        if len(license_code_set) > 2 or (len(license_code_set) == 2 and '' not in license_code_set):
            self.set_conflict_ucid_by_candidate_idx(candidate_idx, '企业')
        elif len(tax_code_set) > 2 or (len(tax_code_set) == 2 and '' not in tax_code_set):
            self.set_conflict_ucid_by_candidate_idx(candidate_idx, '企业')
        else:
            # 不冲突
            self.excel_data.loc[candidate_idx, 'UCID'] = self.get_id('企业', True)
        # 清空
        candidate_idx.clear()
        license_code_set.clear()
        tax_code_set.clear()

    # 多个冲突的 ucid，需要一个一个设置
    def set_conflict_ucid_by_candidate_idx(self, candidate_idx, member_type):
        for idx in candidate_idx:
            self.excel_data.loc[idx, 'UCID'] = self.get_id(member_type, False)

    def generate_ucid(self):
        self.data_from_xlsx()
        self.excel_data.sort_values('UCID', inplace=True)
        self.excel_data.to_excel('./out.xlsx', index=False, header=True)


if __name__ == '__main__':
    ucid = UCIDGenerator('./test.xlsx')
    ucid.generate_ucid()
