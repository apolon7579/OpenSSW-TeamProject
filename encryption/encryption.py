file = open('명지로고.gif', 'rb')
buffer = file.read()
file.close()

byte_string = ""

encoding_map = {}
decoding_map = {}

for i in range(0,256):
  encoding_map[i] = (i + 33) % 256
  decoding_map[(i+33)%256] = i
#  print(dic[i])

data = []

for b in buffer:
  data.append(encoding_map[b])

with open("amho", "wb") as f:
  f.write(bytes(data))


