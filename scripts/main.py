__author__ = 'arashsaidi'

from create_word_lists import *
from printing import *

# print len(get_word_list())

freq_list = read_xml('../corpus/kiap-norsk-xml/noecon01.xml')
ml = get_global_word_list()
fq = get_global_word_freq_list()

print_simple_list(ml)
print_count_object(fq)