# Create dictionary
import pickle

# Function to save a dictionary
def save_dict(dict, dict_file):
  with open(dict_file, 'wb') as file:
    pickle.dump(dict, file)

# Function to load the dictionary
def load_dict(dict_file):
   with open(dict_file, 'rb') as file:
    return pickle.load(file)

save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
print(load_dict('test.pickle'))