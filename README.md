# MMboshi: Multilingual Mboshi Parallel Corpus
This is an extension of the Mboshi-French parallel corpus available at [besacier/mboshi-french-parallel-corpus](https://github.com/besacier/mboshi-french-parallel-corpus). The French portion of the corpus was translated into four other well-resourced languages (English, German, Portuguese, Spanish) using the [DeepL translation platform](https://www.deepl.com/translator).

### Content:
* This corpus is made of 5,130 aligned sentences in the following languages:
   + Mboshi (Bantu C25); audio files, phonetic transcriptions with segmentation information;
   + French; text (original translation made by linguists)
   + English; German; Portuguese; Spanish; text (translated from French using DeepL)

* Forced-alignment (word-level) between Mboshi and French;
* Pseudo phones (with and without gold silence information), extracted using ZRC recipe from [beer-asr/asr](https://github.com/beer-asr/beer);
* True phones, from the [limsi-align](https://github.com/besacier/mboshi-french-parallel-corpus/tree/master/forced_alignments_supervised_spkr/limsi-align).

The new ZRC reference is available [here](https://github.com/mzboito/ZRC_corpora).

### Citing:
The original paper for this corpus is available [here](http://arxiv.org/abs/1710.03501), while this extension was presented at [this paper](https://arxiv.org/abs/1910.05154).

Use this following bibtex for citing the mboshi-french-parallel-corpus:
~~~
@article{DBLP:journals/corr/abs-1710-03501,
  author    = {Pierre Godard and
               Gilles Adda and
               Martine Adda{-}Decker and
               Juan Benjumea and
               Laurent Besacier and
               Jamison Cooper{-}Leavitt and
               Guy{-}No{\"{e}}l Kouarata and
               Lori Lamel and
               H{\'{e}}l{\`{e}}ne Maynard and
               Markus M{\"{u}}ller and
               Annie Rialland and
               Sebastian St{\"{u}}ker and
               Fran{\c{c}}ois Yvon and
               Marcely Zanon Boito},
  title     = {A Very Low Resource Language Speech Corpus for Computational Language
               Documentation Experiments},
  journal   = {CoRR},
  volume    = {abs/1710.03501},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.03501},
  archivePrefix = {arXiv},
  eprint    = {1710.03501},
  timestamp = {Tue, 16 Jan 2018 11:17:17 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1710-03501},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
~~~

Use this following bibtex for citing the mmboshi corpus:
~~~
@article{boito2019does,
  title={How Does Language Influence Documentation Workflow? 
         Unsupervised Word Discovery Using Translations in Multiple Languages},
  author={Boito, Marcely Zanon and 
          Villavicencio, Aline and 
          Besacier, Laurent},
  journal={LIFT 2019},
  year={2019}
}
~~~
