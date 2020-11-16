from FlaskWebProject4.DAO.GetTasks import getTasks
from FlaskWebProject4.ViewModels.Tasks import Tasks
from FlaskWebProject4.Models.Task import Task

class TasksMB(object):
    """description of class"""
    def getTasksModel(self,user_id):
        tasks = Tasks()
        result = getTasks(user_id)
        for row in result:
            tasks.add_task(Task(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        return tasks