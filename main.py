from matplotlib import pyplot as plt
from numpy import array

def FibonacciSeries(num:int) -> list:

    toReturn=[]
    a, last = 0, 1
    
    for i in range(1, num+1):
        toReturn.append(a)
        a, last = a+last, a
    
    return toReturn

if __name__ == "__main__":
    
    arr=FibonacciSeries(12)
    
    plt.xlabel("Position of Fibonacci Number")
    plt.ylabel("Fibonacci Numbers")
    plt.plot(array(arr), 'o:r')
    
    plt.show()