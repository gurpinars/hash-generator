import hashlib

class Generator(object):
    """
    >>> generator = Generator()
    >>> generator.md5('string')

    Class including hash genarating methods.

    """
    
    def __init__(self,ui):
        self.ui = ui
    
    def md5(self,text):
        self.hash = hashlib.md5(text).hexdigest()
        self.ui.textEdit.setText(self.hash)
    
    def sha(self,text):
        self.hash = hashlib.sha1(text).hexdigest()
        self.ui.textEdit.setText(self.hash)
    
    def sha224(self,text):
        self.hash = hashlib.sha224(text).hexdigest()
        self.ui.textEdit.setText(self.hash)

    def sha256(self,text):
        self.hash = hashlib.sha256(text).hexdigest()
        self.ui.textEdit.setText(self.hash)

    def sha384(self,text):
        self.hash = hashlib.sha384(text).hexdigest()
        self.ui.textEdit.setText(self.hash)

    def sha512(self,text):
        self.hash = hashlib.sha512(text).hexdigest()
        self.ui.textEdit.setText(self.hash)