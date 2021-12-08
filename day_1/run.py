import json, sample


res = json.loads(sample.getData())
index = 0
lastValue = -1
amountIncreased = 0
for x in res:
  print(f"Index: {index} value: {x} Increased?: {'(N/A - no previous measurement)' if lastValue == -1 else '(increased)' if x > lastValue else '(decreased)'}")
  index += 1
  if (x > lastValue):
    amountIncreased += 1
  lastValue = x

print(amountIncreased)