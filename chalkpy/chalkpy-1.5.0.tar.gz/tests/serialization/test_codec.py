import enum
import unittest
from datetime import date, datetime
from typing import List, Set

import pendulum

from chalk.features import feature, features
from chalk.features.feature import unwrap_feature
from chalk.serialization.codec import FeatureCodec


class CustomClass:
    def __init__(self, w: str):
        self.w = w

    def __eq__(self, other):
        return isinstance(other, CustomClass) and self.w == other.w


class Color(enum.Enum):
    blue = "blue"
    green = "green"
    orange = "orange"


@features
class Hello:
    a: str
    b: int
    c: datetime
    d: Color
    e: date
    y: Set[int]
    z: List[str]
    fancy: CustomClass = feature(encoder=lambda x: x.w, decoder=lambda x: CustomClass(x))


class FeatureCodecTestCase(unittest.TestCase):
    codec = FeatureCodec()

    def _check_roundtrip(self, f, value):
        f = unwrap_feature(f)
        encoded = self.codec.encode(f, value)
        decoded = self.codec.decode(f, encoded)
        self.assertEqual(decoded, value)

    def test_datetime(self):
        serialized = "2022-04-08T22:26:03.303000+00:00"
        decoded = self.codec.decode(unwrap_feature(Hello.c), serialized)
        self.assertEqual(decoded, pendulum.parse(serialized))
        re_encoded = self.codec.encode(unwrap_feature(Hello.c), decoded)
        self.assertEqual(serialized, re_encoded)

    def test_custom_codecs(self):
        self._check_roundtrip(Hello.fancy, CustomClass("hihi"))

    def test_color(self):
        self._check_roundtrip(Hello.d, Color.green)

    def test_date(self):
        self.assertEqual(
            "2022-04-08",
            self.codec.encode(unwrap_feature(Hello.e), date.fromisoformat("2022-04-08")),
        )
        self._check_roundtrip(Hello.e, date.fromisoformat("2022-04-08"))

    def test_list(self):
        self._check_roundtrip(Hello.z, ["hello", "there"])
