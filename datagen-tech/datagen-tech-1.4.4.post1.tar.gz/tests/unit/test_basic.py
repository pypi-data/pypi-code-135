import json

import unittest

from pathlib import Path
import datagen as dg
# import prettyprinter as pp

# pp.install_extras(exclude=['python'])


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dataset_path = Path.cwd().parent.joinpath("resources", "datasets", "identities", "With_Glasses")
        cls.dataset = dg.load(str(dataset_path))

    def test_scenes_num(self):
        self.assertEqual(len(self.dataset.scenes), 3)

    def test_cameras_num(self):
        self.assertTrue(all(map(lambda scene: len(scene.cameras) == 1, self.dataset.scenes)))

    def test_dataset_size(self):
        self.assertEqual(len(self.dataset), 9)

    def test_dataset_subscription(self):
        self.assertEqual(len(self.dataset[0:4]), 4)

    def test_scene_subscription(self):
        scene = self.dataset.scenes[0]
        self.assertEqual(len(scene[0:2]), 2)

    def test_camera_subscription(self):
        camera = self.dataset.scenes[0].cameras[0]
        self.assertEqual(len(camera[0:2]), 2)

    def test_camera_metadata(self):
        camera_metadata = self.dataset.scenes[0]


class CameraMetadataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dataset_path = Path.cwd().parent.joinpath("resources", "datasets", "identities", "Transparent_Background")
        dataset = dg.load(str(dataset_path))
        dp = dataset[0]
        cls.camera_metadata_modality = dp.camera_metadata
        with open(dp.camera_path.joinpath("camera_metadata.json")) as cam_metadata_file:
            cls.camera_metadata_json = json.load(cam_metadata_file)

    def test_name(self):
        self.assertEqual(self.camera_metadata_modality.camera_name, self.camera_metadata_json["camera_name"])

    def test_type(self):
        self.assertEqual(self.camera_metadata_modality.type, self.camera_metadata_json["type"])

    def test_type(self):
        self.assertEqual(self.camera_metadata_modality.focal_length, self.camera_metadata_json["focal_length"])

    def test_sensor(self):
        self.assertEqual(
            self.camera_metadata_modality.sensor.height, self.camera_metadata_json["sensor"]["sensor_height"]
        )
        self.assertEqual(
            self.camera_metadata_modality.sensor.width, self.camera_metadata_json["sensor"]["sensor_width"]
        )

    def test_location(self):
        self.assertTrue(all(self.camera_metadata_modality.location == [self.camera_metadata_json["location"].pop(k) for k in ["x", "y", "z"]]))

    def test_orientation(self):
        modality_orientation = self.camera_metadata_modality.orientation
        j = self.camera_metadata_json["orientation"]
        self.assertTrue(
            all(modality_orientation.look_at_vector == [j["look_at_vector"].pop(k) for k in ["x", "y", "z"]]) and
            all(modality_orientation.up_vector == [j["up_vector"].pop(k) for k in ["x", "y", "z"]])
        )

    def test_fov(self):
        self.assertTrue(
            self.camera_metadata_modality.fov.horizontal == self.camera_metadata_json["fov"]["horizontal"] and
            self.camera_metadata_modality.fov.vertical == self.camera_metadata_json["fov"]["vertical"]
        )


if __name__ == '__main__':
    unittest.main()