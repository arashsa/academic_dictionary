# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'arashsaidi'

import string
import xml.etree.ElementTree as ElTree
from lxml import etree
from collections import Counter
import re

most_frequent_words = []  # List of most frequent words taken from file

global_word_list = []  # The word_list as read from file(s)

global_word_freq_list = {}  # List of frequencies for one xml/text document
global_word_list_many_freq_lists = []  # Frequency list of many xml/text documents

global_word_list_relative_frequent_words = []  # List of words with relative frequent words removed
global_word_list_most_frequent_removed = []  # List of words that have been read, most frequent words removed

global_word_list_finished = []  # The preliminary finished list


def read_many_xml_in_one_file(filename, to_xml=' '):
    """Reads a file with many xml documents"""
    global global_word_list_many_freq_lists

    with open(filename) as f:
        for line in f:
            to_xml += line
            if '</document>' in to_xml:
                # goes through each document and adds to list
                global_word_list_many_freq_lists.append(read_xml(to_xml, True))
                to_xml = ' '

    return global_word_list_many_freq_lists


def read_xml(filename, from_string=False):
    """Reads xml and strips tags
    creates a string with file, returns a frequency list of all the words in xml"""
    # TODO: write the stripped xml to file for OBT (Oslo Bergen Tagger)
    if from_string:
        try:
            tree = ElTree.fromstring(filename)
            no_tags = ElTree.tostring(tree, encoding='utf8', method='text')
        except Exception as inst:
            return {'Error reading xml': inst}
    else:
        tree = etree.parse(filename)
        no_tags = etree.tostring(tree, encoding='utf-8', method='text')
        no_tags = re.sub(ur'[^a-zA-Z0-9]', ' ', no_tags, re.UNICODE)

    return create_word_list(no_tags)


def read_txt(filename):
    """Reads a text file and sends it to create_word_list method"""
    file_object = open(filename, 'r')
    file_as_string = file_object.read()
    return create_word_list(file_as_string)


def create_word_list(text_as_string):
    """Creates a list of all the words, without punctuation
    adds words to global_word_list
    increments tokens for each added token to global_word_list
    Returns the word list for all documents read in one session"""
    global global_word_list

    for w in text_as_string.split():
        word = w.translate(string.maketrans("", ""), string.punctuation).lower()
        if len(word) > 0:
            global_word_list.append(word)  # Appends each word to global word list

    return global_word_list


def count_words(word_list, print_words=False):
    """Creates a dictionary with frequency of each word"""
    freq_dist = Counter(word_list)
    global global_word_freq_list

    if print_words:
        for (word, freq) in freq_dist.items():
            print('{}: {}'.format(word, freq))

    global_word_freq_list = freq_dist.copy()
    return freq_dist


def reduced_frequency():
    """The swedish method taken from the article: 'An Academic Word List for Swedish'"""
    pass


def remove_most_frequent_words():
    """Should only be run once reduce_frequency method has been run
    Otherwise the method will not run"""
    global global_word_list_most_frequent_removed
    global most_frequent_words
    global global_word_list_relative_frequent_words

    if not most_frequent_words:
        with open('../1000_hifreq_lemmas_forms.txt') as fp:
            for line in fp:
                most_frequent_words.append(re.sub(r'\s+', '', line))

    if global_word_list_relative_frequent_words:
        for w in global_word_list_relative_frequent_words:
            if w not in most_frequent_words:
                global_word_list_most_frequent_removed.append(w)


# GETTERS: Various global lists
# Mainly for testing
def get_global_word_list():
    if global_word_list:
        return global_word_list
    else:
        return 'global_word_list is empty'


def get_global_word_list_many_freq_lists():
    if global_word_list_many_freq_lists:
        return global_word_list_many_freq_lists
    else:
        return 'global_word_list_many_freq_lists is empty'


def get_global_word_list_relative_frequent_words_removed():
    if global_word_list_relative_frequent_words:
        return global_word_list_relative_frequent_words
    else:
        return 'global_word_list_relative_frequent_words_removed is empty'


def get_global_word_list_most_frequent_removed():
    if global_word_list_most_frequent_removed:
        return global_word_list_most_frequent_removed
    else:
        return 'global_word_list_most_frequent_removed is empty'


def get_global_word_freq_list():
    if global_word_freq_list:
        return global_word_freq_list
    else:
        return 'global_word_freq_list is empty'


def get_finished_list():
    if global_word_list_finished:
        return global_word_list_finished
    else:
        'global_word_list_finished is empty'