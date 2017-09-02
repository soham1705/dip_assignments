import numpy as np
import cv2
import matplotlib.pyplot as plt

def hist_equalise(img):

	N,M=img.shape
	n=dict()
	n2=dict()
	T=dict()
	L=256

	#count per intensity value
	
	for row in range(N):
		for col in range(M):
			if img[row][col] not in n:
				n[img[row][col]]=0
			else:
				n[img[row][col]]+=1

	#pixelwise transformation

	for r in n:
		T[r]=0
		for j in range(r+1):
			T[r]+=n[j]
		T[r]=(L-1)*T[r]/(M*N)
		

	#transformed image

	transformed_img=np.zeros([N,M])

	for row in range(N):
		for col in range(M):
			transformed_img[row][col]=T[img[row][col]]

	#equalised histogram

	for row in range(N):
		for col in range(M):
			if transformed_img[row][col] not in n2:
				n2[transformed_img[row][col]]=0
			else:
				n2[transformed_img[row][col]]+=1

	return transformed_img


if __name__=='__main__':

	img=cv2.imread('q1_input.jpg')
	img_blue,img_green,img_red=cv2.split(img)
	img_blue_transformed=hist_equalise(img_blue)
	#img_green_transformed=hist_equalise(img_green)
	#img_red_transformed=hist_equalise(img_red)

	#print img_blue_transformed

	cv2.imshow('image',img_blue_transformed)
	cv2.waitKey(0)
	#cv2.imshow('image',img_red_transformed)
	#cv2.waitKey(0)
	#cv2.imshow('image',img_green_transformed)
	#cv2.waitKey(0)
	cv2.destroyAllWindows()



