from . import constants

def is_document(url):
    for document_format in constants.get_document_formats():
        if url.endswith('.{}'.format(document_format)):
            return True
        return False
