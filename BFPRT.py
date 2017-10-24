import timeit
import math
import random
import sys

# too much recursion
# stack overflow
# not practical

def BFPRT(alist,start,end,k):
    if start == end:
        return start
    pivotIndex = getPivotIndex(alist,start,end)
    cur = partition(alist,start,end,pivotIndex)
    if k == cur:
        return cur
    elif k < cur:
        return BFPRT(alist,start,cur-1,k)
    else:
        return BFPRT(alist,cur+1,end,k-cur)

# get the index of the median of medians
def getPivotIndex(alist,start,end):
    if end-start<5:
        alist = sorted(alist[start:end+1])
        return (start+end)>>1
    length = math.floor((end-start)/5)
    mds = start - 1
    for i in range(length):
        st = start + i * 5
        ed = start + i * 5 + 5
        md = start + i * 5 + 2
        alist[st:ed] = sorted(alist[st:ed])
        mds += 1
        alist[mds], alist[md] = alist[md], alist[mds]
    return BFPRT(alist,start,mds,((mds+start)>>1)-start+1)

def partition(alist,start,end,pivotIndex):
    alist[pivotIndex],alist[end] = alist[end],alist[pivotIndex]
    j = start - 1
    for i in range(start,end):
        if alist[i] < alist[end]:
            j += 1
            alist[i],alist[j] = alist[j],alist[i]
    j += 1
    alist[j],alist[end] = alist[end],alist[j]
    return j

sys.setrecursionlimit(1000000)
alist = [24,45,25,23,64,73,45,3,54,56,46,234,46,72,54,73,45,24,754,235,7,35,24]
print(alist[BFPRT(alist,0,len(alist)-1,3)])

# sys.setrecursionlimit(1000000)
# alist = list(range(100))
# random.shuffle(alist)
# BFPRT(alist,0,len(alist)-1,5)


# sys.setrecursionlimit(1000000)
# for i in range(100,10001,200):
#     t = timeit.Timer("BFPRT(alist,0,len(alist)-1,5)", "from __main__ import random,alist,BFPRT")
#     alist = list(range(i))
#     random.shuffle(alist)
#     lst_time = t.timeit(number=1000)
#     print("%d,%10.3f" % (i, lst_time))

