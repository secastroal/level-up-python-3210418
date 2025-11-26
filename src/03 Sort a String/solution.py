# Create sorting function
def sort_words(sentence):
  # Split sentence in words
  sentence = [word for word in sentence.split(" ")]
  # Sort words
  sentence = sorted(sentence, key = str.lower)
  # Put words togueter
  sentence = ' '.join(sentence)
  # Return sorted sentence
  return sentence

# Test sorting function
print(sort_words('banana ORANGE apple'))
print(sort_words('banana ORANGE apple cherry Beef grapes APRICOT'))
