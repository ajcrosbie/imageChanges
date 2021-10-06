import cv2
import os

def oneImage(img, name):
    os.chdir("..")
    os.chdir("outputImages")


    name = "lines" + name
    cv2.imwrite(name, cv2.Canny(img, 200, 300))
    cv2.waitKey()
    cv2.destroyAllWindows()

def folder():
    filePath = "images"
    os.chdir(filePath)
    files = os.listdir(os.getcwd())
    for f in range(len(files)):
        if files[f].endswith(".jpg") or files[f].endswith(".png"):
            img = cv2.imread(files[f], 0)
            oneImage(img, files[f])
            os.chdir("..")
            os.chdir(filePath)
            
if __name__ == "__main_":
    folder()