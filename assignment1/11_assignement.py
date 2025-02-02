import cv2

image = cv2.imread('assignment-001-given.jpg')

text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 5
text_color = (0, 255, 0)
bg_color = (0, 0, 0)
opacity = 0.5
img_height, img_width, _ = image.shape

(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)

padding = 120
text_x = img_width - text_width - padding
text_y = text_height + padding

rect_x1, rect_y1 = text_x - 10, text_y - text_height - 10
rect_x2, rect_y2 = text_x + text_width + 10, text_y + baseline + 10

overlay = image.copy()
cv2.rectangle(overlay, (rect_x1, rect_y1), (rect_x2, rect_y2), bg_color, -1)
cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)


cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

cv2.rectangle(image, (200, 200), (950, 950), (0, 255, 0), 10)

cv2.imshow('Image Assignment', image)

cv2.waitKey(0)
cv2.imwrite('result.jpg', image)

cv2.destroyAllWindows()
