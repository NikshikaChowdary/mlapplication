#generator
def square(i):
  for i in range(i):
    i=i**2
    yield i
    #return n
square(10)
for i in square(10):
  print(i)