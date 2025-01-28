list=[6,3,8,4,9]
iterate_var=iter(list)
for number in iterate_var:
  if number > 5:
    number+=1
    print(number)