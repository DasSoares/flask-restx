from flask_restx import Resource, Namespace, abort
from .api_models import CourseModel, StudentModel
from .controllers.courses import CourseController
from .controllers.students import StudentController

from operator import itemgetter
from functools import wraps
import uuid, jwt, json
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


@nsc.route('/<int:id>')
@nsc.doc(params={'id': 'Id do curso'})
class CoursesAPIID(Resource):

    @nsc.marshal_list_with(cm.item) # retorna como o item de exemplo
    def get(self, id: int):
        course = CourseController()
        data = course.get(id)
        return data, 200

    def delete(self, id: int):
        CourseController().delete(id=id)
        return None, 204

@nsc.route('/students/<id>')
@nsc.doc(params={'id': 'Id do curso'})
class CoursesWithStudentsRelationsAPIByID(Resource):
    
    @nss.marshal_list_with(cm.with_relations)
    def get(self, id):
        return CourseController().get(id)
    
@nsc.route('/relations')
class CoursesWithStudentsRelationsAPI(Resource):
    
    @nss.marshal_list_with(cm.with_relations)
    def get(self):
        return CourseController().list()


@nss.route('/')
class StudentsAPI(Resource):
    
    @nss.marshal_list_with(sm.item)
    def get(self):
        return StudentController().list()
    
    @nss.expect(sm.new)
    @nss.marshal_list_with(sm.item)
    def post(self):
        name, course_id = itemgetter('name', 'course_id')(nss.payload)
        student = StudentController().add(name, course_id)
        return student, 201
    
    @nss.expect(sm.put)
    @nss.marshal_list_with(sm.with_relations)
    @nss.response(400, 'Parametros incorretos')
    def put(self):
        id, name, course_id = itemgetter('id', 'name', 'course_id')(nss.payload)
        student = StudentController()
        
        try:
            data = student.update(id, name, course_id)
            return data, 200
        except Exception as e:
            return abort(400, str(e))
    

@nss.route('/relations')
class StudentsRelationsAPI(Resource):
    
    @nss.marshal_list_with(sm.with_relations)
    def get(self):
        return StudentController().list()


@nss.route('/<id>')
class StudentsByCoursesAPI(Resource):
    
    @nss.marshal_list_with(sm.item)
    @nss.doc(params={ 'id': 'Id do estudante'})
    def get(self, id: int):
        return StudentController().get(id)
    
    def delete(self, id: int):
        StudentController().delete(id=id)
        return None, 204
