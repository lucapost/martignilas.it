generate: 
	./minimalsite.py -t templates/default_template.py -s src_it -d dst/
	./minimalsite.py -t templates/default_template.py -s src_en -d dst/en
	./minimalsite.py -t templates/default_template.py -s src_de -d dst/de

update:
	make
	git add .
	git commit -am fix
	git push

upload:
	rsync -avr -e ssh ./dst/* linode:www/martignilas.it/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;

all: 
	make generate
	make update
	make upload
