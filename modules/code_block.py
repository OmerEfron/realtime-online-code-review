
class CodeBlock:
    count = 0
    def __init__(self, title, code):
        CodeBlock.count += 1
        self._id = CodeBlock.count
        self._title = title
        self._code = code

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_code(self):
        return self._code

    def set_code(self, new_code):
        self._code = new_code