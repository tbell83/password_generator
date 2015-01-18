from random import randint
import os

def generate_password():
	noun_list = open(os.path.join(os.path.dirname(__file__),'/usr/bin/my_site/my_site/application/nounlist.txt'))
	adjective_list = open(os.path.join(os.path.dirname(__file__),'/usr/bin/my_site/my_site/application/adjectives.txt'))
	verb_list = open(os.path.join(os.path.dirname(__file__),'/usr/bin/my_site/my_site/application/verbs.txt'))

	nouns = []
	adjectives = []
	verbs = []

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
	print nouns
	verb = verbs[randint(0,verb_count)].capitalize()
	adjective = adjectives[randint(0,adjective_count)].capitalize()
	noun = nouns[randint(0, noun_count)].capitalize()
	number = randint(10,99)

	passwd = "{0}{1}{2}{3}".format(verb,adjective,noun,number)
	return passwd
	

def gen_pass():
	nouns = open('/usr/bin/my_site/my_site/application/nounlist.txt')
	words = []

	for noun in nouns:
		words.extend([noun.translate(None, "\r\n ")])
	nouns.close()

	length = len(words)

	passwd = "{0}{1}{2}".format(words[randint(0,length)].capitalize(), words[randint(0,length)].capitalize(), randint(10,99))
	return passwd

print generate_password()
