import cv2
import sys
import os

if (len(sys.argv) == 2): 
	folder = sys.argv[1]
	# Opens the Video file
	cap= cv2.VideoCapture('D:/is/data/' + folder + '/og.mp4')
	i=0
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == False:
			break
		cv2.imwrite('D:/is/data/' + folder + '/2_'+str(i)+'.jpg',frame)
		i+=1
 
	cap.release()
	cv2.destroyAllWindows()

else:
	subfolders = [ f.path for f in os.scandir('D:/is/data/') if f.is_dir() ]

	for f in subfolders:
		print(f)
		folder = f
		# Opens the Video file
		cap= cv2.VideoCapture(folder + '/og.mp4')
		i=0
		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == False:
				break
			cv2.imwrite(folder + '/2_'+str(i)+'.jpg',frame)
			i+=1
 
		cap.release()
		cv2.destroyAllWindows()