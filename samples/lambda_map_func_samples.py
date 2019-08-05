##
# This  is Python Lambda & Map Functions Tutorial.
# -



full_name= lambda fn, ls:  fn.strip().title() + " " + ls.strip().title()

full_name("  mahoni", "    KEMBLE")
'''
Output :
'Mahoni Kemble'

'''

temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires",19),("Los Angeles", 26),("Tokyo", 27),("New York", 28)]

c_to_f = lambda data: (data[0],(9/5)*data[1]+32)

print(list(map(c_to_f,temps)))

'''
Output:
[('Berlin', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokyo', 80.6), ('New York', 82.4)]


'''