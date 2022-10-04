import pandas as pd
import random
from flapjack import Flapjack


# # this is for testing without flapjack
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class id_thing():
#     def __init__(self, id_in):
#         self.id = [id_in]


# class Flapjack():

#     def create(self, *args):

#         # UNCOMMENT ONE OF THE TWO
#         print(args)
#         # temp = args

#         return id_thing(random.randint(1, 100))
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# still requires some work to ensure studies etc created too
def flapjack_upload(fj_url, fj_user, fj_pass, excel_path):
    hash_map = {}

    # UNCOMMENT BELOW TO USE FLAPJACK
    # # log in to flapjack instance
    fj = Flapjack(url_base=fj_url) #Local Instance
    fj.log_in(username=fj_user, password=fj_pass)

    # read in Excel Data
    xls = pd.read_excel(excel_path,sheet_name=None)
    fj_conv_sht = xls.parse('FlapjackCols', skiprows=0)

    # order is important as Chemicals and DNA must be created before
    # they can be referenced
    types = ['Chemical', 'DNA', 'Supplement', 'Vector', 'Strain', 'Media',
             'Signal', 'Study', 'Assay', 'Sample', 'Measurement']
    #types = ['DNA', 'Supplement', 'Vector', 'Strain', 'Media',
             #'Signal', 'Measurement']
    # initiate hashmap for linking to chemicals
    hash_map = {}

    for obj in types:
        # Read in the conversion sheet for col name to flapjack name
        fj_conv_sht_obj = fj_conv_sht.loc[(fj_conv_sht['Sheet Name'] == obj)]
        fj_conv_sht_obj = fj_conv_sht_obj.set_index('ColName').to_dict('index')

        # read in the object sheet
        obj_df = xls.parse(obj, skiprows=0, index_col=f'{obj} ID')
        cols = list(obj_df.columns)

        # drop columns not used by flapjack and rename the ones that are
        new_cols = []
        col_drop = []
        for col in cols:
            if col in fj_conv_sht_obj.keys():
                new_cols.append(fj_conv_sht_obj[col]['FlapjackName'])
            else:
                col_drop.append(col)
        obj_df = obj_df.drop(columns=col_drop)
        obj_df.columns = new_cols

        # Create a dictionary of the data for flapjack
        obj_dict = obj_df.to_dict('index')

        # REMOVE THIS LINE WHEN USING FLAPJACK
        #fj = Flapjack()

        # Upload all the objects to flapjack
        for key in obj_dict:
            data = obj_dict[key]

            # Change to flapjack id rather than name for chemicals and dnas
            lookups = {'chemical', 'dnas', 'study', 'vector', 'strain', 'media', 'assay', 'sample', 'signal'}
            lk_inter = lookups.intersection(set(data.keys()))
            print(lk_inter)
            for it in list(lk_inter):
                data[it] = hash_map[data[it]]

            # CHANGE THIS WHEN USING FLAPJACK
            # add ** infront of data later when not patched!!!!!!!!
            print(obj)
            data['model'] = obj.lower()
            print(data)

            flapjack_id = fj.create(**data)
            # flapjack_id = fj.create(data)

            # add Chemical and DNA to hash map to allow cross referencing
            print(flapjack_id)
            hash_map[key] = flapjack_id.id[0]

    return hash_map
