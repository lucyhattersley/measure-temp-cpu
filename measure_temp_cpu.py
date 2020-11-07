import os
import time
import csv
import re
import subprocess

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

stress_time = 10 #run stress for x seconds
cooldown_time = stress_time + 5 # run cooldown for x seconds
start_time = time.time()  # remember when we started

results = [] # list of temperature readings

try:
    subprocess.check_call(['glxgears', '-fullscreen'],
                        timeout=stress_time)
    subprocess.check_call(['stress-ng', '--cpu' , '0', '--cpu-method', 'fft'],
                        timeout=stress_time)

    current_temp = measure_temp()
    current_cpu = measure_cpu()
    results.append([current_temp, current_cpu])
    time.sleep(1)

except subprocess.TimeoutExpired: 
    print('subprocess has been killed on timeout')
else:
    print('subprocess has exited before timeout')

while (time.time() - start_time) < cooldown_time:
    current_temp = measure_temp()
    current_cpu = measure_cpu()
    results.append([current_temp, current_cpu])
    time.sleep(1)

print(results)

with open('temps.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerow(["Temp", "CPU"])
     writer.writerows(results)