#!/usr/bin/env python

import json

def main():
    d = json.load(open('bad_api.json'))
    entries = d['entries']

    print('books by Frank Herbert before 1980')
    for entry in entries:
        for d in entry:
            if 'author' in d:
                if d['author'] == 'Frank Herbert':
                    for beta in entry:
                        if 'copyright' in beta:
                            if beta['copyright'] < 1980:
                                print(entry)

if __name__ == "__main__":
    main()
