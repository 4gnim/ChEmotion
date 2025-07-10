from PIL import Image
import pytesseract
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(file):
    image = Image.open(io.BytesIO(file))
    text = pytesseract.image_to_string(image, lang="eng")
    return text
