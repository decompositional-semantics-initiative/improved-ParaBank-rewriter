# Improved Monolingual Rewriter

This is the rewriter described in our paper:

> @inproceedings{N18-1007,
>   title = "Improved Lexically Constrained Decoding for Translation and Monolingual Rewriting",
>   author = "Hu, J. Edward and Khayrallah, Huda and Culkin, Ryan and Xia, Patrick and Chen, Tongfei and Post, Matt and Van Durme, Benjamin",
>  booktitle = "Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
>  month = jun,
>  year = "2019",
>  address = "Minneapolis, Minnesota",
>  publisher = "Association for Computational Linguistics",

It is available from

   https://github.com/decompositional-semantics-initiative/improved-ParaBank-rewriter/releases

You can also interact with it using [our online demo](http://cs.jhu.edu/~vandurme/pbr-1b-demo).

## Installation

After downloading the release, unpacking it, and changing to that directory, run the following command:

    pip3 install -r requirements.txt

You may also have to install spacy models:

    python3 -m spacy download en
    python3 -m spacy download en_core_web_lg

## Usage

The rewriter takes raw, unprocessed input and returns the same.
It applies all the pre-processing automatically, and undoes it afterwards.
To run the pipeline, use the `paraphrase.sh` script:

Usage:

    cat sentences.txt | /path/to/rewriter/paraphrase.sh > paraphrases.txt

It uses Sockeye internally, so takes many Sockeye options.
By default, Sockeye looks for a GPU.
You can use a CPU instead by passing

    paraphrase.sh --use-cpu

To change the beam or batch sizes, use the `--beam-size X` and `--batch-size Y` options.
You can set the GPU device with `--device-ids N`, where `N` is a 0-indexed CUDA device ID.

To get n-best output, use

   paraphrase.sh --nbest-size K

Finally, you can experiment with negative and positive constraints by passing them in as the second and third tab-delimited field, respectively.
Separate constraints are separated by a bar.
For example, 

```bash
echo -e "In times like this, one takes one’s happiness where one can find it.\tfortune|happiness|chances" | ./paraphrase.sh
```

will use *fortune*, *happiness*, and *chances* as negative constraints.
Positive constraints could be added with the use of a third field.
