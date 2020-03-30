def rem(arr, lenth, n): 
    result = 1
    for i in range(lenth): 
        
        result = (result*(arr[i]%n))%n
    return result%n

arr= [100, 10, 5, 25, 35, 14]
lenth = len(arr)
n = 11
print(rem(arr, lenth, n))
