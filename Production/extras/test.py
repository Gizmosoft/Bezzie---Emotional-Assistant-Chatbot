import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

ex = 'I had a very bad day at office today. Shashank, my boss, does not even appreciate my work and keeps on burdening me with extra work. Today he scolded me in front of everyone. That is very sad!'

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
print(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print(cs)
iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)
