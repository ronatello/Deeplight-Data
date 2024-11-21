import math
import numpy as np
import cv2

arr = []

for angle1 in range(0, 32):
	for angle2 in range(0, 32):

		phi = 5.625 * angle1
		theta = 11.25 * angle2

		D_x = math.sin(math.radians(phi)) * math.cos(math.radians(theta))
		D_y = math.sin(math.radians(phi)) * math.sin(math.radians(theta))
		D_z = -1 * math.cos(math.radians(phi))

		if(D_x == 0 and D_y == 0):
			r = 0
		else:
			r = (math.sin(1/2 * math.acos(-1 * D_z)) / (2 * math.sqrt((D_x ** 2) + (D_y ** 2))))

		u = 1/2 + (r * D_x)
		v = 1/2 - (r * D_y)

		u *= 32
		v *= 32

		u = round(u)
		v = round(v)

		arr.append(u*100 + v)
		#print(u, v)

img = np.zeros((32, 32))
temp_arr = []
phi_arr = []
theta_arr = []
phi_theta_arr = []

for pixel1 in range(0, 32):
	for pixel2 in range(0, 32):

		if(pixel1 == 0 and pixel2 == 0):
			continue

		u = float(pixel1)/32
		v = float(pixel2)/32

		r = math.sqrt((2*u - 1)**2 + (2*v - 1)**2)
		theta2 = math.atan2(-2*v + 1, 2*u - 1)
		try:
			phi2 = 2*math.asin(r)
			img[pixel1, pixel2] = 1
		except:
			#print(u, v, r)
			img[pixel1, pixel2] = 0
			continue

		theta2_deg = math.degrees(theta2)
		phi2_deg = math.degrees(phi2)

		theta2_deg = round(theta2_deg, 3)
		phi2_deg = round(phi2_deg, 3)

		if(theta2_deg < 0):
			theta2_deg = 360 + theta2_deg
		
		if(phi2_deg < 0):
			phi2_deg = 360 + phi2_deg

		print(phi2_deg, theta2_deg)
		temp_arr.append((phi2_deg, theta2_deg))

		phi_arr.append(round(phi2_deg, 0))
		theta_arr.append(round(theta2_deg, 0))

		phi_theta_arr.append((round(phi2_deg, 0), round(theta2_deg, 0)))

	print("")
	print("")
	print("")


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()  

arr2 = set(arr)
temp_arr2 = set(temp_arr)

print(len(temp_arr))
print(len(temp_arr2))

#print(len(arr))
#print(len(arr2))

for i in range(0, 182):
	if(i not in phi_arr):
		print(i)

print("")
print("")
print("")

for j in range(0, 360):
	if (j not in theta_arr):
		print(j)

print("")
print("")
print("")

#for i in range(0, 180):
#	for j in range(0, 360):
#		if((i, j) not in phi_theta_arr):
#			print((i, j))