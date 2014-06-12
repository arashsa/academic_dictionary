from main_functions import setup
from main_functions import read_xml
from main_functions import get_word_list_most_frequent_removed

# print len(get_word_list())

setup()  # sets up the project
freq_list = read_xml('../corpus/kiap-norsk-xml/noecon01.xml')

current_list = get_word_list_most_frequent_removed()