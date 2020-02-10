#Assignment #3

check_out_aplikasi = 'y'
while check_out_aplikasi == 'y':
    check = False
    while check == False:
        menu = input('Menu: \n 1.Segitiga Siku-Siku \n 2.Segitiga Sama Kaki \n 3.Persegi \n 4.Keluar \n Pilih Menu Nomor : ')
        if(menu.isdigit()==True):
            check=True
            if(int(menu)>0 and int(menu)<=4):
                if(menu.isdigit()==True):
                    check=True
                    if(int(menu)== 1):
                        segitigasiku = (input('Masukkan tinggi segitiga: '))
                        if(segitigasiku.isdigit()==True):
                            check=True
                            out = ''
                            for item in range(int(segitigasiku)):
                                out += ' * '
                                print(out) 
                            # check_out_aplikasi = input('Ingin Kembali ke Menu ? (Y/N)')                                                       
                        else:
                            print('-----------------------------------')
                            print('Input salah, masukkan angka')    
                            print('-----------------------------------')                
                    elif(int(menu)== 2):
                        segitigakaki = (input('Masukkan tinggi segitiga : '))
                        if(segitigakaki.isdigit()==True):
                            check=True
                            out = ''
                            for i in range (int(segitigakaki)):
                                for j in range (int(segitigakaki)+1):
                                    if j>= int(segitigakaki)-i and j <= int(segitigakaki)+i:
                                        out += '   *'
                                    else:
                                        out += '  '
                                out += '\n'
                            print(out)
                            # check_out_aplikasi = input('Ingin Kembali ke Menu ? (Y/N)')    
                        else:
                            print('-----------------------------------')
                            print('Input salah, masukkan angka')    
                            print('-----------------------------------')        
                    elif(int(menu)== 3):
                        persegi = input('Masukkan panjang sisi persegi : ')
                        if(persegi.isdigit()==True):
                            check=True
                            out = ''
                            for i in range( int(persegi) ):
                                for i in range (0,int(persegi)):
                                    print('*',end=' ')
                                print()
                                # check_out_aplikasi = input('Ingin Kembali ke Menu ? (Y/N)')                               
                        else:
                            print('-----------------------------------')
                            print('Input salah, masukkan angka')    
                            print('-----------------------------------')
                    elif(int(menu)== 4):
                        print('Exiting.')
                        print('Exiting..')
                        print('Exiting...')
                        check_out_aplikasi = 'n'                       
            else:
                print('----------------------------------')    
                print('Input salah, masukkan 1, 2, atau 3')  
                print('----------------------------------')                                                             
        else:
            print('----------------------------------')    
            print('Input salah, masukkan 1, 2, atau 3')  
            print('----------------------------------')                                 