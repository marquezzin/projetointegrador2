# 📋 Issue Tracker — Plataforma de Ensino Introdutório de Programação

> Última atualização: 2026-03-16

## Legenda de Status

| Emoji | Status |
|-------|--------|
| ⬜ | Backlog |
| 🟡 | Em progresso |
| ✅ | Concluída |
| 🔴 | Bloqueada |

## Issues

| # | ID | Título | Prioridade | Deps | Status |
|---|-----|--------|------------|------|--------|
| 1 | 001 | Setup inicial do backend (Django + DRF) | Critical | — | ✅ |
| 2 | 002 | Setup inicial do frontend (React + Vite) | Critical | — | ✅ |
| 3 | 003 | Model User + Auth (JWT login, registro, perfis) | Critical | 001 | ⬜ |
| 4 | 005 | Models de Conteúdo (Module, Lesson, VideoLesson, Exercise, ExerciseTestCase) | Critical | 001 | ⬜ |
| 5 | 004 | Páginas de Auth no frontend (login, registro, recuperação) | Critical | 002, 003 | ⬜ |
| 6 | 007 | Models de ClassGroup e ClassEnrollment | Critical | 001, 003 | ⬜ |
| 7 | 012 | Models de Submission e SubmissionResult | Critical | 001, 005 | ⬜ |
| 8 | 014 | Models de Progresso (Module, Lesson, Exercise Progress) | Critical | 001, 005 | ⬜ |
| 9 | 018 | Autorização e permissões (RBAC) | Critical | 003 | ⬜ |
| 10 | 009 | Trilha de Aprendizagem — Aluno (API + frontend) | Critical | 005, 004 | ⬜ |
| 11 | 006 | CRUD Admin de Conteúdo (API + frontend) | Critical | 005, 004 | ⬜ |
| 12 | 017 | Gestão de Usuários pelo Admin (API + frontend) | Critical | 003, 004 | ⬜ |
| 13 | 008 | Gestão de Turmas — Professor (API + frontend) | Critical | 007, 004 | ⬜ |
| 14 | 010 | Página de Aula — Vídeo + Material Escrito + Exercícios | Critical | 009 | ⬜ |
| 15 | 011 | Editor de Código + Execução Skulpt + Correção Automática | Critical | 010 | ⬜ |
| 16 | 013 | Submissão de código e persistência de resultado (API + frontend) | Critical | 011, 012 | ⬜ |
| 17 | 015 | Progresso do Aluno — Cálculo e visualização | Critical | 014, 013 | ⬜ |
| 18 | 016 | Painel do Professor — Progresso coletivo e individual | Critical | 008, 015 | ⬜ |
| 19 | 019 | Segurança e proteção (rate limiting, validação, CORS) | Important | 018 | ⬜ |
| 20 | 020 | UI/UX Polish — Interface guiada e intuitiva | Important | Todas | ⬜ |

## Grafo de Dependências

```
001 ──┬── 003 ──┬── 004 ──┬── 006
      │         │         ├── 008
      │         │         ├── 009 ── 010 ── 011 ──┐
      │         │         └── 017                  │
      │         ├── 007 ── 008                     │
      │         └── 018 ── 019                     │
      ├── 005 ──┬── 006                            │
      │         ├── 009                            │
      │         ├── 012 ─────────────────── 013 ◄──┘
      │         └── 014 ── 015 ── 016
      └── 012
002 ──── 004
                              020 (depende de todas)
```

## Ordem Sugerida de Execução

1. ~~001 + 002~~ (Setup — já concluídos)
2. 003 (User + Auth backend)
3. 005 (Models de Conteúdo)
4. 004 (Auth frontend)
5. 007 + 012 + 014 (Models: turmas, submissões, progresso)
6. 018 (RBAC)
7. 009 (Trilha do Aluno)
8. 006 + 017 (Admin: conteúdo + usuários)
9. 008 (Turmas do Professor)
10. 010 (Página de Aula)
11. 011 (Editor + Skulpt)
12. 013 (Submissão de código)
13. 015 (Progresso do Aluno)
14. 016 (Painel do Professor)
15. 019 (Segurança)
16. 020 (UI/UX Polish)
