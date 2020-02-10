# PIlih MEnu
# 1) Show Dictionary
# 2) Add Dictionary
# 3) Search Dictionary
# 4) Exit

# fDictionary = {}

# #function untuk melihat dictionary
# def menuDictionary(input):
#     # key : value
#     print('|        key         |          value        |')
#     hasil = ''
#     i=0
#     for key,value in input.items():
#         i+=1
#         hasil += f'{i})     {key}                {value}\n'
#     return hasil

# def showDictionary():
#     print(menuDictionary(fDictionary))

# def addDictionary():
#     inputLooping = int(input('Berapa kali akan memasukkan data ke dictionary : '))
#     for i in range(inputLooping):
#         print('Pilih tipe dictionary \n1) String \n2) Number')
#         pilihDictionary = input('Pilih : ')
#         if pilihDictionary == '1':
#             key = input('Key : ')
#             value = input('Value : ')
#             fDictionary[key]=value
#         elif pilihDictionary =='2':
#             key1 = input('Key : ')
#             value1 = input('Value : ')
#             fDictionary[key1] = int(value1)
#         print()

# def searchDictionary():
#     search = input('Cari kata : ')
#     #proses filter
#     filter_Dictionary = filter(lambda item : search.lower() in item.lower(), fDictionary.keys())
#     newDic = {}
#     for item in filter_Dictionary:
#         newDic[item] = fDictionary[item]
#     print(menuDictionary(newDic))

# def out_aplikasi():
#     print('Terima kasih telah menggunakan aplikasi sederhana ini!')
#     exit()

# backToMenu = 'y'
# while backToMenu == 'y':
#     print('Pilih Menu : \n1)Show Dictionary \n2)Add Dictionary \n3)Search Dictionary \n4)Exit')
#     pilihMenu = input('Pilh Menu : ')
#     index = int(pilihMenu) -1
#     menu = [showDictionary,addDictionary,searchDictionary,out_aplikasi]
#     menu[index]()
#     backToMenu = input('Kembali ke menu awal ? (y/n) : ')
#     print('')
#     print('Terimakasih telah menggunakan aplikasi sederhana ini')

# Example python fundamental
# Decision['testing'][2][1]['Hello',3][2][1]()(True)
# Decision['testing'][2][1]['ada apa'][1][0]


# from math import floor, pow, sqrt, ceil
# a = [1,2,3,5,4,3,2,1,4,5,6,7,8,4,2,3,4,5,7,1,2,2,4,5]

# def bubblesort(list):
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j] . list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     return list

# def mean_list(list):
#     return sum(list)/len(list)

# # print(mean_list(a))

# def median_list(list):
#     list = bubblesort(list)
#     if len(list) %2 ==0:
#         return((list[(len(list)//2)-1]) + (list[(len(list)//2)]))/2
#     else:
#         return list[floor(len(list)/2)]

# # print(median_list(a))

# def mode_list(list):
#     ind =set(list)
#     counter = {}
#     modus = []
#     for i in ind :
#         z = 0
#         for j in list:

#              if i == j:
#                 z += 1
#         counter[i] = z
#     max_count = max(counter.values())
#     for k in counter:
#         if counter[k]== max_count:
#             modus.append(k)
#     if len(modus) == len(set(list)):
#         modus = []
#     return modus

# # print(mode_list(a))   

# def variance_list(list):
#     z = 0
#     mean =  mean_list(list)
#     for i in list:
#         z+= pow((i-mean),2)
#     return z/(len(list)-1)

# def stdev(list):
#     z = 0
#     mean = mean_list(list)
#     for i in list:
#         z+= pow((i -mean),2)
#     return sqrt(z/(len(list)-1))

# def sample_statistic(list,type = 'mean'):
#     if type == 'mean':
#         return mean_list(list)
#     elif type == 'stdev':
#         return stdev(list)
#     elif type == 'median':
#         return median_list(list)
#     elif type == 'mode':
#         return mode_list(list)
#     elif type == 'variance':
#         return variance_list(list)
#     else:
#         return 'Input tidak sesuai'

# # print(variance_list(a))
# a = [1,2,3,5,4,3,2,1,4,5,6,7,8,4,2,3,4,5,7,1,2,2,4,5]
# print(sample_statistic(a,'mean'))
# print(sample_statistic(a,'stdev'))
# print(sample_statistic(a,'median'))
# print(sample_statistic(a,'mode'))
# print(sample_statistic(a,'variance'))
# from math import pow
# angka = input('masukkan angka 3 digit : ')
# def getSquare(angka):
#     angka1 = str(angka)
#     out = ''
#     for i in list(angka1):
#         out += str(int(pow(int(i),2)))
#     print(out)
# getSquare(angka)



def domainName(input):
    list_domain = input.split('.')
    if (len(list_domain) == 3):
        print(list_domain[1])
    elif (len(list_domain) == 2):
        print(list_domain[0].split('//')[1])

domainName('http://github.com/angrahnurhamid/apapun')
domainName('http://www.zombie-bites.com')
