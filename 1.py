arr = "111111111110000000000000000"

def task(array):
    for index in range(len(arr)):
        if arr[index] == "0":    
            return index
        
print(task(arr))