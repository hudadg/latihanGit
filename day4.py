size = int(input ('Size of Pyramid ? : '))
out = ''
for i in range (size):
    for j in range (size+1):
        if j>= size-i and j <= size+i:
            out += '   *'
        else:
            out += '  '
    out += '\n'
print(out)

# i = 0
# out = ''
# num = 1
# while (i < 5):
#     j = 0
#     while(j < (5-i)):
#         out += str(num) + ' '
#         if (i == 0):
#             out += ' '
#         num = num +2
#         j += 1
#     i += 1
#     out += '\n'
# print(out)
