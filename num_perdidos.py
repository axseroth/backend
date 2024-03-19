# dado una array de enteros buscar el menor y el mayor y dar una lista con los numeros perdidos

def numeros_perdidos(array):
    array.sort()
    low = array[0]
    high = array[-1]
    
    for low in range(low,high+1):
        if low not in array:
            print (low)



print(numeros_perdidos([1, 2, 3, 8, 9, 10, 50, 20]))