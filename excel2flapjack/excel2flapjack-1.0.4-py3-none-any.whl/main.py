import pandas as pd
from flapjack import Flapjack


# still requires some work to ensure studies etc created too
def flapjack_upload(fj_url, fj_user, fj_pass, excel_path, sbol_hash_map={},
                    add_sbol_uris=False, flapjack_override=False,
                    print_progress=False):
    hash_map = {}

    # UNCOMMENT BELOW TO USE FLAPJACK
    # # log in to flapjack instance
    fj = Flapjack(url_base=fj_url) #Local Instance
    fj.log_in(username=fj_user, password=fj_pass)

    # read in Excel Data
    xls = pd.ExcelFile(excel_path)
    fj_conv_sht = xls.parse('FlapjackCols', skiprows=0)

    # order is important as Chemicals and DNA must be created before
    # they can be referenced
    types = ['Chemical', 'DNA', 'Supplement', 'Vector', 'Strain', 'Media',
             'Signal', 'Study', 'Assay', 'Sample', 'Measurement']

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

        # Upload all the objects to flapjack
        for key in obj_dict:
            if print_progress:
                print(key)
            data = obj_dict[key]

            if key in sbol_hash_map and add_sbol_uris:
                data['sboluri'] = sbol_hash_map[key]

            # Change to flapjack id rather than name for chemicals and dnas
            lookups = {'chemical', 'dnas', 'study', 'vector', 'strain', 'media', 'assay', 'sample', 'signal'}
            lk_inter = lookups.intersection(set(data.keys()))
            for it in list(lk_inter):
                data[it] = hash_map[data[it]]

            data['model'] = obj.lower()
            flapjack_id = fj.create(**data, confirm=not(flapjack_override))

            # add Chemical and DNA to hash map to allow cross referencing
            hash_map[key] = flapjack_id.id[0]

    return hash_map
