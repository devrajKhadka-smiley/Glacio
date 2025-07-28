from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/gadgets")
def get_gadgets():
    return [
        {"name": "Smartphone", "brand": "TechCorp"},
        {"name": "Laptop", "brand": "CompuWorld"},
    ]


@router.get("/gadgets/{gadget_id}")
def get_gadget(gadget_id: int):

    gadgets = [
        {"id": 1, "name": "Smartphone", "brand": "TechCorp"},
        {"id": 2, "name": "Laptop", "brand": "CompuWorld"},
        {"id": 3, "name": "Tablet", "brand": "TabletTech"},
        {"id": 4, "name": "Smartwatch", "brand": "WatchWorks"},
    ]
    
    # Find the gadget with the matching ID
    for gadget in gadgets:
        if gadget["id"] == gadget_id:
            return gadget
    
    # If gadget not found, raise 404 error
    raise HTTPException(status_code=404, detail="Gadget not found")
