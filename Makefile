.PHONY: all clean

# Default target
all: my-dissertation/build/main.pdf

# Build the main PDF using latexmk
my-dissertation/build/main.pdf: my-dissertation/main.tex
	cd my-dissertation && latexmk -xelatex -outdir=build main.tex

# Clean up all generated files
clean:
	cd my-dissertation && latexmk -C -outdir=build
	rm -rf my-dissertation/build

