'''
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то 
количествоподряд идущих нулей: 111111111111111111111111100000000.Найти индекс первого нуля (то есть найти 
такое место, где заканчиваются единицы, и начинаются нули)
'''

arr = "111111111110000000000000000"

def task(array):
    for index in range(len(array)):
        if array[index] == "0":    
            return index
        
print(task(arr))