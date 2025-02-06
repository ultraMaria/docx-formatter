import csv

from docx import Document
from python_docx_replace import docx_replace

def create_document(info: dict, path: str):
    document = Document()
    document = Document(path)

    docx_replace(document, **info)

    document.save('demo.docx')

def process_config():
    with open('config.csv', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        line = []
        for row in reader:
            line.extend(row)
        for ind, element in enumerate(line):
            if not element:
                line.pop(ind)

        filepath = line.pop(0)
        return filepath, line

process_config()