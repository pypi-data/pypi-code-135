class Collect_data:
    def __init__(self, command, flags=list(), input_path=str()):
        import subprocess
        import os

        status, _ = subprocess.getstatusoutput([command])
        if status not in [1, 0]:
            raise FileNotFoundError(f"Can not find executable at '{command}'\nExit-code {status}")
        self.command = command
        self._flags_ = flags
        self._flags_.append('POSITIONAL')
        self._input_path_ = input_path
        self._result_path_ = str(os.path.split(command)[1]) + "_result.tsv"
        self._example_dict_ = {'-h' : True, '-p': 72, '--output': 'output/', 
                               'POSITIONAL': ['file1.fa', 'file2.fa']}


    def __return_full_command_by_dict__(self, flags_dict):
        to_run = [self.command]
        for key in flags_dict.keys():
            if not key in self._flags_:
                raise KeyError(f"Flag '{key}' is not listed as command's available flag")

            if flags_dict.get(key) and key != 'POSITIONAL':
                if type(flags_dict[key]) == bool:
                    to_run.append(key)
                else:
                    to_run.extend([key, str(flags_dict[key])])
        if flags_dict.get('POSITIONAL'):
                for argument in flags_dict.get('POSITIONAL'):
                    to_run.append(argument)
        return to_run

    def start_process(self, flags_dict):
        import subprocess
        command_to_run = self.__return_full_command_by_dict__(flags_dict)
        process = subprocess.Popen(command_to_run, stdout=subprocess.DEVNULL)
        return process

    def kill_by_pid(self, pid): # kill all proccesses if needed
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()

    def set_grid(self, dict_to_grid: dict):
        from sklearn.model_selection import ParameterGrid
        self._flags_grid_ = list(ParameterGrid(dict_to_grid))
        
    def get_grid(self):
        return self._flags_grid_

    def add_to_grid(self, combinations_to_add: list):
        self._flags_grid_.extend(combinations_to_add)
    
    def delete_from_grid(self, combinations_to_delete: list):
        not_found = []
        if type(combinations_to_delete) is not list:
            combinations_to_delete = [combinations_to_delete]
        for combination in combinations_to_delete:
            if combination in self._flags_grid_:
                self._flags_grid_.remove(combination)
            else:
                not_found.append(combination)
        if not_found:
            print("Grid does not contain combination(s):")
            print(not_found)
    
    def _get_temp_clustal_file_(self, seq_number, seq_length, mode='similar', shift_length = 0):
        from Bio import SeqIO
        from Bio.Seq import Seq
        from Bio.SeqRecord import SeqRecord
        import os
        
        directory = 'tmp'
        if not os.path.exists(directory):
            os.makedirs(directory)
        seq_list = []
        name = os.path.basename(self._input_path_)
        if shift_length > 0:
            name_file = f'{os.path.splitext(name)[0]}_{seq_number}seq_{seq_length}n_{mode}.fasta'
        else:
            name_file = f'{os.path.splitext(name)[0]}_{seq_number}seq_{seq_length}n_{mode}_shift_{shift_length}.fasta'


        if mode =='use_external':
            start = 0
            end = seq_length
            for index, record in enumerate(SeqIO.parse(self._input_path_, "fasta")): 
                if end > len(record.seq):
                    start = 0
                    end = seq_length
                seq_list.append(SeqRecord(record.seq[start:end], id=record.id, description=record.description))
                if index == seq_number - 1:
                    break
                start += shift_length
                end += shift_length
        
        elif mode == 'random_nucleotide':
            import random
            letters = ["A", "T", "G", "C"]
            for i in range (seq_number):
                record = ''.join(random.choice(letters) for i in range(seq_length))
                seq_list.append(SeqRecord(Seq(record), id=str(i)))
        
        elif mode == 'random_amino':
            import random
            letters = ["G", "L", "Y", "S", "E", "Q", "D", "N", "F", "A", "K", "R", "C", "H", "V", "P", "W", "I", "M", "T"]
            for i in range (seq_number):
                record = ''.join(random.choice(letters) for i in range(seq_length))
                seq_list.append(SeqRecord(Seq(record), id=str(i)))

        fd = open(os.path.join(directory, name_file), "w")
        SeqIO.write(seq_list, fd, "fasta")
        fd.close()
        return os.path.join(directory, name_file)

    def _psutil_return_load_(pd_series):
        import psutil
        cpu_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        pd_series['cpu1m'] = cpu_load[0]
        pd_series['cpu5m'] = cpu_load[1]
        pd_series['cpu15m'] = cpu_load[2]
        vm = psutil.virtual_memory()
        pd_series['vm_available'] = vm.available
        pd_series['vm_percent'] = vm.percent
        pd_series['proc_number'] = len(psutil.pids())
        return pd_series

    def grid_dict_to_run_command(self, grid_dict):
        generated_file =  self._get_temp_clustal_file_(grid_dict['seq_number'], 
                                                    grid_dict['seq_length'], mode=grid_dict['input_mode'], shift_length=grid_dict['fasta_shift'])
        temp_dict = grid_dict.copy()            
        temp_dict["-i"] = generated_file                                
        del temp_dict['seq_number']; del temp_dict['seq_length']
        del temp_dict['input_mode']; del temp_dict['fasta_shift']
        return temp_dict, generated_file

    def start(self):
        import pandas as pd
        import datetime
        import psutil
        import os
        
        if not os.path.exists("results/" + self._result_path_):
            columns = list(self.get_grid()[0].keys())
            columns.extend(['date_started', 'date_ended', 'return_code', 'seconds_spent'])
            df = pd.DataFrame(columns=columns)
            os.mkdir('results')
            df.to_csv("results/" + self._result_path_, sep='\t', index=False)
        
        while self._flags_grid_:
            current_job = self._flags_grid_[0]
            df = pd.read_csv("results/" + self._result_path_, sep='\t')
            row = pd.Series(current_job)
            command_dict, file_path = self.grid_dict_to_run_command(current_job)
            row = Collect_data._psutil_return_load_(row)
            process = self.start_process(command_dict)
            row['date_started'] = datetime.datetime.now()
            return_code = process.wait()
            row['date_ended'] = datetime.datetime.now()
            row['return_code'] = return_code
            row['seconds_spent'] = (row['date_ended'] - row['date_started']).total_seconds()
            df = pd.concat([df, row.to_frame().T], axis=0, ignore_index=True)
            df.to_csv("results/" + self._result_path_, sep='\t', index=False)
            self._flags_grid_.remove(current_job)
            os.remove(file_path)
        os.rmdir('tmp')
