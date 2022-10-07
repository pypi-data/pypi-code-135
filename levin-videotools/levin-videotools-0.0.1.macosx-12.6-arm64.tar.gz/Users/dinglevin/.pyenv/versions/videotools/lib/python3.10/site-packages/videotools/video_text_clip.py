import logging
import os

from .common import Md5Store, Stopwatch, add_text_clip, md5_sotre


class VideoTextClipProcessor:
    def __init__(self, config):
        self._config = config
        self._md5_store = Md5Store(config.md5_store_file)
        self._md5_store.init()
        self._logger = logging.getLogger("processor")
    
    def process_path(self, in_path, out_path):
        total_processed = 0
        for parent_path, dirs, files in os.walk(in_path):
            for file_name in files:
                input_file = f"{parent_path}/{file_name}"
                if file_name.startswith("."):
                    logging.info(f"File ignored: {input_file}")
                    continue
                
                file_name = file_name[0:file_name.rindex(".")]
                output_file = f"{parent_path.replace(in_path, out_path)}/{file_name}.mp4"
                total_processed += self._do_process_one(input_file, output_file)
                
        return total_processed

    def process_file(self, in_file, dest_file):
        self._do_process_one(in_file, dest_file)
        
    def close(self):
        self._md5_store.close()
    
    def _process_one_in_path(self, input_file, output_file):
        stopwatch = Stopwatch()
        try:
            self._do_process_one(input_file, output_file)
            self._logger.info(f"Process one in path finished, input: {input_file}, output: {output_file}" +
                              f", spends: {stopwatch.stop()}")
        except:
            self._logger.exception(f"Process one in path failed, file: {input_file}, spends: {stopwatch.stop()}")
            return 0
        
    def _do_process_one(self, input_file, output_file):
        check_result = self._md5_store.check_exists_file(input_file)
        if check_result.id:
            logging.error(f"File already processed, pre_file_name: {check_result.file_name}, " +
                f"process_time: {check_result.gmt_create}, cur_file_name: {input_file}")
            return 0

        add_text_clip(input_file, output_file, self._config.text_to_clip)
        self._md5_store.insert_md5_item(check_result.md5_val, input_file)
