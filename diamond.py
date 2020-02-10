out = ''
for i in range (0,11):
    if(i<10):
        for j in range (0,21):
            if j>= 10-i and j <= 10+i:
                out += ' * '
            else:
                out += '   '
        out += '\n'
    else:
        for k in range (11,-1,-1):
            for l in range (0,21):
                if l>= 10-k and l <= 10+k:
                    out += ' * '
                else:
                    out += '   '
            out += '\n'
print(out)