from random import randint

def gen_pass():
	nouns = open('/usr/bin/my_site/my_site/application/nounlist.txt')
	words = []

	for noun in nouns:
		words.extend([noun.replace("\n", "")])
	nouns.close()

	length = len(words)

	passwd = "{0}{1}{2}".format(words[randint(0,length)].capitalize(), words[randint(0,length)].capitalize(), randint(10,99))
	return passwd

gen_pass()
