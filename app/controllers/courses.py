from app.models import db
from app.models import Course

# Create your controller here.
class CourseController(object):
    
    def list(self):
        return Course.query.all()
    
    def get(self, id):
        course = db.get_or_404(Course, id)
        return course

    def add(self, name):
        course = Course(name=name)
        db.session.add(course)
        db.session.commit()
        return course
    
    def update(self, id: int, name: str):
        course = db.get_or_404(Course, id)
        course.name = name
        
        db.session.commit()
        return course
    
    def delete(self, id: int):
        course = db.get_or_404(Course, id)
        db.session.delete(course)
        db.session.commit()
        return course