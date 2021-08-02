import time
import sys

for i in range(101):
    time.sleep(0.02)
    sys.stdout.write("[ " + ('>'*i)+(''*(100-i))+("\r [ %d"%i+"% ] ") )
    sys.stdout.flush()
