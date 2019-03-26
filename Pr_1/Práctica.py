import numpy as np
import cv2

if __name__ == '__main__':

    INPUT = input("Input image: ")
    target = input("Target image: ")
    threshold = float(input("Threshold: "))

    img_I_color = np.float64(cv2.imread(INPUT, -1))
    img_T_color = np.float64(cv2.imread(target, -1))

    img_I = np.float64(cv2.imread(INPUT, cv2.IMREAD_GRAYSCALE))
    img_T = np.float64(cv2.imread(target, cv2.IMREAD_GRAYSCALE))

    imgT_w = img_T.shape[0]
    imgT_h = img_T.shape[1]

    imgI_w = img_I.shape[0]
    imgI_h = img_I.shape[1]

    imgFinal_w = img_I.shape[0] - img_T.shape[0] + 1
    imgFinal_h = img_I.shape[1] - img_T.shape[1] + 1
    img_FINAL = np.zeros((imgFinal_w, imgFinal_h))

    bigestError = 0
    lowestError = 100000000

    for y in range(0, imgFinal_h):
        for x in range(0, imgFinal_w):
            iterativeRes = 0
            for j in range(0, img_T.shape[1]):
                for i in range(0, img_T.shape[0]):
                    iterativeRes += (img_T[i, j] - img_I[x + i, y + j]) ** 2
            if iterativeRes > bigestError:
                bigestError = iterativeRes
            if iterativeRes < lowestError:
                lowestError = iterativeRes
            if iterativeRes < threshold:
                cv2.rectangle(img_I_color, (x - 1, y - 1), (x + imgT_w, y + imgT_h), (0.0, 255.0, 0.0))
            img_FINAL[x, y] = iterativeRes

    if lowestError / bigestError < threshold:
        print("TARGET FOUND")

    img_FINAL[:] = (img_FINAL[:] / bigestError * 255.0)


    cv2.imshow('Target Image', np.uint8(img_T_color))
    cv2.imshow('Input Image', np.uint8(img_I_color))
    cv2.imshow('Maching Map', np.uint8(img_FINAL))
    cv2.waitKey(0)
