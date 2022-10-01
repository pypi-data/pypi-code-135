""" jouissance.pt.data """

import os
import glob

import torch
import torchvision

from jouissance.util import read_conf, make_hash
from jouissance.util import get_scenes_conditions_h5py
from jouissance.util import make_glob


class MyData(torch.utils.data.Dataset):
    """ custom dataset """

    def __init__(self, files, _hash, configs):
        self.files = files
        self.sfiles = [file.split("/")[-1] for file in files]
        self._hash = _hash
        self.con = configs

    def __len__(self):
        return len(self.files)

    def __getitem__(self, index):
        if (
            os.path.exists(f"{self._hash}/scenes{self.sfiles[index]}") and
            os.path.exists(f"{self._hash}/conditions{self.sfiles[index]}")
        ):
            return (
                torch.load(
                    f"{self._hash}/scenes{self.sfiles[index]}"),
                torch.load(
                    f"{self._hash}/conditions{self.sfiles[index]}")
            )

        scenes, conditions = get_scenes_conditions_h5py(
            self.files[index], bck="pt")
        scenes, conditions = torch.Tensor(scenes), torch.Tensor(conditions)

        scenes = torchvision.transforms.Resize((
            int(self.con["scene_reshape1"]),
            int(self.con["scene_reshape2"])
        ))(scenes)

        conditions = torchvision.transforms.Resize((
            int(self.con["reanalysis_reshape1"]),
            int(self.con["reanalysis_reshape2"])
        ))(conditions)

        os.makedirs(f"{self._hash}", exist_ok=True)

        torch.save(
            scenes, f"{self._hash}/scenes{self.sfiles[index]}")
        torch.save(
            conditions, f"{self._hash}/conditions{self.sfiles[index]}")

        return scenes, conditions


def make_data():
    """ make a dataset """

    configs = read_conf()
    cache_fold = f"{configs['cache_prefix']}{make_hash(configs)}pt"

    if configs["use_cache_only"]:
        files = glob.glob(f"{cache_fold}/scenes*")
        files = [file.replace("scenes", "") for file in files]
    else:
        files = make_glob(con=configs)

    return torch.utils.data.DataLoader(
        MyData(files, cache_fold, configs),
        batch_size=int(configs["batch_size"]),
        shuffle=True,
        num_workers=0,
    )
