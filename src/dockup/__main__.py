

from . import dockup
from . import config
import argparse


def parseCommand():
    parser = argparse.ArgumentParser()

    parser.add_argument('action', type=str)
    parser.add_argument('target', type=str)

    return parser.parse_args()


def main():
    config.init()

    cmd = parseCommand()

    if cmd.action == 'install':
        dockup.install(cmd.target)
    elif cmd.action == 'uninstall':
        dockup.uninstall(cmd.target)
    elif cmd.action == 'installproxy':
        dockup.installProxy(cmd.target)
    else:
        print('Unknown command')


main()
