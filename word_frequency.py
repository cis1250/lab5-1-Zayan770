#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

def is_sentence(text):
    if not isinstance(text, str) or not text:
        return False
    if not text[0].isupper():
        return False
    if text[-1] not in {'.', '!', '?'}:
        return False
    return True

def get_sentence():
    """Prompt until a valid sentence is entered, then return it."""
    while True:
        text = input("Enter a sentence: ").strip()
        if is_sentence(text):
            return text
        print("Invalid sentence. A sentence must start with a capital letter and end with .!?")

def calculate_frequencies(sentence):
    """Return two lists: unique words and their corresponding frequencies."""
    
    sentence_body = sentence[:-1].lower()
    raw_words = sentence_body.split()

    words = []
    freqs = []
    for w in raw_words:
        
        w_clean = re.sub(r'^\W+|\W+$', '', w)
        if not w_clean:
            continue
        if w_clean in words:
            idx = words.index(w_clean)
            freqs[idx] += 1
        else:
            words.append(w_clean)
            freqs.append(1)
    return words, freqs

def print_frequencies(words, frequencies):
    """Print words and their frequencies in a readable format."""
    print("\nWord frequencies:")
    for w, f in zip(words, frequencies):
        print(f"{w}: {f}")

def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)

if __name__ == "__main__":
    main()
# ...existing code...
  
