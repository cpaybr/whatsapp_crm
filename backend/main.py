from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.supabase import supabase
from routes.auth import router as auth_router

app = FastAPI()

# Allow requests from any origin during early development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/test-user")
async def create_test_user():
    try:
        user_data = {
            "email": "test.user@exemplo.com",
            "password": "Test1234",
            "user_metadata": {"name": "Test User"}
        }
        response = supabase.auth.sign_up(user_data)
        profile_data = {
            "user_id": response.user.id,
            "name": "Test User",
            "role": "attendant"
        }
        supabase.table("profiles").insert(profile_data).execute()
        settings_data = {
            "client_id": response.user.id,
            "recipes_enabled": True
        }
        supabase.table("client_settings").insert(settings_data).execute()
        return {"message": "User created", "user_id": response.user.id}
    except Exception as e:
        return {"error": str(e)}

@app.post("/upload-recipe")
async def upload_recipe(file: UploadFile = File(...), user_id: str = "8d124d16-b1e7-435f-a8ec-ef0c66acfd06"):
    try:
        supabase.auth.sign_in_with_password({"email": "test.user@exemplo.com", "password": "Test1234"})
        settings = supabase.table("client_settings").select("recipes_enabled").eq("client_id", user_id).execute()
        if not settings.data or not settings.data[0]["recipes_enabled"]:
            raise HTTPException(status_code=403, detail="Recipes module not enabled")
        file_content = await file.read()
        file_name = f"{user_id}/{file.filename}"
        supabase.storage.from_("recipes").upload(file_name, file_content)
        return {"message": "File uploaded", "file_name": file_name}
    except Exception as e:
        return {"error": str(e)}
