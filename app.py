from flask import Flask, request, render_template, redirect, flash, url_for
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
def question_page(question_id):

    """if they are trying to access the question page too soon, redirect to start page"""

    
    """If they have answered all the questions, redirect to thank you page"""

    """if they try to navigate to a new page without answering the current question, 
    flash message and redirect to correct page"""

    """
    utilize url_for somehow?
    """

    

    question = surveys.questions[question_id]
    return render_template("question.html", question_num=question_id, question=question)


if __name__ == '__main__':
    app.run(debug=True)