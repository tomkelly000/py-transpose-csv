import sys

filename = sys.argv[1]
file = open(filename, 'r')

## first put it in normal array
array = []
for row in file:
    array.append(row.split(','))
file.close()

if (len(array) == 0): 
	sys.exit(0) # empty file

# make skeleton with none 
transpose = [[None for i in range(len(array))] for j in range(len(array[0]))]

# fill the transpose array
i = 0 # row index
for row in array:
    j = 0 # column index
    for cell in row:
        transpose[j][i] = cell.strip()
        j += 1
    i += 1
print transpose[len(array[0]) - 1]

name = filename.rpartition('.')

# write to file
transposefile = open(name[0] + '_transposed.' + name[2], 'w')
for row in transpose:
	transposefile.write(','.join(row) + '\n')

transposefile.close()
