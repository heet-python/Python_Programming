n=[{1:10},{2:20},{3:30},{4:40},{5:20},{4:50},{2:60},{3:40}]
print("Original List : ",n)
u_value = set( val for dic in n for val in dic.values())
print("Unique Values: ",u_value)
