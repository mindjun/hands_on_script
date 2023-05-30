import os
import pandas as pd


# name_list = './data1'
# name_list = os.listdir(name_list)
name_list = ['./test.xlsx']
for i in name_list:
    if i.endswith('.xlsx'):
        df = pd.read_excel(i)
        # df = pd.read_csv('./data1/' + i)
        # 填充空缺值
        df = df.fillna('')
        # 更改名称
        df['member_type'] = df['member_type'].map(lambda x: '个人' if x.startswith('个人') else '企业')

        company_keys = ['unified_code', 'license_code', 'tax_code']
        person_keys = ['legal_cert_no_mask']
        df['UCID'] = None
        class IdGenerator:
            def __init__(self):

                self.ids = [
                    -1, # formal company
                    -1, # formal person
                    -1, # tmp company
                    -1, # tmp person
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
                    id=self.ids[current]
                )

        id_generator = IdGenerator()

        while df.UCID.isna().sum():
            # processing print
            print(f"\rResume: {df.UCID.isna().sum(): > 10}", end='')

            crt_idx = df[df.UCID.isna()].index[0]
            member_type = df.loc[crt_idx, 'member_type']
            keys = {
                '个人': person_keys,
                '企业': company_keys
            }.get(member_type)


            _df = df.loc[[crt_idx]]
            before_idx = _df.index.tolist()

            for _ in range(len(keys)):

                vals = {
                    k: [*filter(lambda x: x != '', _df[k].unique().tolist())]
                    for k in keys
                }

                candidate_matrix = pd.concat([df[k].isin(v) for k, v in vals.items() if v], axis=1)
                candidate_idx = df.UCID.isna() & (df.member_type == member_type) & candidate_matrix.any(axis=1)

                if before_idx != df[candidate_idx].index.tolist():
                    _df = df[candidate_idx]
                    before_idx = _df.index.tolist()
                else:
                    break

            if len(before_idx) == 1 or all([len(v) == 1 for k, v in vals.items() if v]):
                df.loc[candidate_idx, 'UCID'] = id_generator.get_id(member_type, True)
            else:
                df.loc[candidate_idx, 'UCID'] = id_generator.get_id(member_type, False)

        print('\nFinish')
        # df.to_csv('./data1/result_{}.csv'.format(i.split('.csv')[0]),index=False)
        df.to_excel('./out.xlsx', index=False, header=True)
