import cv2
import matplotlib.pyplot as plt
from task3a import preprocess_receipt 

def show_result(image_path):
    # Load original
    original = cv2.imread(image_path)
    original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    
    # Run your preprocessing
    processed = preprocess_receipt(image_path)
    
    # Display side-by-side
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Receipt")
    plt.imshow(original_rgb)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title("Preprocessed (For OCR)")
    plt.imshow(processed, cmap='gray')
    plt.axis('off')
    
    plt.show()

# Replace with the name of the file you downloaded
show_result('0.jpg') 
