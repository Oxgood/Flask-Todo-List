from flask import Flask, render_template, redirect, url_for, request
from forms import TodoForms


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETE'


lists = []


@app.route("/", methods=['POST', 'GET'])
def home():
    form = TodoForms()
    if request.method == 'POST':
        if form.validate_on_submit():
            todo_name = form.todo_name.data
            todo_date = form.todo_date.data
            todo_obj = {
                'todo_name': todo_name,
                'todo_date': todo_date
            }
            lists.append(todo_obj)
            form.todo_name.data = None
            form.todo_date.data = None
            return redirect(url_for('home'))
        todo_index = int(request.form.get('todo_index'))
        if 0 <= todo_index < len(lists):
            del lists[todo_index]
            return redirect(url_for('home'))
    return render_template('TodoList.html', form=form, lists=lists)


if __name__ == "__main__":
    app.run(debug=True)
