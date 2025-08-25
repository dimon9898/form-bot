from fastapi.routing import APIRouter
import database.requests as rq
from fastapp.schema import SubsSchema

api_router = APIRouter()

@api_router.get('/subscriptions', response_model=list[SubsSchema])
async def get_subscriptions():
    subs = await rq.get_subscriptions()
    return subs

@api_router.get('/subscription/id/{sub_id}', response_model=SubsSchema)
async def get_subs(sub_id: int):
    result = await rq.get_subscription(sub_id)
    return result