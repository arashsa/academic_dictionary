# Functions for printing lists, dictionaries, and Count objects
# Mainly for testing


def print_simple_list(the_list):
    for w in the_list:
        print w


def print_freq_list(the_dict):
    for w, count in the_dict:
        print w, count

        
def print_count_object(count_object):
    for c in count_object.items():
        print c[0], c[1]