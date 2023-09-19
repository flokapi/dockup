
import subprocess


from . import utils
from . import config


COMPOSE_NAME = 'docker-compose.yml'
COMPOSE_PATH = config.APP_PATH.joinpath(COMPOSE_NAME)


def _getBaseData():
    return {
        'version': '3',
        'services': {
            's_reverse_proxy': {
                'container_name': 'reverse_proxy',
                'build': {
                    'context': 'reverse_proxy'
                },
                'ports': [
                    '443:443',
                    '80:80'
                ],
                'volumes': [],
            }
        }
    }


def _addAppService(data, target):
    service = {
        'container_name': target,
        'build': {
            'context': f'./{target}'
        }
    }

    data['services'][f's_{target}'] = service


def _addAppProxyConf(data, target):
    volumes = data['services'][f's_reverse_proxy']['volumes']
    volume = f'./{target}/nginx.conf:/home/nginxcfg/{target}.conf'
    volumes.append(volume)


def buildFile():
    data = _getBaseData()

    for dir in config.APP_PATH.iterdir():
        if dir.is_dir() and dir.name != 'reverse_proxy':
            _addAppService(data, dir.name)
            _addAppProxyConf(data, dir.name)

    utils.saveYaml(COMPOSE_PATH, data)


def run(cmd):
    subprocess.run(['docker', 'compose', '-f', str(COMPOSE_PATH)] + cmd)
