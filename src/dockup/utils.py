
import yaml


def readYaml(filePath):
    with open(filePath, 'r') as file:
        return yaml.safe_load(file)


def saveYaml(filePath, data):
    with open(filePath, 'w') as file:
        return yaml.dump(data, file, default_flow_style=False, sort_keys=False)
