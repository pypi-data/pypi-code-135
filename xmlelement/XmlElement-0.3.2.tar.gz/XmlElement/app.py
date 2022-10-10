import sys
from .xml_element import XmlElement
import json

def xml_to_json():
    if len(sys.argv) == 2:
        obj = XmlElement.from_file(sys.argv[1]).to_dict()
    else:
        input = ""
        for line in sys.stdin:
            input += line
        obj = XmlElement.from_string(input).to_dict()
    
    print(json.dumps(obj, indent=4))


def json_to_xml():
    if len(sys.argv) == 2:
        with open(sys.argv[1], "rb") as json_fp:
            obj = json.load(json_fp)
    else:
        input = ""
        for line in sys.stdin:
            input += line
        obj = json.loads(input)
    
    xe = XmlElement.from_object("xml", obj)
    print(xe.to_string())