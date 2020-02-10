# x = [ 1,2,3,2,5,2,7,2 ]
# def getMode(list) :
#     countList = []
# # create countList
#     for num in list :
#         check = False
#         for list1 in countList :
#             if(list1[0] == num) :
#                 list1[1] += 1
#                 check = True
#         if(check == False) :
#             countList.append([num, 0])

# # create list of mode/s
#     maxFrequency = 0
#     modes = []
#     for list1 in countList :
#         if (list1[1] > maxFrequency) :
#             modes = [list1[0]]
#             maxFrequency = list1[1]
#         elif (list1[1] == maxFrequency) :
#             modes.append(list1[0])

# # if every value appears same amount of times
#     if (len(modes) == len(countList)) :
#         modes = []
#     return modes
# print(getMode(x))

#==========================================

# x = {                 # key1 bisa disebut key
#     'key1':'item1',   # item1 bisa disebut val
#     'key2':'item2',
# }
# print(x['key1']) #yang akan muncul item 1, artinya iterasi 0 atau dengan kata lain key 1, yang akan terpanggil sebelahnya atau setelah titik 2 (:) yaitu item 1

# #MODIFY DICTIONARY

# #nambahin key dan value dalam list x

# x[0] = 'ini angka'
# x['nama'] = 'anya'
# print(x)

# #untuk memanggil key nya aja atau val nya aja
# for key,val in x.items():
#     print(val)    # bisa print(key)


#FUNGSI ZIP
# x = [1,2,3,4,5]
# y = [2,3,4,5,6]
# for item in zip[x,y]:
#     print(item)

#===========================================

#LAMBDA

#===========================================

#MAP
#return sebuah objek dari map tersebut (sesuai dengan perintah)
# def add(n):
#     return n + n

# number = (1,2,3,4)
# result = map(add,number)
# print(list(result)) #hasilnya jadi [2,4,6,8,], #INGET KASIH LIST DEPAN RESULT DALAM PERINTAH PRINT
                    #arti dari map adalah map(fungsi,iterasi)

# num1 = [1,2,3]
# num2 = [4,5,6]

# result = map(lambda x,y : x+y,num1,num2) #itu lambda bla bla bla masuknya ke fungsi. dan num1,num2 masuk keiterasi
# print(list(result)) #inget ya list dii tulis biar keluar hasil bahasa manusia bukan bahsa robot he


#mencoba memahami cara kerja map  dengan sebagai berikut:

# number = [1,2,3,4,5,6]

# def duplicateMAP(function,iteration):
#     hasil = []

#     for item in iteration:
#         hasil.append(function(item))
#     return hasil

# result = duplicateMAP(lambda x : x+2, number)  
# print(result)

#===========================================================
#FILTER
#Dia akan membuat kondisi tersebut betul atau tidak 

tahun = [1993,1995,1997,2000]
# test = filter(lambda tahun : tahun % 2 == 0, tahun )
# print(list(test))

def duplicateFILTER(function,iteration):
    hasil = []
    for item in iteration :
        if function(item):
            hasil.append(item)
    return hasil
result = duplicateFILTER(lambda tahun : tahun % 2 == 0, tahun)
print(list(result))