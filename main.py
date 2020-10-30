from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from calculator import Calculator
from models import Base, CalculateCost, ResultCost


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get(
    '/',
    response_description='Render template',
    response_class=HTMLResponse,
)
async def index(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse('index.html', {'request': request, 'schema': Base.schema()})


@app.post(
    '/',
    description='Calculates the cost of an order',
    response_description='Calculated result cost',
    response_model=ResultCost,
)
async def calculate(request: CalculateCost) -> ResultCost:
    cost_with_discount, cost_with_tax = await Calculator(**request.dict()).calculate()
    return ResultCost(cost_with_discount=cost_with_discount, cost_with_tax=cost_with_tax)
