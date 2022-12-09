x=str(input('masukan nama: '))
y=0
for i in range(len(x)):
    y=y+1
    print(x[:y])

for i in range(len(x)):
    y=y-1
    print(x[:y])
