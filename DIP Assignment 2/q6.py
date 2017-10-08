import cv2
import numpy as np


def downsample(img,n):

	N,M=img.shape
	transformed_img=np.zeros([N,M])
	for row in range(0,N,n):
		for col in range(0,M,n):
			img[row:row+n,col:col+n]=img[row][col]


if __name__=='__main__':

	img=cv2.imread('kudremukha.jpg')
	img=cv2.split(img)[0]
	
	N,M=img.shape
	img=np.pad(img,(M-N,0),'constant',constant_values=0)[:,-M:M+N+1]

	downsample(img,4)

