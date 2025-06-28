
def is_palindrome(sentence):
  
  sentence = sentence.lower().replace(' ', '').replace('\'', '').replace('.', '')
  
  tmp = [char for char in sentence]
  tmp.reverse()

  tmp = ''.join(tmp)
  
  return sentence == tmp

print(is_palindrome('Hello world'))
print(is_palindrome('Thissiht'))
print(is_palindrome('hello world'))
print(is_palindrome("Go hang a salami, I'm a lasagna hog."))