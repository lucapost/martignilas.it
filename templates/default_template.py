import time
import datetime

SITE_NAME = "martignilas"
AUTHOR = "lucapost"
SRC = "/home/lucapost/repo/martignilas.it/src_"
DST = "./dst/"
SITEMAP = "sitemap_orig.xml"
URL = "http://martignilas.it"
PREFIX = "/"
HOME = "home"
PATH_SEPARATOR = '/'
SRC_EXT = {"markdown": "md", "textile": "tt"}
DST_EXT = "html"
HIDDEN = set(["404.md", "privacy.md"])
menu_code = ''
PAGES = {
         SRC + "it/01_index.md": ("casa", "Pagina principale del sito internet della Casa Vacanze Martignilas in Val Resia"),
	 SRC + "it/10_alloggi.md": ("alloggi", "Descrizione degli alloggi della Casa Vacanze Martignilas in Val Resia"),
	 SRC + "it/20_informazioni.md": ("informazioni", "Eventi ed attrattivita da visitare vicino alla Casa Vacanze Martignilas in Val Resia"),
	 SRC + "it/30_contatti.md": ("contatti", "Come contattare il propietario della Casa Vacanze Martignilas in Val Resia"),
         SRC + "en/01_index.md": ("home", "Martignilas holidays home website"),
	 SRC + "en/10_accomodation.md": ("accomodation", "description of building and offers"),
	 SRC + "en/20_informations.md": ("informations", "some informations about restaurant and museum"),
	 SRC + "en/30_contacts.md": ("contacts", "how you can contacs with we"),
         SRC + "de/01_index.md": ("haus", "Martignilas"),
	 SRC + "de/10_unterkunft.md": ("unterkunft", "Hausbeschreibung"),
	 SRC + "de/20_informationen.md": ("informationen", "Ereignisse und Dinge zu sehen"),
	 SRC + "de/30_kontacte.md": ("kontacte", "Kommunikation mit dem Besitzer")
}

current_time = datetime.datetime.now()

def get_page_contents(node):
    """Return page title and description from the global variable slides_alloggi if a
    match with current node page.src_file is found.
    """  
    try:
        return (SITE_NAME + ' | ' + PAGES[node.page.src_pathname][0], \
            PAGES[node.page.src_pathname][1],
            PAGES[node.page.src_pathname][0])
    except KeyError:
        return ('%%%TITLE%%%', '', '')

def menu(node):
    """Generate a hierarchical menu."""

    global menu_code

    menu_code = '\n'
    root = node
    while root.parent:
        root = root.parent
    menu_(root, node)
    return menu_code

def menu_(node, cur_node, node_prefix = PREFIX, indent = ''):
    """Auxiliary recursive function for menu generation."""

    if node.page.dst_pathname == '/home/lucapost/repo/martignilas.it/dst/de':
      node_prefix = '/de/'

    if node.page.dst_pathname == '/home/lucapost/repo/martignilas.it/dst/en':
      node_prefix = '/en/'

    global menu_code

    menu_code += indent + '<ul>\n'
    for child in sorted(node.children, key=lambda n: n.page.src_pathname):
	(title, description, linkname) = get_page_contents(child)
        if child.page.src_file in HIDDEN:
            continue
        menu_code += indent + '<li class="level-' + str(child.page.level)
        if(child == cur_node
        or (cur_node.page.dst_file.startswith("index.") and child == cur_node.parent)):
            menu_code += ' current'
        menu_code += '"><a href="' + node_prefix + child.page.dst_file
        if child.children:
            menu_code += "/index." + DST_EXT + '">' + linkname + '</a>\n'
            menu_(child, cur_node, node_prefix + child.page.dst_file + '/', indent + '\t')
            menu_code += indent + '</li>\n'
	else:
	    menu_code += '">'   + linkname + '</a></li>\n'
    menu_code += indent + '</ul>\n'

