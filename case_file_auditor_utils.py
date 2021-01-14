import docx

# filename: name of file to be read
# scrub_list: list of words to removed from document
def read_docx_text(filename, scrub_list):
    document = docx.Document(filename)  # creating word reader object.
    data = ''

    paragraphs = []
    for pgh in document.paragraphs:
        paragraphs.append(pgh.text)

    text = '\n'.join(paragraphs)

    return data
