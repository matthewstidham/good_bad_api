#!/usr/bin/env python3

import json

def main():
    d = json.load(open('bad_api.json'))
    entries = d['entries']
    
    print(entries)

    for entry in entries[1]:
        if 'author' in entry.keys():
            print(entry['author'])


    for entry in entries[0]:
        if 'book' in entry.keys():
            print(entry['book'])

    for entry in entries:
        for booker in entry:
            if 'book' in booker.keys():
                if booker['book'] == 'Dune':
                    for auth in entry:
                        if 'author' in auth.keys():
                            print(auth['author'])


if __name__ == "__main__":
   main()
