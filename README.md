This is the improvered rewriter model described in Hu et al. 2019b.

Required packages are listed in `requirement.txt`. Please download `params.best` from the project website and place it under this directory.

Usage: `echo -e "This is a test.\tis|test\twas|exam" | ./paraphrase.sh`, where "is" and "test" are negative constraints, and "was" and "exam" are positive constraints.

Please cite the following papers if you would like to use this rewriter in your work:

> Hu, J. E., R. Rudinger, M. Post, & B. Van Durme. 2019a. [ParaBank: Monolingual Bitext Generation and Sentential Paraphrasing via Lexically-constrained Neural Machine Translation](http://aaai.org/Papers/AAAI/2019/AAAI-HuJ.4052.pdf). Proceedings of AAAI 2019, Honolulu, Hawaii, January 26 – Feb 1, 2019.
> Hu, J. E., H. Khayrallah, R. Culkin, P. Xia, T. Chen, M. Post, & B. Van Durme. 2019b. [Improved Lexically Constrained Decoding for Translation and Monolingual Rewriting](TBD). Proceedings of NAACL 2019, Minneapolis, Minnesota, June 2 – 7, 2019.


To interact with the improved monolingual rewriter online, [please check out this live demo](http://cs.jhu.edu/~vandurme/pbr-1b-demo).
