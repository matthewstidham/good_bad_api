#!/usr/bin/env python3

import json

def main():
    d = json.load(open('good_api.json'))
    print(d)

    entries = d['entries']
    print(entries[1]['author'])
    print(entries[0]['book'])

    for x in entries:
        if x['book'] == 'Dune':
            print(x['author'])

if __name__ == "__main__":
   main()
