##
# This  is Python Lambda Function Tutorial.
# -

'''

full_name= lambda fn, ls:  fn.strip().title() + " " + ls.strip().title()

full_name("  mahoni", "    KEMBLE")

Output :
'Mahoni Kemble'

'''

temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires",19),("Los Angeles", 26),("Tokyo", 27),("New York", 28)]

c_to_f = lambda data: (data[0],(9/5)*data[1]+32)

print(list(map(c_to_f,temps)))

