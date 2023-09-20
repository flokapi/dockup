import platformdirs
from pathlib import Path


from . import utils


APP_NAME = 'dockup'
CONFIG_NAME = 'config.yml'

APP_PATH = Path(platformdirs.user_data_dir(APP_NAME))
CONFIG_PATH = APP_PATH.joinpath(CONFIG_NAME)


def init():
    APP_PATH.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.touch()


def getParam(param):
    config = utils.readYaml(CONFIG_PATH)
    if param in config:
        return config[param]
    else:
        return None


def getPackageCfg(target):
    pkgCfgPath = APP_PATH.joinpath(target, 'dockup.yml')
    return utils.readYaml(pkgCfgPath)
