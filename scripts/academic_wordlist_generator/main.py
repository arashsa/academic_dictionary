__author__ = 'arashsaidi'

from create_word_lists import *
from printing import *
from read_corpus import *
from write_to_file import *
import time


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


start_time = time.time()
print 'Starting Script: Create Academic Word List'
read_all_files('../corpus/DUO_Corpus/Bokmaal/*.txt', 'txt')
create_list()
write_dict_to_file(get_global_reduced_freqs())
print("--- %s seconds ---" % (time.time() - start_time))