
import todoist_api_python
import todoist_api_python.api
from config import Config

class TDHandler:

    def __init__(self, c: Config) -> None:
        self.api = todoist_api_python.api.TodoistAPI(c.todoist_api_key)

    def get_projects(self) -> str:
        # TODO: Finish this
        result = []
        try:
            projects = self.api.get_projects()
        except Exception as error:
            print(error)
        for p in projects:
            text =  f'''
            Name: {p.name}, Id: {p.id}
            '''
            result.append(text)
        
        return "\n".join(result)
    
    def get_tasks(self) -> str :
        result = []
        try:
            tasks = self.api.get_tasks()
        except Exception as error:
            print(error)
        for t in tasks:
            text =  f'''
Name: {t.content}, 
Order: {t.order}, Parent: {t.parent_id}, 
Priority: {t.priority}, Project: ${t.project_id}, 
URL: ${t.url}'''
            if t.due:
                text += f'''
DueDate: {t.due.date}, Recurs: {t.due.is_recurring} {t.due.string}'''
            if t.comment_count != 0:
                comments = self.api.get_comments(task_id=t.id)
                for c in comments:
                    text += f'''
Comment:
Date:{c.posted_at}, ID:  {c.task_id} 
"{c.content}"'
                            '''
            result.append(text)
        
        return '\n'.join(result)
                
    def get_report(self) -> str:

        projects =  self.get_projects()
        tasks = self.get_tasks()

        return f'''
            Projects:
            {projects}
            Tasks:
            {tasks}
        '''