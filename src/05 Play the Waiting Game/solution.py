import random
import time

# Create function waiting game
def waiting_game():
  # Randomly select the target seconds
  sec = random.choice([2, 3, 4])
  # Print target time
  print("Your target time is", sec, "seconds.")
  # Request input
  input("---Press Enter to Begin---")
  begin = time.time()
  # Request second input
  print("...Press Enter again after", sec, "seconds...")
  input()
  end = time.time()
  elapsed = end - begin
  print(f'\nElapsed time: {elapsed :.3f} seconds')
  if elapsed == sec:
    print(f'\nCongratulations! You did it perfectly.')
  elif elapsed < sec:
    print(f'\nYou were {sec - elapsed:.3f} seconds too fast.')
  elif elapsed > sec:
    print(f'\nYou were {elapsed - sec:.3f} seconds too slow.')

waiting_game()
waiting_game()
waiting_game()
waiting_game()
waiting_game()