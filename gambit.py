

import codecs

strDecimal = "81 35 236 117 45 172 41 1 239 119 37 242 106 50 245 117 31 244 114 45 238 124 222 230 120 48 160 124 45 236 127 39 238 112 222 244 113 35 160 80 31 237 107 39 244 41 33 232 106 42 236 110 44 231 110 236 160 89 42 229 106 49 229 41 49 229 119 34 160 130 45 245 123 222 243 120 42 245 125 39 239 119 222 225 119 34 160 76 20 160 125 45 160 114 33 225 119 33 239 109 35 192 112 31 237 107 39 244 123 35 243 110 31 242 108 38 174 108 45 237 41 47 245 120 50 233 119 37 160 123 35 230 110 48 229 119 33 229 67 222 177 60 244 176 62 32 178 66 240 230 55" 
rgstrDecimals = strDecimal.split()
rgDecimals = [int(n) for n in rgstrDecimals]

merged_binary = ''.join(rgDecimals)
print merged_binary.encode('UTF-8')

for i in range(len(rgDecimals) / 2):
	temp = rgDecimals[i]
	rgDecimals[i] = rgDecimals[len(rgDecimals) - i - 1]
	rgDecimals[len(rgDecimals) - i - 1] = temp

merged_binary = ''.join(rgDecimals)
print merged_binary.encode('UTF-8')

#merged_binary = ''.join(rgDecimals)
#print merged_binary#.encode('UTF-8')

exit()

# rgDecimals = [hex(int(n)) for n in rgstrDecimals]

# print rgDecimals.encode('UTF-8')

# merged_binary = ''.join(rgDecimals)
# print merged_binary.encode('UTF-8')

# exit()


# rgstrDecimals = strDecimal.split()
# rgDecimals = [bin(int(n)).zfill(8) for n in rgstrDecimals]
# merged_binary = ''.join(rgDecimals)
# print merged_binary.encode('UTF-8')

# exit()

# strUnicode = rgBytes.decode('UTF-8')

# print strUnicode

# exit()


# rgstrDecimals = strDecimal.split()
# rgDecimals = [bin(int(n)) for n in rgstrDecimals]

# output = b''.join
# for dec in rgDecimals:
# 	output += format(dec, '02x')

# print output.decode('utf-8')



#with open('plain.txt', 'wb') as f:
#	f.write(plaintext)
#with codecs.open('plain.txt', encoding='utf-8') as f:
#	for line in f:
#		print line



# filename = 'foo.txt'
# with gzip.open(filename, 'wb') as outfile:
#     outfile.write(bytes(plaintext, 'UTF-8'))
# with gzip.open(filename, 'r') as infile:
#     outfile_content = infile.read().

#print plaintext.decode('UTF-8')


output = []
for num in rgstrDecimals:
	output.append(unichr(int(num)))
print ''.join(output)
