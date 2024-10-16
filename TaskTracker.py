import json
import datetime

class Task:
    @property
    def todo(self):
        return "To do"
    @property
    def inProgress(self):
        return "In progress"
    @property
    def done(self):
        return "Done"
    
    def __init__(self):
        pass
        
    def CreateNewTask(self, description):
        self.id = 1
        self.description = description
        self.status = self.todo
        self.createdAt = datetime.datetime.now().strftime("%y-%m-%d, %H:%M:%S")
        self.updatedAt = datetime.datetime.now().strftime("%y-%m-%d, %H:%M:%S")
        
    def PrintTask(self):
        print(f"ID: {self.id}")
        print(f"Decripton: {self.description}")
        print(f"Status: {self.status}")
        print(f"Created at: {self.createdAt}")
        print(f"Updated at: {self.updatedAt}")
   
    def to_dict(self):
        return{
            'id':self.id,
            'description':self.description,
            'status':self.status,
            'created_at':self.createdAt,
            'updated_at':self.createdAt
            }
        
        

print("Hello python")
print("Hello python")

task1 = Task()
task1.CreateNewTask("Create github account")

task2 = Task()
task2.CreateNewTask("Post code")

task3 = Task()
task3.CreateNewTask("Finish project")

tasks = [task1,task2,task3]

tasksdict = [task.to_dict() for task in tasks]
with open('tasks.json','w') as f:
    json.dump(tasksdict, f, indent=4)



