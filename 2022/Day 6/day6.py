def detect_packet_start(data):

  last_four = []

  for i, c in enumerate(data):
    last_four.append(c)
    if len(last_four) > 4:
      last_four.pop(0)
    if len(set(last_four)) == 4:
      return i+1
  return -1

with open("input.txt", "r") as f:
  data = f.read()

packet_start = detect_packet_start(data)

print(packet_start)

def detect_message_start(data):

  last_fourteen = []

  for i, c in enumerate(data):
    last_fourteen.append(c)
    
    if len(last_fourteen) > 14:
      last_fourteen.pop(0)

    if len(set(last_fourteen)) == 14:
      return i+1

  return -1

with open("input.txt") as f:
  data = f.read()

message_start = detect_message_start(data)

print(message_start)
