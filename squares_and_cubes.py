single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
for i in single_digits:
  i = i ** 2
  squares.append(i)
print(squares)                
cubes  = [x ** 3 for x in single_digits]
print(cubes)
