from dataclasses import dataclass, field

from views.employees.schemas import Employee, EmployeeCreate


@dataclass
class EmployeeStorage:
    last_id: int = 0
    employees: dict[int, Employee] = field(default_factory=dict)
    @property
    def next_id(self):
        return self.last_id + 1
    def employees_create(self, employee_in: EmployeeCreate) -> Employee:
        new_employee = Employee(id = self.next_id, **employee_in.model_dump())
        self.last_id = new_employee.idgi
        self.employees[new_employee.id] = new_employee
        return new_employee
    def full_employee_get(self):
        return self.employees.copy()
    def id_employee_get(self, id: int):
        return self.employees.get(id)
    def id_employee_delete(self, id: int):
        return self.employees.pop(id)

storage1 = EmployeeStorage()




