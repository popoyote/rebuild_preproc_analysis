import cv2
import numpy as np
from paddleocr import PaddleOCR
import os
from PIL import Image

def improve_image_quality(image_path):
    """Улучшает качество изображения: повышение резкости и шумоподавление."""
    # Чтение изображения
    image = cv2.imread(image_path)

    # Повышение резкости
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)

    # Шумоподавление
    denoised = cv2.fastNlMeansDenoisingColored(sharpened, None, 10, 10, 7, 21)

    # Сохранение улучшенного изображения
    improved_path = "improved_" + image_path
    cv2.imwrite(improved_path, denoised)
    return improved_path


def extract_text_from_image(image_path):
    """Извлекает текст из изображения с помощью PaddleOCR."""
    # Улучшение качества изображения
    improved_path = improve_image_quality(image_path)

    # Инициализация PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='ru')

    # Извлечение текста
    result = ocr.ocr(improved_path, cls=True)
    extracted_text = " ".join([line[-1][0] for line in result])
    return extracted_text


def convert_to_png(image_path):
    """Конвертирует изображение в формат PNG, если оно не в PNG."""
    if not image_path.lower().endswith('.png'):
        img = Image.open(image_path)
        png_path = os.path.splitext(image_path)[0] + ".png"
        img.save(png_path, "PNG")
        return png_path
    return image_path
