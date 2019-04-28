from Question import Question
import csv
import random
import os.path
from os import path
import sys
import pdftables_api
import re


# Checking file exist in csv folder
def checkFileExistcsv(a):
    return path.exists("E:/4-1/Final Project/csv/" + a + ".csv")


# Checking file exist in pdf folder
def checkFileExistpdf(b):
    return path.exists("E:/4-1/Final Project/pdf/" + b + ".pdf")


# Pdf to csv converter
def pdfToExcel(d):
    c = pdftables_api.Client('wa9l2jbtqv2t')
    c.csv('"E:/4-1/Final Project/pdf/"+ d + ".pdf"',
          '"E:/4-1/Final Project/csv/"+ d + ".csv"')


# Email Validation using Regular Expression
def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


# Taking inputs from the user
def email_verifi():
    email_address = input("Enter a valid Email_ID [email@domain.com]:")
    if (valid_email(email_address)):
        state="EMAIL VERIFIED!"
        return state
    else:
        print("Invalid Email!")
        email_verifi()

def getQuestions(file,level):
    print(level)
    question_1 = []
    with open('E:/4-1/Final Project/csv/' + file + '.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            for d in level:
                if (d in row[1]):
                    question_1.append(row[1])
    return question_1

def getAnswer(file,level):
    answer_1 = []
    with open('E:/4-1/Final Project/csv/' + file + '.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            for d in level:
                if (d in row[1]):
                    answer_1.append(row[2])
    return answer_1



# generating questions (Adaptive Model)
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n\n")
        print("\n")
        if (answer == question.answer):
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    return score


KNOWLEDGE = ["Write", "List", "Label", "Name", "State", "Define", "Count", "Describe", "Draw", "Find", "Identify",
             "Match",
             "Quote", "Recall", "Recite", "Sequence", "Tell", "Arrange", "Duplicate", "Memorize", "Order", "Outline",
             "Recognize", "Relate", "Repeat", "Reproduce", "Select", "Choose", "Copy", "How", "Listen", "Locate",
             "Memorise", "Observe", "Omit", "Read", "Recognise", "Record", "Remember", "Retell", "Show", "Spell",
             "Trace", "What", "When", "Where", "Which", "Who", "Why"
             ]

COMPREHENSION = ["Explain", "Summarize", "Paraphrase", "Describe", "Illustrate", "Conclude", "Demonstrate", "Discuss",
                 "Generalize", "Identify", "Interpret", "Predict", "Report", "Restate", "Review", "Tell", "Classify",
                 "Convert", "Defend", "Distinguish", "Estimate", "Express", "Extend", "Give example", "Indicate",
                 "Infer", "Locate", "Recognize", "Rewrite", "Select", "Translate", "Ask", "Cite", "Compare",
                 "Contrast", "Generalise", "Give examples", "Match", "Observe", "Outline", "Purpose", "Relate",
                 "Rephrase", "Show", "Summarise"
                 ]

APPLICATION = [
    "Use", "Compute", "Solve", "Demonstrate", "Apply", "Construct", "Change", "Choose", "Dramatize", "Interview",
    "Prepare", "Produce", "Select", "Show", "Transfer", "Discover", "Employ", "Illustrate",
    "Interpret", "Manipulate", "Modify", "Operate", "Practice", "Predict", "Relate schedule", "Sketch",
    "Use write", "Act", "Administer", "Associate", "Build", "Calculate", "Categorise", "Classify",
    "Connect", "Correlation", "Develop", "Dramatise", "Experiment", "With", "Group", "Identify",
    "Link", "Make use of", "Model", "Organise", "Perform", "Plan", "Relate", "Represent", "Simulate",
    "Summarise", "Teach", "Translate"
]

ANALYSIS = ["Analyse", "Categorize", "Compare", "Contrast", "Separate", "Characterize", "Classify", "Debate", "Deduce",
            "Diagram", "Differentiate", "Discriminate", "Distinguish", "Examine", "Outline", "Relate", "Research",
            "Appraise", "Breakdown", "Calculate", "Criticize", "Derive", "Experiment", "Identify", "Illustrate",
            "Infer", "Interpret", "Model", "Outline", "Point out", "Question", "Select", "Subdivide", "Test",
            "Arrange", "Assumption", "Categorise", "Cause and", "Effect", "Choose", "Difference", "Discover",
            "Dissect", "Distinction", "Divide", "Establish", "Find", "Focus", "Function", "Group", "Highlight",
            "In-depth", "Discussion", "Inference", "Inspect", "Investigate", "Isolate", "List", "Motive", "Omit",
            "Order", "Organise", "Point out", "Prioritize", "Rank", "Reason", "Relationships", "Reorganise", "See",
            "Similar to", "Simplify", "Survey", "Take part in", "Test for", "Theme", "Comparing"
            ]

SYNTHESIS = ["Create", "Design", "Hypothesize", "Invent", "Develop", "Compose", "Construct", "Integrate", "Make",
             "Organize", "Perform", "Plan", "Produce", "Propose", "Rewrite", "Arrange", "Assemble", "Categorize",
             "Collect", "Combine", "Comply", "Devise", "Explain", "Formulate", "Generate", "Prepare", "Rearrange",
             "Reconstruct", "Relate", "Reorganize", "Revise", "Set up", "Summarize", "Synthesize", "Tell", "Write",
             "Adapt", "Add to", "Build", "Change", "Choose", "Combine", "Compile", "Convert", "Delete", "Discover",
             "Discuss", "Elaborate", "Estimate", "Experiment", "Extend", "Happen", "Hypothesise", "Imagine",
             "Improve", "Innovate", "Make up", "Maximise", "Minimise", "Model", "Modify", "Original", "Originate",
             "Predict", "Reframe", "Simplify", "Solve", "Speculate", "Substitute", "Suppose", "Tabulate", "Test",
             "Theorise", "Think", "Transform", "Visualise"
             ]

EVALUATION = ["Judge", "Recommend", "Critique", "Justify", "Appraise", "Argue", "Assess", "Choose", "Conclude",
              "Decide", "Evaluate", "Predict", "Prioritize", "Prove", "Rank", "Rate", "Select", "Attach", "Compare",
              "Contrast", "Defend", "Describe", "Discriminate", "Estimate", "Explain", "Interpret", "Relate",
              "Summarize", "Support", "Value", "Agree", "Award", "Bad", "Consider", "Convince", "Criteria",
              "Criticise", "Debate", "Deduct", "Determine", "Disprove", "Dispute", "Effective", "Give reasons", "Good",
              "Grade", "How do we", "Know", "Importance", "Infer", "Influence", "Mark", "Measure", "Opinion",
              "Perceive", "Persuade", "Prioritise", "Rule on", "Test", "Useful", "Validate", "Why"
              ]


state = email_verifi()
print(state)

fileName = input("Enter Subject Name:")
f = checkFileExistcsv(fileName)
if (not f):
    file = checkFileExistpdf(fileName)
    if (file):
        pdfToExcel(fileName)
    else:
        print("We are sorry we have sent your request to our technical team. Thank You for being with us we will let you know by email.")

#print(fileName)
levelOfBlooms = 0
finalScore = 0
while(levelOfBlooms<6):
    blooms=['KNOWLEDGE','COMPREHENSION','APPLICATION','ANALYSIS','SYNTHESIS','EVALUATION']
    question_prompt = getQuestions(fileName,blooms[levelOfBlooms])
    answer_prompt = getAnswer(fileName,blooms[levelOfBlooms])
    countOfQuestions = len(question_prompt)
    Number = 0
    answer1 = []
    questions = []
    while (Number < 3):
        i = 0
        randomNumber = random.randint(1, countOfQuestions - 20)
        questions.append(question_prompt[randomNumber])
        answer1.append(answer_prompt[randomNumber])
        Number = Number + 1
    question_prompt = questions
    answer_prompt = answer1
    questions = [
        Question(question_prompt[0], answer_prompt[0]),
        Question(question_prompt[1], answer_prompt[1]),
        Question(question_prompt[2], answer_prompt[2])

    ]
    totalScore = run_test(questions)
    levelOfBlooms += 1
    finalScore += totalScore


print("Congrats You Got " + str(finalScore))



# print(countOfQuestions)
#question_prompt = question_1
#answer_prompt = answer_1
#countOfQuestions = len(question_prompt)
#Number = 0
#answer1 = []
#questions = []






