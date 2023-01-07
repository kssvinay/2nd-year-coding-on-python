list_of_numbers=[1,2,3,2,1,5,8,2,4,10] 
uniques=[] 
for number in list_of_numbers: 
          if number not in uniques:
               uniques.append(number)
print(uniques)
