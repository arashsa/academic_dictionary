import requests


class ReadDUO():
    def __init__(self, url='https://www.duo.uio.no/oai/request?verb=ListRecords&resumptionToken=0001-01-01T00:00:'
                           '00Z/9999-12-31T23:59:59Z//oai_dc/'):
        self.url = url
        self.start = 100

    def read_from_url(self):
        while True:
            self.write_url_to_file()
            self.start += 100

    def write_url_to_file(self):
        """Reads a set of URLs and extracts links to DUO files
        This will download all urls pointing to the pdf files on DUO"""
        f = requests.get(self.url + str(self.start))
        html = f.text.encode('utf8').split()
        html_len = len(html)

        file_object = open('duo' + str(self.start) + '.txt', 'w')

        for w in range(html_len):
            if 'Fulltext' in html[w] and (w + 1) < html_len:
                try:
                    end = html[w + 1].index('pdf')
                except ValueError:
                    end = False

                if end:
                    link = html[w + 1][:end + 3] + '\n'
                    file_object.write(link)

        file_object.close()

test = ReadDUO()
test.read_from_url()