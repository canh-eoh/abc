import sys

def my_function(a, b):
    return int(a) + int(b)


if __name__ == '__main__':
    sys.argv
    print('call my_function({})'.format(sys.argv))
    my_function(sys.argv[1], sys.argv[2])
