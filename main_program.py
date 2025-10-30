import random
import ipywidgets as widgets
from IPython.display import display, clear_output

# Quiz Questions (Randomized)
quiz = [
    {"question": "Which language is primarily used for web development?",
     "options": ["Python", "HTML", "C++", "Java"], "answer": "HTML"},

    {"question": "What is 15 + 27?",
     "options": ["42", "40", "43", "41"], "answer": "42"},

    {"question": "Which library is used for data visualization in Python?",
     "options": ["NumPy", "Matplotlib", "Pandas", "Scikit-learn"], "answer": "Matplotlib"},

    {"question": "Which one is a Python data type?",
     "options": ["Integer", "Boolean", "String", "All of the above"], "answer": "All of the above"},

    {"question": "Which of the following is used to create plots in Python?",
     "options": ["Matplotlib", "NumPy", "Pandas", "TensorFlow"], "answer": "Matplotlib"},

    {"question": "Which keyword is used to define a function in Python?",
     "options": ["func", "def", "function", "define"], "answer": "def"},

    {"question": "Which of these is mutable in Python?",
     "options": ["List", "Tuple", "String", "Integer"], "answer": "List"},

    {"question": "Which symbol is used for comments in Python?",
     "options": ["//", "#", "/* */", "<!-- -->"], "answer": "#"},

    {"question": "Which operator is used for exponentiation in Python?",
     "options": ["^", "**", "%", "//"], "answer": "**"},

    {"question": "Which method is used to add an element to a list?",
     "options": ["add()", "append()", "insert()", "extend()"], "answer": "append()"},

    {"question": "Which keyword is used for conditional statements in Python?",
     "options": ["if", "for", "while", "def"], "answer": "if"},

    {"question": "What does 'len()' function do in Python?",
     "options": ["Calculates length", "Adds elements", "Removes elements", "None of these"],
     "answer": "Calculates length"},
]


random.shuffle(quiz)

# Initialize variables
score = 0
question_index = 0


def start_quiz():
    """Display start screen"""
    clear_output()
    title = widgets.HTML("<h1 style='color:teal;text-align:center;'>🧠 Python Interactive Quiz</h1>")
    subtitle = widgets.HTML("<h3 style='text-align:center;'>Test your Python knowledge!</h3>")
    start_btn = widgets.Button(description="Start Quiz", button_style='success', icon='play')
    start_btn.style.button_color = 'green'
    display(title, subtitle, start_btn)

    def on_start(b):
        show_question(0)

    start_btn.on_click(on_start)

def show_question(index):
  
    global score, question_index
    clear_output(wait=True)

    question = quiz[index]

    # Progress Bar
    progress = widgets.FloatProgress(
        value=(index / len(quiz)),
        min=0,
        max=1,
        description=f"Q{index+1}/{len(quiz)}",
        bar_style='info',
        orientation='horizontal'
    )

    # Question Display
    question_html = widgets.HTML(
        f"<h3 style='color:#333;'>{question['question']}</h3>"
    )

    # Option Buttons
    options_widget = widgets.RadioButtons(
        options=question['options'],
        description='',
        style={'description_width': 'initial'}
    )

    submit_button = widgets.Button(description="Submit", button_style='success', icon='check')
    feedback = widgets.Output()

    def on_submit(b):
        nonlocal index
        with feedback:
            clear_output()
            if options_widget.value == question['answer']:
                global score
                score += 1
                display(widgets.HTML("<p style='color:green;font-weight:bold;'>✅ Correct!</p>"))
            else:
                display(widgets.HTML(
                    f"<p style='color:red;font-weight:bold;'>❌ Wrong! Correct Answer: {question['answer']}</p>"
                ))

        index += 1
        if index < len(quiz):
            # Delay before next question
            from time import sleep
            sleep(1)
            show_question(index)
        else:
            show_result()

    submit_button.on_click(on_submit)

    display(progress, question_html, options_widget, submit_button, feedback)

def show_result():
    """Display the final result"""
    clear_output(wait=True)
    percentage = (score / len(quiz)) * 100

    if percentage >= 80:
        remark = "🌟 Excellent work!"
        color = "green"
    elif percentage >= 50:
        remark = "👍 Good effort!"
        color = "orange"
    else:
        remark = "📘 Keep practicing!"
        color = "red"

    result_html = widgets.HTML(
        f"""
        <h2 style='color:teal;'>🎉 Quiz Completed!</h2>
        <h3>Your Score: {score}/{len(quiz)} ({percentage:.1f}%)</h3>
        <p style='color:{color};font-weight:bold;'>{remark}</p>
        """
    )

    restart_button = widgets.Button(description="Restart Quiz", button_style='info', icon='refresh')

    def on_restart(b):
        global score, question_index
        score = 0
        question_index = 0
        random.shuffle(quiz)
        start_quiz()

    restart_button.on_click(on_restart)
    display(result_html, restart_button)

start_quiz()
