import random
from random import randint

def random_string(mini, maxi, charset):
    return "".join(random.choice(charset) for x in range(randint(mini, maxi)))

chars = ".","-"
morsearray = set("")
alphaarray = (" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0")
seedval = int(input("Seed:  (can only contain lowercase a-z and 0-9)\n>>>"),36)
random.seed(seedval)

for n in range(0,50):
  morseletter = list(random_string(4, 6, chars))
  morseletter2 = []
  for l in morseletter:
    if l == ".":
      morseletter2.append("1")
    if l == "-":
      morseletter2.append("111")
    morsearray.add("0".join(morseletter2))
morselist = list(morsearray)

while 1 == 1:
  alphastring = []
  morsestring = []
  outstring = []
  hexstring = []
  asciistring = []
  finalhexstring = []
  cryptstring = ""
  task = str(input("Encrypt or Decrypt:\n>>>"))


  if task.lower() == "encrypt":
    while 1 == 1:
      cryptstring = str(input("String to encrypt: (can only contain lowercase a-z, 0-9, and space)\n>>>"))
      if cryptstring.lower() == "exit":
        break
      else:
        alphastring = list(cryptstring.lower())
        for letter in alphastring:
          morsestring.append(morselist[alphaarray.index(letter)])
        concatstring = "000".join(morsestring)
        outstring = [(concatstring[i:i+8]) for i in range(0, len(concatstring), 8)]
        print len(concatstring)
        outstring[len(outstring)-1] = outstring[len(outstring)-1].ljust(8,"0")
        for binary in outstring:
          hexstring.append(hex(int(binary, 2)).lstrip("0x"))
        for blurb in hexstring:
          finalhexstring.append(blurb.zfill(2))
        asciistring = "".join(finalhexstring)
        print str(asciistring)


  elif task.lower() == "decrypt":
    while 1 == 1:
      asciistring = str(input("String to decrypt:\n>>>"))
      if asciistring.lower() == "exit":
        break
      else:
        length = int(input("Length:\n>>>"))
        hexstring = [(asciistring[i:i+2]) for i in range(0, len(asciistring), 2)]
        for hexy in hexstring:
          outstring.append(bin(int(hexy, 16)).lstrip("0b").zfill(8))
        concatstring = "".join(outstring)
        concatstring = concatstring[0:length]
        morsestring = concatstring.split("000")
        for letter in morsestring:
          alphastring.append(alphaarray[morselist.index(letter)])
        cryptstring = "".join(alphastring)
        print str(cryptstring)