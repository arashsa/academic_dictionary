__author__ = 'arashsaidi'

import operator


def write_list_to_file(the_list, args=''):
    make_file = open('test_file.txt', 'w')
    if args:
        make_file.write(args + '\n')
    for w in the_list:
        make_file.write(w + '\n')


def write_dict_to_file(the_dict, args=''):
    make_file = open('test_list.txt', 'w')
    if args:
        make_file.write(args + '\n')

    for w, count in sorted(the_dict.items()):
        make_file.write(w + ' ' + str(count) + '\n')

