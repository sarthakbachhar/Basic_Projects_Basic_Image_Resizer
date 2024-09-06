import cv2

# Load the image
img= cv2.imread("C:\\Users\\Acer\\Desktop\\nobi.jpg")

# Check if the image was loaded successfully
if img is None:
  print("Unable to load image.")

else:
  # Resize the loaded image
  new_img = cv2.resize(img,(720,720))

  # Display the resized image
  cv2.imshow("Resized Image", new_img)

  # Wait until a key is pressed
  cv2.waitKey(0)
  
  # Destroy all windows opened by OpenCV
  cv2.destroyAllWindows()