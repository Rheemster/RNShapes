import Pyramid,Sphere,Box

m1 = input("If you would like to test for a rectangular prism, enter B.  If you would like to test for a rectangular pyramid, enter P.  If you would like to test for an ellipsoid, enter S.")
m1 = upper(m1)

l = float(input("Enter the length of your object:"))
w = float(input("Enter the width of your object:"))
h = float(input("Enter the height of your object:"))

if m1 == "B":
	myShape = Box.Box(l,w,h)
elif m1 == "P":
	myShape = Pyramid.Pyramid(l,w,h)
elif m1 == "S":
	myShape = Sphere.Sphere(l,w,h)
else:
	print("Invalid mode.")
print("Volume: ",str(myShape.getVolume()))
print("Surface area: ",str(myShape.getSurfaceArea()))
