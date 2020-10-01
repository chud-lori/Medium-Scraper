"""
Medium Scraper will scrape a document from medium blog
"""
import pprint as pp
import requests
import feedparser
import xml.etree.ElementTree as ET

# define blog url
BLOG_URL = "https://medium.com/feed/@chud_lori"


def load_RSS(url):
    """Load rss"""

    # load rss
    root = feedparser.parse(url)

    return root


def handle_RSS(rss):
    pass


def main():
    # load rss from web to update existing xml file
    RSS = load_RSS(BLOG_URL)

    # parse xml file
    # news_items = handle_RSS(RSS)

    # return news_items


def test():
    """debugging"""
    # create element tree object
    tree = feedparser.parse(BLOG_URL)
    # print('Title: ', end='')
    # print(tree.entries[0].title)
    # print('-'*60)
    # pp.pprint(tree.entries[0].link)

    for i, _ in enumerate(tree.entries):
        print('Title: ', end='')
        print(tree.entries[i].title)
        print('Link: ', end='')
        print(tree.entries[i].link)
        print('-'*60)

    # get root element
    # root = tree.getroot()


if __name__ == "__main__":

    # calling main function
    # main()
    # testing function
    test()
