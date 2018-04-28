#encoding=utf8
import requests
from lxml import html
import json

import config

def booklist_jsonify(books):
    result = []
    for book in books:
        img_src = book.xpath('.//img/@src')[0]
        title = book.xpath('./div[@class="productTitle"]/a')[0].text
        author = book.xpath('./div[@class="productByLine"]')[0].text.strip()
        price = book.xpath('.//span[@class="a-color-price"]/text()')[0]
        relative_link = book.xpath('.//a[@class="a-link-normal"]/@href')[0]
        link = config.base_url + relative_link
        book_dict = {
            "img_src":img_src,
            "title":title,
            "author":author,
            "price":price,
            "link":link,
        }
        result.append(book_dict) 
    return json.dumps(result)

def main():
    resp = requests.get(config.daily_url)
    tree = html.fromstring(resp.content)
    books = tree.xpath('//div[@class="gridProductContainer"]')
    js_result = booklist_jsonify(books)
    with open("today_book.json", 'w') as fout:
        fout.write(js_result)
    
if __name__ == '__main__':
    main()
