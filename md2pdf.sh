# Verifica se um argumento foi passado
if [ -z "$1" ]; then
    echo "Uso: $0 arquivo.md"
    exit 1
fi

# Pega o nome do arquivo sem a extensão .md
FILENAME=$(basename "$1" .md)

# Executa o comando Pandoc
# $1 é o arquivo de entrada (ex: artigo.md)
# $FILENAME.pdf será o arquivo de saída (ex: artigo.pdf)
echo "Convertendo $1 para $FILENAME.pdf..."

pandoc "$1" \
    -o "$FILENAME.pdf" \
    -V geometry:margin=2.5cm \
    -V fontsize=12pt \
    --pdf-engine=pdflatex \
    --number-sections \
    --highlight-style pygments

if [ $? -eq 0 ]; then
    echo "Sucesso! Arquivo gerado: $FILENAME.pdf"
else
    echo "Erro na conversão."
    exit 1
fi
