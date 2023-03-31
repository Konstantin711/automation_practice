import configparser
import os


def get_config_reader(func):
    config_path = os.path.abspath('../configurations/config.ini')

    def get_parser():
        parser = configparser.RawConfigParser()
        parser.read(config_path)
        return func(parser)
    return get_parser


@get_config_reader
def get_test_data(parser):
    return parser.get('test_data', 'email'), parser.get('test_data', 'password')


@get_config_reader
def get_app_data(parser):
    return parser.get('app_data', 'url')
