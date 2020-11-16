class Task:
  def __init__(self, task_id, user_id, candidate_id, name, task, details, technology, source, link, time, notes):
    self.task_id = task_id
    self.user_id = user_id
    self.candidate_id = candidate_id
    self.name = name
    self.task = task
    self.details = details
    self.technology = technology
    self.source = source
    self.link = link
    self.time = time
    self.notes = notes