import collections

def read_file(filename):
  """Reads a text file and returns a list of words."""
  with open(filename, "r") as f:
    text = f.read()
  return text.split()

def count_words(words):
  """Counts the number of occurrences of each word in a list."""
  word_counts = collections.Counter(words)
  return word_counts

def main():
  """The main function."""
  filename = "example.txt"
  words = read_file(filename)
  word_counts = count_words(words)

  for word, count in word_counts.items():
    print(word, count)
if __name__ == "__main__":
  main()
