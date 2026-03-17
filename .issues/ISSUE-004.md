# ISSUE-004: Páginas de Auth no frontend (login, registro, recuperação)

**Status:** ⬜ Backlog
**Prioridade:** Critical
**Dependências:** 002, 003

## Descrição
Implementar as páginas de autenticação no frontend: login, registro e recuperação de senha. Incluir redirecionamento por role após login (aluno → trilha, professor → painel, admin → admin).

## Critérios de Aceite
- [ ] Página de Login com email e senha
- [ ] Página de Registro com campos do User model
- [ ] Página de Recuperação de Senha
- [ ] Armazenamento de JWT (access + refresh tokens)
- [ ] Redirecionamento por role após login
- [ ] Tratamento de erros (credenciais inválidas, conta inativa)
- [ ] Proteção de rotas autenticadas
- [ ] Componente de layout para páginas de auth
