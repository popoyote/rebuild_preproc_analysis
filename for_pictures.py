import time

import cv2
import numpy as np
from paddleocr import PaddleOCR
import os
from PIL import Image


def improve_image_quality(image_path, output_folder="improved_pictures"):
    """Улучшает качество изображения: повышение резкости и шумоподавление."""
    # Создаем папку для улучшенных изображений, если её нет
    os.makedirs(output_folder, exist_ok=True)

    # Чтение изображения
    image = cv2.imread(image_path)

    # Проверка, загружено ли изображение
    if image is None:
        print(f"Ошибка: Не удалось загрузить изображение {image_path}")
        return None

    # Повышение резкости
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)

    # Шумоподавление
    denoised = cv2.fastNlMeansDenoisingColored(sharpened, None, 10, 10, 7, 21)

    # Сохранение улучшенного изображения
    improved_filename = "improved_" + os.path.basename(image_path)
    improved_path = os.path.join(output_folder, improved_filename)
    cv2.imwrite(improved_path, denoised)
    return improved_path


def extract_text_from_image(image_path, confidence_threshold=0.7):
    """Извлекает текст из изображения с учетом структуры данных PaddleOCR."""
    # Улучшение качества изображения
    improved_path = improve_image_quality(image_path)
    if not improved_path:
        return ""

    # Инициализация PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='ru')
    result = ocr.ocr(improved_path, cls=True)

    # Обработка результата
    extracted_text = []

    # Проверка, что результат не None и итерируем
    if result is None:
        return ""

    for line_group in result:
        # Пропускаем None и неитерируемые элементы
        if line_group is None or not isinstance(line_group, (list, tuple)):
            continue

        for line in line_group:
            # Проверка структуры строки
            if line and len(line) >= 2:
                text_info = line[1]
                if text_info and isinstance(text_info, (list, tuple)) and len(text_info) >= 2:
                    text, confidence = text_info[0], text_info[1]
                    if confidence >= confidence_threshold:
                        extracted_text.append(str(text))

    return " ".join(extracted_text)


def convert_to_png(image_path, output_folder="improved_pictures"):
    """Конвертирует изображение в формат PNG, если оно не в PNG."""
    # Создаем папку для улучшенных изображений, если её нет
    os.makedirs(output_folder, exist_ok=True)

    if not image_path.lower().endswith('.png'):
        img = Image.open(image_path)
        png_filename = os.path.splitext(os.path.basename(image_path))[0] + ".png"
        png_path = os.path.join(output_folder, png_filename)
        img.save(png_path, "PNG")
        return png_path
    return image_path
