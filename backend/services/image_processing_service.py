from PIL import Image
import pytesseract
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

def process_image(file_path):
    """
    Processes the image to extract metadata and text.

    Args:
        file_path (str): The path to the image file.

    Returns:
        dict: A dictionary containing metadata about the image and extracted text.
    """
    try:
        # Open the image file
        with Image.open(file_path) as img:
            # Extract metadata
            metadata = extract_metadata(img, file_path)

            # Perform OCR to extract text
            extracted_text = pytesseract.image_to_string(img)

            # Analyze the text for sensitive information
            sensitivity_rating = analyze_text_for_sensitivity(extracted_text)

        return {
            "metadata": metadata,
            "extracted_text": extracted_text,
            "sensitivity_rating": sensitivity_rating,
        }
    except Exception as e:
        return {"error": str(e)}

def extract_metadata(img, file_path):
    """
    Extract metadata from the image.

    Args:
        img (Image): The opened image object.
        file_path (str): The path to the image file.

    Returns:
        dict: A dictionary containing metadata about the image.
    """
    return {
        'filename': os.path.basename(file_path),
        'format': img.format,
        'size': img.size,  # (width, height)
        'mode': img.mode,
        'info': img.info,  # Additional information, if available
    }

def analyze_text_for_sensitivity(text):
    """
    Analyze the extracted text to determine its sensitivity level.

    Args:
        text (str): The extracted text from the image.

    Returns:
        str: A rating of the sensitivity of the text.
    """
    # Basic rules for sensitivity rating (can be enhanced with more complex logic)
    if "confidential" in text.lower() or "sensitive" in text.lower():
        return "Critical"
    elif "grade" in text.lower() or "score" in text.lower():
        return "Sensitive"
    elif "personal" in text.lower():
        return "Average"
    else:
        return "Weak"

# Example usage
if __name__ == "__main__":
    file_path = 'static/uploads/your_image.jpg'  # Update with an actual image path
    result = process_image(file_path)
    print(result)
