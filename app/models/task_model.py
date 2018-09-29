class Task:
    todo_list = []

    def create_task(self, task):
        """
        Adds a task to the todo list.

        Args: 
            task(str): The task to be created

        Returns: 
            tuple: With two elements, amessage and a bool. 
            ('success', True), ('Failure', False)
        """

        #  Check if task already exists
        if task in self.todo_list:
            return "Task already exists", False

        #  Create a new task
        self.todo_list.append(task)
        return "Task has been created successfully", True

    def delete_task(self, task):
        """
        Removes the specified task from the todo list.

        Args:
            task(str): The task to be removed

        Returns: 
            tuple: With two elements, a message and a bool. 
            ('success', True), ('Failure', False)
        """

        #  Check if the todo list is empty
        if len(self.todo_list) == 0:
            return "There are no items in your todo list", False

        #  Check if the selected task exists
        if task not in self.todo_list:
            return "Selected task does not exist", False

        #  Remove the selected task
        self.todo_list.remove(task)
        return "Selected task has been deleted successfully", True

    def mark_as_finished(self, task):
        """
        Appends a label '[finished]' at the end of the task to 
        indicate that the task has been finished.

        Args:
            task(str): The task to be labelled

        Returns: 
            tuple: With two elements, a message and a bool. 
            ('success', True), ('Failure', False)
        """

        #  Check if the selected task is already marked as finished
        if "finished" in task:
            return "The selected task has already been finished", False

        task_position = self.todo_list.index(task)
        self.todo_list[task_position] = task + " [finished]"
        return "Task has been marked successfully", True

    def delete_all_tasks(self):
        """
        Deletes all tasks from the todo list
        """

        self.todo_list.clear()

    def display_todo_list(self):
        """
        Prints all tasks in the todo list
        """

        print("\n----------------------------------------")
        print("Your Tasks")
        print("----------------------------------------")
        for i, item in enumerate(self.todo_list):
            print("{}. {}".format(i+1, item))
        print("----------------------------------------")

    def is_list_empty(self):
        """
        Checks if the todo list is empty

        Returns:
            bool: True for success, False otherwise
        """
        if len(self.todo_list) == 0:
            return True
        return False

    def is_task_in_the_list(self, task_position):
        """
        Checks if the selected task in the todo list

        Args:
            task_position(int): The position of the task in the todo list

        Returns:
            bool: True for success, False otherwise
        """

        items = [i for i, item in enumerate(self.todo_list)]
        if task_position not in items:
            return False
        return True
