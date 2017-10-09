import cv2
import numpy as np

from collections import OrderedDict

def run_length(img,w):

	N,M=img.shape
	transformed_image=np.zeros([N,M])

	for row in range(0,N-w,w):
		for col in range(0,N-w,w):
			if np.ptp(img[row:row+w,col:col+w])<=15:
				transformed_image[row:row+w,col:col+w]=int(np.median(img[row:row+w,col:col+w]))

	return transformed_image


def huffman(arr):

	p=np.zeros(np.size(arr))
	unique,count=np.unique(arr,return_counts=True)
	count=[float(x)/np.size(arr) for x in count]
	p=dict(zip(unique,count))
	p_ranked=OrderedDict()
	while any(p):
		mx=max(p.values())
		for x in p:
			if p[x]==mx:
				p_ranked[x]=mx
				del(p[x])
				break


if __name__=='__main__':

	img=cv2.imread('kudremukha.jpg')
	img=cv2.split(img)[0]

	#img=run_length(img,3)

	huffman(img[:,0])

	#cv2.imwrite('sample.jpg',img)
	
