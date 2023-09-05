str1='HEET PATEL 33' 
my_dict={}
for i in str1:
    my_dict[i]=my_dict.get(i,0)+1
print(my_dict)
