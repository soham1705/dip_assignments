import cv2
import numpy as np


def GradientFilter(img):

	N,M=img.shape
	transformed_img=np.zeros([N,M])

	for row in range(N-1):
		for col in range(M-1):
			#x-dimension
			Gx=int(img[row+1][col])-int(img[row][col])
			#y-dimension
			Gy=int(img[row][col+1])-int(img[row][col])
			transformed_img[row][col]=(np.sqrt(Gx**2+Gy**2))

	return transformed_img


def LaplacianFilter(img):

	N,M=img.shape
	transformed_img=np.zeros([N,M])

	for row in range(N-1):
		for col in range(M-1):
			transformed_img[row][col]=int(img[row+1][col])+int(img[row-1][col])+int(img[row][col+1])+int(img[row][col-1])-4*int(img[row][col])

	return transformed_img


if __name__=='__main__':

	img=cv2.imread('3.jpg')
	img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	final1=GradientFilter(img)

	cv2.imwrite('q4_output_gradient.jpg',final1)

	final2=LaplacianFilter(img)

	cv2.imwrite('q4_output_laplacian.jpg',final2)

