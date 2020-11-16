from FlaskWebProject4.Models.Task import Task

class Tasks:
    def __init__(self):
        self.task_list = list()

    def add_task(self,task):
        self.task_list.append(task)