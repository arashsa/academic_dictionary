import os
import random


def read_files(path='/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/DUO_Corpus'):
    """ Renames txt files in a given path
    :param path: Path to files
    :return:
    """
    for root, dirs, files in os.walk(path):
        # Goes through files and sends them to check_language
        for f in files:
            if '.txt' in f:
                current_path_to_file = os.path.join(root, f)
                # print(current_path_to_file)
                random_int = random.randint(0, 99999999)
                os.rename(current_path_to_file, 'DUO_BM_' + str(random_int) + '.txt')

read_files()