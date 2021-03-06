import docx
import os
import re
import pandas as pd

# filename: name of file to be read
# scrub_list: list of words to removed from document
def read_docx_text(filename, scrub_list=None):
    document = docx.Document(filename)  # creating word reader object.
    data = ''

    paragraphs = []
    for pgh in document.paragraphs:
        paragraphs.append(pgh.text)

    text = '\n'.join(paragraphs)

    return text

# can be used to read .txt and .doc file extensions
# other formats may return some sort of unicode
def read_file_contents(filename, scrub_list=None):
    with open(filename, 'r',encoding='utf-8') as file:
        return file.read()

# one big string of all text in folder
def get_words_goodie_bag(folder_directory):
    bag = ''

    for subdir, dirs, files in os.walk(folder_directory):
        for file in files:
            if re.search(r'.docx$', file):
                bag += read_docx_text(os.path.join(subdir, file))

            elif re.search(r'.txt$',file):
                bag += read_file_contents(os.path.join(subdir, file))


            elif re.search(r'.csv$', file):
                df = pd.read_csv(os.path.join(subdir, file))

                # concat strings in matrix
                text = ' '.join([' '.join([str(element) for element in row]) for row in df.values])

                # add column names
                text += ''.join(df.columns)

                bag += text

    return bag


def folder_as_document_list(folder_directory):
    documents = []
    pdfs = []
    for subdir, dirs, files in os.walk(folder_directory):
        for file in files:
            if re.search(r'.docx$', file):
                documents.append(read_docx_text(os.path.join(subdir, file)))

            elif re.search(r'.txt$', file):
                documents.append(read_file_contents(os.path.join(subdir, file)))

            elif re.search(r'.csv$', file):
                df = pd.read_csv(os.path.join(subdir, file))

                # concat strings in matrix
                text = ' '.join([' '.join([str(element) for element in row]) for row in df.values])

                # add column names
                text += ''.join(df.columns)

                documents.append(text)

            elif re.search(r'.pdf$', file):
                pdfs.append(file)

    return documents, pdfs
