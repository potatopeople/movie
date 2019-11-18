hourse = 22
minutes = 30 + 155
for item in range(minutes // 60):
    if hourse == 24:
        hourse = 0
    hourse += 1
    print(hourse)
minutes = minutes % 60
if hourse == 24:
    hourse = '00'
elif hourse <= 10:
    hourse = '0' + str(hourse)
if minutes < 10:
    minutes = '0' + str(minutes)
print(str(hourse) + ':' + str(minutes))
