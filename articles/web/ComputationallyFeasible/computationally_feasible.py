
import math
import timeit

def timeMe(base):
    
    limit = int(math.log(1e10) / math.log(base))
    
    for exponent in range(1, limit+1):
        
        n = 0
        cmd = 'for i in range(%d**%d): n = i+i' % (base, exponent)
        nSecs = timeit.timeit(cmd, number = 1)
        
        print('Loop %d^%d in %.2fs' % (base, exponent, nSecs))

print('-'*10)
timeMe(2)
print('-'*10)
timeMe(10)
print('-'*10)
