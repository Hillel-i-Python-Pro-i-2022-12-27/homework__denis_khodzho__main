from task_is.task_1 import fist_task_file_reader, third_task_what, second_task_users_generator, last_task_reader

file = "tasks/files/people_data(extended).csv"
len_users = 100

def start():
    fist_task_file_reader(file)
    second_task_users_generator(len_users)
    third_task_what()
    last_task_reader(file)

if __name__ == "__main__":
    start()
