# ISSUE-014: Models de Progresso (Module, Lesson, Exercise Progress)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 001, 005

## Descrição
Implementar os models de acompanhamento de progresso do aluno por módulo, aula e exercício.

## Entidades (ref: domain_model.md)
- StudentModuleProgress (student_profile_id, module_id, progress_status, started_at, completed_at)
- StudentLessonProgress (student_profile_id, lesson_id, progress_status, started_at, completed_at)
- StudentExerciseProgress (student_profile_id, exercise_id, progress_status, attempts_count, first_attempt_at, completed_at)

## Critérios de Aceite
- [ ] Todos os models implementados conforme domain_model.md
- [ ] Enum ProgressStatus (NOT_STARTED, IN_PROGRESS, COMPLETED)
- [ ] Constraints de unicidade por (student, item)
- [ ] Invariantes: completed_at preenchido → status COMPLETED
- [ ] Invariantes: NOT_STARTED → started_at e completed_at vazios
- [ ] Migrações geradas
- [ ] Testes unitários
