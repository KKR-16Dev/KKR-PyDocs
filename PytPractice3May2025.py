# 3
# 44
# 555
# 6666
# 77777

for i in range(3,8):
    print(str(i) * (i-2))

# 3
# 3,4
# 3,4,5
# 3,4,5,6
# 3,4,5,6,7

for rev in range(1, 6):
    row = []
    for j in range(rev):
        row.append(str(3 + j))
    print(','.join(row))

        
