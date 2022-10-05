from .validators import allowable_url_schemes


def test_true():
    assert True


def test_allowable_url_schemes():
    """Test the allowable_url_schemes function."""
    assert allowable_url_schemes() == ["http", "https", "ftp", "ftps", "sftp"]
    assert ["weddav"] in allowable_url_schemes("weddav")
