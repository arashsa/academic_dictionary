__author__ = 'arashsaidi'
import operator

# Functions for printing lists, dictionaries, and Count objects
# Mainly for testing


def print_simple_list(the_list):
    for w in the_list:
        print w


def print_dictionary_alphabetically(the_dict):
    for w, count in sorted(the_dict.items()):
        print w, count


def print_dictionary_by_value(the_dict):
    sorted_dict = sorted(the_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for (w, v) in sorted_dict:
        print w, v

        
def print_count_object(count_object):
    for (w, count) in count_object.items():
        print w, count