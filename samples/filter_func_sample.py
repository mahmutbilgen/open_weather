
'''
Filter Function

'''
import statistics


data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg=statistics.mean(data)

#filter(lambda x: x>avg, data)

print (f'Original data :{data} is like these')
print(list(filter(lambda x: x>avg, data)))

prilist(filter(lambda x: x<avg, data)))