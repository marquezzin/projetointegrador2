# ISSUE-013: Submissão de código e persistência de resultado (API + frontend)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 011, 012

## Descrição
Implementar o fluxo completo de submissão: aluno executa código no Skulpt, resultado é consolidado e enviado ao backend para persistência. Ref: J-003 (passos 4-8), BR-012.

## Critérios de Aceite
- [ ] API POST `/api/v1/submissions/` recebe resultado do Skulpt e persiste
- [ ] API GET `/api/v1/submissions/?exercise_id=X` retorna histórico de submissões do aluno
- [ ] Frontend: botão "Submeter" executa código + envia resultado ao backend
- [ ] Resultado consolidado (passed/failed/error + feedback) persistido
- [ ] Apenas alunos podem submeter (BR-011)
- [ ] Exercício deve estar PUBLISHED para receber submissão
- [ ] Histórico de submissões visível para o aluno
