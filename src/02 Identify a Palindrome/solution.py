
def is_palindrome(sentence):
  
  sentence = sentence.lower()
  
  tmp = [char for char in sentence]
  tmp.reverse()

  tmp = ''.join(tmp)
  
  return sentence == tmp

print(is_palindrome('Hello world'))
print(is_palindrome('Thissiht'))