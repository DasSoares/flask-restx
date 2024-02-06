from . import create_app

app = create_app()

@app.route('/cursos')
def cursos():
    return ['Math', 'Biology']