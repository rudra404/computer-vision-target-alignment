import cv2
import numpy as np


def main():
    global area
    camera = cv2.VideoCapture(0)

    while True:
        ret, image = camera.read()

        if not ret:
            break

        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v1_min=0
        v2_min=144
        v3_min=155
        v1_max=18
        v2_max=227
        v3_max=220

        w1_min = 87        #new
        w2_min = 76        #new
        w3_min = 92        #new
        w1_max = 138       #new
        w2_max = 232       #new
        w3_max = 164       #new

        #threshold the image to get only target value colours.
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
        thresh1 = cv2.inRange(frame_to_thresh, (w1_min, w2_min, w3_min), (w1_max, w2_max, w3_max))  #new

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)       #new
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_CLOSE, kernel)        #new



        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            area = np.pi*radius*radius

            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(image, center, 3, (0, 0, 255), -1)
                cv2.putText(image, "centroid", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255),
                            1)
                cv2.putText(image, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

        npImg = np.asarray(mask1)  # No copying takes place      #new

        coordList = np.argwhere(npImg == 255)                    #new
        numWhitePoints = len(coordList)                          #new
        num1 = 0                                                 #new
        num2 = 0                                                 #new
        for i in range(numWhitePoints):                          #new
            if coordList[i][1] < 320:                            #new
                num1 = num1 + 1                                  #new
            elif coordList[i][1] > 320:                          #new
                # else:                                          #new
                num2 = num2 + 1                                  #new

        #print("num1: ", num1)
        #print("num2: ", num2)

        # show the frame to our screen
        cv2.imshow("Original", image)
        cv2.imshow("Thresh", thresh)
        cv2.imshow("Mask", mask)
        cv2.imshow("Thresh1", thresh1)      #new
        cv2.imshow("Mask1", mask1)          #new


        if cv2.waitKey(400) & 0xFF is ord('q'):
            cv2.destroyAllWindows()
            break

        if center:
            #print("area =", area)
            #print("x= ", center[0],"y= ",center[1])
            if center[0] in range(360,640):
                print("Move Right")
            elif center[0] in range(0,280):
                print("Move Left")
            else:
                print("Centre")
                pass

            if 100<area<23000:
                print ("Move Forward")
            elif 82000<area<90000:
                print ("Move Backward")
            else :
                print("Distance OK")

                if (num1/num2)<0.95:                      #new
                    print("rotate counterclockwise")      #new

                elif (num1/num2)>1.05:                    #new
                    print("rotate clockwise")             #new

                else:                                     #new
                    print("GO")                           #new
                    #break                                #new
            print (" \n***************")                  #new

        else:
            continue

if __name__ == '__main__':
    main()