from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import PlainTextResponse
from pydantic import ValidationError

from adapter.api.controllers.product_controller import ProductController
from adapter.api.controllers.category_controller import CategoryController

from core.application.use_cases.product.product_case import ProductCase
from core.application.use_cases.category.category_case import CategoryCase



from scripts.populate_database import populate


app = FastAPI(title="Tasty Delivery")


@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)

# Products
products_controller = ProductController(ProductCase)

# Categories
category_controller = CategoryController(CategoryCase)

app.include_router(products_controller.router)
app.include_router(category_controller.router)



@app.on_event("startup")
async def populate_database():
    populate()
