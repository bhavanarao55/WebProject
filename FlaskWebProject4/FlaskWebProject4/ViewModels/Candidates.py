from FlaskWebProject4.Models.Candidate import Candidate

class Candidates:
    def __init__(self):
        self.candidate_list = list()

    def add_candidate(self,candidate):
        self.candidate_list.append(candidate)