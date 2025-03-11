import os
import pandas as pd


def extract_text_from_table(file_path):

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == '.csv':
        df = pd.read_csv(file_path, dtype=str)
    elif ext == '.xlsx':
        df = pd.read_excel(file_path, dtype=str)
    else:
        print(f"Неподдерживаемый формат файла: {file_path}")
        return None
    return '\n'.join([' '.join(row) for row in df.astype(str).values])