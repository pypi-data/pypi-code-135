from .settings import settings
from .validators import allowable_url_schemes

# Initialize the settings
settings.configure()


def test_true():
    assert True


def test_allowable_url_schemes():
    """Test the allowable_url_schemes function."""
    assert allowable_url_schemes() == ["http", "https", "ftp", "ftps", "sftp"]

    settings.EXTRA_URL_SCHEMES = ["weddav"]
    assert "weddav" in allowable_url_schemes()
