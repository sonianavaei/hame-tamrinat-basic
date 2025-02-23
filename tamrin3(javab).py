def echo_speaker(word):
  """
  This function simulates the echo effect in the speaker and prints each step.

  Args:
    word: The original word spoken by the speaker.
  """
  for i in range(len(word)):
    modified_word = list(word)
    for j in range(i):
        modified_word[j] = modified_word[j+1]
    print("".join(modified_word))

# Get input from user
word = input()

# Call the function to print the echo words
echo_speaker(word)
