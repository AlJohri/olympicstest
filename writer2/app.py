import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "SimpleNLG-4.4.8.jar"))

from simplenlg.framework import NLGFactory, CoordinatedPhraseElement, ListElement, PhraseElement
from simplenlg.lexicon import Lexicon
from simplenlg.realiser.english import Realiser
from simplenlg.features import Feature, Tense, NumberAgreement
from simplenlg.phrasespec import NPPhraseSpec

from java.lang import Boolean

lexicon = Lexicon.getDefaultLexicon()
nlgFactory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

print("hello world")

p = nlgFactory.createSentence("my dog is happy")
sentence = realiser.realiseSentence(p)
print(sentence)

p = nlgFactory.createClause()
p.setSubject("Mary")
p.setVerb("chase")
p.setObject("the monkey")

sentence2 = realiser.realiseSentence(p)
print(sentence2)
