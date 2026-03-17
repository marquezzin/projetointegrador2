# ISSUE-018: Autorização e permissões (RBAC)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 003

## Descrição
Implementar o sistema de autorização baseado em papéis conforme a authorization matrix. Ref: authorization.md.

## Critérios de Aceite
- [ ] Permission classes DRF para cada role (IsAdmin, IsTeacher, IsStudent)
- [ ] Filtros contextuais: professor vê apenas dados de suas turmas
- [ ] Filtros contextuais: aluno vê apenas dados próprios
- [ ] Conta INACTIVE/SUSPENDED bloqueada independente do role
- [ ] Proteção de rotas no frontend por role
- [ ] CorrectionTest acessível apenas por admin
- [ ] Testes de autorização para cada endpoint
