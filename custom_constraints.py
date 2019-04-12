#!/usr/bin/env python3

import spacy
import json
from subword_nmt.apply_bpe import *
from broadcast_factors import calcCapFactor, broadcast

candidate_sents = []
posCon_list = []
negCon_list = []

def tokenizeEngWithSpacy(en_input, return_str=False, spacy_model='en'): 
    if not 'spacy_nlp' in globals():
        global spacy_nlp
        spacy_nlp = None
    if spacy_nlp == None:
        spacy_nlp = spacy.load(spacy_model, disable=['ner', 'parse'])
    
    en_tokenized_list = []
    for token in spacy_nlp(en_input):
        en_tokenized_list.append(token.text)
    if return_str:
        return ' '.join(en_tokenized_list)
    else:
        return en_tokenized_list
    
def createJSON(text, src_bpe, trg_bpe, neg_lists=[], pos_lists=[], expand=True, factors=None):
    assert pos_lists == [] or neg_lists == [] or len(neg_lists) == len(pos_lists)
    conStr_list = []
    for i in range(max(len(neg_lists), len(pos_lists))):
        if neg_lists[i] == None or pos_lists[i] == None:
            obj = {'text': ''}
            conStr_list.append(json.dumps(obj, ensure_ascii=False))
            continue
        
        bpe_text = src_bpe.process_line(text)
        obj = {'text': bpe_text}
        if factors:
            new_factors = broadcast(bpe_text, factors, True)
            obj['factors'] = new_factors
        if len(neg_lists) != 0:
            neg_list_final = []
            for con in neg_lists[i]:
                # original word
                neg_list_final.append(trg_bpe.process_line(con))
                if expand:
                    # exclude the uppercased word
                    neg_list_final.append(trg_bpe.process_line(con.capitalize()))
            if len(neg_list_final) != 0:
                obj['avoid'] = neg_list_final
        if len(pos_lists) != 0:
            pos_list_final = []
            for con in pos_lists[i]:
                pos_list_final.append(trg_bpe.process_line(con))
            if len(pos_list_final) != 0:
                obj['constraints'] = pos_list_final
        conStr_list.append(json.dumps(obj, ensure_ascii=False))
    return conStr_list

if __name__ == '__main__':
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(
        description='Get the JSON file for decoding.',
        formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--output', help='Path to json output.', default='STDOUT')
    parser.add_argument('--BPE-codes', help='Path to BPE codes file.')
    parser.add_argument('--BPE-vocab', help='Path to BPE vocab file.')
    parser.add_argument('--compute-factor', action='store_true',
                        help='Compute BPE and Capitalization factors (use this for the new model).')
   
    args = parser.parse_args()
    
    fbpe_code = open(args.BPE_codes, 'r', encoding='UTF-8')
    fbpe_vocab_src = open(args.BPE_vocab+'.src.no_nbr', 'r', encoding='UTF-8')
    fbpe_vocab_trg = open(args.BPE_vocab+'.trg.no_nbr', 'r', encoding='UTF-8')
    bpe_vocab_src = read_vocabulary(fbpe_vocab_src, 50)
    bpe_vocab_trg = read_vocabulary(fbpe_vocab_trg, 50)

    bpe_src = BPE(fbpe_code, -1, '@@', bpe_vocab_src, None)
    bpe_trg = BPE(fbpe_code, -1, '@@', bpe_vocab_trg, None)

    all_sentences = []

    # read sentences from stdin
    for line in sys.stdin:
        sentence = line.strip()
        neg_constraints = []
        pos_constraints = []
        splitted_sent = sentence.split('\t')
        if len(splitted_sent) == 0:
            raise ValueError('wrong number of columns ' + str(sentence.split('\t')))
        if len(splitted_sent) >= 2:
            if splitted_sent[1] != '':
                neg_constraints = splitted_sent[1].split('|')
        if len(splitted_sent) >= 3:
            if splitted_sent[2] != '':
                pos_constraints = splitted_sent[2].split('|')
        sentence = sentence.split('\t')[0]
        
        en_line = tokenizeEngWithSpacy(sentence, return_str=True)
        
        factors = None
        if args.compute_factor:
            factors = []
            en_line, factor_cap = calcCapFactor(en_line)
            factors.append(factor_cap)
     
        print(createJSON(en_line, bpe_src, bpe_trg, \
                    neg_lists=[neg_constraints], pos_lists=[pos_constraints], \
                    expand=True, factors=factors)[0], flush=True)
