import pdb

from exceptions import InvalidInput
import re


def param_sanitizer(input):
    if len(input) < 2:
        raise InvalidInput("Please, pass a string as an input!")

    return input[1]


def input_sanitizer(text):
    if re.search("\d{9}", text.strip()):
        return text.strip()

    raise InvalidInput("Please enter 9 digits input!")
