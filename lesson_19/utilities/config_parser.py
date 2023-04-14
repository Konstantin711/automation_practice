import configparser
import os


CONFIG_PATH = os.path.abspath('../configurations/config.ini')


def get_site_urls(func):
    def get_parser(url):
        parser = configparser.RawConfigParser()
        parser.read(CONFIG_PATH)
        return func(parser, url)
    return get_parser


def get_data_from_config(func):
    def wrapper():
        parser = configparser.RawConfigParser()
        parser.read(CONFIG_PATH)
        return func(parser)
    return wrapper


@get_data_from_config
def get_test_data(parser):
    return parser.get('test_data', 'email'), parser.get('test_data', 'password')


@get_data_from_config
def get_errors(parser):
    return parser.get('login_errors', 'status'),\
        parser.get('login_errors', 'no_customer_found'),\
        parser.get('login_errors', 'wrong_password')


@get_site_urls
def get_custom_urls(parser, url):
    return parser.get('site_urls', url)

