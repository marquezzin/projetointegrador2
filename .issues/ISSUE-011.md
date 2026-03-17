# ISSUE-011: Editor de Código + Execução Skulpt + Correção Automática

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 010

## Descrição
Implementar o editor de código Python no navegador com execução via Skulpt e correção automática por test cases. Ref: J-003 (passos 3-8), ADR-004.

## Critérios de Aceite
- [ ] Editor de código Python integrado (CodeMirror ou Monaco)
- [ ] Integração com Skulpt para execução de código no browser
- [ ] API retorna test cases do exercício (ocultos e visíveis)
- [ ] Execução dos testes client-side contra output do código do aluno
- [ ] Timeout para loops infinitos (limite de tempo de execução)
- [ ] Feedback visual: testes aprovados/reprovados
- [ ] Mensagens de erro de sintaxe Python traduzidas para linguagem simples
- [ ] Tratamento de código em branco
- [ ] Suporte a validação por function_name e por print/output
