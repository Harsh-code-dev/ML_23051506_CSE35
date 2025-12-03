import cv2

path = "Screenshot 2025-11-19 170810.png"

img = cv2.imread(path)

if img is None:
    print("Error: Image not found")
else:
    print("Loaded 1 image")
