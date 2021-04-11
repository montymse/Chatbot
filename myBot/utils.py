import torch
import numpy as np
import nltk
from nltk.stem.snowball import SnowballStemmer
import json

nltk.download('punkt') # If not already downloaded, this command will download the data package for tokenizing words

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    stemmer = SnowballStemmer("danish")
    return stemmer.stem(word.lower())

# analyze_words takes a tokenzied sentence and a list of stemmed words
def analyze_words(sentence, words):
    stemmed_words = [stem(word) for word in sentence]
    bag = []
    for w in words:
        if w in stemmed_words:
            bag.append(1)
        else:
            bag.append(0)

    return np.asarray(bag, dtype=np.float32)


def load_data(filename):
    with open(filename, 'r') as file:
        result = json.load(file)
    return result


def prepare_data(intents, tags, words, pattern_tag_list, words_to_ignore):
    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)

        for pattern in intent['patterns']:
            w = tokenize(pattern)
            words.extend(w)
            pattern_tag_list.append((w, tag))

    words = [stem(w) for w in words if w not in words_to_ignore]
    words = sorted(set(words))
    tags = sorted(set(tags))

    return words, tags


def create_data(inputs, targets, pattern_tag_list, tags, words):
    for (pattern_sentence, tag) in pattern_tag_list:

        bag = analyze_words(pattern_sentence, words)
        inputs.append(bag)

        label = tags.index(tag)
        targets.append(label)
    inputs = np.array(inputs)
    targets = np.array(targets)
    return inputs, targets


def train(num_epoch, optimizer, criterion, model, train_loader):
    for epoch in range(num_epoch):
        for (words, labels) in train_loader:
            # Cleaning old gradients
            optimizer.zero_grad()
            # Forward pass
            outputs = model(words)
            # Calculate loss
            loss = criterion(outputs, labels)
            # Gradient decent
            loss.backward()
            # Optimize
            optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{num_epoch}], Loss: {loss.item():.4f}')


def save_training_data(model_state, words, tags, input_size, hidden_size, output_size):
    data = {
        "model_state": model_state,
        "words": words,
        "tags": tags,
        "input_size": input_size,
        "hidden_size": hidden_size,
        "output_size": output_size
    }
    torch.save(data, "Data/data.pth")