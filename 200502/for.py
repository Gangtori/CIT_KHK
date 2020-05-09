# kanghee = 1
# rui = 1
# jiwon = 7
#
# for i in [7,6,5,4,3,2,1]:
#     kanghee = kanghee * i
#
# print(kanghee)
number = 1
mult = 1
limit = 7
i = 0
for mult in [7,6,5,4,3,2,1]:
    limit = number
    number = mult
    mult = limit + mult

print(number)
