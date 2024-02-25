from flask_restx import fields
from .extensions import api

from typing import Optional

# Os Models são os modelos que define como será a entrada e saída de uma requisição (input e output)

# Teste
# class CourseModelResponseError:
#     @property
#     def not_found(self):
#         return api.model("404", {
#             "message": "Registro não encontrado!"
#         })

class CourseModel:
            
    @property
    def new(self):
        return api.model("CourseNew", {
            'name': fields.String,
        })
    
    @property
    def put(self):
        return api.model("CoursePut", {
            'id': fields.Integer,
            'name': fields.String,
        })

    @property
    def item(self):
        return api.model("Course", {
            "id": fields.Integer,
            "name": fields.String,
        })

    @property
    def with_relations(self):
        return api.model("CourseByStudents", {
            "id": fields.Integer,
            "name": fields.String,
            "students": fields.List(fields.Nested(StudentModel().item))
        })


class StudentModel:
    
    @property
    def new(self):
        return api.model("StudentNew", {
            "name": fields.String,
            "course_id": fields.Integer,
        })
    
    @property
    def put(self):
        return api.model("StudentPut", {
            "id": fields.Integer,
            "name": fields.String,
            "course_id": fields.Integer
        })
    
    @property
    def item(self):
        return api.model("StudentItem", {
            "id": fields.Integer,
            "name": fields.String,
        })
    
    @property
    def with_relations(self):
        return api.model("Student-relations", {
            "id": fields.Integer,
            "name": fields.String,
            "course": fields.Nested(CourseModel().item), # Registro do curso
        })
