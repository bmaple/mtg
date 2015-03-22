from flask import Flask, render_template, send_from_directory
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/AllSets-x.json')
def generate_sets_json():
    def generate():
        return send_from_directory('static', filename='AllSets-x.json')


if __name__ == '__main__':
    app.run(debug=True)



