import cv2
import numpy as np


def GradientFilter(img):

	N,M=img.shape
	transformed_img=np.zeros([N,M])

	for row in range(1,N-1):
		for col in range(1,M-1):
			#x-dimension
			Gx=int(img[row][col])-int(img[row-1][col])
			#y-dimension
			Gy=int(img[row][col])-int(img[row][col-1])
			transformed_img[row][col]=(np.sqrt(Gx**2+Gy**2))
			#transformed_img[row][col]=Gy	

	return transformed_img

if __name__=='__main__':

	img=cv2.imread('q3_input.jpg')
	img=cv2.split(img)[0]

	final1=GradientFilter(img)

	cv2.imwrite('q4_output_gradient.jpg',final1)