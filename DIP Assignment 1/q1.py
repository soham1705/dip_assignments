import numpy as np
import cv2

def hist_equalise(img):

	N,M=img.shape
	L=256
	p=np.zeros(L,dtype=int)
	T=np.zeros(L,dtype=int)

	#count per intensity value
	
	for row in range(N):
		for col in range(M):
			p[img[row][col]]+=1

	#pixelwise transformation

	T=(L-1)*np.cumsum(p)/(M*N)

	#transformed image

	for row in range(N):
		for col in range(M):
			img[row][col]=T[img[row][col]]
			

if __name__=='__main__':

	img=cv2.imread('1.jpg')
	img_blue,img_green,img_red=cv2.split(img)

	hist_equalise(img_blue)
	hist_equalise(img_green)
	hist_equalise(img_red)

	final=cv2.merge((img_blue,img_green,img_red))
	cv2.imwrite('q1_output.jpg',final)
	



