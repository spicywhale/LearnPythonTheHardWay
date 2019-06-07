import random 
from urllib.request import urlopen 
import sys

WORLD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a calss named %%% that is-a %%%.",
    "class %%%(object):\n\tdef ___init__ (self, ***)":
        "class %%% has -a __init__ that takes self and @@@ params.",
    "class %%%(object): \n\t def ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance  of class %%%",
    "***.*** = '(@@@)'":
        "From *** get the function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True 
else:
    PHRASE_FIRST = False
    
#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.stip(), encoding="utf-8"))
    
    
def convert(snippit, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippit.count("%%%"))]
other_names = random.sample(WORDS, snippit.count("***"))
results = []
param_names = [] 