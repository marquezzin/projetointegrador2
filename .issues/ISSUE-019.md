# ISSUE-019: Segurança e proteção (rate limiting, validação, CORS)

**Status:** ⬜ Backlog
**Prioridade:** Important
**Dependências:** 018

## Descrição
Implementar medidas de segurança conforme spec.md seção 9: rate limiting, validação de entrada, proteção contra vulnerabilidades comuns.

## Critérios de Aceite
- [ ] Rate limiting em rotas de auth e submissão
- [ ] Validação de entrada em todos os endpoints
- [ ] CORS configurado para permitir apenas o frontend
- [ ] Proteção contra CSRF em operações sensíveis
- [ ] Headers de segurança configurados (X-Frame-Options, etc.)
- [ ] Sanitização de conteúdo submetido por usuários
- [ ] Testes de segurança básicos
