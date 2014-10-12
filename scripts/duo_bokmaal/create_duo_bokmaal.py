# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil


class Detection():
    """A simple method for detecting English, Norwegian (bokmaal and nynorsk).
    The method simply counts words
    """
    def __init__(self):
        # list from http://omilia.uio.no/frekvenser/index.php
        # bokmaal freq list
        # 'vi', 'vil', 'så', 'skal', 'også', 'etter', 'ble', 'ved', 'dette'
        self.bm = ['en', 'de', 'ikke', 'et', 'fra', 'kan', 'jeg', 'seg']

        # list from http://omilia.uio.no/frekvenser/index.php
        # nyorsk freq list
        self.nn = ['ikkje', 'dei', 'ein', 'ho', 'eg', 'eit', 'frå', 'berre']

        # list from http://www.wordfrequency.info/top5000.asp
        # english freq list
        # 'that', 'you', 'he', 'with', 'on', 'do', 'say', 'this', 'they', 'but', 'we', 'his', 'from', 'that', 'not',
        # 'by', 'she', 'or', 'as', 'what'
        self.en = ['the', 'be', 'and', 'of', 'in', 'to', 'have', 'it']

        self.word_count_en_bm_nn = {'en': 0,
                      'bm': 0,
                      'nn': 0}

        self.en_count = 0
        self.bm_count = 0
        self.nn_count = 0
        self.corrupt_count = 0
        self.all_count = 0

        self.info = open('info.txt', 'w')

    def read_files(self, path='/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/duo/'):
        """ Recursively traverses all files in the path

        :param path: path to corpus
        :return: None
        """
        for root, dirs, files in os.walk(path):
            # Goes through files and sends them to check_language
            for f in files:
                if '.txt' in f:
                    current_path_to_file = os.path.join(root, f)
                    current_file = open(current_path_to_file, 'r')
                    self.check_language(current_file, current_path_to_file)

    def check_language(self, text_file, path_to_file):
        """ Checks words in file for occurrences in lists
        :param text_file: The current text_file
        :return: None
        """
        for line in text_file.readlines():
            for word in line.split():
                lower_case = word.lower()
                if lower_case in self.bm:
                    self.word_count_en_bm_nn['bm'] += 1
                elif lower_case in self.nn:
                    self.word_count_en_bm_nn['nn'] += 1
                elif lower_case in self.en:
                    self.word_count_en_bm_nn['en'] += 1

        self.move_file(path_to_file)

    def move_file(self, path_to_file):

        key = max(self.word_count_en_bm_nn, key=self.word_count_en_bm_nn.get)
        # print "largest {}\n".format(key)

        if self.word_count_en_bm_nn[key] < 50:
            # print "File may be corrupted"
            # self.write_info(current_file)
            self.corrupt_count += 1
            filename = 'DUO_Corrupt_' + str(self.corrupt_count) + '.txt'
            shutil.copyfile(path_to_file, "../../corpus/DUO_Corpus/Corrupted/" + filename)
        elif key == 'bm':
            self.bm_count += 1
            filename = 'DUO_BM_' + str(self.bm_count) + '.txt'
            shutil.copyfile(path_to_file, "../../corpus/DUO_Corpus/Bokmaal/" + filename)
        elif key == 'nn':
            self.nn_count += 1
            filename = 'DUO_NN_' + str(self.nn_count) + '.txt'
            shutil.copyfile(path_to_file, "../../corpus/DUO_Corpus/Nynorsk/" + filename)
        elif key == 'en':
            self.en_count += 1
            filename = 'DUO_English_' + str(self.en_count) + '.txt'
            shutil.copyfile(path_to_file, "../../corpus/DUO_Corpus/English/" + filename)

        # if self.all_count % 100 == 0:
        #     self.write_info(current_file)

        self.word_count_en_bm_nn['bm'] = 0
        self.word_count_en_bm_nn['nn'] = 0
        self.word_count_en_bm_nn['en'] = 0
        self.all_count += 1

    def write_info(self):
        self.info.write("-" * 30)
        self.info.write("DUO corpus:")
        self.info.write("English articles: {}\nBM articles: {}\nNN articles: {}\nCorrupt articles: {}".format(
            test.en_count,
            test.bm_count,
            test.nn_count,
            test.corrupt_count))
        self.info.write("-" * 30)

test = Detection()
test.read_files()
print "English articles: {}\nBM articles: {}\nNN articles: {}\nCorrupt articles: {}".format(test.en_count,
                                                                                            test.bm_count,
                                                                                            test.nn_count,
                                                                                            test.corrupt_count)