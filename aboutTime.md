
# 4.6 시간에 대한 함수들을 비교함.

```python

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
```
  
* 정확한 시간 측정에는 time.perf_counter() 를 사용하라! 
* ref Listing 4.7: time_perf_counter.py


## 4.1.6 time components.

```python

# 타임존 변경하기 - 간단하게 time.tzset()해보았음.   tag: 101ex , needsToDrawPic

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
```


## Listing 4.10: time_strptime.py

```
import time


def show_struct(s):
    print('  tm_year :', s.tm_year)
    print('  tm_mon  :', s.tm_mon)
    print('  tm_mday :', s.tm_mday)
    print('  tm_hour :', s.tm_hour)
    print('  tm_min  :', s.tm_min)
    print('  tm_sec  :', s.tm_sec)
    print('  tm_wday :', s.tm_wday)
    print('  tm_yday :', s.tm_yday)
    print('  tm_isdst:', s.tm_isdst)


now = time.ctime(1483391847.433716)
print('현재:', now)

parsed = time.strptime(now)
print('\n파싱값:')
show_struct(parsed)

print('\n서식화된 결과:',
      time.strftime("%a %b %d %H:%M:%S %Y", parsed))

```

## 결과는
```
현재: Mon Jan  2 21:17:27 2017

파싱값:
  tm_year : 2017
  tm_mon  : 1
  tm_mday : 2
  tm_hour : 21
  tm_min  : 17
  tm_sec  : 27
  tm_wday : 0
  tm_yday : 2
  tm_isdst: -1

서식화된 결과: Mon Jan 02 21:17:27 2017
```
