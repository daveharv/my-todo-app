FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):   # This is the parameter
    """ Read a text file and return the list   # this is a doc string
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list to the text file."""   # This is a doc-string
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#  print(__name__)
"""
When this is called from cli.py, __name__ is 'functions'.
When this is run directly, __name__ is '__main__'.
In this way, you control when certain parts get executed.
"""
if __name__ == "__main__":
    print("Hello")
    todos = get_todos()
    print(todos)
