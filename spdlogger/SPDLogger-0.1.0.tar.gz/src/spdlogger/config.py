from dynaconf import Dynaconf
import site
path = site.getsitepackages()[0]
# path = "/Users/pcsh0974/Documents/SPDLogger/src"
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["{}/spdlogger/config/settings.toml".format(path), "{}/spdlogger/config/conf.yaml".format(path)],
    # includes=["{}/spdlogger/config/settings.toml".format(path), "{}/spdlogger/config/.secrets.toml".format(path)]
)


