#!/usr/bin/env bash
# Publica uma correção da skill no GitHub: branch, testes, checagem de dado
# pessoal, PR e merge. A outra instalação recebe na próxima chamada.
# Uso: scripts/publicar.sh "o que mudou (fonte: norma ou URL)" [--dry-run]
set -euo pipefail

msg="${1:-}"
dry="${2:-}"
[ -n "$msg" ] || { echo "Uso: $0 \"o que mudou (fonte: ...)\" [--dry-run]" >&2; exit 2; }

skill="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
root="$(git -C "$skill" rev-parse --show-toplevel)"
cd "$root"

[ -n "$(git status --porcelain)" ] || { echo "Nada para publicar."; exit 0; }
perm="$(gh repo view --json viewerPermission -q .viewerPermission 2>/dev/null || echo NONE)"
case "$perm" in
  ADMIN|MAINTAIN|WRITE) ;;
  *) echo "Sem permissão de escrita no repositório ($perm). A correção fica só nesta instalação; proponha por issue ou fork." >&2; exit 1 ;;
esac
fora="$(git status --porcelain | awk '{print $NF}' | grep -v -E '^(contador/|README\.md$|install\.sh$)' || true)"
if [ -n "$fora" ]; then
  echo "Mudanças fora da skill, não publico:" >&2
  echo "$fora" >&2
  exit 1
fi

python3 contador/scripts/testar.py >/dev/null || {
  echo "Testes falharam (rode python3 contador/scripts/testar.py para ver). Nada publicado." >&2
  exit 1
}

git add -A contador README.md install.sh
# Repositório público: dado de cliente fica em $CONTADOR_HOME, nunca aqui.
if git diff --cached | grep -E '^\+' | grep -E -q \
   '[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}|[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}|[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z.]{2,}'; then
  git reset -q
  echo "O diff tem CPF, CNPJ ou e-mail. Dado de cliente vai para \$CONTADOR_HOME, não para a skill. Nada publicado." >&2
  exit 1
fi

if [ "$dry" = "--dry-run" ]; then
  git diff --cached --stat
  git reset -q
  echo "dry-run: testes e checagens ok, nada publicado."
  exit 0
fi

GIT_TERMINAL_PROMPT=0 git pull -q --ff-only origin main || {
  git reset -q
  echo "main remota mudou e não deu fast-forward; rode atualizar.sh e refaça a correção. Nada publicado." >&2
  exit 1
}

titulo="$(printf '%s' "$msg" | head -n1 | cut -c1-72)"
branch="atualiza/$(date +%Y%m%d-%H%M%S)"
git checkout -q -b "$branch"
git commit -q -m "$msg"
# Usa o login do gh sem mexer na configuração global do git.
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push -q -u origin "$branch"
url="$(gh pr create --base main --head "$branch" --title "$titulo" \
  --body "Atualização da skill contador feita durante o uso. Os testes de scripts/testar.py passaram antes do envio.

$msg")"
gh pr merge "$url" --squash --delete-branch >/dev/null
git checkout -q main 2>/dev/null || true
GIT_TERMINAL_PROMPT=0 git pull -q --ff-only origin main
git branch -D "$branch" >/dev/null 2>&1 || true
echo "Publicado: $url"
