#!/usr/bin/env python

import json

def main():
    d = json.load(open('good_api.json'))
    entries = d['entries']

    print('books by Frank Herbert written before 1980')
    for entry in entries:
        if entry['copyright'] < 1980:
            if entry['author'] == 'Frank Herbert':
                print(entry['book'])
    
    print([entry for entry in entries if 
     entry['author'] == 'Frank Herbert' and 
     entry['copyright'] < 1980])

if __name__ == "__main__":
    main()
