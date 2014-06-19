__author__ = 'arashsaidi'

from create_word_lists import *
from printing import *

read_xml('../corpus/kiap-norsk-xml/noecon05.xml')
print len(global_word_list)
reduced_frequency()
print len(global_reduced_freqs)
remove_most_frequent_words()
print len(global_word_list)
print len(global_reduced_freqs)


