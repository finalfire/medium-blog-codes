from tinydb import TinyDB
import nltk
import nltk.tag.stanford as st

# tagger
tagger = st.StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')

# tinydb
db = TinyDB('characters.json')

# reading the book
with open('text') as f:
	text = [l.strip() for l in f][:-10]

# retrieving all of the characters
people = set()
current_index = 0

for i, sentence in enumerate(nltk.sent_tokenize(' '.join(text))):
	print('sentence n.', i)

	tokens = nltk.tokenize.word_tokenize(sentence)
	tags = tagger.tag(tokens)

	for t in tags:
		if t[1] == 'PERSON':
			if t[0] not in people:
				db.insert({'c': t[0], 'i': current_index})
				people.add(t[0])
				current_index += 1

