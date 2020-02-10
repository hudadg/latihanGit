#Assignment #1

    #No.1

#var in

angka= int(input('Tulis angka(4 digit) yang ingin diacak : '))
d = 2

a = angka//100
b = angka%100



#fc out
print('result : '+str(b)+str(a))


    #No. 2

#var in
radius = int(input('Tulis radius lingkaran dalam cm : '))
A = str(3.14*radius**2)


#fc out
print('Luas lingkaran :'+ A + " cm")

    #No.3

#var in

angka1 = int(input('masukkan angka : '))
angka2 = int(input('masukkan angka(2 digit) : '))
print('akan kita silang')

#fc out

c = angka1 //10
d = angka2 //10
e = angka1 %10
f = angka2 %10

print('hasil : '+str(c)+str(d)+str(e)+str(f))
print(c*1000 + d*100 + e*10 + f)

    #No.4

#var in

kalimat = str(input('Tulis kalimat : '))
huruf = str(input('Masukkan huruf yg inging dihilangkan : '))

#fc out

print(kalimat.replace(huruf,""))

    #No.5

#var
kalimat = str(input("Tulis kalimat (2 kata) : "))

tukar= kalimat.split(" ")
#out
print(tukar[1]+' '+tukar[0])



 

 