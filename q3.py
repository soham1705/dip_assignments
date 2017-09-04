import cv2
import numpy as np


def GaussianFilter(img):

	N,M=img.shape
	img=np.pad(img,(1,),'constant',constant_values=0)
	gaussian_mask=(1/16.)*np.matrix('1 2 1;2 4 2;1 2 1')
	transformed_img=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			x1=np.multiply(gaussian_mask,img[row:row+3,col:col+3])
			transformed_img[row][col]=(np.sum(np.sum(x1)))

	return transformed_img.astype(int)


def MedianFilter(img):

	N,M=img.shape
	img=np.pad(img,(1,),'constant',constant_values=0)
	transformed_img=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			transformed_img[row][col]=np.median(img[row:row+3,col:col+3])

	return transformed_img


if __name__=='__main__':

	img=cv2.imread('q3_input.jpg')
	img=cv2.split(img)[0]

	final1=GaussianFilter(img)

	cv2.imwrite('q3_output_gaussian.jpg',final1)

	final2=MedianFilter(img)

	cv2.imwrite('q3_output_median.jpg',final2)

