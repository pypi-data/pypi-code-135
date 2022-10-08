import enum
import glob
import logging
import os
from multiprocessing import Pool
from pathlib import Path
from typing import Any, Dict, List, Union

import torchio
from preprocess.utils.utils import compute_volume_stats


class Modality(enum.Enum):
    CT="CT"
    MRI="MRI"

class VolumeType(enum.Enum):
    NIFTY="nii.gz"

class Dataset:
    def __init__(self, path, modality: Modality, volume_type: VolumeType) -> None:
         self.path = path
         self.modality = modality
         self.volume_type = volume_type
        
    def load_volume(self, volume_path: Union[str, Path]) -> Any:
        return torchio.ScalarImage(volume_path)
        
    
class DatasetAnalyzer:
    def __init__(self, dataset, **kwargs) -> None:
         self.dataset: Dataset = dataset 
         self.volume_paths: List[Union[str, Path]] = glob.glob(self.dataset.path + "/*.nii.gz", recursive = True)
         self.num_process: int = kwargs.get('num_process', min(os.cpu_count(), len(self.volume_paths)))
         
    def load_volume_and_compute_stats(self, volume_path: Union[str, Path]) -> List[float]:
        """_summary_: Load volume and compute stats (intensity properties, shape, spacing)

        Args:
            volume_path (Union[str, Path]): _description_

        Returns:
            List[float]: _description_
        """
        volume = self.dataset.load_volume(volume_path)
        volume_np = volume.data.numpy()
        volume_stats = compute_volume_stats(volume_np)
        return {**volume_stats, "shape": volume_np.shape, "spacing": volume.spacing, "name": volume_path.split('/')[-1]}
    
    def collect_volume_properties(self) -> Dict[str, Any]:
        """_summary_ Collect volume properties (intensity properties, shape, spacing)

        Returns:
            _type_: _description_
        """
        logging.debug("Collecting intensity properties with {} proccesses and for {} volumes".format(self.num_process, 
                                                                                                     len(self.volume_paths)))
        p = Pool(self.num_process)
        volumes_stats = p.map(self.load_volume_and_compute_stats, self.volume_paths) 
        p.close()
        p.join()
        return volumes_stats
