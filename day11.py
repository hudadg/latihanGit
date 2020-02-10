
# def remove_outlier(data):
#     dataSorted = sorted(data)
#     mid = len(data)//2
#     data1 = dataSorted[0:mid]
#     data3 = dataSorted[-mid:]
#     q1=data1[len(data1)//2] if len(data1) != 0 else (data1(len(data1)//2) + data1(len(data1)//2+1))
#     q3=data3[len(data3)//2] if len(data3) != 0 else (data3(len(data3)//2) + data1(len(data3)//2-1))
#     Iqr = q3-q1
#     lower_limit = q1 - 1.5 * Iqr
#     upper_limit = q3 + 1.5 * Iqr
#     data_no_outlier = []
#     for item in data:
#         if item > lower_limit and item < upper_limit :
#             data_no_outlier.append(item)
#     print(f'Data Asli adalah = {data}')
#     print(f'Data setelah di sort = {dataSorted}')
#     print(f'Setengah Data Pertama = {data1}')
#     print(f'Setengah Data Terakhir = {data3}')
#     print(f'Q1 adalah = {q1}')
#     print(f'Q3 adalah = {q3}')
#     print(f'Lower limitnya adalah = {lower_limit}')
#     print(f'Upper alimitnya adlah = {upper_limit}')
#     print(f'Data yang tidak outlier = {data_no_outlier}')

# remove_outlier([71,70,73,70,70,69,70,72,71,300,71,69])

# #

# def countVowels(data):
#     jumlahVowels = 0
#     vowels = ['a','i','u','e','o']
#     for item in data:
#         if(item.lower() in vowels):
#             jumlahVowels += 1
#     print(jumlahVowels)

# countVowels('bUdi pergi ke pasar')
# countVowels('PURWWADHIKA')

# #

# # inputan = [[3,2,1],[4,6,5], [], [9,7,8]]
# def given(array):
#     tempList = []
#     for item in array :
#         for element in item :
#             tempList.append(element)
#     tempList.sort()
#     print(tempList)
#     # print(sorted(tempList)) #alternatif

# given([[3,2,1],[4,6,5], [], [9,7,8]])
# given([[3,4,2,1],[1,2,3], [5,4,3,1]])

#

def countWords(words):
    wordList = words.split(' ')
    countWords = {}
    for item in wordList:
        if(item in countWords.keys()):
            countWords[item] += 1
        else:
            countWords[item] = 1
    for key,value in countWords.items():
        print(f"Jumlah kata '{key.capitalize()}' ada sebanyak {value}")
    
countWords('jangan jangan kamu adalah aku')