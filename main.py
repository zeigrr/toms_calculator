from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from calculator import Calculator
from models import Index, PriceWithDiscount, PriceWithTax, ResultCost


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get(
    '/',
    response_description='Render template',
    response_class=HTMLResponse,
)
async def index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse('index.html', {'request': request, 'schema': Index.schema()})


@app.post(
    '/with_discount',
    description='Calculates the cost of an order with discount',
    response_description='Calculated cost with discount',
    response_model=ResultCost,
)
async def calculate_with_discount(request: PriceWithDiscount) -> ResultCost:
    result_cost = await Calculator(**request.dict()).calculate_with_discount()
    return ResultCost(result_cost=result_cost)


@app.post(
    '/with_tax',
    description='Calculates the cost of an order with tax',
    response_description='Calculated cost with tax',
    response_model=ResultCost,
)
async def calculate_with_tax(request: PriceWithTax) -> ResultCost:
    result_cost = await Calculator(**request.dict()).calculate_with_tax()
    return ResultCost(result_cost=result_cost)
