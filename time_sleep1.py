
import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=False)
  print("\r", end="", flush=True)
  time.sleep(1)
 