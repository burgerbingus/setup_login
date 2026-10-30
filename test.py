from database import Database

db = Database()

def test_database():
    print("Testing database")

    tasks = db.get_tasks()

    print(tasks)

def test_add_task():
    db.add_task("Finish homework")

    print("Added task")

if __name__ == "__main__":
    test_database()
    test_add_task()
