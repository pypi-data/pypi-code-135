import random
import unittest

from datapoint_request_validation_service_openapi_client import GlassesSchema as Glasses, ColorType
from datagen.api.catalog import OnLoad


class LensColorRandomization(OnLoad[Glasses]):
    def _apply(self, asset: Glasses) -> None:
        asset.lens_color = random.choice([ColorType.GOLD, ColorType.GREEN, ColorType.APPLE_GREEN])


class FrameColorRandomization(OnLoad[Glasses]):
    def _apply(self, asset: Glasses) -> None:
        asset.frame_color = random.choice([ColorType.RED, ColorType.BLUE, ColorType.YELLOW, ColorType.ORANGE])


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ...

    def test_hair_assets(self):

        from datagen.api import catalog, datapoint

        lens_color_randomization, frame_color_randomization = LensColorRandomization(), FrameColorRandomization()
        catalog.glasses.hooks.add(lens_color_randomization, frame_color_randomization)

        aviators_count = catalog.glasses.count(     # "Lets see how much aviator assets there are"
            style=catalog.GlassesStyle.AVIATOR
        )

        glasses_assets = catalog.glasses.get(
            style=catalog.AnyOf(                    # "I'd like any of the following glasses styles"
                catalog.GlassesStyle.BROWLINE,
                catalog.GlassesStyle.CAT_EYE,
                catalog.GlassesStyle.AVIATOR,
                catalog.GlassesStyle.GEOMETRIC,
                catalog.GlassesStyle.OVERSIZED,
                catalog.GlassesStyle.ROUND
            ),
            # gender=catalog.AllOf(                   # "Unisex glasses" - Attributes must contain both male AND female
            #     catalog.Gender.MALE,
            #     catalog.Gender.FEMALE
            # ),
            # OR -
            # gender=catalog.Gender.MALE,
            limit=10                                # "I only need 10 assets".
        )

        glasses = glasses_assets[0]                 # Plug & Play object, straight into the datapoint request obj

        glasses_attributes = glasses.attributes                 # A simple attributes object:
                                                    # GlassesAttributes(
                                                    #   supported_position=[<AccessoryPosition.NOSE: 'nose'>],
                                                    #   gender=[<Gender.MALE: 'male'>, <Gender.FEMALE: 'female'>],
                                                    #   style=<GlassesStyle.BROWLINE: 'browline'>
                                                    #)
        for actor in actors:
            dp_request = datapoint.requests.create(actor, background, camera)

        # glasses_attributes
        # aviators_count
        # limited_hdri_assets = catalog.glasses.get(environment=catalog.Environment.INDOOR, limit=10)
        # hdri_assets_count = catalog.hdri.count(environment=catalog.Environment.INDOOR)






        i = 0

if __name__ == "__main__":
    unittest.main()
