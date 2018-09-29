class Tasks:
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
        pass

    def delete_task(self, task):
        """
        Removes the specified task from the todo list.

        Args:
            task(str): The task to be removed

        Returns: 
            tuple: With two elements, a message and a bool. 
            ('success', True), ('Failure', False)
        """
        pass

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
        pass

    def delete_all_tasks(self):
        """
        Deletes all tasks from the todo list
        """
        pass

    def display_todo_list(self):
        """
        Prints all tasks in the todo list
        """
        pass

    def is_list_empty(self):
        """
        Checks if the todo list is empty

        Returns:
            bool: True for success, False otherwise
        """
        pass

    def is_task_in_the_list(self, task_position):
        """
        Checks if the selected task in the todo list

        Args:
            task_position(int): The position of the task in the todo list

        Returns:
            bool: True for success, False otherwise
        """

        pass
