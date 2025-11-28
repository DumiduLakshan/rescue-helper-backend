from fastapi import APIRouter,Request,Depends
import logging
from app.utils.supabase_client import get_supabase

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/create",summary="use for create new rescue post")
def create_rescue_post(request:Request,db=Depends(get_supabase)):
  logger.info(f"Access /create endpoint - {request.client}")
  print(type(db))