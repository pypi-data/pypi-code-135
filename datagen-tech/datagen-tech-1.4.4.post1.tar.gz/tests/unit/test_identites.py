import json

import unittest

import datagen as dg
from pathlib import Path


class ActorMetadataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dataset_path = Path.cwd().parent.joinpath("resources", "datasets", "identities", "With_Glasses")
        dataset = dg.load(str(dataset_path))
        dp = dataset[0]
        cls.actor_metadata_modality = dp.actor_metadata
        with open(dp.scene_path.joinpath("actor_metadata.json")) as actor_metadata_file:
            cls.actor_metadata_json = json.load(actor_metadata_file)

    def test_identity_label(self):
        mdlty, jsn = self.actor_metadata_modality.identity_label, self.actor_metadata_json["identity_label"]
        self.assertTrue(
            mdlty.age == jsn["age"] and mdlty.ethnicity == jsn["ethnicity"] and mdlty.gender == jsn["gender"]
        )

    def test_identity_id(self):
        self.assertEqual(self.actor_metadata_modality.identity_id, self.actor_metadata_json["identity_id"])

    def test_face_expression(self):
        mdlty, jsn = self.actor_metadata_modality.face_expression, self.actor_metadata_json["face_expression"]
        self.assertTrue(mdlty.name == jsn["name"] and mdlty.intensity_level == jsn["intensity_level"])

    def test_facial_hair_included(self):
        self.assertEqual(
            self.actor_metadata_modality.facial_hair_included, self.actor_metadata_json["facial_hair_included"]
        )

    def test_head_root_location(self):
        mdlty, jsn = \
            self.actor_metadata_modality.head_metadata.head_root_location, \
            self.actor_metadata_json["head_metadata"]["head_root_location"]
        all(mdlty == [jsn.pop(k) for k in ["x", "y", "z"]])


if __name__ == '__main__':
    unittest.main()
