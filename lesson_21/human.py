"""
Implement provided methods. You need to convert the class instance to JSON or XML. When the user provides the command
json to cli, the program should call convert_to_json, when providing xml to cli program should convert the class
instance to xml string. And print it, or even better write it to a separate file.
You can use third parties libraries for this. If you use such a library please add it to requirenment.txt
"""

from dict2xml import dict2xml
import json


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        return dict2xml(self.__dict__, wrap='human')
