from fastapi import APIRouter

router = APIRouter()


@router.get("/books")
def get_books():
    return [
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    ]
