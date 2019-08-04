'''
Filter Function : Appling filter on List Data
'''
import statistics


data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg=statistics.mean(data)

#filter(lambda x: x>avg, data)

print (f'Original data :{data} ')
print(f" Greater than AVG :")
print(list(filter(lambda x: x>avg, data)))
print(f" Lower than AVG :")
print(list(filter(lambda x: x<avg, data)))

'''
Output:

Original data :[1.3, 2.7, 0.8, 4.1, 4.3, -0.1] 
 
 Greater than AVG :
[2.7, 4.1, 4.3]

 Lower than AVG :
[1.3, 0.8, -0.1]

'''