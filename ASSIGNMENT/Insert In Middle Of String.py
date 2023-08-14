str1=input("Enter Anything:")
split=str1.split()
strm = "Love"
mpos = len(split) // 2
split.insert(mpos,strm)
print("New String:" + str(" ".join(split)))
