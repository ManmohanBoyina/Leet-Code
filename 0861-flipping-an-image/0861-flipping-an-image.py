class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j]=image[i][j]^1
            image[i]=image[i][::-1]
        return image