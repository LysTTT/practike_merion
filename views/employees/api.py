from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from employees.crud import EmployeeStorage
from views.employees.crud import storage1
from views.employees.schemas import Employee, EmployeeCreate

router = APIRouter(prefix="/employees")

@router.get("", response_model=list[Employee])
def view_full():
    return list(storage1.full_employee_get().values())

@router.get("/{id}", response_model=Employee)
def view_one(id: int):
    user = storage1.employees.get(id)
    if user:
        return user
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"User {id} not found")

@router.post("/add", response_model=Employee)
def view_create(employee: EmployeeCreate):
    return storage1.employees_create(employee)
@router.delete("/{id}", response_model=Employee)
def delete_view(id: int):
    user = storage1.employees.get(id)
    if user:
        storage1.id_employee_delete(id)
        raise HTTPException(status_code=HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f"User {id} not found")
