# 000
# 111
# 222
# out = ''
# for i in range(3):
#     for j in range(3):
#         out+= str(i)
#     out+= '\n'
# print(out)    

#function

# def contoh():
#     print('Aku adalah seorang kapiten')

# contoh()

angka1 = int(input('masukkan angka (1) : '))
angka2 = int(input('masukkan angka (1) : '))
def pertambahan():
    print(angka1+angka2)
pertambahan()

#

nama1=input('masukkan nama depan  : ')
nama2=input('masukkan nama belakang : ')

def namalengkap():
    print(nama1+nama2)
namalengkap()

#

x = int(input('masukkan angka : '))
y = int(input('masukkan angka : '))
def perkalian():
    total = x*y
    return total

print(perkalian())
