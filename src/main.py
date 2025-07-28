from fastapi import FastAPI
from src.api.books.routes import router as books_router
from src.api.gadgets.routes import router as gadgets_router

version = "1.0.0"

app = FastAPI(
    title="Glacio",
    description="A FastAPI application for managing and serving data efficiently.",
    version=version,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(books_router, prefix=f"/api", tags=["books"])
app.include_router(gadgets_router, prefix=f"/api", tags=["gadgets"])
