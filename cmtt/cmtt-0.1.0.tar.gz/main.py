from cmtt.data import *

# Load online resource files
print("Load url function")
result_json = load_url('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')
print(result_json['code'])

result_csv = load_url('https://gist.githubusercontent.com/rnirmal/e01acfdaf54a6f9b24e91ba4cae63518/raw/6b589a5c5a851711e20c5eb28f9d54742d1fe2dc/datasets.csv')
print(result_csv['about'][20])
print(len(result_csv['about']))
print()

# List CMTT dataset keys and all available cmtt datasets
print("List dataset keys and cmtt datasets function")
keys = list_dataset_keys()
print(keys)

data = list_cmtt_datasets()
print(data)
print()

# Download cmtt datasets
print("Download cmtt datasets function")
lst = download_cmtt_datasets(["linc_ner_hineng", "L3Cube_HingLID_all", "linc_lid_spaeng"])

print()
path = download_dataset_url('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')

print()
print(lst)
print(path)