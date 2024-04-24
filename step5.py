class Employee:
    def __init__(self, emp_id):
        print("Employee::__init__()")
        self.emp_id = emp_id

    def get_paid(self, hours):
        print("Employee::get_paid()")


class Manager(Employee):
    PAID = 1800

    def __init__(self, emp_id):
        print("Manager::__init__")
        super().__init__(emp_id)

    def get_paid(self, hours):
        print("Manager::get_paid")
        return self.PAID * hours


class Worker(Employee):
    PAID = 2200

    def __init__(self, emp_id):
        print("Worker::__init__")
        super().__init__(emp_id)

    def get_paid(self, hours):
        print("Worker::get_paid")
        return self.PAID * hours


manager = Manager("1")
worker = Worker("2")

print(f"Зарплата менеджера: {manager.get_paid(120)}")
print(f"Зарплата работника: {worker.get_paid(120)}")
