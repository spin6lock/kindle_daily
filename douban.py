#encoding:utf8
import requests
from config import douban_url
import json

def get_douban_rating(title):
    resp = requests.get(douban_url+title)
    result = resp.json()
    if len(result["books"]) > 0:
        first_match = result["books"][0]
        average = first_match["rating"]["average"]
        return average
    else:
        return 0

def main():
    with open('today_book.json', 'r') as fin:
        books = json.loads(fin.read())
        for book in books:
            book['douban_rating'] = get_douban_rating(book["title"])
    with open('today_book_douban.json', 'w') as fout:
        fout.write(json.dumps(books))

if __name__ == '__main__':
    main()
