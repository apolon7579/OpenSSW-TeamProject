absolutepath = "C:/Users/apolo/Desktop/openssw/passFile.txt"
relativepath = "passFile.txt"


fn = open(absolutepath, 'r')

for line in fn.readlines():
  print(line)

fn.close()