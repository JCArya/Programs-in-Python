
import threading 
import time
  
def print_hello_three_times():
  while True:
    time.sleep(1)
    print("Hello")
t1 = threading.Thread(target=print_hello_three_times)   
t1.start()

