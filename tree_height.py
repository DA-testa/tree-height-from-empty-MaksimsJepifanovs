# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # # Your code here
    # levels = list(range(n))
    # for i in levels : levels[i] = 0
    # visited = list(range(n))
    # for i in levels : visited[i] = 0
    # pointer = 0
    # for i in range(n) :
    #     #levels[i] += levels[parents[i]] + 1
    #     if visited[i] == 1 : continue
    #     visited[i] = 1
    #     if parents[i] != -1 :
    #         if visited[parents[i]] != 1 :
    #             visited[parents[i]] = 1
    #             levels[parents[i]] += 1

    #         levels[i] += levels[parents[i]] + 1
            
    #         def levIncr(lp) :
    #             locCh = list(np.where(parents == lp)[0])
    #             #print(locCh)
    #             if len(locCh) < 1 : return

    #             for j in range(len(locCh)) :
    #                 levels[locCh[j]] += 1
    #                 levIncr(j)

    #         levIncr(i)

    #     else :
    #         for x in range(len(levels)) :
    #             if levels[x] < 1 :
    #                 levels[x] += 1

    #     print(levels)

    # max_height = max(levels) + 1




        # if parents[i] == -1 :
        #     visited[i] = 1
        #     for j in range(n) :
        #         levels[j] += 1
        #     continue

        # levels[i] += 1
        # visited[i] = 1
        
        # if visited[parents[i]] != 1 :
        #     visited[parents[i]] = 1
        #     levels[parents[i]] += 1
        #     levels[i] += 1
        



    #root = np.where(parents == -1)[0]


    prn1 = {}
    prn2 = {}
    for i in range(n) :
        
        if parents[i] == -1 : 
            prn1[parents[i]] = -1
        else :
            prn1[parents[i]] = parents[parents[i]]
        
        pass
    max_height += 1
    
    while True :
        if len(prn1) > 0 :
            for i in prn1 :
                prn2[prn1[i]] = prn1[prn1[i]]
            prn1.clear()
        else :
            for i in prn2 :
                prn1[prn2[i]] = prn2[prn2[i]]
            prn2.clear()

        max_height += 1
        if len(prn1) == 1 or len(prn2) == 1 : break

    print(max_height)
    return max_height


def main():
    nodesNumber = 0
    par = ""
    # implement input form keyboard and from files
    
    mode = input()
    if mode[0] == "F" :
        fname = "./test/" + input()
        #print(fname)
        f = open(fname, "r")
        nodesNumber = int(f.readline())
        par = f.readline()
        f.close()

    if mode == "I" :
        nodesNumber = int(input())
        par = input()
        parl = par.split(" ")
        par = ""
        for i in range(nodesNumber) :
            par += parl[i] + " "
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    
    # input values in one variable, separate with space, split these values in an array
    
    parList = list(map(int, par.split()))
    parArr = np.array(parList)
    #for i in parents
    # call the function and output it's result
    compute_height(nodesNumber, parArr)
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))