from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DBCodeBlock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True,nullable=False)
    code = db.Column(db.String)
    solution = db.Column(db.String)

    def check_code(self):
        if self.code == self.solution:
            return True
        else:
            return False
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'code': self.code,
            'solution': self.solution
        }
class CodeBlock:
    count = 0
    def __init__(self, title, code, solution):
        CodeBlock.count += 1
        self._id = CodeBlock.count
        self._title = title
        self._code = code
        self._solution = solution

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_code(self):
        return self._code
    def get_solution(self):
        return self._solution
    def set_code(self, new_code):
        self._code = new_code
