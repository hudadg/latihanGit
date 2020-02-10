#Assignment #2
while True :

    menu = input('Pilih Menu \n 1.Belajar \n 2.Belanja \n 3.Exit \n Pilih Menu Nomor : ')
    if(menu.isdigit()==True):
        if(int(menu)>0 and int(menu)<=3):
            if(menu.isdigit()==True):
                if(int(menu)== 1):
                    belajar = input('Pilih Perhitungan \n 1.Segitiga(luas) \n 2.Trapesium(luas) \n Pilih Perhitungan Nomor : ')
                    if(int(belajar)== 1):
                        AlasS = int(input('Masukkan panjang alas segitiga dalam cm : '))
                        TinggiS = int(input('Masukkan tinggi segitiga dalam cm : '))
                                    
                        LuasS = AlasS*TinggiS*1/2

                        print(f'Luas segitiga : {LuasS} cm ')
                    if(int(belajar)== 2):
                        AlasT1 = int(input('Masukkan panjang sisi satu trapesium dalam cm : '))
                        AlasT2 = int(input('Masukkan panjang sisi satu trapesium dalam cm : '))
                        TinggiT = int(input('Masukkan tinggi trapesium dalam cm : '))

                        LuasT = 1/2*(AlasT1+AlasT2)*TinggiT

                        print(f'Luas trapesium : {LuasT} cm')
                if(int(menu)== 2):
                    belanja = input('Mau Beli apa ? \n Menu \n 1.Ayam Bakar Rp.20,000 \n 2.Ayam Geprek Rp.30,000 \n 3.Ikan Bakar Rp.40,000 \n Pilih Menu Nomor : ')
                    if(int(belanja)== 1):
                        qtyAB = int(input('Berapa banyak ? '))
                        TotAB = 20000*qtyAB
                        print(f'Total Belanja Ayam Bakar Rp.{TotAB}')
                    if(int(belanja)== 2):
                        qtyAG = int(input('Berapa banyak ? '))
                        TotAG = 30000*qtyAG
                        print(f'Total Belanja Ayam Bakar Rp.{TotAG}')
                    if(int(belanja)== 3):
                        qtyIB = int(input('Berapa banyak ? '))
                        TotIB = 40000*qtyIB
                        print(f'Total Belanja Ayam Bakar Rp.{TotIB}')
                    
        else:
            break
                                                                
        

        # elif(int(menu)==3 ):
        #     keluar = input('Apa kamu benar ingin keluar? (Y/N)')
#     else:
#         print('Input salah, masukkan pilihan 1-3')
#         print('---------------------------------')
# else:
#     print('Input salah, masukkan pilihan 1-3')
#     print('---------------------------------')