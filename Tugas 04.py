#NO.1
def namaID():
    nama=str(input('masukkan nama : '))
    z=''
    for i in range(0,len(nama)):
        for  j in range(0,i+1):
            j==0
            z+=nama[i]
    print(z)

namaID()

#NO.2
def namaBR():
    nama=str(input('masukkan nama : '))
    z=''
    for i in range(0,len(nama)):
        z+='-'
        for j in range(0,i+1):
            if j == 0:
               z+=nama[i].capitalize() 
            else:
               z+=nama[i]         
    print(z)

namaBR()

#No.3
def urutan():

    num = [1,10,6,2,10,8]
    print(sorted(num,reverse=False))

    num = [1,10,6,2,10,8]
    print(sorted(num,reverse=True))

urutan()

















#???


# num = input("Please enter the Total Number of List Elements: ")

# for i in range(1, int(num)+1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     num.append(value)
#     num.sort()
# print(sorted(num,reverse=False))


# z = list(num)

# for i in range(1, int(num) + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     z = list(str(num))
#     z.append(value)
#     z.sort()
# print(f'Element After Sorting List in Ascending Order is : {z}')



            

