import string
stop_words = {"the", "and", "to", "of", "a", "in", "that", "is", "for", "it", "with", "as", "was", "on", "be", "at", "by", "i"}
def count_words(text):

    word_counts = {}
    

    words = text.split()
    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        if word in stop_words:
            continue
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    return word_counts

def display_results(word_counts, top_n=10):
    items = list(word_counts.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
    # Add these stats:
    total_unique = len(word_counts)
    total_words = sum(word_counts.values())  # Sum all counts
    
    print(f'\n=== Word Frequency Analysis ===')
    print(f'Total words analyzed: {total_words}')
    print(f'Unique words: {total_unique}')
    print(f'\nTop {top_n} most common words:')
    for word, count in sorted_items[:top_n]:
        print(f'{word}: {count}')

with open("sample.txt", "r") as file:
    text = file.read()
result = count_words(text)
display_results(result, 10)