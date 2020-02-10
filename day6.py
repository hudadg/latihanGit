# num = [1,5,6,4,3,2,10,2,11,3,4,6,7]

# def sort_ascending():


#     for i in range(len(num)):
#         for j in range(i+1, len(num)):
#             if num[i] > num[j]:
#                 num[i] , num[j] = num[j] , num[i]  #tukar posisi
#     return num

# print(sort_ascending())

# def blender(buah):
#     print(f'Jus  {str(jbu)}')
# jbu =''
# buah = str(input('Ketik nama buah : ')) 
# jbu += buah[0].capitalize()
# blender(buah)

# def remove_character(text,remove):
#     lower_text = text.lower()
#     rmv_text = lower_text.replace(remove,'') #ganti-replace jadi kososng
#     print(rmv_text)

# remove_character('Huda Hutama', 'u')



def MainSuit():
    check = False
    tangan1= input('Suit! Pilih (gunting/kertas/batu) ? : ')
    tangan2= input('Suit! Pilih (gunting/kertas/batu) ? : ')
    while check == False:
        if (tangan1.isalpha()==True):
            check== True
            if(tangan2.isalpha()==True):
                check== True
                if(tangan1=='gunting') or (tangan1=='batu') or (tangan1=='kertas'):
                    check== True
                    if(tangan2=='gunting') or (tangan2=='batu') or (tangan2=='kertas'):
                        check== True
                        if tangan1 == 'gunting' and tangan2 == 'kertas' :
                            print(f'pemenang suit kali ini player 1')
                            break
                        elif tangan1 == 'gunting' and tangan2 == 'batu' :
                            print(f'pemenang suit kali ini player 2')
                            break
                        elif tangan1 == 'gunting' and tangan2 == 'gunting' :
                            print(f'pemenang suit kali tidak ada (seri)')
                            break
                        elif tangan1 == 'kertas' and tangan2 == 'kertas' :
                            print(f'pemenang suit kali tidak ada (seri)')
                            break
                        elif tangan1 == 'kertas' and tangan2 == 'batu' :
                            print(f'pemenang suit kali ini player 1')
                        elif tangan1 == 'kertas' and tangan2 == 'gunting' :
                            print(f'pemenang suit kali ini player 2')
                            break
                        elif tangan1 == 'batu' and tangan2 == 'kertas' :
                            print(f'pemenang suit kali ini player 2')
                        elif tangan1 == 'batu' and tangan2 == 'batu' :
                            print(f'pemenang suit kali tidak ada (seri)')
                            break  
                        elif tangan1 == 'batu' and tangan2 == 'gunting' :
                            print(f'pemenang suit kali ini player 1')
                            break
                        else:
                            print('----------------------------------------')
                            print('harus pilih gunting, batu atau kertas!!!')  
                            print('----------------------------------------')
                            break
                    else:
                        print('-----------------------------------------')
                        print('tolong ketik gunting, batu atau kertas..!')
                        print('-----------------------------------------')
                        break
                else:
                    print('-----------------------------------------')
                    print('tolong ketik gunting, batu atau kertas..!')
                    print('-----------------------------------------')
                    break
            else:
                print('----------------------------------------')
                print('tolong ketik gunting, batu atau kertas..')
                print('----------------------------------------')
                break
        else:
            print('----------------------------------------')
            print('tolong ketik gunting, batu atau kertas..')
            print('----------------------------------------')
            break

# MainSuit()        

# def perkalian_2(x):
#     if x <3 :
#         return 4
#     else:
#         return (x * tujuh())

# def tujuh():
#     return 7

# print(perkalian_2(2))
# print(perkalian_2(4))

def remove_character():
    text = str(input('Masukkan kata yang ingin dihapus vocal nya : '))
    lower_text = text.lower()
    rmv_text1 = lower_text.replace('a','')    #ganti-replace jadi kososng
    rmv_text2 = rmv_text1.replace('i','')
    rmv_text3 = rmv_text2.replace('u','')
    rmv_text4 = rmv_text3.replace('e','')
    rmv_text = rmv_text4.replace('o','') 
    print(rmv_text)

# remove_character()

def remove_vowels():

    name = str(input('masukkan nama yg huruf vocal nya ingin dihilangkan : '))

    vowels = ['a','i','u','e','o','A','I','U','E','O']
    for alphabet in vowels:
        name = name.replace(alphabet,'')
    print(name)

# remove_vowels()

# list_angka = [2,'Hello',[1,5,'Hai', [9,False]]]
# print(list_angka[1][2])

def check_name():
    name = str(input('Input ypur name for alphabet check : '))
    alphabet = str(input('Input alphabet that would be checked :'))
    check = False
    # alpha = list(alphabet)
    index= list(name)
    for alphabet in index :
        if alphabet.isalpha() == True:
            if alphabet in index:
                check == True
                print(f'True, there is alphabet {alphabet} in your name')
            else:
                check == False
                print('False, alphabet not found')
        else:
            print('Please input your name with only alphabets')
            break
    # print(list(name))
check_name()


# name = str(input('Input ypur name for alphabet check : '))
# alphabet = str(input('Input alphabet that would be checked :'))
# name_break = name.split()

# # for alphabet in list(name_break):
# #         if name.isalpha() == True:
# #             if alphabet in list(name_break):
# #                 print(f'True, there is alphabet {alphabet} in your name {name}')
# #             else:
# #                 print(f'False, there in no alphabet {alphabet} in your name {name}')
# #         else:
# #             print('Please input with only alphabets')        
# print(split.name)


def split(words):
    return list(words)

print(split('wow'))

  



