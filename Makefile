generate: 
	./minimalsite.py -t templates/default_template.py -s src_it -d .
	./minimalsite.py -t templates/default_template.py -s src_en -d en
	./minimalsite.py -t templates/default_template.py -s src_de -d de

update:
	make
	git add .
	git commit -am fix
	git push

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
