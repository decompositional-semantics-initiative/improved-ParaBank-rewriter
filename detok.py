#!/usr/bin/env python3

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

if __name__ == '__main__':
    for line in sys.stdin:
        splitted = line.strip('\n')
        splitted = fixTokenization(detokenizer(splitted.split()))
        print(splitted)
   
