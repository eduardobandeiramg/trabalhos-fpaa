possibilidades = [(1,2), (-1,3), (4,5), (5,2), (2,4), (3,-1), (0,0)]

possibilidades = [elemento for elemento in possibilidades if (elemento[0] >= 0 and elemento[0] < 5) and (elemento[1] >= 0 and elemento[1] < 5)]

print(possibilidades)