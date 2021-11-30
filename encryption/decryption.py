file = open('amho', 'rb')
buffer = file.read()
file.close()

byte_string = ""

decoding_map = {}

for i in range(0,256):
  decoding_map[(i+33)%256] = i

data = []

for b in buffer:
    data.append(decoding_map[b])


with open("명지.gif", "wb") as f:
  f.write(bytes(data))
