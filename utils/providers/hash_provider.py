from passlib.hash import pbkdf2_sha256

class Hash:

    @staticmethod
    def generate(text):
        return pbkdf2_sha256.hash(text)

    @staticmethod
    def verify(text, hashed_text):
        return pbkdf2_sha256.verify(text, hashed_text)