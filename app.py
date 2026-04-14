from flask import Flask, render_template, request
from model import recommend_career
from db import init_db, save_result

app = Flask(__name__)

# initialize database
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    skills_input = request.form.get("skills")

    if not skills_input:
        return "Please enter skills!"

    skills = skills_input.split(",")

    career = recommend_career(skills)

    # save result to database
    save_result(skills, career)

    return render_template("result.html", career=career)

if __name__ == "__main__":
    app.run(debug=True)
