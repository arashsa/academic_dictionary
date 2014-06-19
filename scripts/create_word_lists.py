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

global_reduced_freqs = {}  # Dict of relative frequency

global_word_list_finished = []  # The preliminary finished list


def read_many_xml_in_one_file(filename, to_xml=' ', write_to_file=False):
    """Reads a file with many xml documents
    """
    global global_word_list_many_freq_lists

    with open(filename) as f:
        for line in f:
            to_xml += line
            if '</document>' in to_xml:
                # goes through each document and adds to list
                global_word_list_many_freq_lists.append(read_xml(to_xml, True, write_to_file))
                to_xml = ' '

    return global_word_list_many_freq_lists


def read_xml(filename, from_string=False, write_to_file=False):
    """Reads xml and strips tags
    creates a string with file, returns a frequency list of all the words in xml
    """
    # TODO: write the stripped xml to file for OBT (Oslo Bergen Tagger)
    if write_to_file:
        pass

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
    """Reads a text file and sends it to create_word_list method
    """
    file_object = open(filename, 'r')
    file_as_string = file_object.read()
    return create_word_list(file_as_string)


def create_word_list(text_as_string):
    """Creates a list of all the words, without punctuation
    adds words to global_word_list
    increments tokens for each added token to global_word_list
    Returns the word list for all documents read in one session
    """
    global global_word_list

    for w in text_as_string.split():
        word = w.translate(string.maketrans("", ""), string.punctuation).lower()
        if len(word) > 0:
            global_word_list.append(word)  # Appends each word to global word list

    return global_word_list


def reduced_frequency():
    """The swedish method taken from the article: 'An Academic Word List for Swedish
    A summation of frequencies of a word in a document given a range
    """
    global global_word_list
    global global_reduced_freqs

    doc_length = len(global_word_list)
    freq_list = count_words(global_word_list)  # Calls count_words()

    for (w, freq) in freq_list.items():
        global_reduced_freqs[w] = 0
        interval = doc_length / freq
        if interval != doc_length:
            for i in range(0, doc_length, interval):
                global_reduced_freqs[w] += 1
        else:
            global_reduced_freqs[w] = 1


def count_words(word_list, print_words=False):
    """Creates a dictionary with frequency of each word
    """
    freq_dist = Counter(word_list)
    global global_word_freq_list

    if print_words:
        for (word, freq) in freq_dist.items():
            print('{:25}{:10}'.format(word, freq))

    global_word_freq_list = freq_dist.copy()
    return freq_dist


def remove_most_frequent_words():
    """Should only be run once reduce_frequency method has been run
    removes both from global_word_list and global_relative_freqs
    """
    global most_frequent_words
    global global_reduced_freqs
    global global_word_list

    if not most_frequent_words:
        with open('../1000_hifreq_lemmas_forms.txt') as fp:
            for line in fp:
                most_frequent_words.append(re.sub(r'\s+', '', line))

    for w in most_frequent_words:
        if w in global_word_list:
            global_word_list.remove(w)
        if w in global_reduced_freqs:
            del global_reduced_freqs[w]


# GETTERS (for testing)
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