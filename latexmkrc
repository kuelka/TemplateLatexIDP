# Configuracao do latexmk para o template do IDP.
# Uso: latexmk -pdf main.tex   |   latexmk -c (limpa auxiliares)   |   latexmk -C (limpa tudo, inclusive o PDF)

$pdf_mode = 1;              # pdflatex
$bibtex_use = 2;
$biber = 'biber --input-encoding=utf8 --output-encoding=utf8 %O %S';
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 -file-line-error %O %S';

# Extensoes extras geradas pelas listas/floats personalizados (quadros e graficos)
push @generated_exts, 'loq', 'logr', 'lof', 'lot', 'bcf', 'run.xml', 'synctex.gz';
$clean_ext .= ' %R.loq %R.logr %R.bbl %R.run.xml %R.synctex.gz';
