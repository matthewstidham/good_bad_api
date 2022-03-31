#!/usr/bin/env python3

import json

def main():
    d = json.load(open('bad_api.json'))
    print(d)

    entries= d['entries']
    print([x for x in entries[1] if list(x.keys())[0] == 'author'][0]['author'])
    print([x for x in entries[0] if list(x.keys())[0] == 'book'][0]['book'])

if __name__ == "__main__":
   main()
