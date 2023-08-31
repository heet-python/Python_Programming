def Convert(tup, di):
    for a,b in tup:
        di.setdefault(a,[]).append(b)
    return di
 

tuple1 = [("KOHLI",18),("MSD",7),("ROHIT",45),("SKY",63),("HP",33)]
dictionary = {}
print(Convert(tuple1, dictionary))
