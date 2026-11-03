import re
from collections import Counter

# Count N-grams and estimate probabilities for N = 1..5
text = """
Language models assign probabilities to sequences of words. A language model can predict the next word, score a sentence, or generate text. N-gram models are simple language models based on the previous N-1 words. Unigram models ignore context, bigram models use one previous word, and trigram models use two previous words. Higher-order N-grams capture more context but need more data. Data sparsity is a major challenge for N-gram language models. Smoothing assigns some probability mass to unseen events. Add-k smoothing is a simple smoothing method. Perplexity measures how well a language model predicts a test corpus. A lower perplexity means a better model.
"""

# Split the text into sentences, then into lowercase word tokens
sentences = [re.findall(r"\w+|[^\w\s]", s.lower())
             for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
# Vocabulary includes every word and the sentence-boundary symbols.
vocab = {w for s in sentences for w in s} | {"<s>", "</s>"}

def ngrams(n):
    # Pad each sentence with n-1 <s> tokens and one </s>.
    counts = Counter()
    for sentence in sentences:
        padded = ["<s>"] * (n - 1) + sentence + ["</s>"]
        for i in range(len(padded) - n + 1):
            counts[tuple(padded[i:i + n])] += 1
    return counts

def prob(counts, context, word, k=0.1):
    # P(word | context) = (count(context, word) + k) / (count(context) + k|V|)
    context_count = sum(c for gram, c in counts.items() if gram[:-1] == context)
    return (counts[context + (word,)] + k) / (context_count + k * len(vocab))

# Compare N = 1..5 using a real context from the first sentence
for n in range(1, 6):
    counts = ngrams(n)
    position = min(n - 1, len(sentences[0]) - 1)
    context = tuple(sentences[0][:position])
    word = sentences[0][position]
    probability = prob(counts, context, word)
    print(f"\nN={n}: {len(counts)} unique {n}-grams; "
          f"P({word} | {context}) = {probability:.4f}")
    for gram, count in counts.most_common(3):
        print(" ", " ".join(gram), count)
