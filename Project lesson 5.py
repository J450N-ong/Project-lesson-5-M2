print("Mirrored Right Triangle Star Pattern")

rows = int(input("Please Enter the Total Number of Rows  : "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j <= rows - i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()