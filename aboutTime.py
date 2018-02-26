
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
