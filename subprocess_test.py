#!/usr/bin/env python3
import subprocess
import time
import os

run_time = 10 #run  for x seconds
start_time = time.time()  # remember when we started

p = subprocess.Popen(['ps' ,'-A'])
time.sleep(10)
p.kill()
 
# while (time.time() - start_time) < run_time:

