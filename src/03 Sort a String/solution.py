def sort_words(sentence):
  sentence = [word for word in sentence.split(" ")]

  sentence = sorted(sentence, key = str.lower)

  sentence = ' '.join(sentence)
  
  return sentence

print(sort_words('banana ORANGE apple'))
print(sort_words('banana ORANGE apple cherry Beef grapes APRICOT'))
