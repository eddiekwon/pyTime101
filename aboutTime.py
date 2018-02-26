
# 4.6 시간에 대한 함수들을 비교함.

import time

temp = ' 타임.ctime() {} - 타임.time() {:0.2f} - 타임.clock() {:0.2f}'

print(temp.format (
  
  time.ctime() , time.time() , time.clock()
  
  )
)

for i in range(3,0,-1):
  print('haha' ,i )
  time.sleep(i)
  print(temp.format(
  
    time.ctime() , time.time() , time.clock()
  
  )
  
  )
  
  
# 정확한 시간 측정에는 time.perf_counter() 를 사용하라! 
# ref Listing 4.7: time_perf_counter.py


## 4.1.6 time components.

# 타임존 변경하기 - 간단하게 time.tzset()해보았음.
import time
import os

os.environ['TZ'] = 'EST'
time.tzset()
whatTimeIsIt = time.ctime()
print('시간:,',whatTimeIsIt)

os.environ['TZ'] = 'EET'
time.tzset()
whatTimeIsIt = time.ctime()

print('시간:,',whatTimeIsIt)
print()


