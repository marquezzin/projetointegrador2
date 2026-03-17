# ISSUE-003: Model User + Auth (JWT login, registro, perfis)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 001

## Descrição
Implementar o model User customizado com roles (STUDENT, TEACHER, ADMIN), status de conta, e os perfis especializados (StudentProfile, TeacherProfile, AdminProfile). Implementar autenticação JWT com endpoints de login, registro, refresh e `/me/`.

## Entidades (ref: domain_model.md)
- User (full_name, email, password_hash, role, account_status, last_login_at)
- StudentProfile (user_id, learning_status, first_started_at)
- TeacherProfile (user_id)
- AdminProfile (user_id)

## Critérios de Aceite
- [ ] Custom User model com campos do domain model
- [ ] Enums: UserRole, AccountStatus, LearningStatus
- [ ] StudentProfile, TeacherProfile, AdminProfile criados
- [ ] Endpoint POST `/api/v1/auth/login/` retorna JWT
- [ ] Endpoint POST `/api/v1/auth/register/` cria conta de aluno
- [ ] Endpoint POST `/api/v1/auth/refresh/` renova token
- [ ] Endpoint GET `/api/v1/auth/me/` retorna dados do usuário logado
- [ ] Perfil especializado criado automaticamente ao registrar
- [ ] Conta INACTIVE/SUSPENDED não consegue logar
- [ ] Testes unitários cobrindo auth e models
