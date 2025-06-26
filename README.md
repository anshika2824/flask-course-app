# Flask Course App

A simple Flask web application that takes either a **Student ID** or **Course ID** as input and performs the following:

- For **Student ID**:
  - Displays all course records for the student
  - Calculates and displays the total marks

- For **Course ID**:
  - Displays all student records for the course
  - Calculates average and maximum marks
  - Plots a histogram of marks using `matplotlib`

---

## 🔧 Features

- HTML form for ID input (`index.html`)
- Error handling for invalid/missing IDs (`error.html`)
- Visualization using Matplotlib (`static/plot.png`)
- Template-based rendering (`student.html`, `course.html`)

---

## 📁 Project Structure

mad1_lab4/
├── app.py
├── data.csv
├── static/
│   └── plot.png
└── templates/
├── index.html
├── error.html
├── student.html
└── course.html


---

## 🚀 Run the App

```bash
# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install Flask
pip install flask matplotlib

# Run the app
python app.py


#Open your browser and go to:
📍 http://127.0.0.1:5000
