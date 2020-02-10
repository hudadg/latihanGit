#1

def check_Name(name,alphabet):
    if(alphabet.lower() in name or alphabet.upper() in name):
        print('True')
    else:
        print('False')

#2

def add_even(num):
    if (num % 2 ==0):
        print('Angka ' + str(num) + ' adalah angka genap!')
    else:
        print('Angka ' + str(num) + ' adalah angka ganjil!')

# add_even(1981)
# add_even(122)

#3

def max_number(num1,num2,num3,num4):
    max_num = max(num1,num2,num3,num4)
    print('Nilai maksimalnya adalah ' + str(max_num))

# max_number(911,875,671,875)

#4

def string_filter(text):
    filter_string = ''.join([i for i in text if i.isdigit()])
    print(filter_string)

# string_filter('123uga111')

#5

from datetime import date
def check_plat(plat):
    for i in plat:
        if (i.isdigit()):
            digit = int(i)
            if (digit % 2 ==0):
                digit_akhir = 'Genap'
            else:
                digit_akhir = 'Ganjil'
    hari = date.today().day
    if hari % 2 == 0:
        hari_ini = 'Genap'
    else:
        hari_ini = 'Ganjil'
        if digit_akhir == hari_ini:
            print('Hari ini tanggal ' + str(hari) + ' plat nomor : ' + str(plat) + ' diperbolehkan lewat')
        else:
            print('Hari ini tanggal ' + str(hari) + ' plat nomor : ' + str(plat) + ' tidak diperbolehkan lewat')

check_plat('D 4444 CBR')
check_plat('D 5761 CBR')

