from FlaskWebProject4.DAO.GetCandidates import getCandidates, getHiringCandidates, getPlacedCandidates
from FlaskWebProject4.ViewModels.Candidates import Candidates
from FlaskWebProject4.Models.Candidate import Candidate

class CandidatesMB(object):
    """description of class"""
    def getCandidatesModel(self):
        candidates = Candidates()
        result = getCandidates()
        for row in result:
            candidates.add_candidate(Candidate(row[0],row[1],row[2],"","","","","","","","","","","","","",""))
        return candidates

    def getHiringCandidatesModel(self):
        candidates = Candidates()
        result = getHiringCandidates()
        for row in result:
            candidates.add_candidate(Candidate(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]))
        return candidates

    def getPlacedCandidatesModel(self):
        candidates = Candidates()
        result = getPlacedCandidates()
        for row in result:
            candidates.add_candidate(Candidate(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]))
        return candidates