# Define function to test if a character is a palindrome
def is_palindrome(sentence):
  # turn to lower case and remove spaces and punctuation
  sentence = sentence.lower().replace(' ', '').replace('\'', '').replace('.', '')
  # Split by character
  tmp = [char for char in sentence]
  # Reverse order
  tmp.reverse()
  # Paste all character togueter 
  tmp = ''.join(tmp)
  # Return logical if sentence is equal to tmp
  return sentence == tmp

# Testing phrases
print(is_palindrome('Hello world'))
print(is_palindrome('Thissiht'))
print(is_palindrome('hello world'))
print(is_palindrome("Go hang a salami, I'm a lasagna hog."))