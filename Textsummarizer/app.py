text = """Created by artist/writer Rob Liefeld and writer Fabian Nicieza,[13][14][15] Deadpool made his first appearance on the pages of The New Mutants #98 cover-dated Feb. 1991.[16] According to Nicieza, Liefeld came up with the character's visual design and name, and Nicieza himself came up with the character's speech mannerisms.[17]

Liefeld's favorite comic title before X-Men was Avengers, which featured weapons like Captain America's shield, Thor's hammer and Hawkeye's bow and arrow. Because of this, he also decided to give weapons to his new characters.[18] Liefeld, a fan of the Teen Titans comics, showed his new character to then-writer Fabian Nicieza. Upon seeing the costume and noting his characteristics (killer with super agility), Nicieza contacted Liefeld, saying, "This is Deathstroke from Teen Titans". Nicieza gave Deadpool the real name of "Wade Wilson" as an inside-joke to being "related" to "Slade Wilson", Deathstroke.[19]

Liefeld spoke on how the character was influenced by Spider-Man: "The simplicity of the mask was my absolute jealousy over Spider-Man and the fact that both of my buddies, [fellow Marvel artists] Erik Larsen and Todd McFarlane, would tell me, 'I love drawing Spider-Man. You just do an oval and two big eyes. You’re in, you’re out.' ... The Spider-Man I grew up with would make fun of you or punch you in the face and make small cracks. That was the entire intent with Deadpool. ... I specifically told Marvel, 'He's Spider-Man, except with guns and swords.' The idea was, he's a jackass."[20] Other inspirations were Wolverine and Snake Eyes. Liefeld states: "Wolverine and Spider-Man were the two properties I was competing with at all times. I didn't have those, I didn't have access to those. I had to make my own Spider-Man and Wolverine. That's what Cable and Deadpool were meant to be, my own Spider-Man and my own Wolverine."[21] "G.I. Joe was my first obsession. Those were the toys in the sandbox with me, kung fu grip, eagle eye, I had them all. G.I. Joe is a world of characters that I have always aspired to participate in. Snake Eyes was a profound influence on my creating Deadpool."[22]

Both Deadpool and Cable were also meant to be tied into Wolverine's history already from the start, as Liefeld describes: "Wolverine was my guy. If I could tie anything into Wolverine, I was winning." Like Wolverine, Deadpool is (or is thought to be) Canadian.[23][24] The original story had him joining the Weapon X program after being kicked out of the U.S. Army Special Forces and given an artificial healing factor based on Wolverine's, thanks to Dr. Emrys Killebrew, one of the hea"""
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
[token.text.lower() for token in doc if not token.is_stop and not token.is_punct and not token.like_num]

token1 = []
stopwords = list(STOP_WORDS)
allowed_pos = ['NOUN', 'PROPN', 'VERB', 'ADJ']
for token in doc:
    if token.text in stopwords or token.text in punctuation:
        continue
    if token.pos_ in allowed_pos:
        token1.append(token.text)
print(token1)
from collections import Counter

word_freq = Counter(token1)
max_frq = max(word_freq.values())

for word, freq in word_freq.items():
    word_freq[word] = freq / max_frq
    sent_token = [sent.text for sent in doc.sents]
sent_score = {}
for sent in sent_token:
    for word in sent.split():
        if word.lower() in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent] = word_freq[word]
            else:
                sent_score[sent] += word_freq[word]
import pandas as pd

pd.DataFrame(list(sent_score.items()), columns=['sentence', 'score'])
from heapq import nlargest
from collections import defaultdict

num_sent = 3
summary = nlargest(num_sent, sent_score, key=sent_score.get)
" ".join(summary)
print(summary)