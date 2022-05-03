img = cv2.imread("./sample_image0.png")
config = ('-l eng --oem 1 --psm 3')
text = pytesseract.image_to_string(img, config=config)
print(img)
