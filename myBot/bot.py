from myBot.neural import NeuralNetwork
from myBot.utils import load_data, tokenize, analyze_words
import random
import torch

# Loading data from json
intents = load_data('myBot/Data/intents.json')

# Loading training data
FILE = "myBot/Data/data.pth"

data = torch.load(FILE)

all_words = data['words']
tags = data['tags']
model_state = data["model_state"]


input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']


# Model set to evaluate
model = NeuralNetwork(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

def bot_response(message):
    message = tokenize(message)
    X = analyze_words(message, all_words)
    X = X.reshape(1, -1)
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.50:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return (random.choice(intent['responses']))
    else:
        return "Undskyld. Jeg forstod ikke din besked"