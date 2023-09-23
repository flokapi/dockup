
from . import config


DOCKER_CFG = {
    'website': '''
        FROM nginx:latest

        COPY . /usr/share/nginx/html
    ''',
    'flet': '''
        ARG PYTHON_VERSION=3.11.4
        FROM python:${{PYTHON_VERSION}}-alpine as base

        WORKDIR /app

        COPY requirements.txt ./

        RUN pip install -r requirements.txt
            
        COPY . .

        CMD uvicorn 'main:app' --host=0.0.0.0 --port=80
        ''',
    'flet_abs': '''
        ARG PYTHON_VERSION=3.11.4
        FROM python:${{PYTHON_VERSION}}-alpine as base

        WORKDIR /app

        COPY requirements.txt ./

        RUN pip install -r requirements.txt
            
        COPY . .

        CMD uvicorn 'main:app' --host=0.0.0.0 --port=80
        '''
}


def _getDockerFilePath(target):
    return config.APP_PATH.joinpath(target, 'Dockerfile')


def _getCfgType(packageCfg):
    if 'type' in packageCfg.keys():
        return packageCfg['type']
    else:
        return None


def makeDockerFile(target):
    dockerFilePath = _getDockerFilePath(target)

    if dockerFilePath.is_file():
        return

    packageCfg = config.getPackageCfg(target)
    cfgType = _getCfgType(packageCfg)

    if cfgType not in DOCKER_CFG:
        print(f'Docker file not defined for type: {cfgType}')
        exit()

    with open(dockerFilePath, 'w') as f:
        for line in DOCKER_CFG[cfgType].split('\n'):
            f.write(line.strip().format(**packageCfg)+'\n')
