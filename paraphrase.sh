#!/bin/bash

MODEL_PATH=$(dirname $0)
BPE_CODES="$MODEL_PATH/bpe.codes"
BPE_VOCAB="$MODEL_PATH/bpe.vocab"

python3 $MODEL_PATH/custom_constraints.py \
    --BPE-codes $BPE_CODES \
    --BPE-vocab $BPE_VOCAB \
    --compute-factor \
| \
    python3 -m sockeye.translate \
      -m $MODEL_PATH \
      --json-input \
      --output-type json \
      --beam-size 20 \
      --beam-prune 20 \
      --batch-size 10 \
      --device-ids 0 \
      --disable-device-locking \
      "$@" \
| ${MODEL_PATH}/detok.py
