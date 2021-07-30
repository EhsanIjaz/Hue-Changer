import cv2
import numpy as np
import os
import sys
import glob



def hue_changer(i):
    outs=i
#     print(i)
    # load image with alpha channel
    img = cv2.imread(i, cv2.IMREAD_UNCHANGED)
#     print (img)

    # extract alpha channel
    alpha = img[:,:,2]
    alpha_2 = img[:,:,2]

    # extract bgr channels
    bgr = img[:,:,0:3]

    # convert to HSV
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    #h = hsv[:,:,0]
    #s = hsv[:,:,1]
    #v = hsv[:,:,2]
    h,s,v = cv2.split(hsv)

    # purple is 276 in range 0 to 360; so half in OpenCV
    # green is 120 in range 0 to 360; so half in OpenCV
    purple = 208
    green = 200

    # diff color (green - hue)
    diff_color = -8
    diff_color_2 = 5

    # modify hue channel by adding difference and modulo 180
    hnew = np.mod(h + diff_color, 180).astype(np.uint8)
    hnew_2 = np.mod(h + diff_color_2, 180).astype(np.uint8)

    # recombine channels
    hsv_new = cv2.merge([hnew,s,v])
    hsv_new_2 = cv2.merge([hnew_2,s,v])

    # convert back to bgr
    bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)
    bgr_new_2 = cv2.cvtColor(hsv_new_2, cv2.COLOR_HSV2BGR)

    # put alpha back into bgr_new
    bgra = cv2.cvtColor(bgr_new, cv2.COLOR_BGR2BGRA)
    bgra_2 = cv2.cvtColor(bgr_new_2, cv2.COLOR_BGR2BGRA)
    bgra[:,:,2] = alpha
    bgra_2[:,:,2] = alpha_2

    print(i)


    #string formating
    path = "/".join(i.split('/')[:-1])
    print(path)
    filename= i.split('/')[-1].split('.')[0]
    print(filename)
    basename, ext = os.path.splitext(filename)
    out_name = '{}_{:03d}.png'.format(basename,1)

    # save output
    cv2.imwrite(path+'/'+filename+'_Black_white.png', alpha)
#     cv2.imwrite(path+'/'+filename+'_Orignal.png', bgr)
    cv2.imwrite(path+'/'+filename+'_new.png', bgr_new)
    cv2.imwrite(path+'/'+filename+'_new_2.png', bgr_new_2)
    # cv2.imwrite('sword_green.png', bgra)
    # cv2.imwrite('sword_green_2.png', bgra_2)



    # # save all images
    # alpha.save(sword_alpha.png)
    # bgr.save(bgr)
    # bgr_new.save(bgr_new)
    # bgra.save(bgra)

    # Display various images to see the steps
    # cv2.imshow('alpha',alpha)
    # cv2.imshow('bgr',bgr)
    # cv2.imshow('bgr_new',bgr_new)
    # cv2.imshow('bgra',bgra)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
def main(ins):
    f=glob.glob(ins+"/*")
    for i in f:
        hue_changer(i)
        
if __name__ == "__main__":
    main(sys.argv[1])
