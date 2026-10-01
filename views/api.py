from fastapi import APIRouter
from employees.api import router as employees_router
router = APIRouter(prefix="/api")
router.include_router(employees_router)