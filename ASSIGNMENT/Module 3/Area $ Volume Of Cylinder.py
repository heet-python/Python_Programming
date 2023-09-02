pi=3.14
height = float(input('Height of cylinder: '))
radius = float(input('Radius of cylinder: '))
volume = pi * (2*radius)* height
sur_area = ((2*pi*radius) * height) + ((pi*radius**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)
