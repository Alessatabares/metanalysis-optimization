#!/usr/bin/env bash
# Crea un nuevo meta-análisis copiando _template/ a projects/<nombre>/
# Uso: ./scripts/new-project.sh <nombre-corto>
#   ej: ./scripts/new-project.sh meta-diabetes-metformina

set -e

if [ -z "$1" ]; then
  echo "Uso: $0 <nombre-corto>"
  echo "Ejemplo: $0 meta-diabetes-metformina"
  exit 1
fi

NAME="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$ROOT/projects/$NAME"

if [ -d "$TARGET" ]; then
  echo "Error: ya existe $TARGET"
  exit 1
fi

cp -r "$ROOT/_template" "$TARGET"
# Limpiar .gitkeep dentro del proyecto nuevo
find "$TARGET" -name ".gitkeep" -delete

echo "Creado: projects/$NAME"
echo ""
echo "Siguientes pasos:"
echo "  1. Edita $TARGET/STATUS.md con el título y PICO"
echo "  2. Edita $TARGET/protocolo/protocolo.md (PRISMA-P)"
echo "  3. En Claude Code, di: 'trabajemos en projects/$NAME, sigue el workflow PRISMA desde el paso actual'"
