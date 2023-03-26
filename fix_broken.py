#!/usr/bin/env python3

import json
from collections import ChainMap

def dict_merger(entries):
    result = dict()
    for entry in entries:
        for d in entry:
            if d in result.keys():
                if type(result[d]) == list:
                    result[d].append(result[d])
                else:
                    result[d] = [result[d]]+[entry[d]]
            else:
                result[d] = entry[d]
    return result

def main():
    d = json.load(open('bad_api.json'))
    # entries = list()
    # for entry in d['entries']:
    #     entries.append(dict_merger(entry))
    entries = [dict_merger(entry) for entry in d['entries']]

    print(entries)
    print(entries[1]['author'])
    print(entries[0]['book'])

    for x in entries:
        if x['book'] == 'Dune':
            print(x['author'])
    


if __name__ == "__main__":
   main()
