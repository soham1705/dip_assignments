import cv2
import numpy as np

def downsample(img,n):

	N,M=img.shape
	transformed_image=np.zeros([N/n,M/n])
	i=0
	for row in range(0,N,n):
		j=0
		for col in range(0,M,n):
			transformed_image[i][j]=img[row][col]
			j+=1
		i+=1

	return transformed_image


def create_haar_matrix(N):

	H=np.zeros([N,N])

	for i in range(N):

		k=i

		for j in range(N):

			p=0 if k==0 else int(np.log2(k))
			q=k-2**p+1

			z=float(j)/N

			if k==p==q==0:
				H[i][j]=1

			else:
				if (q-1.0)/(2.0**p)<=z<(q-0.5)/(2.0**p):
					H[i][j]=2**(p/2.0)
				elif (q-0.5)/(2.0**p)<=z<(q)/(2.0**p):
					H[i][j]=-2**(p/2.0)
				else:
					H[i][j]=0	

	H=H/(np.sqrt(N))

	return H


if __name__=='__main__':

	img=cv2.imread('kudremukha.jpg')
	img=cv2.split(img)[0]
	
	N,M=img.shape
	img=np.pad(img,(M-N,0),'constant',constant_values=0)[:,-M:M+N+1]

	img=downsample(img,8)

	N,M=img.shape
	X=2**N.bit_length()
	img=np.pad(img,(X-N,0),'constant',constant_values=0)

	H=create_haar_matrix(X)

	img=np.matmul(np.matmul(H,img),H)
	
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,'Q6. Output',(200,50),font,0.8,(255,255,255),2,cv2.LINE_AA)
	cv2.imwrite('q6_output.jpg',img)