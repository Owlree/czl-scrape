__formats__ = []

def get_document_formats():
    return __formats__

with open('static/formats.dat') as f:
    for line in f:
        __formats__.append(line.strip())
