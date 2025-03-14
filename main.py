import requests
import re
from collections import defaultdict
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from functools import reduce
import operator

def fetch_text_from_url(url):
    response = requests.get(url)
    return response.text

def map_reduce(text):
    words = re.findall(r'\b\w+\b', text.lower())
    
    word_count_map = list(map(lambda word: (word, 1), words))
    
    word_count = defaultdict(int)
    for word, count in word_count_map:
        word_count[word] += count
    
    return word_count

def visualize_top_words(word_count):
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
    
    words, counts = zip(*sorted_word_count)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Words Frequency')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"  
    
    text = fetch_text_from_url(url)
    
    word_count = map_reduce(text)
    
    visualize_top_words(word_count)