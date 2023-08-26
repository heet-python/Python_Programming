d1={'Where Does The Sun Arise From':'East','National Animal Of India':'Tiger','National Bird Of India':'Peacock','National Flower Of India':'Lotus','Missile Men Of India':'APJ Abdul Kalam','Prime Minister Of India':'Narendra Modi','President Of India':'Draupadi Murmu','Father Of Nation':'Mahatma Gandhi'}
score = 0
for i in d1:
    print(i)
    x=input("Enter Answer:")
    if x == d1.get(i):
        score +=5
    else:
        score -=10
    print("The Total Score is ",score)
