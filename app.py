from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as surveys

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = '<supercalifragelisticexpealidocious'

debug = DebugToolbarExtension(app)



@app.route("/")
def start_survey_page():
    """survey landing page"""

    return render_template("main.html", survey=surveys)


@app.route('/start', methods=['POST'])
def survey_start():
    """first survey  question"""

    return redirect("question/0")

@app.route("/question/<int:question_id>")
def question_page():
    
    return render_template("question.html")