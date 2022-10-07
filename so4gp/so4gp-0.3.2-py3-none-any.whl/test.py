from src.so4gp import so4gp
import json

# out_json, gps = so4gp.rsgps('DATASET.csv', max_iteration=20, return_gps=True)
# out_json, gps = so4gp.graank('DATASET.csv', return_gps=True)
out_json, gps = so4gp.clugps('DATASET.csv', e_probability=0.1, return_gps=True)
# print(out_json)
print(so4gp.analyze_gps('DATASET.csv', 0.5, gps, approach='dfs'))

# out_obj = json.loads(out_json)
# print(out_obj["Invalid Count"])

# gp = so4gp.ExtGP()
# gp.add_items_from_list(['3-', '1-', '0+'])
# print(gp.to_string())

# d_gp = so4gp.DfsDataGP('DATASET.csv', 0.5)
# d_gp.init_transaction_ids()
# print(d_gp.item_to_tids)
