import time

for i in range(15*60,1,-1):
    # print('  \r', end='')
    print(str(i)+'\r',end='')
    time.sleep(1)
    print('    \r',end='')