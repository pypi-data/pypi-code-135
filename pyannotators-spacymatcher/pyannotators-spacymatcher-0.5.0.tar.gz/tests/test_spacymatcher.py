from typing import List

from dirty_equals import HasLen, IsList, IsPartialDict, HasAttributes

from pyannotators_spacymatcher.spacymatcher import PATTERNS_EXAMPLE_STR
from pyannotators_spacymatcher.spacymatcher import SpacyMatcherAnnotator, SpacyMatcherParameters
from pymultirole_plugins.v1.schema import Document


def test_np():
    model = SpacyMatcherAnnotator.get_model()
    model_class = model.construct().__class__
    assert model_class == SpacyMatcherParameters
    annotator = SpacyMatcherAnnotator()
    parameters = SpacyMatcherParameters(mapping={
        "np": PATTERNS_EXAMPLE_STR})

    docs: List[Document] = annotator.annotate([Document(
        text="Paris is the capital of France and Emmanuel Macron is the president of the French Republic.",
        metadata={'language': 'en'})], parameters)
    doc0 = docs[0]
    assert doc0.annotations == HasLen(3)
    assert doc0.annotations == IsList(
        HasAttributes(labelName='np', text='capital of France'),
        HasAttributes(labelName='np', text='Emmanuel Macron'),
        HasAttributes(labelName='np', text='president of the French Republic'),
    )

    parameters.left_longest_match = False
    docs: List[Document] = annotator.annotate([Document(
        text="Paris is the capital of France and Emmanuel Macron is the president of the French Republic.",
        metadata={'language': 'en'})], parameters)
    doc0 = docs[0]
    assert doc0.annotations == HasLen(5)
    assert doc0.annotations == IsList(
        HasAttributes(labelName='np', text='capital of France'),
        HasAttributes(labelName='np', text='Emmanuel Macron'),
        HasAttributes(labelName='np', text='president of the French'),
        HasAttributes(labelName='np', text='French Republic'),
        HasAttributes(labelName='np', text='president of the French Republic'),
    )
