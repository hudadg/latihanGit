# produk = ['Jeruk','Semangka','Mangga']
# harga = [2000, 3000, 2500]
# def PrintMenu():
#     hasil = ''
#     for item in range(len(produk)):
#         hasil = str(item+1) + '.' + produk[item] + ' Rp. ' + str(harga[item]) + '\n'
#     return hasil

# def ShowProduk():
#     print(PrintMenu())

# def InputData():
#     newProd = input('Masukkan Nama Produk : ')
#     newPrice = int(input(f'Masukkan Harga dari {newProd} : '))
#     produk.append(newProd)
#     harga.append(newPrice)
#     print('Produk berhasil ditambahkan !\n' + PrintMenu())

# def UpdateHarga():
#     pilihProd = input('Pilih produk yang akan di update \n' + PrintMenu() + '\n Pilih salah satu :')
#     pilih = int(pilihProd) - 1
#     newHarga = int(input('Harga '+ produk[pilih] + 'akan dirubah berapa harganya : ' ))
#     harga[pilih] = newHarga
#     print('Harga Produk berhasil dirubah \n'+ PrintMenu())

# def deleteData():
#     pilihProd = input('Pilih produk yang akan dihapus \n' + PrintMenu() + '\n Pilih salah satu : ')
#     index = int(pilihProd) - 1
#     produk.pop(index)
#     harga.pop(index)
#     print('Produk berhasil dihapus :\n' + PrintMenu())

# backtoMenu = False
# while backtoMenu == False:
#     pilihMenu = input('Pilih Menu \n1)Show Produk \n2)Add Produk \n3)Update Harga \n4)Delete Produk \n Pilih salah satu : ')
#     index=int(pilihMenu)
#     menu = [ShowProduk, InputData, UpdateHarga, deleteData]
#     menu[index]()
#     ask_keluar = input(' Ingein kembali ke menu awal ? (y/n) : ')
#     if ask_keluar == 'n':
#         print('Terima Kasih telah menggunaklan aplikasi sederhana ini : ')
#         backtoMenu = True
#     else:
#         backtoMenu = False


##
##
##

# def hello():
#     print('Ghello')
    
# def function():
#     return [1,2,hello]

# function()[2]()

##
##

# produk =[
#     ['Jeruk',2000],
#     ['Apel',3000],
#     ['Pear',4000]
# ]
# cart =[
#     [0,3],
#     [1,4],
#     [2,5]
# ]

# out = ''
# for item in range(len(cart)):
#     index = cart[item][0]
#     out += str(item+1) + '.' + produk[index][0] + 'Rp. ' + str(produk[index][1]) + ' x ' + str(cart[item][1]) + ' = ' + 'Rp. ' + str(produk[index][1]*cart[item][1]) + '\n'


# print(out)
# print(produk[2][1])

# Dictionary
# {}, changable, index
# nama = {
#     'depan' : 'Anugrah', 'Huda', 'Iqra'
#     'belakang' : 'Nurhamid', 'Hutama', 'Hardianto'
# }

# print(nama['depan'])
# print(nama['belakang'])

# Tuple
# (), unchangeble

# variable_tuple = (1,2,3,4,5,6,7,8,9,10)
# print(type(variable_tuple))

#example

# a= ('anugrah', [1,True], {'nama' : 'Anugrah'}) 
# # print(a[1][1]) #menghasilkan True
# # a[1][1] = False #index tuple merupakan list
# # print(a[1][1])
# a[1].append('False')
# print(a)

#Sets
#Unique

# ini_set =  {'apel','jeruk','cherry'}
# print(type(ini_set))

def perkalian(num):
    return num * 2 #num parameter



list_num = [1,2,3,4,5]
list_num = [perkalian(item) for item in list_num] #function di dalam list
print(list_num)

# x = lambda a,b,c,d,e : (a*2),(b*2),(c*2),(d*2),(e*2) #alternate in lambda
# print(x(1,2,3,4,5))

#