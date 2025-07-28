from fastapi import APIRouter

router = APIRouter()


@router.get("/gadgets")
def get_gadgets():
    return [
        {"name": "Smartphone", "brand": "TechCorp"},
        {"name": "Laptop", "brand": "CompuWorld"},
    ]
