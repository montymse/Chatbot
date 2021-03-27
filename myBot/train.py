from utils import prepare_data, load_data, create_data, save_training_data, train
from dataset import ChatbotDataset

from neural import NeuralNetwork

import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, TensorDataset

tags = []
words = []
pattern_tag_list = []
words_to_ignore = ['?', '.', '!']

inputs = []
targets = []

# Loading data from json
intents = load_data('Data/intents.json')

# Preparing data by tokenizing and stemming
prepare_data = prepare_data(
    intents, tags, words, pattern_tag_list, words_to_ignore)
words, tags = prepare_data

# Creating data for training
create_data = create_data(inputs, targets, pattern_tag_list, tags, words)
inputs, targets = create_data

# Training data
dataset = ChatbotDataset(inputs, targets)
train_loader = DataLoader(dataset=dataset,
                          batch_size=8,
                          shuffle=True)

input_size = len(inputs[0])
hidden_size = len(tags)
output_size = len(tags)
model = NeuralNetwork(input_size,hidden_size,output_size)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training phase
train(100, optimizer, criterion, model, train_loader)

# Save data
save_training_data(model.state_dict(), words, tags, input_size, hidden_size, output_size)
