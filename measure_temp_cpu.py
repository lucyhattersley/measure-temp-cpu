import os
import time
import csv
import re

def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp_strip = re.sub( r'(temp=)|(\'C)', "", temp) # strip off text
    temp_flt = float(temp_strip) # convert to float 
    return(temp_flt)

def measure_cpu():
    cpu_speed = os.popen("vcgencmd measure_clock arm").readline()
    cpu_speed_strip = re.sub( r'frequency\(\d*\)=', "", cpu_speed)
    cpu_speed_int = int(cpu_speed_strip)
    return(cpu_speed_int)

run_time = 3 # run for x seconds
start_time = time.time()  # remember when we started

data = [] # list of temperature readings

while (time.time() - start_time) < run_time:
    current_temp = measure_temp()
    current_cpu = measure_cpu()
    data.append([current_temp, current_cpu])
    time.sleep(1)

print(data)

with open('temps.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerow(["Temp", "CPU"])
     writer.writerows(data)