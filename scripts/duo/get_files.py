import os
import subprocess
import urllib2
import random
import time


class GetFiles():
    """Class for reading urls from duo[number].txt files, getting the pdf file and converting to txt."""
    def __init__(self):
        self.number_of_links = 0
        self.total_number_of_links = 0
        self.number_of_temp_pdf = random.randint(1, 1000000000)
        self.links = ''
        self.path = '/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/scripts/duo/'
        self.current_file = ''

        # Start file (duo[number])
        self.range = 19400
        # Until this file
        self.range_end = 20000
        # Folder to save in
        self.save_txt_folder = '191-200/'

        # Start file (duo[number])
        # self.range = 191
        # self.range *= 100
        # # Until this file
        # self.range_end = self.range + 900
        # # Folder to save in
        # self.save_txt_folder = str(self.range)[0:3] + '-' + str(self.range_end)[0:3] + '/'

    def print_test(self):
        print "from: {}. to: {}. folder: {}".format(self.range, self.range_end, self.save_txt_folder)

    def read_urls_from_files(self):
        # Reads url from duo[number].txt files
        # for root, dirs, files in os.walk(self.path):
        #     for f in files:
        #         if 'txt' in f:
        print self.save_txt_folder
        while self.range <= self.range_end:
            self.links = 'duo' + str(self.range) + '.txt'
            link_file = open(self.path + self.links, 'r')
            for l in link_file.readlines():
                self.number_of_links += 1
                self.total_number_of_links += 1
                self.get_pdf(l)
                self.convert_to_pdf()
                os.remove(self.current_file)
            self.number_of_temp_pdf = random.randint(1, 1000000000)
            self.range += 100
            self.number_of_links = 0

        print 'Number of links in converted: {}'.format(self.total_number_of_links)
        self.print_test()

    def get_pdf(self, url):
        """Tries to download and convert pdf to txt"""
        self.current_file = self.path + str(self.number_of_temp_pdf) + '.pdf'

        try:
            f = urllib2.urlopen(url)
        except urllib2.URLError or urllib2.HTTPError:
            f = None

        if f:
            data = f.read()
        else:
            data = ''

        with open(self.current_file, "wb") as code:
            code.write(data)
            code.close()

    def convert_to_pdf(self):
        subprocess.call(['java', '-jar', '/Users/arashsaidi/Work/Tools/pdf-converter/pdfbox-app-1.8.6.jar',
                         'ExtractText', self.current_file,
                         '/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/duo/' + self.save_txt_folder +
                         self.links[:-4] + '_' + str(self.number_of_links) + '.txt'])

test = GetFiles()
time.sleep(60)
test.print_test()
test.read_urls_from_files()