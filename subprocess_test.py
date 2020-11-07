#!/usr/bin/env python3
import subprocess

try:
    subprocess.check_call(['glxgears', '-fullscreen'],
                        timeout=10)
    subprocess.check_call(['stress-ng', '--cpu' , '0', '--cpu-method', 'fft'],
                        timeout=10)

except subprocess.TimeoutExpired: 
    print('subprocess has been killed on timeout')
else:
    print('subprocess has exited before timeout')