import json
import datetime
import os.path

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        
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
            'updated_at':self.updatedAt
            }
    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['id'], 
                   task_dict['description'], 
                   task_dict['status'],
                   task_dict['created_at'],
                   task_dict['updated_at'])
        

def generate_id(taskList):
    return len(taskList)

def generate_date():
    return datetime.datetime.now().strftime("%y-%m-%d, %H:%M:%S")
    
def get_last_index(taskList):
    return taskList[-1].id

def update_task(taskList, id, description):
    index=0
    for task in taskList:
        if task.id == id:
            print(f"Updating task \"{task.description}\" to \"{description}\".")
            task.description = description
            task.updatedAt = generate_date()
            break
        index+=1

def list_all_task(taskList, status):
    for task in taskList:
        if task.status == status or status == "All":
            print(f"ID:  {task.id}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}")
            print(f"Created at: {task.createdAt}")
            print(f"Updated at: {task.updatedAt}")
            print("************************************")
            
        
    
def delete_task(taskList, id):
     index=0
     result = False
     for task in taskList:
        if task.id == id:
            print(f"Deleting task: \"{task.description}\".")
            taskList.pop(index)
            print("Task deleted.")
            result = True
            break
        else:
            index+=1
     if result == False:
         print(f"ID {id} not found.")
         
def mark_in_progress(taskList, id):
    index=0
    for task in taskList:
        if task.id == id:
            print(f"Updating task: \"{task.description}\". Now in progress")
            task.status = "In progress"
            task.updatedAt = generate_date()
            break
        else:
            index+=1
     
def mark_done(taskList, id):
    index=0
    for task in taskList:
        if task.id == id:
            print(f"Updating task: \"{task.description}\". Now done")
            task.status = "Done"
            task.updatedAt = generate_date()
            break
        else:
            index+=1

taskList = list()

#Check if json file exists, if exists read contents
jsonPath = 'tasks.json'
fileExist = os.path.isfile(jsonPath)
if(fileExist):
    with open(jsonPath,'r') as f:
        tasks_dict = json.load(f)
        taskList = [Task.from_dict(task) for task in tasks_dict]


print("Hello python")

task1 = Task((get_last_index(taskList)+1), "New Task", "To do", generate_date(), generate_date())
#taskList.append(task1)

update_task(taskList,3,"Upload lo github")
delete_task(taskList,16)

mark_done(taskList,3)
list_all_task(taskList, "To do")

tasksdict = [task.to_dict() for task in taskList]
with open('tasks.json','w') as f:
    json.dump(tasksdict, f, indent=4)