def header(node):
    """Build the header and return it to a string."""

    (title, description, linkname) = get_page_contents(node)
 
    flagit = ''
    flagde = ''
    flagen = ''
    lang = 'it'
    imagebg = ''

    if DST == '/home/lucapost/repo/martignilas.it/dst/de':
      desc = 'Ferienhaus in Val Resia'
      flagde = ' active'
      lang = 'de'
    elif DST == '/home/lucapost/repo/martignilas.it/dst/en':
      desc = 'Holidays house in Val Resia'
      flagen = ' active'
      lang = 'en'
    else:
      desc = 'Casa vacanze in Val Resia'
      flagit = ' active'
      lang = 'it'

    if linkname == 'casa' or linkname == 'haus' or linkname == 'home':
	imagebg = ' casa'
    if linkname == 'alloggi' or linkname == 'unterkunft' or linkname == 'accomodation':
	imagebg = ' alloggi'
    if linkname == 'info':
	imagebg = ' info'
    if linkname == 'contatti' or linkname == 'kontacte' or linkname == 'contacts':
	imagebg = ' contatti'

    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="''' + lang + '''"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="''' + lang + '''"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="'''+ lang + '''"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="''' + lang + '''"> <!--<![endif]-->
	<head>
      		<title>''' + title + '''</title>
    		<meta charset="utf-8" />
       		<meta name="author" content="''' + AUTHOR + '''" />
	    	<meta name="description" content="''' + description + '''" />
  		<meta name="viewport" content="width=device-width">
		<!--[if lt IE 9]>
  			<script src="/assets/js/html5.js"></script>
		<![endif]-->
		<!--[if (gt IE 8) | (IEMobile)]><!-->
		  	<link rel="stylesheet" href="/assets/css/unsemantic-grid-responsive.css" />
		<!--<![endif]-->
		<!--[if (lt IE 9) & (!IEMobile)]>
  			<link rel="stylesheet" href="/assets/css/ie.css" />
		<![endif]-->
		<link rel="stylesheet" type="text/css" media="all" href="/assets/css/style.css" />
  		<script src="/assets/js/modernizr.js"></script>
		<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
		<script src="/assets/js/slippry.min.js"></script>
		<script src="/assets/js/slippryinit.js"></script>
		<script src="//use.edgefonts.net/cabin;source-sans-pro:n2,i2,n3,n4,n6,n7,n9.js"></script>
		<meta name="viewport" content="width=device-width">
    		<link rel="stylesheet" href="/assets/css/demo.css">
    		<link rel="stylesheet" href="/assets/css/slippry.css">
	</head>
	<body id="top">
		<div class="grid-container box">
			<header class="grid-40 mobile-grid-100">
				<a href="/" title="home page">
					<h1>''' + SITE_NAME + '''</h1>
					<h2>''' + desc + '''</h2>
				</a>
			</header>
			<nav class="grid-30 menu mobile-grid-100">
				''' + menu(node) + '''
			</nav>
			<nav class="flag">
				<a href="/" title="italiano">
					<figure class="grid-10 mobile-grid-33">
						<img src="/images/flag_ita.png" alt="lingua italiana" class="''' + flagit + '''">
					</figure>
				</a>
				<a href="/en" title="english">
					<figure class="grid-10 mobile-grid-33">
						<img src="/images/flag_eng.png" alt="english language" class="''' + flagen + '''">
					</figure>
				</a>
				<a href="/de" title="deutsch">
					<figure class="grid-10 mobile-grid-33">
						<img src="/images/flag_deu.png" alt="deutch" class="''' + flagde + '''">
					</figure>
				</a>
			</nav>
		</div>
		<div class="grid-container box">
			<article class="grid-60 mobile-grid-100'''+ imagebg +'''">
'''
def footer(node):
    """Build the footer and return it to a string."""

    (title, description, linkname) = get_page_contents(node)

    html = '''\n</article>'''
    if linkname == 'casa' or linkname == 'haus' or linkname == 'home':
	html += '''<div class="grid-40 mobile-grid-100"><figure class="fronte"><img alt="ingresso della casa" src="/images/slides_allo/10.jpg" title="casa martignilas" class="casa"/></figure></div>'''
    elif linkname == 'alloggi' or linkname == 'unterkunft' or linkname == 'accomodation':
	html += '''
