def chave():
  keyFromFile = open("/media/sf_kali-pasta-compartilhada/projeto-ic/perspective/perspective.txt")
  key = keyFromFile.read()
  keyFromFile.close()

  return key