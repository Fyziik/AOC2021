import json, sample, time


res = json.loads(sample.getData())
index = 0
lastValue = -1
amountIncreased = 0
for x in res:
  print(f"{x} {'(N/A - no previous measurement)' if lastValue == -1 else '(increased)' if x > lastValue else '(decreased)'}")
  index += 1
  time.sleep(2)
  if (x > lastValue):
    amountIncreased += 1
  lastValue = x

print(amountIncreased - 1)