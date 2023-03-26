#!/usr/bin/env python3

import json

def main():
    d = json.load(open('bad_api.json'))
    entries = d['entries']
    
    print(entries)

    for entry in entries[1]:
        if list(entry.keys())[0] == 'author':
            print(entry['author'])


    for entry in entries[0]:
        if list(entry.keys())[0] == 'book':
            print(entry['book'])

    for entry in entries:
        book = ''
        for booker in entry:
            if list(booker.keys())[0] == 'book':
                book = booker['book']
        if book == 'Dune':
            for auth in entry:
                if list(auth.keys())[0] == 'author':
                    print(auth['author'])


if __name__ == "__main__":
   main()
