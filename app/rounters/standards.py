from typing import Optional, List
from fastapi import APIRouter, Query
from app.schemas import StandardCreate, StandardUpdate, StandardOut
from app.services.standard_service import (
    create_standard,
    list_standards,
    get_standard,
    update_standard,
)

router = APIRouter(prefix="/standards", tags=["standards"])


@router.post("", response_model=StandardOut, status_code=201)
def create_standard_route(payload: StandardCreate):
    return create_standard(payload.model_dump(exclude_none=True))


@router.get("", response_model=List[StandardOut])
def list_standards_route(
    name: Optional[str] = Query(default=None),
    organization: Optional[str] = Query(default=None),
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0),
):
    return list_standards(name, organization, limit, offset)


@router.get("/{standard_id}", response_model=StandardOut)
def get_standard_route(standard_id: int):
    return get_standard(standard_id)


@router.put("/{standard_id}", response_model=StandardOut)
def update_standard_route(standard_id: int, payload: StandardUpdate):
    return update_standard(standard_id, payload.model_dump(exclude_none=True))
