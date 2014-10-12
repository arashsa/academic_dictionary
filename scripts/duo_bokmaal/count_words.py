# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import nltk


def count_words():
    """ Two different methods (one commented out) for counting words in a set of documents.
    First is more precise, but quite slow.
    :return: None
    """
    info = open('/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/DUO_Corpus/info_bm.txt', 'w')
    documents = 0
    words = 0
    for root, dirs, files in os.walk(
            '/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/DUO_Corpus/Bokmaal/'):
        for f in files:
            documents += 1
            if 'txt' in f:
                # Slow but precise word count
                # current_path_to_file = os.path.join(root, f)
                # current_file = open(current_path_to_file, 'r').read()
                # items = current_file.decode('utf-8')
                # tokens = nltk.word_tokenize(items)
                # words += len(tokens)

                # Fast but not precise word count
                current_path_to_file = os.path.join(root, f)
                current_file = open(current_path_to_file, 'r').read().split()
                words += len(current_file)

    info.write('Bokmaal Corpus: \n')
    info.write('Number of documents: {}\n'.format(documents))
    info.write('Number of words: {}\n'.format(words))
    info.close()

count_words()