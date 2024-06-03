from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Function Excecuted!")
    return 'Hello World!'

@app.route('/abs_disp')
def abs_disp():
    abs_set = ['Crunches', 'Situps', 'Planks', 'Raisers', 'Russian_twists', 'Side-planks']
    return render_template('html-test.html',name='Benjamin', list_name=abs_set)
    #return render_template('html2.html')
#app.run(debug=True)
