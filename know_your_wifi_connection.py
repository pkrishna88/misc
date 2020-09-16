# Using the subprocess to know the connect wifi details
import os
import subprocess

p = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
out, err = p.communicate()
t = out.decode('utf-8')
print(t)
# for i in t:
#     print(i)