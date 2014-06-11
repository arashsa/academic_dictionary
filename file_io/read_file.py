# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'arashsaidi'

import string
import xml.etree.ElementTree as ElTree
from lxml import etree
from collections import Counter
import re

many_freq_lists = []


def read_many_xml(filename, to_xml=' '):
    """Reads a file with many xml documents"""
    global many_freq_lists

    with open(filename) as f:
        for line in f:
            to_xml += line
            if '</document>' in to_xml:
                many_freq_lists.append(read_xml(to_xml, True))
                to_xml = ' '

    return many_freq_lists


def read_xml(filename, from_string=False):
    """Reads xml and strips tags
    creates a string with file, returns a frequency list of all the words in xml"""

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
    return create_word_list(filename)


def create_word_list(text_as_string):
    """Creates a list of all the words, without punctuation"""
    word_list = []

    for w in text_as_string.split():
        word = w.translate(string.maketrans("", ""), string.punctuation).lower()
        if len(word) > 0:
            word_list.append(word)

    return count_words(word_list)


def count_words(word_list, print_words=False):
    """Creates a dictionary with frequency of each word"""
    freq_dist = Counter(word_list)

    if print_words:
        for (word, freq) in freq_dist.items():
            print('{}: {}'.format(word, freq))

    return freq_dist