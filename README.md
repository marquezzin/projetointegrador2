# 📚 Plataforma de Ensino Introdutório de Programação

Plataforma web para ensino de programação introdutória voltada a estudantes do 8º e 9º ano do ensino fundamental. Combina conteúdo didático progressivo, exercícios práticos com editor de código Python (via Skulpt) e correção automática no navegador.

## 🏗️ Estrutura do Projeto

```
├── backend/          # API REST — Django + DRF
├── frontend/         # Interface web — React + Vite
├── ingenia-documents/ # Documentação de requisitos e design
└── .issues/          # Issue tracker do projeto
```

---

## ⚙️ Pré-requisitos

- **Python** 3.9+
- **Node.js** 18+
- **npm** 9+
- **Git**

---

## 🚀 Configuração

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd proojetointegrador2
```

### 2. Backend (Django REST Framework)

```bash
# Entrar na pasta do backend
cd backend

# Criar ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# Atualizar pip
pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt

# Verificar se está tudo OK
python manage.py check

# Aplicar migrações do banco de dados
python manage.py migrate

# (Opcional) Criar superusuário admin
python manage.py createsuperuser

# Rodar o servidor de desenvolvimento
python manage.py runserver
```

O backend estará disponível em **http://localhost:8000**.

### 3. Frontend (React + Vite)

```bash
# Em outro terminal, entrar na pasta do frontend
cd frontend

# Instalar dependências
npm install

# Rodar o servidor de desenvolvimento
npm run dev
```

O frontend estará disponível em **http://localhost:5173**.

---

## 📁 Estrutura do Backend

```
backend/
├── config/              # Configuração do projeto Django
│   ├── settings.py      # Settings (DRF, JWT, CORS, i18n)
│   ├── urls.py          # Rotas principais
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── accounts/        # Usuários, autenticação, perfis
│   ├── content/         # Módulos, aulas, vídeos, exercícios, testes
│   ├── submissions/     # Submissões de código e resultados
│   ├── progress/        # Progresso do aluno (módulo, aula, exercício)
│   └── classgroups/     # Turmas e matrículas
├── manage.py
└── requirements.txt
```

## 📁 Estrutura do Frontend

```
frontend/src/
├── domains/
│   ├── auth/            # Login, registro, recuperação de senha
│   ├── student/         # Trilha, aulas, exercícios, progresso
│   ├── teacher/         # Painel do professor, turmas
│   └── admin/           # Gestão de conteúdo e usuários
├── shared/
│   ├── components/      # Componentes reutilizáveis
│   ├── hooks/           # Hooks compartilhados
│   ├── services/        # API client (axios, fetch)
│   └── utils/           # Utilitários
└── assets/              # Imagens, ícones, fontes
```

---

## 🔧 Variáveis de Ambiente

O backend aceita as seguintes variáveis (via `.env` ou variáveis de sistema):

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `DJANGO_SECRET_KEY` | (insegura, dev only) | Chave secreta do Django |
| `DJANGO_DEBUG` | `True` | Modo debug |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Hosts permitidos |
| `CORS_ALLOWED_ORIGINS` | `http://localhost:5173,...` | Origens CORS permitidas |

Para produção, crie um arquivo `.env` na raiz de `backend/`:

```env
DJANGO_SECRET_KEY=sua-chave-secreta-aqui
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=seudominio.com
CORS_ALLOWED_ORIGINS=https://seudominio.com
```

---

## 📋 Issue Tracker

O progresso do projeto é acompanhado em `.issues/TRACKER.md`. Cada issue tem seu arquivo individual em `.issues/ISSUE-XXX.md`.

Para ver o status atual:
```bash
cat .issues/TRACKER.md
```

---

## 🛠️ Comandos Úteis

### Backend
```bash
python manage.py check                        # Verificar configuração
python manage.py makemigrations               # Criar novas migrações a partir dos models
python manage.py makemigrations nome_do_app   # Criar migrações para um app específico
python manage.py migrate                      # Aplicar migrações no banco de dados
python manage.py runserver                    # Iniciar servidor dev
python manage.py createsuperuser              # Criar admin
python manage.py test                         # Rodar testes
```

### Frontend
```bash
npm run dev      # Servidor de desenvolvimento
npm run build    # Build de produção
npm run preview  # Preview do build
npm run lint     # Verificar código
```

---

## 👥 Perfis do Sistema

| Perfil | Descrição |
|--------|-----------|
| **Aluno** | Acessa trilha de aprendizagem, resolve exercícios, acompanha progresso |
| **Professor** | Gerencia turmas, acompanha progresso dos alunos |
| **Administrador** | Gerencia conteúdo, exercícios e usuários |

---

## 📖 Documentação

A documentação completa dos requisitos está em `ingenia-documents/`:

- `discover/` — Especificação, escopo, stakeholders, premissas
- `design/` — Modelo de domínio, jornadas, autorização, fluxos UX
