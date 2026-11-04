#!/usr/bin/env bash
# Traz a versão mais nova da skill do GitHub. Roda no começo de cada uso.
# Nunca falha: sem rede ou com conflito, avisa e segue com a versão local.
set -u

skill="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
root="$(git -C "$skill" rev-parse --show-toplevel 2>/dev/null)" || {
  echo "contador: instalada como cópia, sem atualização automática (instale com install.sh para ter git pull)."
  exit 0
}
cd "$root"

branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
if [ "$branch" != "main" ]; then
  if [ -z "$(git status --porcelain)" ]; then
    git checkout -q main 2>/dev/null || { echo "contador: não consegui voltar para main; seguindo com a versão local."; exit 0; }
  else
    echo "contador: há alteração local não publicada no branch $branch; seguindo sem atualizar."
    exit 0
  fi
fi

antes="$(git rev-parse HEAD)"
# Remoto lento não pode travar a conversa: desiste se ficar 10 s abaixo de 1 KB/s.
if ! GIT_TERMINAL_PROMPT=0 git -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=10 \
     pull -q --ff-only origin main 2>/dev/null; then
  echo "contador: sem acesso ao GitHub ou com alteração local em conflito; seguindo com a versão local ($(git log -1 --format=%cs))."
  exit 0
fi
depois="$(git rev-parse HEAD)"

if [ "$antes" = "$depois" ]; then
  echo "contador: já na versão mais nova ($(git log -1 --format='%h de %cs'))."
  exit 0
fi
echo "contador: atualizada de ${antes:0:7} para ${depois:0:7}."
git log --format='  - %s' "$antes..$depois"
if git diff --name-only "$antes" "$depois" | grep -q '^contador/SKILL.md$'; then
  echo "SKILL.md mudou: releia o SKILL.md antes de seguir."
fi
