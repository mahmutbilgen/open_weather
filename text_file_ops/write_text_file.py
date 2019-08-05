'''

Write text file with open .... as write_f
a: append file : if file exist it will append if not exist it will create
w : write file : if not exist it will create or override

'''

# oceans=['Pacific','Atlantic','Indian','Southern','Arctic','Another Ocean']
#
# #with open("./write_file_sample.txt","w") as write_f:   ##  write file
# with open("./write_file_sample.txt","a") as write_f:  ## write file with append option
#     for ocean in oceans:
#         write_f.write(ocean)
#         write_f.write('\n')
#

'''
output:

./write_file_sample.txt:

Pacific
Atlantic
Indian
Southern
Arctic
Another Ocea

'''

oceans=['Pacific','Atlantic','Indian','Southern','Arctic','Another Ocean']

## Write to file with print function
## Write each line in new line,
with open("./write_file_sample.txt","w") as write_file:   ##  write over file
    for ocean in oceans:
       print(ocean,file=write_file)

'''
output:

./write_file_sample.txt:

Pacific
Atlantic
Indian
Southern
Arctic
Another Ocea

'''



