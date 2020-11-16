"""
Routes and views for the flask application.
"""
from flask import render_template, request
from FlaskWebProject4 import app
from FlaskWebProject4.ModelBuilders.UsersMB import UsersMB
from FlaskWebProject4.ModelBuilders.TasksMB import TasksMB
from FlaskWebProject4.ModelBuilders.CandidatesMB import CandidatesMB
from FlaskWebProject4.ModelBuilders.InterviewsMB import InterviewsMB
from FlaskWebProject4.DAO.SubmitEntry import submitEntry
from FlaskWebProject4.DAO.SubmitPlacedCandidate import submitPlacedCandidate
from FlaskWebProject4.DAO.SubmitHiringCandidate import submitHiringCandidate
from FlaskWebProject4.DAO.SubmitInterviewCandidate import submitInterviewCandidate
from FlaskWebProject4.DAO.GetCandidates import deleteHiringCandidate

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/hiring', methods=['GET'])
def hiring():
    return render_template('hiring.html', candidates=CandidatesMB().getHiringCandidatesModel())

@app.route('/marketing', methods=['GET'])
def marketing():
    return render_template('marketing.html', users=UsersMB().getUsersModel())

@app.route('/onboarding1', methods=['GET'])
def onboarding():
    return render_template('onboarding.html')

@app.route('/task', methods=['GET'])
def task():
    user_id = request.args.get('userid')
    return render_template('task.html', tasks=TasksMB().getTasksModel(user_id))

@app.route('/hiringDelete', methods=['GET'])
def hiringDelete():
    cid = request.args.get('candidate_id')
    deleteHiringCandidate(cid)
    return "success"

@app.route('/candidate', methods=['GET'])
def candidate():
    return render_template('placedCandidates.html', candidates=CandidatesMB().getPlacedCandidatesModel())

@app.route('/interview', methods=['GET'])
def interview():
    return render_template('interviewCandidates.html', interviews=InterviewsMB().getInterviewCandidatesModel())

@app.route('/submitEntry', methods=['POST'])
def Entry():
    submitEntry(task_id = request.form['task_id'],
                name =  request.form['name'],
                task = request.form['task'],
                details = request.form['task'],
                technology = request.form['technology'],
                source = request.form['source'],
                link = request.form['link'],
                time = request.form['time'],
                notes = request.form['notes'])
    return "success"

@app.route('/submitPlacedCandidate', methods=['GET'])
def Placed():
    submitPlacedCandidate(Firstname = request.args.get('Firstname'),
                Lastname = request.args.get('Lastname'),
                EmailID = request.args.get('EmailID'),
                Contact_Number = request.args.get('Contact_Number'),
                Visa_Status = request.args.get('Visa_Status'),
                College_Name1 = request.args.get('College_Name1'),
                College_Name2 = request.args.get('College_Name2'),
                Technology = request.args.get('Technology'),
                StartDate = request.args.get('StartDate'),
                EndDate = request.args.get('EndDate'),
                Vendor_Name = request.args.get('Vendor_Name'),
                Client_Name = request.args.get('Client_Name'),
                Job_Location = request.args.get('Job_Location'),
                dollarRate_per_hour = request.args.get('dollarRate_per_hour'))
    return render_template('placedCandidates.html', candidates=CandidatesMB().getPlacedCandidatesModel())

@app.route('/submitHiringCandidate', methods=['GET'])
def Hiring():
    submitHiringCandidate(Firstname =  request.args.get('Firstname'),
                Lastname = request.args.get('Lastname'),
                EmailID = request.args.get('EmailID'),
                Contact_Number = request.args.get('Contact_Number'),
                Visa_Status = request.args.get('Visa_Status'),
                College_Name1 = request.args.get('College_Name1'),
                College_Name2 = request.args.get('College_Name2'),
                reference = request.args.get('reference'))
    return render_template('hiring.html', candidates=CandidatesMB().getHiringCandidatesModel())

@app.route('/submitInterviewCandidate', methods=['GET'])
def InterviewCandidates():
    submitInterviewCandidate(Firstname =  request.args.get('Firstname'),
                Lastname = request.args.get('Lastname'),
                Consultant_Name = request.args.get('Consultant_name'),
                Date = request.args.get('Date'),
                Vendor_Name = request.args.get('Vendor_Name'),
                Technology = request.args.get('Technology'),
                Client_Name = request.args.get('Client_Name'),
                Marketed_by = request.args.get('Marketed_by'),
                Interviewer_Names = request.args.get('Interviewer_Names'),
                Feedback = request.args.get('Feedback'),
                State = request.args.get('State'))
    return render_template('interviewCandidates.html', interviews=InterviewsMB().getInterviewCanidatesModel())