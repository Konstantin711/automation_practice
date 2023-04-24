from argparse import ArgumentParser
from human import Human

parser = ArgumentParser(description='Parser for data converter')
parser.add_argument('--json_to_cli', default=False)
parser.add_argument('--xml_to_cli', default=False)
args = parser.parse_args()


def data_writer(data, flag):
    if flag.json_to_cli:
        with open('convert_to_json.json', 'w') as json_file:
            json_file.write(data.convert_to_json())
    if flag.xml_to_cli:
        with open('convert_to_xml.xml', 'w') as xml_file:
            xml_file.write(data.convert_to_xml())
    if not flag.json_to_cli and not flag.xml_to_cli:
        raise Exception('To write data to file use correct flag - "--json_to_cli"'
                        'or "--xml_to_cli" with True value')


if __name__ == '__main__':
    human = Human(name='Konstantin', age='32', gender='male', birth_year=1990)
    data_writer(human, args)
