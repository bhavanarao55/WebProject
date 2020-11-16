from FlaskWebProject4.Models.Interview import Interview

class Interviews:
    def __init__(self):
        self.interview_list = list()

    def add_interview(self,interview):
        self.interview_list.append(interview)