# ISSUE-006: CRUD Admin de Conteúdo (API + frontend)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 005, 004

## Descrição
Implementar API e interface para o administrador gerenciar módulos, aulas, videoaulas, exercícios e testes de correção. Ref: J-007.

## Critérios de Aceite
- [ ] API CRUD para Module, Lesson, VideoLesson, Exercise, ExerciseTestCase
- [ ] Apenas administradores podem acessar (RBAC)
- [ ] Frontend: listagem, criação, edição de módulos
- [ ] Frontend: gestão de aulas dentro de módulo
- [ ] Frontend: gestão de exercícios e testes dentro de aula
- [ ] Validação: exercício não pode ser PUBLISHED sem ao menos 1 test case
- [ ] Ordenação por sequence_order
