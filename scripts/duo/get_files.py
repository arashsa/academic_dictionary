import os
import subprocess
import urllib2
import random


class GetFiles():
    """Class for reading urls from duo[number].txt files, getting the pdf file and converting to txt."""
    def __init__(self):
        self.number_of_links = 0
        self.number_of_temp_pdf = random.randint(1, 1000000000)
        self.links = ''
        self.path = '/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/scripts/duo/'
        self.current_file = ''

    def read_urls_from_files(self):
        # Reads url from duo[number].txt files
        # for root, dirs, files in os.walk(self.path):
        #     for f in files:
        #         if 'txt' in f:
        self.links = 'duo' + '1100' + '.txt'
        link_file = open(self.path + self.links, 'r')
        for l in link_file.readlines():
            self.number_of_links += 1
            self.get_pdf(l)
            self.convert_to_pdf()
            os.remove(self.current_file)

        print 'Number of links in converted: {}'.format(self.number_of_links)

    def get_pdf(self, url):
        self.current_file = self.path + str(self.number_of_temp_pdf) + '.pdf'
        f = urllib2.urlopen(url)
        data = f.read()
        with open(self.current_file, "wb") as code:
            code.write(data)
            code.close()

    def convert_to_pdf(self):
        subprocess.call(['java', '-jar', '/Users/arashsaidi/Work/Tools/pdf-converter/pdfbox-app-1.8.6.jar',
                         'ExtractText', self.current_file,
                         '/Users/arashsaidi/Work/TextLab/Code/academic_dictionary/corpus/duo/' + self.links[:-4] +
                         '_' + str(self.number_of_links) + '.txt'])

test = GetFiles()
test.read_urls_from_files()