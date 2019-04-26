all: build/main.pdf

# hier Python-Skripte:
build/plot_schall_impuls.pdf: plot_schall_impuls.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot_schall_impuls.py

build/plot_schall_durch.pdf: plot_schall_durch.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot_schall_durch.py

build/plot_daempfung.pdf: plot_daempfung.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot_daempfung.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot_schall_impuls.pdf build/plot_schall_durch.pdf build/plot_daempfung.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
