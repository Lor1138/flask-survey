from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES_KEY= "responses"

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = '<supercalifragelisticexpealidocious'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


debug = DebugToolbarExtension(app)



@app.route("/")
def start_survey_page():
    """survey landing page"""

    return render_template("main.html", survey=survey)


@app.route('/start', methods=['POST'])
def survey_start():
    """first survey  question"""

    session[RESPONSES_KEY] = []

    return redirect("question/0")

@app.route("/answer", methods=["POST"])
def handle_question():
    choice = request.form['answer']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if(len(responses) == len(survey.questions)):
        return redirect("/completion")

    else:
        return redirect(f"/question/{len(responses)}")


@app.route("/question/<int:question_id>")
def question_page(question_id):
    responses = session.get(RESPONSES_KEY)

    if (responses is None):
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        return redirect("/completion")

    if (len(responses) != question_id):
        flash(f"Invalid question ID: {question_id}. Please answer in the correct order")
        return redirect(f"/question/{len(responses)}")

    question = survey.questions[question_id]
    return render_template("question.html", question_num=question_id, question=question)



@app.route("/completion")
def survey_complete():
    
    return render_template("/completion.html")

if __name__ == '__main__':
    app.run(debug=True)