generate: 
	./minimalsite.py -t templates/default_template.py 
#	./minimalsite.py -t templates/default_template.py -s src_en -d en

update:
	make
	git commit -am fix
	git push

clean:
	find . -type f -name "*.html" -exec rm -f {} \;
	find . -type d -empty -exec rm -rf {} \ ;
