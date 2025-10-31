class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j]=image[i][j]^1
            start,end=0,len(image[0])-1
            while start<end:
                image[i][start],image[i][end]=image[i][end],image[i][start]
                start+=1
                end-=1
        return image