
from . import config


DOCKER_CFG = {
    'python':  '''
        ARG PYTHON_VERSION=3.11.4
        FROM python:${{PYTHON_VERSION}}-alpine as base

        WORKDIR /app

        COPY requirements.txt ./

        RUN pip install -r requirements.txt
            
        COPY . .

        EXPOSE 80

        CMD uvicorn 'main:app' --host=0.0.0.0 --port=80
        '''
}


def _getDockerFilePath(target):
    return config.APP_PATH.joinpath(target, 'Dockerfile')


def _getCfgType(packageCfg):
    if 'docker_file' in packageCfg.keys():
        return packageCfg['docker_file']
    else:
        return 'python'


def makeDockerFile(target):
    dockerFilePath = _getDockerFilePath(target)

    if dockerFilePath.is_file():
        return

    packageCfg = config.getPackageCfg(target)
    cfgType = _getCfgType(packageCfg)

    with open(dockerFilePath, 'w') as f:
        for line in DOCKER_CFG[cfgType].split('\n'):
            f.write(line.strip().format(**packageCfg)+'\n')