<div class="grid-40 mobile-grid-100 gallery">
		<section class="demo_wrapper">
			<article class="demo_block">
<!--				<a href="#glob" class='prev'>Prev</a> / <a href="#glob" class='next'>Next</a>
		|| <a href="#glob" class='init'>Init</a> | <a href="#glob" class='reset'>Destroy</a> | <a href="#glob" class='reload'>Reload</a>
		|| <a href="#glob" class='stop'>Stop</a> | <a href="#glob" class='start'>Start</a> -->
			<ul id="demo1">
				<li><a href="#slide1"><img src="/images/slides_allo/01.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/02.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/03.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/04.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/05.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/06.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/07.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/08.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/09.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/10.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/11.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_allo/12.jpg" alt=""></a></li>
			</ul>
			</article>
		</section>
</div>'''
    elif linkname == 'informazioni' or linkname == 'informationen' or linkname == 'informations':
#	html += '''<figure class="grid-40 mobile-grid-100"><img class="logo" src="/images/slides_alloggi/mappa_info.png" alt="mappa informazioni"/><!--<img class="logo" src="http://upload.wikimedia.org/wikipedia/it/8/8b/Resia-Stemma.png" alt="logo del comune di resia"/><img class="logo" src="http://www.parcoprealpigiulie.it/public/image/LOGHI/Logo_Parco_naturale_delle_Prealpi_Giulie.jpg" alt="logo del comune di resia"/>--></figure>'''
	html += '''
<div class="grid-40 mobile-grid-100 gallery">
		<section class="demo_wrapper">
			<article class="demo_block">
			<ul id="demo1">
				<li><a href="#slide1"><img src="/images/slides_info/12.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/13.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/14.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/15.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/16.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/17.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/18.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/19.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/20.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/21.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/22.jpg" alt=""></a></li>
				<li><a href="#slide1"><img src="/images/slides_info/23.jpg" alt=""></a></li>
			</ul>
			</article>
		</section>		
		<figure><img class="logo" src="/images/pages/mappa_info.png" alt="mappa informazioni"/><img class="logo" src="https://upload.wikimedia.org/wikipedia/it/8/8b/Resia-Stemma.png" alt="logo del comune di resia"/><img class="logo" src="https://www.parcoprealpigiulie.it/public/image/LOGHI/Logo_Parco_naturale_delle_Prealpi_Giulie.jpg" alt="logo del comune di resia"/></figure>
</div>
'''
    elif linkname == 'contatti' or linkname == 'kontacte' or linkname == 'contacts':
        html += '''<figure class="grid-40 mobile-grid-100">
<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d31257.008462646285!2d13.318498!3d46.371157!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDbCsDIyJzE2LjIiTiAxM8KwMTknMDYuNiJF!5e1!3m2!1sit!2sus!4v1427747375802" width="100%" height="400" frameborder="0" style="border:0"></iframe>
		</figure>'''
    html += '''
		</div>
		<div class="grid-container box">
			<footer>
				<div class="grid-60 mobile-grid-100">
                			<p>email: <a href="mailto:patdilenardo@gmail.com">patdilenardo@gmail.com</a>; tel: +393389456208 <br/>
                			Fraz. Martignilas n. 8, 33010 Resia, Udine - Italia</p>
				</div>
				<div class="grid-40 mobile-grid-100">
					<p class="right">&copy; ''' + str(current_time.year) + ''' <a href="https://luca.postregna.name" title="lucapost blog">lucapost</a> <a rel="license" href="https://creativecommons.org/licenses/by-nc/3.0/">license</a> | <a href="/privacy.html">privacy</a> <br/> edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
				</div>
			</footer>
		</div>
		<script type="text/javascript">
			var _gaq = _gaq || [];
			_gaq.push(['_setAccount', 'UA-6164762-13']);
  			_gaq.push(['_trackPageview']);
  			(function() {
    			var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    			ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    			var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  			})();
		</script>	
	</body>
</html>'''
    return html	
