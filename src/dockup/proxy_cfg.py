
from . import config


NGINX_CFG = {
    'default': '''
        location /{path}/ {{
            proxy_pass         http://{name}/;
            proxy_http_version 1.1;
            proxy_set_header   Upgrade $http_upgrade;
            proxy_set_header   Connection keep-alive;
            proxy_set_header   Host $host;
            proxy_cache_bypass $http_upgrade;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto $scheme;
        }}
        ''',
    'flet': '''
        location /{path}/ {{
            proxy_pass         http://{name}/;
            proxy_http_version 1.1;
            proxy_set_header   Upgrade $http_upgrade;
            proxy_set_header   Connection keep-alive;
            proxy_set_header   Host $host;
            proxy_cache_bypass $http_upgrade;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto $scheme;
        }}

        location /{path}/ws {{
            proxy_pass         http://{name}/ws;
            proxy_http_version 1.1;
            proxy_set_header   Upgrade $http_upgrade;
            proxy_set_header   Connection "upgrade";
            proxy_set_header   Host $host;
            proxy_cache_bypass $http_upgrade;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto $scheme;
        }}
        '''
}


def _getProxyCfgPath(target):
    return config.APP_PATH.joinpath(target, 'nginx.conf')


def _getCfgType(packageCfg):
    if 'proxy_cfg' in packageCfg.keys():
        return packageCfg['proxy_cfg']
    else:
        return 'default'


def makeConfig(target):
    proxyCfgPath = _getProxyCfgPath(target)

    if proxyCfgPath.is_file():
        return

    packageCfg = config.getPackageCfg(target)
    cfgType = _getCfgType(packageCfg)

    with open(proxyCfgPath, 'w') as f:
        for line in NGINX_CFG[cfgType].split('\n'):
            f.write(line.strip().format(**packageCfg)+'\n')
