from flask_restx import Resource, Namespace
from .api_models import CourseModel, StudentModel
from .controllers.courses import CourseController
from .controllers.students import StudentController

from operator import itemgetter
from functools import wraps
import uuid, jwt
from datetime import datetime

# 
cm = CourseModel()
sm = StudentModel()

# Separador de endpoints chamados de Namespace
ns = Namespace('/')
nsc = Namespace('course')
nss = Namespace('student')

# read more: https://flask-restx.readthedocs.io/en/latest/swagger.html

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return { 'hello': 'restx' }


@nsc.route('/')
class CoursesAPI(Resource):
    @nsc.response(404, 'Registro não encontrado')
    @nsc.marshal_list_with(cm.item)
    def get(self):
        return CourseController().list(), 200
    
    @nsc.expect(cm.new) # novo item
    @nsc.marshal_with(cm.item) # dados do curso
    def post(self):
        course = CourseController().add(ns.payload['name'])
        return course, 201
    
    @nsc.expect(cm.put)
    @nsc.marshal_list_with(cm.item)
    def put(self):
        course_id, course_name = itemgetter('id', 'name')(nsc.payload) # Payload -> objeto de informações
        course = CourseController().update(course_id, course_name)
        return course, 200


@nsc.route('/courses/<int:id>')
@nsc.doc(params={'id': 'ID do curso'})
class CoursesAPIID(Resource):

    def delete(self, id: int):
        course = CourseController().delete(id=id)
        return course, 204


@nss.route('/')
class StudentsAPI(Resource):
    
    @nss.marshal_list_with(sm.item)
    def get(self):
        return StudentController().list()
    
    @nss.expect(sm.new)
    @nss.marshal_list_with(sm.item)
    def post(self):
        name, course_id = itemgetter('name', 'course_id')(nss.payload)
        studen = StudentController().add(name, course_id)
        return studen, 201
    
    def put(self):
        ...
    

@nss.route('/relations')
class StudentsRelationsAPI(Resource):
    
    @nss.marshal_list_with(sm.with_relations)
    def get(self):
        return StudentController().list()


@nss.route('/by-course-id/<int:course_id>')
class StudentsByCoursesAPI(Resource):
    
    @nss.marshal_list_with(cm.with_relations)
    @nss.doc(params={ 'course_id': 'Id do curso'})
    def get(self, course_id: int):
        return CourseController().get(course_id)
