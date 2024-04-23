import re
from collections import Counter
from nltk.corpus import stopwords

def process_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    return words

def count_word_frequency(words):
    return Counter(words)

def main():
    with open('paragraphs.txt', 'r') as file:
        text = file.read()
    
    processed_text = process_text(text)
    word_frequency = count_word_frequency(processed_text)
    
    for word, frequency in word_frequency.items():
        print(f'{word}: {frequency}')


main()
