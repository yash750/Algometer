from PIL import Image
import pytesseract


def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


print(extract_text("Screenshot from 2024-09-24 13-22-42.png"))

if __name__ == "__main__":
    path = "Screenshot from 2024-09-24 13-22-42.png"
    extract_text(path)
