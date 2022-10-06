import os
import excel2flapjack.main as e2f

#fj_url = "localhost:8000"
fj_url = "flapjack.rudge-lab.org:8000" #Web Instance
fj_user = ""
fj_pass = ""

direct = __file__
test_file_path = os.path.join(os.path.split(os.path.split(direct)[0])[0],
                              'tests', 'test_files')
excel_path = os.path.join(test_file_path, "flapjack_excel_converter_v030.xlsx")

shm = {'Study1': 'https://synbiohub.org/user/JVM/Flapjack/Study1/1', 'Assay1': 'https://synbiohub.org/user/JVM/Flapjack/Assay1/1', 'Assay2': 'https://synbiohub.org/user/JVM/Flapjack/Assay2/1', 'Sample1': 'https://synbiohub.org/user/JVM/Flapjack/Sample1/1', 'Sample2': 'https://synbiohub.org/user/JVM/Flapjack/Sample2/1', 'Sample3': 'https://synbiohub.org/user/JVM/Flapjack/Sample3/1', 'Sample4': 'https://synbiohub.org/user/JVM/Flapjack/Sample4/1', 'M9Glucose': 'https://synbiohub.org/user/JVM/Flapjack/M9Glucose/1', 'Signal1': 'https://synbiohub.org/user/JVM/Flapjack/Signal1/1', 'Signal9': 'https://synbiohub.org/user/JVM/Flapjack/Signal9/1', 'EcoliT7': 'https://synbiohub.org/user/JVM/Flapjack/EcoliT7/1', 'Rep_HIGH_degrate_plasmid': 'https://synbiohub.org/user/JVM/Flapjack/Rep_HIGH_degrate_plasmid/1', 'Rep_LOW_degrate_plasmid': 'https://synbiohub.org/user/JVM/Flapjack/Rep_LOW_degrate_plasmid/1', 'DNA1': 'https://synbiohub.org/user/JVM/Flapjack/DNA1/1', 'DNA2': 'https://synbiohub.org/user/JVM/Flapjack/DNA2/1', 'DNA3': 'https://synbiohub.org/user/JVM/Flapjack/DNA3/1'}

hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, excel_path, sbol_hash_map=shm,
                    add_sbol_uris=True, flapjack_override=True, print_progress=True)
print(hash_map)
