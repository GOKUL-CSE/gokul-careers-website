from re import DEBUG, template
from flask import Flask, render_template
app = Flask(__name__)
JOBS = [
    {
        'id' : 1,
        'role' : "Data Analyst",
        'salary' : "Rs. 10,00,000"
    },
    {
        'id' : 2,
        'role' : "Data Scientist",
        'salary' : "Rs. 20,00,000"
    },
    {
        'id' : 3,
        'role' : "Machine Learning Engineer",
        'salary': "Rs. 15,00,000"
    },
    {
        'id' : 4,
        'role' : "Data Engineer",
        'salary' : "Rs. 10,00,000"
    }

    
]




@app.route('/')
def hello_world():
    return render_template('home.html',jobs = JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug  = True)