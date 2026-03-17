# ISSUE-009: Trilha de Aprendizagem — Aluno (API + frontend)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 005, 004

## Descrição
Implementar a visualização da trilha de aprendizagem para o aluno, com módulos e indicação de progresso. Ref: J-002.

## Critérios de Aceite
- [ ] API GET `/api/v1/content/modules/` retorna módulos PUBLISHED com progresso do aluno
- [ ] API GET `/api/v1/content/modules/:id/lessons/` retorna aulas do módulo
- [ ] Frontend: trilha visual com módulos e status de progresso
- [ ] Frontend: navegação de módulo para lista de aulas
- [ ] Conteúdos DRAFT/ARCHIVED não aparecem para alunos (BR-019)
- [ ] Apenas alunos autenticados acessam a trilha
