from flask import Flask

def create_app():
    app=Flask(__name__)
    from myapps.student_info.views import mod as student_module
    # from myapps.faculty_infi.views import mod as faculty_module

    app.register_blueprint(student_module)
    # app.register_blueprint(faculty_module)
    return app