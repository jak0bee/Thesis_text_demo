import cv2
import pytesseract
from pytesseract import Output


# Load the image
image_path = "example_image.png"  # Replace with your image path
image = cv2.imread(image_path)

# Convert image to grayscale (optional, for better OCR performance)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR with output as a dictionary
data = pytesseract.image_to_data(gray, output_type=Output.DICT)

# Extract text and bounding box coordinates
text_data = []
for i in range(len(data['text'])):
    if data['text'][i].strip():  # Check if text is not empty
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        text = data['text'][i]
        text_data.append({'text': text, 'x': x, 'y': y, 'width': w, 'height': h})

# Print results
for item in text_data:
    print(f"Text: {item['text']} | Coordinates: ({item['x']}, {item['y']}, {item['width']}, {item['height']})")

# Optionally visualize the results
for item in text_data:
    x, y, w, h = item['x'], item['y'], item['width'], item['height']
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, item['text'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image
cv2.imshow("Text Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
