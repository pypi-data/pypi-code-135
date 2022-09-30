"""
Embedding tests
"""
from nerfstudio.fields.modules.embedding import Embedding


def test_indexing():
    """Test embedding indexing"""
    in_dim = 100
    out_dim = 64

    embedding = Embedding(in_dim, out_dim)
    assert embedding
    # TODO
