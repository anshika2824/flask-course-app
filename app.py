from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        type = request.form['ID']
        id = request.form['id_value']
        
        if id == "":
            return render_template('error.html')
        
        id = int(id)
        data = []
        
        with open('data.csv', 'r') as file:
            file.readline()
            if type == "student_id":
                for row in file:
                    row = list(map(int, row.strip().split(',')))
                    if row[0] == id:
                        data.append(row)
            elif type == "course_id":
                for row in file:
                    row = list(map(int, row.strip().split(',')))
                    if row[1] == id:
                        data.append(row)

        if len(data) == 0:
            return render_template('error.html')   

        if type == 'student_id':
            total_marks = sum([x[2] for x in data])
            return render_template('student.html', total_marks=total_marks, data=data)
        else:
            marks = [x[2] for x in data if x[1] == id]
            a = sum(marks) / len(marks)
            m = max(marks)
            plt.figure()  
            plt.hist(marks)
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            plt.savefig('static/plot.png') 
            plt.close()  
            return render_template('course.html', average_marks=a, maximum_marks=m, img='static/plot.png')

app.run()