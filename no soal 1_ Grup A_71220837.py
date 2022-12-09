#test case 1
x= int(input('masukkan awal deret: '))
y= int(input('masukan akhir deret: '))
for count in range(10,31):
    if count%6 !=0 and count%3 !=0 and count%2 ==1:
        print (count, end=' ')

        
#test case 2
x= int(input('masukkan awal deret: '))
y= int(input('masukan akhir deret: '))
for count in range(40,100):
    if count%6 !=0 and count%3 !=0 and count%2 ==1:
        print (count, end=' ')
