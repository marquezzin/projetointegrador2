# ISSUE-012: Models de Submission e SubmissionResult

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 001, 005

## Descrição
Implementar os models de submissão de código e resultado de avaliação.

## Entidades (ref: domain_model.md)
- Submission (exercise_id, student_profile_id, source_code, evaluation_status, score_percentage, submitted_at)
- SubmissionResult (submission_id, passed_tests_count, failed_tests_count, feedback_message, result_status)

## Critérios de Aceite
- [ ] Submission e SubmissionResult implementados conforme domain_model.md
- [ ] Enums: SubmissionStatus (EVALUATED, FAILED), ResultStatus (PASSED, FAILED, ERROR)
- [ ] Constraint: unique(submission_id) em SubmissionResult
- [ ] Índices de performance criados
- [ ] Migrações geradas
- [ ] Testes unitários
