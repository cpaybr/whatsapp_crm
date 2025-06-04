# Projeto Inicial - Setup

## Backend (FastAPI)

1. Instalar dependências:
   - fastapi
   - uvicorn
   - python-jose[cryptography]
   - passlib[bcrypt]
   - supabase-py
2. Estrutura:
   - /main.py: Configuração do FastAPI
   - /routes/auth.py: Endpoints de login/registro
   - /config/supabase.py: Conexão com Supabase
3. Endpoints iniciais:
   - `GET /health`: verifica se o servidor está online.
   - `POST /auth/register`: cria um usuário e perfil no Supabase.
   - `POST /auth/login`: autentica o usuário e retorna o token.

## Frontend (Nuxt 3)

1. Instalar dependências:
   - nuxt@latest
   - @nuxtjs/tailwindcss
   - @supabase/supabase-js
2. Estrutura:
   - /pages/index.vue: Página inicial com formulário de login
   - /layouts/default.vue: Layout base com Tailwind CSS
   - /plugins/supabase.client.js: Inicialização do Supabase
3. Página inicial:
   - Formulário de login com email/senha
   - Estilização com Tailwind CSS

## Supabase

1. Criar projeto no Supabase
2. Configurar autenticação (JWT)
3. Criar tabela inicial `users`:
   - id (uuid)
   - email (text)
   - role (text, default: 'attendant')
4. Configurar Storage para uploads futuros

## Testes

1. Backend:
   - Acessar http://localhost:8000/health
   - Testar login via Supabase Auth
2. Frontend:
   - Renderizar página inicial
   - Validar formulário de login
3. Supabase:
   - Verificar criação de usuário
   - Confirmar conexão com backend/frontend
