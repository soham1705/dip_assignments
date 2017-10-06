import cv2
import numpy as np

img=cv2.imread('anadka.jpg')
b,g,r=cv2.split(img)
N,M=b.shape

H=np.zeros([N,M])
S=np.zeros([N,M])
I=np.zeros([N,M])

for i in range(N):
	for j in range(M):

		R=float(r[i][j])
		B=float(b[i][j])
		G=float(g[i][j])

		#print R,B,G

		I[i][j]=(R+G+B)/3

		S[i][j]=1-(3/(R+G+B)*min(R,G,B))

		if R==G==B:
			H[i][j]=0
		else:
			#print R,G,B
			#print ((R-G)**2+(R-B)*(G-B))**0.5
			theta=np.arccos(0.5*((R-G)+(R-B))/(((R-G)**2+(R-B)*(G-B))**0.5))
			if B<=G:
				H[i][j]=theta
			elif B>G:
				H[i][j]=2*np.pi-theta

print "Hue"
print H
print "Saturation"
print S
print "Intensity"
print I
