__author__ = 'arashsaidi'

from create_word_lists import read_xml, read_txt
import glob


def read_all_files(p, ending):
    # reads all files in a folder:
    # Example of usage: read_all_files('/folder/*.xml', 'xml')
    path = p
    files = glob.glob(path)
    for name in files:
        # read_current_file returns a frequency distribution
        print 'Reading file: ' + name
        read_current_file(name, ending)


def read_current_file(f, ending):
    # calls methods according to file type
    if ending == 'xml':
        read_xml(f)
    elif ending == 'txt':
        read_txt(f)
    else:
        print 'ERROR: Do not support type of file'

