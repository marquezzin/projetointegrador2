# ISSUE-005: Models de Conteúdo (Module, Lesson, VideoLesson, Exercise, ExerciseTestCase)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 001

## Descrição
Implementar os models do domínio de conteúdo educacional: módulos, aulas, videoaulas, exercícios e testes de correção.

## Entidades (ref: domain_model.md)
- Module (title, description, sequence_order, publication_status)
- Lesson (module_id, title, written_content, sequence_order, publication_status)
- VideoLesson (lesson_id, title, video_url, duration_seconds)
- Exercise (lesson_id, title, statement, support_message, sequence_order, publication_status)
- ExerciseTestCase (exercise_id, name, function_name, input_data, expected_output, sequence_order, is_hidden)

## Critérios de Aceite
- [ ] Todos os models implementados conforme domain_model.md
- [ ] Enum ContentStatus (DRAFT, PUBLISHED, ARCHIVED)
- [ ] Constraints de unicidade conforme especificado
- [ ] Relacionamentos FK corretos
- [ ] Migrações geradas e aplicáveis
- [ ] Testes unitários dos models
