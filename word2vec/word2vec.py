from gensim.models import Word2Vec

def get_word_frequency(model):
    
    word_frequency = list()
    vocab = list(model.wv.vocab)
    
    for word in vocab:
        word_info = model.wv.vocab[word]
        word_frequency.append(word + '	' + str(word_info.count))
        
    return word_frequency


def write_text(file_name, data):
    with open(file_name, 'w', encoding='utf8') as file:
        for line in data:
            file.write(line)
            file.write('\n')
    
# Word2Vec parameter
# Reference https://radimrehurek.com/gensim/models/word2vec.html
# size: Dimensionality of the word vectors.
# window: Maximum distance between the current and predicted word within a sentence.
# min_count: Ignores all words with total frequency lower than this.

model = Word2Vec(tokenized_data, size=100, window=5, min_count=5)
model.save("word2vec.model")
#model = Word2Vec.load("word2vec.model")

# Get vocabulary
words = list(model.wv.vocab)

# Get word similarity
word_sim = model.wv.similarity('เลี้ยงลูก','มีความสุข')
print(word_sim)

# Get most word similarity
most_sim = model.wv.most_similar('ลาออก')
print(most_sim)


'''
# Get word frequency
word_frequency = get_word_frequency(model)

# write word similarity
write_matrix_excel(model)
write_ver_excel(model)

# Write text file
write_text('word_frequency.txt', word_frequency)

# Visualization
# https://www.vosviewer.com/
'''