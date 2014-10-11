from HTMLParser import HTMLParser
import glob


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attributes):
    #     print "Encountered a start tag:", tag
    #
    # def handle_endtag(self, tag):
    #     print "Encountered an end tag :", tag

    text = []

    def handle_data(self, data):
        self.text.append(data)


# instantiate the parser and fed it some HTML
def parse_xml_to_list_of_words(doc):
    parser = MyHTMLParser()
    parser.feed(doc)
    print parser.text
    return parser.text


def read_all_xml(p):
    # Reads all files in a path
    path = p
    files = glob.glob(path)

    for name in files:
        word_list = parse_xml_to_list_of_words(name)
        word_list_as_string = ''.join(word_list)

