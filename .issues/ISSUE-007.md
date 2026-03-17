# ISSUE-007: Models de ClassGroup e ClassEnrollment

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 001, 003

## Descrição
Implementar os models de turmas e matrículas para o domínio de organização escolar.

## Entidades (ref: domain_model.md)
- ClassGroup (teacher_profile_id, name, description, class_status)
- ClassEnrollment (class_group_id, student_profile_id, enrolled_at, enrollment_status)

## Critérios de Aceite
- [ ] ClassGroup e ClassEnrollment implementados conforme domain_model.md
- [ ] Enums: ClassStatus (ACTIVE, ARCHIVED), EnrollmentStatus (ACTIVE, REMOVED)
- [ ] Constraint: unique(teacher_profile_id, name)
- [ ] Constraint: unique(class_group_id, student_profile_id)
- [ ] Apenas professores podem ser donos de turmas (BR-004)
- [ ] Migrações geradas
- [ ] Testes unitários
