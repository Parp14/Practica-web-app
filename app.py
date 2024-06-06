from flask import Flask, render_template

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India"
        "sa": "Rs. 10,00,000" "
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location":
    },
    {
        "id": 3,
        "title": "Frontend Developer",
        "location": "San Francisco, USA"
    },
    {
        "id": 4,
        "title": "Backend Developer",
        "location": "Remote"
    }
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBSHH)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)