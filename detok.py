#!/usr/bin/env python3

import json
import string
import sys
from mosestokenizer import MosesDetokenizer

detokenizer = MosesDetokenizer('en')

def fixTokenization(candidate):
    candidate = candidate.replace("do n't", "don't")
    candidate = candidate.replace("does n't", "doesn't")
    candidate = candidate.replace("did n't", "didn't")
    candidate = candidate.replace("is n't", "isn't")
    candidate = candidate.replace("are n't", "aren't")
    candidate = candidate.replace("was n't", "wasn't")
    candidate = candidate.replace("were n't", "weren't")
    candidate = candidate.replace("ca n't", "can't")
    candidate = candidate.replace("wo n't", "won't")
    candidate = candidate.replace("would n't", "wouldn't")
    candidate = candidate.replace("could n't", "couldn't")
    candidate = candidate.replace("must n't", "mustn't")
    candidate = candidate.replace("need n't", "needn't")
    candidate = candidate.replace('wan na', 'wanna')
    candidate = candidate.replace('gon na', 'gonna')
    candidate = candidate.replace('got ta', 'gotta')
    candidate = candidate.replace(' - ', '-')
    return candidate

def debpe(s):
    if s.endswith('@@'):
        s = s[:-2]
    return s.replace('@@ ', '')

if __name__ == '__main__':
    for line in sys.stdin:
        # Try to parse as JSON if the line starts with a {.
        # If it fails, drop down to treating it as raw text
        if line.startswith('{'):
            try:
                jobj = json.loads(line)
                for score, translation in zip(jobj['scores'], jobj['translations']):
                    print('{:.3f}'.format(score), fixTokenization(detokenizer(debpe(translation).split())), sep='\t', flush=True)
                continue
            except Exception:
                pass

        # Run if JSON parsing not relevant or fails
        line = line.rstrip()
        print(fixTokenization(detokenizer(debpe(line).split())), flush=True)

   
