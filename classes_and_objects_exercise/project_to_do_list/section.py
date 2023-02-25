from project_to_do_list.task import Task


class Section:
    def __init__(self, name: str, ):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task_to_complete = [tsk for tsk in self.tasks if tsk.name == task_name][0]
        except IndexError:
            return f"Could not find task with the name {task_name}"

        task_to_complete.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):

        completed_tasks = [task for task in self.tasks if task.completed]
        amount_of_removed_tasks = len(completed_tasks)
        for el in self.tasks:
            if el in completed_tasks:
                self.tasks.remove(el)

        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        result = '\n'.join(task.details() for task in self.tasks)
        return f"Section {self.name}:" + "\n" + result


# section = Section("New section")
# task = Task("Tst", "27.04.2020")
# print(section.add_task(task))
# print(section.complete_task("Tst"))
# print(section.clean_section())
