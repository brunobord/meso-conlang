pdf:
	pandoc \
        --pdf-engine=xelatex \
        -V mainfont="Ubuntu" \
        -V monofont="Monaco" \
        -V geometry=a5paper \
        -H chapter_break.tex \
        -f commonmark+hard_line_breaks+footnotes-implicit_figures+pipe_tables+yaml_metadata_block \
        language.md lexicon.md -o meso-a5.pdf
