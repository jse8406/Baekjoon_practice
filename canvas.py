from collections import Counter, defaultdict


def get_vocab(corpus):
    vocab = Counter()
    for word in corpus:     
        # Represent words as characters plus end token
        tokens = tuple(list(word) + ['</w>'])
        vocab[tokens] += 1
    return dict(vocab)


def get_stats(vocab):
    
    pairs = defaultdict(int)
    for word_tokens, count in vocab.items():
        tokens = list(word_tokens)
        for i in range(len(tokens)-1):
            pairs[(tokens[i], tokens[i+1])] += count
    return pairs


def merge_vocab(pair, v_in):
    
    v_out = {}
    bigram = pair
    new_symbol = ''.join(bigram)
    for word_tokens, count in v_in.items():
        tokens = list(word_tokens)
        i = 0
        new_tokens = []
        while i < len(tokens):
            # If tokens match the bigram starting at i, replace with new_symbol
            if i < len(tokens)-1 and tokens[i] == bigram[0] and tokens[i+1] == bigram[1]:
                new_tokens.append(new_symbol)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        v_out[tuple(new_tokens)] = v_out.get(tuple(new_tokens), 0) + count
    return v_out


def learn_bpe(corpus, num_merges=10):
    vocab = get_vocab(corpus)
    merges = []

    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        most_frequent_pair = max(pairs, key=pairs.get)
        freq = pairs[most_frequent_pair]
        if freq < 1:
            break
        merges.append(most_frequent_pair)
        vocab = merge_vocab(most_frequent_pair, vocab)
        # Optionally print progress
        print(f"Merge {i+1}: {most_frequent_pair} (freq={freq})")
    return merges, vocab


def apply_merges(word, merges):
    tokens = list(word) + ['</w>']
    merge_ranks = {merges[i]: i for i in range(len(merges))}

    
    while True:
        
        pairs = []
        for i in range(len(tokens)-1):
            p = (tokens[i], tokens[i+1])
            if p in merge_ranks:
                pairs.append((merge_ranks[p], i, p))
        if not pairs:
            break
        
        pairs.sort()
        rank, idx, pair = pairs[0]
        
        tokens = tokens[:idx] + [''.join(pair)] + tokens[idx+2:]
    # Return tokens without end marker
    if tokens and tokens[-1] == '</w>':
        return tokens[:-1]
    return tokens


if __name__ == '__main__':
    
    corpus = [
        'low', 'lower', 'lowest', 'lowest', 'lowest',
        'new', 'newer', 'newest', 'newer',
        'wide', 'wider', 'widen', 'widely',
        'show', 'shown', 'showing',
        'work', 'worker', 'working', 'workshop',
        'network', 'networks', 'internet',
        'cow', 'cows', 'cowork', 'cower',
        'hello', 'hell', 'hero', 'her'
    ]
    print('Corpus:', corpus)

    
    merges, final_vocab = learn_bpe(corpus, num_merges=25)

    print('\nLearned merges in order:')
    for i, m in enumerate(merges, 1):
        print(f'{i}: {m[0]} + {m[1]}')

    print('\nFinal vocabulary (tokenized forms):')
    for tokens, count in final_vocab.items():
        print(tokens, '->', count)

    
    test_words = [
        'low', 'lower', 'lowest', 'new', 'newer', 'newest',
        'wide', 'wider', 'widen', 'widely',
        'show', 'shown', 'showing',
        'work', 'worker', 'working', 'workshop',
        'internet', 'network', 'networks',
        'cow', 'cowork', 'cower',
        'hello', 'hell', 'her', 'hero'
    ]
    print('\nTokenization examples:')
    for w in test_words:
        print(w, '->', apply_merges(w, merges))
