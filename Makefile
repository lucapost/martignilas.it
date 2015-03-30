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
	make
	rsync -avr -e ssh ./dst/* flarevm:www/martignilas.it/
	rsync -avr -e ssh ./dst/* sun:/mnt/disk1/www/test.iulii.lii/

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
