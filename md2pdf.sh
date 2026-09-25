#!/bin/bash
if [ -z "$1" ]; then
    echo "Uso: $0 caminho/para/arquivo.md"
    exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILE_INPUT="$1"

# Obter caminhos absolutos
ABS_FILE="$(realpath "$FILE_INPUT")"
DIRNAME="$(dirname "$ABS_FILE")"
BASENAME="$(basename "$ABS_FILE" .md)"

echo "Convertendo $ABS_FILE para $DIRNAME/$BASENAME.pdf..."

cd "$DIRNAME"

pandoc "$BASENAME.md"     -o "$BASENAME.pdf"     --resource-path=".:figuras:$ROOT_DIR:$DIRNAME"     -V geometry:margin=2.5cm     -V fontsize=12pt     --pdf-engine=pdflatex     --number-sections     --highlight-style pygments

if [ $? -eq 0 ]; then
    echo "Sucesso! Arquivo gerado: $DIRNAME/$BASENAME.pdf"
else
    echo "Erro na conversão."
    exit 1
fi
