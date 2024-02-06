from app.models import db
from app.models import Student


class StudentController(object):

    def list(self):
        return Student.query.all()
    
    def get(self, id):
        student = db.get_or_404(Student, id)
        return student

    def add(self, name, course_id):
        student = Student(name=name, course_id=course_id)
        db.session.add(student)
        db.session.commit()
        return student
    
    def update(self, id: int, name: str):
        student = db.get_or_404(Student, id)
        student.name = name
        
        db.session.commit()
        return student
    
    def delete(self, id: int):
        student = db.get_or_404(Student, id)
        db.session.delete(student)
        db.session.commit()
        return student
