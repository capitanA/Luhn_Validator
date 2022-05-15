import sys
from sanitizers import input_sanitizer, param_sanitizer
from moduleten import ModuleTen
from exceptions import InvalidInput


def start():
    args = param_sanitizer(sys.argv) #Check if user haven't passed any input!
    input = input_sanitizer(args)
    moduleten = ModuleTen(input)
    res = moduleten.validate()
    print(res)


if __name__ == '__main__':
    try:
        start()

    except InvalidInput as e:
        print(str(e))
