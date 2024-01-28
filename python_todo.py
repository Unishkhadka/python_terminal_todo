import mysql.connector as mc

conn = mc.connect(host="localhost", user="root", password="", database="python_todo")
cursor = conn.cursor()


class Todo:
    id: int
    task: str
    status: int

    def add_task(self, task):
        sql = f"INSERT into todo(task) VALUES('{task}')"
        cursor.execute(sql)
        conn.commit()

    def update_task(self, id, new_task):
        sql = f"UPDATE todo set task = '{new_task}' where id = {id}"
        cursor.execute(sql)
        conn.commit()

    def complete_task(self, id):
        sql = f"UPDATE todo set status = 1 where id = {id}"
        cursor.execute(sql)
        conn.commit()

    def delete(self, id):
        sql = f"DELETE from todo where id = {id}"
        cursor.execute(sql)
        conn.commit()

    def display(self):
        sql = "SELECT * from todo"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if len(rows) > 0:
            for row in rows:
                if row[2] == 1:
                    status = "Completed"
                elif row[2] == 0:
                    status = "Not completed"
                print(f"{row[0]} - {row[1]} - {status}")
        else:
            print("No tasks now!")


task = Todo()
print("--------------------------")
print("TASK LIST")
print("--------------------------")
task.display()
print("--------------------------")
print("Select an option.")
print("1.Add task")
print("2.Complete task")
print("3.Update task")
print("4.Delete task")
c = int(input("Choice:\t"))

if c == 1:
    task_name = input("Task:\t")
    task.add_task(task_name)
if c == 2:
    task_id = int(input("Enter id of task you want to complete:\t"))
    task.complete_task(task_id)
if c == 3:
    task_id = int(input("Enter id of task you want to update:\t"))
    new_task = input("New task:\t")
    task.update_task(task_id, new_task)
if c == 4:
    task_id = int(input("Enter id of task you want to delete:\t"))
    task.delete(task_id)
