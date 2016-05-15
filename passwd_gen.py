from random import randint
import os,sys

def generate_password():
    noun_list = open(os.path.join(os.path.dirname(__file__),'./application/nounlist.txt'))
    adjective_list = open(os.path.join(os.path.dirname(__file__),'./application/adjectives.txt'))
    verb_list = open(os.path.join(os.path.dirname(__file__),'./application/verbs.txt'))

    nouns = []
    adjectives = []
    verbs = []
    symbols = ['!','@','#','$','%','^','&','*','-','_','+']

    for noun in noun_list:
        nouns.extend([noun.translate(None, "\r\n ")])
    noun_list.close()

    for adjective in adjective_list:
        adjectives.extend([adjective.translate(None, "\r\n ")])
    adjective_list.close()

    for verb in verb_list:
        verbs.extend([verb.translate(None, "\r\n ")])
    verb_list.close()

    noun_count = len(nouns)
    adjective_count = len(adjectives)
    verb_count = len(verbs)
    symbol_count = len(symbols)
    
    verb = verbs[randint(0,verb_count)].capitalize()
    adjective = adjectives[randint(0,adjective_count)].capitalize()
    noun = nouns[randint(0, noun_count)].capitalize()
    number = randint(10,99)
    symbol = symbols[randint(0,symbol_count)]

    passwd = "{0}{1}{2}{3}{4}".format(verb,adjective,noun,symbol,number)
    return passwd
