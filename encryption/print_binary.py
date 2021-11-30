file = open('test.txt', 'rb')
buffer = file.read()
file.close()

for b in buffer:
  print(b)