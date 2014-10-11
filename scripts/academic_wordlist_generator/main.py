__author__ = 'arashsaidi'

from scripts.academic_wordlist_generator.create_word_lists import *
from scripts.academic_wordlist_generator.printing import *
from scripts.academic_wordlist_generator.read_corpus import *
from scripts.academic_wordlist_generator.write_to_file import *


def create_list(print_alpha=False, print_val=False, cutoff=15):
    create_most_freq_word_list('../1000_hifreq_lemmas_forms.txt')
    create_english_word_list('../brit-a-z.txt')
    reduced_frequency(cutoff)
    remove_most_frequent_words_numbers_english()
    remove_relative_frequent_words_below_score(cutoff)

    if print_alpha:
        print_dictionary_alphabetically(get_global_reduced_freqs())
    if print_val:
        print_dictionary_by_value(get_global_reduced_freqs())


read_all_files('../corpus/kiap-norsk-xml/*.xml', 'xml')
create_list()
write_dict_to_file(get_global_reduced_freqs())