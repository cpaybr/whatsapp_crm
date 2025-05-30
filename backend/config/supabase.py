from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Carrega variáveis do .env
load_dotenv()

# Configura o cliente Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)