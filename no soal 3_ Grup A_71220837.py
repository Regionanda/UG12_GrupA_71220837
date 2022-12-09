#tase case 1 dan 2
x= int(input('masukkan pembatas: '))
y= int(input('masukan angka yang di larang: '))
for i in range(x):
    if i == y:
        continue
    else:
        print(i,end=' ')
