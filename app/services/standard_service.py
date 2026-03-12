from fastapi import HTTPException
from app.db import supabase


def create_standard(data: dict):
    response = supabase.table("standard").insert(data).execute()
    if not response.data:
        raise HTTPException(status_code=500, detail="Insert failed")
    return response.data[0]


def list_standards(name=None, organization=None, limit=100, offset=0):
    query = supabase.table("standard").select("*")

    if name:
        query = query.eq("name", name)

    if organization:
        query = query.eq("organization", organization)

    response = query.range(offset, offset + limit - 1).execute()
    return response.data or []


def get_standard(standard_id: int):
    response = (
        supabase.table("standard")
        .select("*")
        .eq("id", standard_id)
        .limit(1)
        .execute()
    )
    if not response.data:
        raise HTTPException(status_code=404, detail="Standard not found")
    return response.data[0]


def update_standard(standard_id: int, data: dict):
    if not data:
        raise HTTPException(status_code=400, detail="No fields to update")

    response = (
        supabase.table("standard")
        .update(data)
        .eq("id", standard_id)
        .execute()
    )
    if not response.data:
        raise HTTPException(status_code=404, detail="Standard not found")
    return response.data[0]
