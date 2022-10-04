import os
import excel2flapjack.main as e2f

#fj_url = "localhost:8000"
fj_url = "flapjack.rudge-lab.org:8000" #Web Instance
fj_user = "saisam17"
fj_pass = "Il0vem$her"

direct = __file__
test_file_path = os.path.join(os.path.split(os.path.split(direct)[0])[0],
                              'tests', 'test_files')
excel_path = os.path.join(test_file_path, "flapjack_excel_converter_v028.xlsx")

hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, excel_path)
print(hash_map)
