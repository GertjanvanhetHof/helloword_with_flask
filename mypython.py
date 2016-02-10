from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello_world():
  return render_template('mytemplate.html', my_string='World')

if __name__ == '__main__':
  app.run()
