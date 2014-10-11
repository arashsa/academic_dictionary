# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


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

        self.bm_count = 0
        self.nn_count = 0
        self.en_count = 0

    def read_files(self, path='/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/duo/1-10/'):
        """ Recursively traverses all files

        :param path: path to corpus
        :return: None
        """
        for root, dirs, files in os.walk(path):
            # Goes through files and sends them to check_language
            for f in files:
                if '.txt' in f:
                    current_path_to_file = os.path.join(root, f)
                    current_file = open(current_path_to_file, 'r')
                    self.check_language(current_file)

    def check_language(self, text_file):
        """ Checks words in file for occurrences in lists
        :param text_file: The current text_file
        :return: None
        """
        test_count = 0
        first_lines = ''
        for line in text_file.readlines():
            if test_count < 10:
                first_lines += line
                test_count += 1
            for word in line.split():
                lower_case = word.lower()
                if lower_case in self.bm:
                    self.bm_count += 1
                elif lower_case in self.nn:
                    self.nn_count += 1
                elif lower_case in self.en:
                    self.en_count += 1

        self.move_file(text_file, first_lines)

    def move_file(self, text_file, first_lines=''):
        print "For file: {}".format(first_lines)
        print "bm count: {} \nnn count: {} \nen count: {}".format(self.bm_count, self.nn_count, self.en_count)
        self.bm_count = 0
        self.nn_count = 0
        self.en_count = 0
        time.sleep(7)

test = Detection()
test.read_files()