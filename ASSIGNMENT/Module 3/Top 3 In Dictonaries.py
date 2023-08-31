my_dict = {'a':10,'b':5,'c':20,'d':15,'e':25}
values = my_dict.values()
sorted_values = sorted(values, reverse=True)
top_values = sorted_values[:3]
top_keys = [key for key, value in my_dict.items() if value in top_values]
for i in range(len(top_values)):
   print(f"{i+1}. {top_keys[i]}:{top_values[i]}")
