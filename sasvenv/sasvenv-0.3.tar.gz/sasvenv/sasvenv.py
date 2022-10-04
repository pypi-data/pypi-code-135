import subprocess
def Venv():
    subprocess.run('python -m venv venv', shell=True) 
    
def Install(module_list):
    for module in module_list:
        subprocess.run(f'pip install {module}', shell=True)
