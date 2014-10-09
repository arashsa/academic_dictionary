import os


class GetFiles():
    """Class for reading urls from duo[number].txt files, getting the pdf file and converting to txt."""
    def __init__(self):
        self.number_of_links = 0

    def read_urls_from_files(self, path='/'):
        for root, dirs, files in os.walk(path):
            for f in files:
                print f
                self.number_of_links += 1

test = GetFiles()
test.read_urls_from_files()