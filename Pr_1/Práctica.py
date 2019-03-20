import numpy as np
import cv2

if __name__ == '__main__':

    img_I = cv2.imread('img1.png', cv2.IMREAD_GRAYSCALE)
    img_T = cv2.imread('t1-img1.png', cv2.IMREAD_GRAYSCALE)

    imgFinal_w = img_I.shape[0] - img_T.shape[0] + 1
    imgFinal_h = img_I.shape[1] - img_T.shape[1] + 1
    img_FINAL = np.zeros((imgFinal_w, imgFinal_h))

    bigestError = 0

    for y in range(0, imgFinal_h):
        for x in range(0, imgFinal_w):
            iterativeRes = 0
            for j in range(0, img_T.shape[1]):
                for i in range(0, img_I.shape[0] - 1):
                    iterativeRes += (img_T[i, j] - img_I[x + i, y + j]) ** 2
            if iterativeRes > bigestError:
                bigestError = iterativeRes
            img_FINAL[x, y] = iterativeRes

    img_FINAL[:] / bigestError * 255.0

    cv2.imshow('DAMN',img_FINAL)
    cv2.waitKey(0)
