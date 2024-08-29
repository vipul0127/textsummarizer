from flask import Flask, render_template, request
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

# Initialize Flask app
app = Flask(__name__)

# Load the small English NLP model from SpaCy
nlp = spacy.load('en_core_web_sm')


def summarize_text(text, num_sent=3):
    doc = nlp(text)

    # Remove stopwords and punctuation
    token1 = []
    stopwords = list(STOP_WORDS)
    allowed_pos = ['NOUN', 'PROPN', 'VERB', 'ADJ']
    for token in doc:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in allowed_pos:
            token1.append(token.text)

    # Calculate word frequencies
    word_freq = Counter(token1)
    max_frq = max(word_freq.values())

    for word in word_freq:
        word_freq[word] = word_freq[word] / max_frq

    # Calculate sentence scores
    sent_token = [sent.text for sent in doc.sents]
    sent_score = {}
    for sent in sent_token:
        for word in sent.split():
            if word.lower() in word_freq:
                if sent not in sent_score:
                    sent_score[sent] = word_freq[word.lower()]
                else:
                    sent_score[sent] += word_freq[word.lower()]

    # Get the summary
    summary = nlargest(num_sent, sent_score, key=sent_score.get)
    return " ".join(summary)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']
        num_sentences = int(request.form['num_sentences'])
        summary = summarize_text(text, num_sentences)
        return render_template('index.html', summary=summary, original_text=text)


if __name__ == '__main__':
    app.run(debug=True)
