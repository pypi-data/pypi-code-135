import unittest

from pathlib import Path
import datagen as dg
import prettyprinter as pp

pp.install_extras(exclude=['python'])


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dataset_path = str(Path.cwd().parent.joinpath("resources", "datasets", "hic", "With_Keypoints"))
        cls.dataset = dg.load(dataset_path, dataset_config=dg.DatasetConfig(environment="hic"))

    def test_scenes_num(self):
        center_of_geometry = self.dataset[0].center_of_geometry
        center_of_geometry['1_street_light_on.082']
