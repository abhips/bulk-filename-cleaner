import sys


class ScriptUtils(object):
    """
        Utils functions for file rename class
    """

    """
        initialization
    """

    def __init__(self):
        super().__init__()

    """
        simple function to detect if the user input is the 'exit' command or not
    """

    def check_exit_code(self, user_input):

        if user_input.lower() == 'exit':
            sys.exit(0)


    """
       function to give a formatted response to the users
    """

    def talk_to_user(self, message, start_character='', initial_space=0):
        message = start_character + ' '*initial_space + message
        print(message)

    """
        function to ask question and return the answer
    """
    def ask_question(self, question, start_character='', initial_space=0):
        print()
        question = start_character + ' '*initial_space + question
        answer = input(question)
        self.check_exit_code(answer)

        return answer

    def print_exception(self):
        pass
