generate: 
	./minimalsite.py -t templates/default_template.py -s src_it -d .
	./minimalsite.py -t templates/default_template.py -s src_de -d de

update:
	make
	git commit -am fix
	git push

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
