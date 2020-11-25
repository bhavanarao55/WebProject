from FlaskWebProject4.DAO.GetInterviews import getInterviews
from FlaskWebProject4.ViewModels.Interviews import Interviews
from FlaskWebProject4.Models.Interview import Interview

class InterviewsMB(object):
    """description of class"""
    def getInterviewCandidatesModel(self):
        interviews = Interviews()
        result = getInterviews()
        for row in result:
            interviews.add_interview(Interview(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        return interviews