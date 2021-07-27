import random

def anyword():
  f = open("quotes.txt", encoding='UTF-8')
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  anyword()
