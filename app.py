from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html'
                           )
@app.route('/submit', methods=['POST'])
def submit():
    selected_task = request.form.getlist('tasks')
    return f"You completed: {",".join(selected_task)}"
if __name__ == '__main__':
    app.run(debug=True)