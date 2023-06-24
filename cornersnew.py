import cv2
import numpy as np


def main():
    camera = cv2.VideoCapture(0)

    while True:
        ret1, img = camera.read()

        if not ret1:
            break


        #img = cv2.imread('example.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,5,3,0.04)
        ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
        dst = np.uint8(dst)
        ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
        corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
        # for i in range(1, len(corners)):
        #    x, y = corners[i]
        #    (x[i], y[i]) = (corners[i])
        #    print(corners[i])

        x3, y3 = corners[3]
        x4, y4 = corners[4]
        x5, y5 = corners[5]
        x6, y6 = corners[6]
        x7, y7 = corners[7]
        x8, y8 = corners[8]
        x9, y9 = corners[9]
        x10, y10 = corners[10]

        #if corners:

        if (x3<x6) & (((y10-y3)-(y7-y6))>5):
            print("rotate counterclockwise")
        elif (x3>x6) & (((y10-y3)-(y7-y6))>5):
            print("rotate clockwise")
        else:
            print("GO")
            cv2.destroyAllWindows()           #[ WARN:0] terminating async callback : error is solved using this line
            break

        # if (x[3]<x[6]) & (((y[10]-y[3])-(y[7]-y[6]))>5):
        #     print("rotate counterclockwise")
        # elif (x[3]>x[6]) & (((y[10]-y[3])-(y[7]-y[6]))>5):
        #     print("rotate clockwise")
        # else:
        #     print("GO")
        #     break


        # if -5<((y7-y5)-(y8-y6))<5
        """if ((y7-y5)-(y8-y6))>5:
            print("rotate counterclockwise")
        elif ((y7-y5)-(y8-y6))<-5:
            print("rotate clockwise")
        else:
            print("GO")"""

        img[dst>0.1*dst.max()]=[0,0,255]
        cv2.imshow('image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows

        if cv2.waitKey(400) & 0xFF is ord('q'):
            cv2.destroyAllWindows()              #[ WARN:0] terminating async callback : error is solved using this line
            break


        else:
            continue

if __name__ == '__main__':
    main()