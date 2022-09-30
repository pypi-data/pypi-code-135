import json
from ast import Or
from collections import OrderedDict
from pathlib import Path
from typing import Any, Iterable, List, Mapping, NamedTuple, Optional, Sequence, Union, cast

from attrs import define

from countergen.config import VERBOSE
from countergen.augmentation.simple_augmenter import SimpleAugmenter
from countergen.types import AugmentedSample, Category, Augmenter, Input, Outputs, Paraphraser, Variation
from countergen.tools.utils import all_same, maybe_tqdm
from countergen.config import MODULE_PATH

DEFAULT_DS_PATHS: Mapping[str, str] = {
    "doublebind-heilman": f"{MODULE_PATH}/data/datasets/doublebind-heilman.jsonl",
    "doublebind": f"{MODULE_PATH}/data/datasets/doublebind.jsonl",
    "tiny-test": f"{MODULE_PATH}/data/datasets/tiny-test.jsonl",
    "twitter-sentiment": f"{MODULE_PATH}/data/datasets/twitter-sentiment.jsonl",
    "hate": f"{MODULE_PATH}/data/datasets/hate-test.jsonl",
}

DEFAULT_AUGMENTED_DS_PATHS: Mapping[str, str] = {
    "doublebind-heilman-paraphrased": f"{MODULE_PATH}/data/augdatasets/doublebind-heilman-paraphrased.jsonl",
    "doublebind": f"{MODULE_PATH}/data/augdatasets/doublebind.jsonl",
    "tiny-test-aug-gender": f"{MODULE_PATH}/data/augdatasets/tiny-test.jsonl",
    "twitter-sentiment-aug-gender": f"{MODULE_PATH}/data/augdatasets/twitter-sentiment.jsonl",
    "hate-aug-muslim": f"{MODULE_PATH}/data/augdatasets/hate-test-muslims.jsonl",
}


@define
class Sample:
    input: Input
    outputs: Outputs = []

    @classmethod
    def from_json_dict(cls, json_dict) -> "Sample":
        outputs = json_dict["outputs"] if "outputs" in json_dict else []
        return Sample(json_dict["input"], outputs)

    def to_json_dict(self) -> OrderedDict:
        return OrderedDict({"input": self.input, "outputs": self.outputs})


@define
class SampleWithVariations(Sample, AugmentedSample):
    """AugmentedSample which explicitly stores all variations."""

    variations: List[Variation] = []

    def get_variations(self) -> Sequence[Variation]:
        return self.variations

    def get_outputs(self) -> Outputs:
        return self.outputs

    @classmethod
    def from_sample(cls, s: Sample, variations: List[Variation] = []) -> "SampleWithVariations":
        return SampleWithVariations(s.input, s.outputs, variations)

    @classmethod
    def from_json_dict(cls, json_dict) -> "SampleWithVariations":
        outputs = json_dict["outputs"] if "outputs" in json_dict else []
        variations = [Variation(v["text"], tuple(v["categories"])) for v in json_dict["variations"]]
        return SampleWithVariations(json_dict["input"], outputs, variations)

    def to_json_dict(self) -> OrderedDict:
        d: OrderedDict[str, Any] = OrderedDict({"input": self.input})
        d["outputs"] = self.outputs
        d["variations"] = [{"text": text, "categories": list(categories)} for text, categories in self.variations]
        return d


@define
class Dataset:
    samples: List[Sample]

    @classmethod
    def from_default(cls, name: str = "doublebind") -> "Dataset":
        """Load one of the defaults datasets from "DEFAULT_DS_PATHS"."""
        if name not in DEFAULT_DS_PATHS:
            raise ValueError(
                f"""Default name '{name}' is not a default dataset. Choose one in {list(DEFAULT_DS_PATHS.keys())}"""
            )
        return Dataset.from_jsonl(DEFAULT_DS_PATHS[name])

    @classmethod
    def from_jsonl(cls, path: str) -> "Dataset":
        """Load a dataset from a jsonl file.

        Expected format of each line:
        {"input": "<INP>", "outputs": ["<OUT1>", "<OUT2>", ...]}
        where you have at least one accepted output per input."""
        with Path(path).open("r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
            samples = []
            for d in data:
                samples.append(Sample.from_json_dict(d))
        return Dataset(samples)

    def augment(self, converters: Iterable[Augmenter]) -> "AugmentedDataset":
        return generate_all_variations(converters, self)


@define
class AugmentedDataset:
    samples: List[SampleWithVariations]

    @classmethod
    def from_default(cls, name: str = "doublebind-heilman") -> "AugmentedDataset":
        """Load one of the defaults datasets from "DEFAULT_AUGMENTED_DS_PATHS"."""
        if name not in DEFAULT_AUGMENTED_DS_PATHS:
            raise ValueError(
                f"Default name '{name}' is not a default augmented dataset. Choose one in {list(DEFAULT_AUGMENTED_DS_PATHS.keys())}"
            )
        return AugmentedDataset.from_jsonl(DEFAULT_AUGMENTED_DS_PATHS[name])

    @classmethod
    def from_jsonl(cls, path: str) -> "AugmentedDataset":
        with Path(path).open("r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
            samples = []
            for d in data:
                samples.append(SampleWithVariations.from_json_dict(d))
        return AugmentedDataset(samples)

    def save_to_jsonl(self, path: str):
        with Path(path).open("w", encoding="utf-8") as f:
            for sample in self.samples:
                json.dump(sample.to_json_dict(), f)
                f.write("\n")


def generate_variations(variation: Variation, augmenter: Augmenter) -> List[Variation]:
    if isinstance(augmenter, Paraphraser):
        return generate_paraphrase(variation, cast(Paraphraser, augmenter))

    text, old_categories = variation
    new_variations = [
        Variation(augmenter.transform(text, category), old_categories + (category,))
        for category in augmenter.categories
    ]
    if not all_same([v.text for v in new_variations]):
        return new_variations
    else:
        return [variation]


def generate_paraphrase(variation: Variation, augmenter: Paraphraser) -> List[Variation]:
    text, old_categories = variation
    new_text = augmenter.transform(text)
    if new_text == text:
        return [variation]
    else:
        return [variation, Variation(new_text, old_categories)]


def generate_all_variations(augmenters: Iterable[Augmenter], ds: Dataset) -> AugmentedDataset:
    """Apply each augmenter to each sample of the dataset for each available target category.

    It first replaces samples with the transformed samples through the first augmenter,
    then replaces these with samples transformed through the second augmenter, and so on.
    Return an number of variations that can be exponential in the number of augmenters.

    Remove duplicates.

    If an augmenter is a paraphrase, keep the original input too."""

    augmented_samples = []
    for sample in maybe_tqdm(ds.samples, VERBOSE >= 2):
        variations = [Variation(sample.input, ())]
        for augmenter in augmenters:
            new_variations = []
            for v in variations:
                new_variations += generate_variations(v, augmenter)
            variations = new_variations
        augmented_samples.append(SampleWithVariations.from_sample(sample, variations))
    return AugmentedDataset(augmented_samples)
