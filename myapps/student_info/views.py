from flask import Blueprint,jsonify

mod=Blueprint('student_info',__name__,url_prefix='/student')

@mod.route('/',methods=['GET'])
def getall():
    return "List of students"

@mod.route('/<student_id>',methods=['GET'])
def Show(student_id):
    print('student_id:',student_id)
    response={
        'Student_id':student_id
    }
    return jsonify(response)
