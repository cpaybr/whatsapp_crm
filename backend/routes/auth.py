from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.supabase import supabase


router = APIRouter()


class RegisterPayload(BaseModel):
    email: str
    password: str
    name: str | None = None


class LoginPayload(BaseModel):
    email: str
    password: str


@router.post("/register")
async def register(payload: RegisterPayload):
    """Create a new user and profile using Supabase."""
    try:
        response = supabase.auth.sign_up(
            {
                "email": payload.email,
                "password": payload.password,
                "user_metadata": {"name": payload.name or payload.email},
            }
        )
        profile = {
            "user_id": response.user.id,
            "name": payload.name or payload.email,
            "role": "attendant",
        }
        supabase.table("profiles").insert(profile).execute()
        return {"user_id": response.user.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
async def login(payload: LoginPayload):
    """Authenticate user via Supabase."""
    try:
        session = supabase.auth.sign_in_with_password(
            {"email": payload.email, "password": payload.password}
        )
        return {"access_token": session.session.access_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

