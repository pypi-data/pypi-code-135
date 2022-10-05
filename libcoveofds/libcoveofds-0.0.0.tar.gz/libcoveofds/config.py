from libcove.config import LIB_COVE_CONFIG_DEFAULT, LibCoveConfig  # type: ignore

LIB_COVE_OFDS_CONFIG_DEFAULT = LIB_COVE_CONFIG_DEFAULT.copy()

LIB_COVE_OFDS_CONFIG_DEFAULT.update(
    {
        "schema_url": "https://raw.githubusercontent.com/Open-Telecoms-Data/open-fibre-data-standard/d287a3483996232db2fd3f892894940da144292d/schema/network-schema.json",
        "package_schema_url": "https://raw.githubusercontent.com/Open-Telecoms-Data/open-fibre-data-standard/d287a3483996232db2fd3f892894940da144292d/schema/network-package-schema.json",
        "schema_host": "https://raw.githubusercontent.com/Open-Telecoms-Data/open-fibre-data-standard/0.1-dev/schema/",
        "schema_version": "0.1.0-alpha",
    }
)


class LibCoveOFDSConfig(LibCoveConfig):
    def __init__(self, config: dict = None):
        # We need to make sure we take a copy,
        #   so that changes to one config object don't end up effecting other config objects.
        if config:
            self.config = config.copy()
        else:
            self.config = LIB_COVE_OFDS_CONFIG_DEFAULT.copy()
