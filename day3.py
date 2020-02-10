# nama = 'Huda '
# nama += 'Hutama'
# print(nama)

#Operators
# ==
# >=
# <=
# >
# <

# if (condition) :
#     algorithm/promram1
# elif (condition2) :
#     algorithm2
# else :
#     algorithm3

# nilaimurid = 80

# Solve it!
# y = 'Nomor urut '

# for item in range (1,11):
#     print (y + str(item));

#Solve it! #1

# angka = int(input('Masukkan angka : '))

# if angka % 2 == 0 :
#     print(f'Angka {angka} Tergolong bilangan GENAP')
# else :
#     print(f'Angka {angka} Tergolong bilangan GANJIL')

#     #Solve it! #2
# massa = int(input('Masukkan berat badan dalam kg : '))
# tinggi = int(input('Masukkan tingga badan dalam cm : '))

# IMT = massa /(tinggi/100)**2

# if IMT < 18.5 :
#     print(f'IMT = {IMT}, BERAT BADAN KURANG!')
# elif 18.5 <= IMT < 24.9 :
#     print(f'IMT = {IMT}, BERAT BADAN IDEAL!')
# elif 24.9 <= IMT < 29.9 :
#     print(f'IMT = {IMT}, BERAT BADAN BERLEBIH!')
# elif 29.9 <= IMT <= 39.9 :
#     print(f'IMT = {IMT}, BERAT BADAN SANGAT BERLEBIH!')
# elif IMT >39.9 :
#     print(f'IMT = {IMT}, BERAT BADAN OBESITAS!')

#list
# menu = input('Pilih Menu \n 1.Belanja \n 2.Belajar \n 3.Exit \n Pilih Menu Nomor : ')
# if(menu.isdigit()==True):
#     if(int(menu)>0 and int(menu)<=3):
#         check=True
#         if(menu.isdigit()==True):
#             if(int(menu)== 1):
#                 belanja= input('Mau Belanja apa ? ')
#             elif(int(menu)== 2):
#                 belajar = input('Mau Belajar apa ? ')
#             elif(int(menu)==3 ):
#                 keluar = input('Apa kamu benar ingin keluar? (Y/N)')
#     else:
#         print('Input salah, masukkan pilihan 1-3')
#         print('---------------------------------')
# else:
#     print('Input salah, masukkan pilihan 1-3')
#     print('---------------------------------')

list_item = list(range(5))
print(list_item)

# list_item = [1,2,3,4,5,6,7,8,9]
# print(list_item[6])

# list_makanan = ['ayam','tahu','tempe']

# for makanan in list_makanan :
#     print(makanan)

# for item in list(range(2,10,2)):
#     print(item)

# out = ''
# for item in list(range(5)):
#     out += ' * '
#     print(out)

# y = 'Nomor urut ';

# for item in range(0,21,2) :
#     print(y + str(item));

# out = ''
# for i in range(5,0,-1):
#     if(i>1):
#         for j in range(0,i):
#             out += ' * '
#         out += '\n'   
#     elif i == 1:
#         for i in range(1,6,1):
#             for j in range(0,i):
#                 out += ' * '
#             out += '\n'   
# print(out) 

# out = ''
# for i in range(5,0,-1):
#     if(i>1):
#         for j in range(0,i):
#             out += ' * '
#         out += '\n'   
#     elif i == 1:
#         for k in range(0,5):
#             for l in range(0,k+1):
#                 out += ' * '
#             if k ==4:
#                 break
#             out += '\n'   
# print(out) 

# out = ''
# for i in range(5,-6,-1):
#     print('*'*abs(i))

# out = ''
# for i in range (0,10,1):
#     for j in range (0,21):
#         if j>= 10-i and j <= 10+i:
#             out += ' * '
#         else:
#             out += '   '
#     out += '\n'
# print(out)

# out = ''
# for x in range (0,10):
#     for j in range(0,20)
#     spasi = 10 - x - i
#     bintang = x*2 + 1
#     print() ?????


# out = ''
# for i in range (9,-1,-1):
#     for j in range (0,21):
#         if j>= 10-i and j <= 10+i:
#             out += ' * '
#         else:
#             out += '   '
#     out += '\n'
# print(out)

# out = ''
# for i in range (0,11):
#     if(i<10):
#         for j in range (0,21):
#             if j>= 10-i and j <= 10+i:
#                 out += ' * '
#             else:
#                 out += '   '
#         out += '\n'
#     else:
#         for k in range (11,-1,-1):
#             for l in range (0,21):
#                 if l>= 10-k and l <= 10+k:
#                     out += ' * '
#                 else:
#                     out += '   '
#             out += '\n'
# print(out)

# out = ''
# for i in range (0,10,1):
#     for j in range (0,21):
#         if j>= 10-i and j <= 10+i:
#             out += ' * '
#         else:
#             out += '   '
#     out += '\n'

# for i in range (9,-1,-1):
#     for j in range (0,21):
#         if j>= 10-i and j <= 10+i:
#             out += ' * '
#         else:
#             out += '   '
#     out += '\n'
# print(out)

