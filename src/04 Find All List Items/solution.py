# Create function to find the location of elements in a list of lists
def index_all(search_list, item):
  # Create empty list to store the indexes
  index_list = []
  # Do for loop to find item in each element of the list
  for index, value in enumerate(search_list):
      # If value is equal to item, append to index_list
      if value == item:
          index_list.append([index])
      # Else, if element is a list, use this function again
      elif isinstance(search_list[index], list):
          for i in index_all(search_list[index], item):
            # Append to indexes 
              index_list.append([index] + i)
  # return index_list out of for loop
  return index_list

# Examples
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(example)
print(index_all(example, 2))
print(index_all(example, [1, 2, 3]))

example = [1, 2, 1, 1, 2]
print(example)
print(index_all(example, 1))
print(index_all(example, 2))

# Does not make any sense!
