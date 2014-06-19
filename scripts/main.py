__author__ = 'arashsaidi'

from create_word_lists import *
from printing import *
from read_corpus import *
from write_to_file import *


def create_list(print_alpha=False, print_val=False):
    remove_numbers()
    reduced_frequency()
    remove_most_frequent_words()
    remove_relative_frequent_words_below_score(15)

    if print_alpha:
        print_dictionary_alphabetically(get_global_reduced_freqs())
    if print_val:
        print_dictionary_by_value(get_global_reduced_freqs())


# read_all_files('../corpus/kiap-norsk-xml/*.xml', 'xml')
read_xml('../corpus/kiap-norsk-xml/noling01.xml')
create_list()
write_dict_to_file(get_global_reduced_freqs())
