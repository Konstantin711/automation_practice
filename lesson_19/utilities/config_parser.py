import configparser
import os


CONFIG_PATH = os.path.abspath('../configurations/config.ini')


def get_config_reader(func):
    def get_parser(url):
        parser = configparser.RawConfigParser()
        parser.read(CONFIG_PATH)
        return func(parser, url)
    return get_parser


@get_config_reader
def get_test_data(parser):
    return parser.get('test_data', 'email'), parser.get('test_data', 'password')


@get_config_reader
def get_site_urls(parser, url):
    if url == 'main_url':
        return parser.get('site_urls', url)
    elif url == 'register_url':
        return parser.get('site_urls', url)
    elif url == 'search_url':
        return parser.get('site_urls', url)
