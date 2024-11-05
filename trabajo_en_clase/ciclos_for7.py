simbolo="*"
espacios=" "
num_espacios = 10
simbolo2 = "|||"
for i in range(1,10):
    print((espacios*num_espacios)+(simbolo*i)+(simbolo*(i-1)))
    num_espacios -= 1
num_espacios = 7
for j in range(1, 4):
    print((espacios*num_espacios)+simbolo2*2)