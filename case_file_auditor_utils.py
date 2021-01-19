import docx

# filename: name of file to be read
# scrub_list: list of words to removed from document
def read_docx_text(filename, scrub_list=None):
    document = docx.Document(filename)  # creating word reader object.
    data = ''

    paragraphs = []
    for pgh in document.paragraphs:
        paragraphs.append(pgh.text)

    text = '\n'.join(paragraphs)

    return data

# can be used to read .txt and .doc file extensions
# other formats may return some sort of unicode
def read_file_contexts(filename, scrub_list=None):
    with open(filename, 'r') as file:
        return file.read()
