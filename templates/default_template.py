import time
import datetime

SITE_NAME = "martignilas"
AUTHOR = "lucapost"
SRC = "/home/lucapost/repo/martignilas.it/src_"
DST = "./"
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
         SRC + "it/01_index.md": ("casa", "sito internet della casa vacanze Martignilas"),
	 SRC + "it/10_alloggi.md": ("alloggi", "descrizione della casa"),
	 SRC + "it/20_informazioni.md": ("info", "eventi e cose da visitare"),
	 SRC + "it/30_contatti.md": ("contatti", "comunicare con il propietario"),
         SRC + "en/01_index.md": ("home", "Martignilas holidays home website"),
	 SRC + "en/10_accomodation.md": ("accomodation", "description of building and offers"),
	 SRC + "en/20_informations.md": ("info", "some informations about restaurant and museum"),
	 SRC + "en/30_contacts.md": ("contacts", "how you can contacs with we"),
         SRC + "de/01_index.md": ("haus", "Martignilas"),
	 SRC + "de/10_unterkunft.md": ("unterkunft", "descrizione della casa"),
	 SRC + "de/20_informationen.md": ("info", "eventi e cose da visitare"),
	 SRC + "de/30_kontacte.md": ("kontacte", "comunicare con il propietario")
}

current_time = datetime.datetime.now()

def get_page_contents(node):
    """Return page title and description from the global variable pages if a
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

    if node.page.dst_pathname == '/home/lucapost/repo/martignilas.it/de':
      node_prefix = '/de/'

    if node.page.dst_pathname == '/home/lucapost/repo/martignilas.it/en':
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

    if DST == '/home/lucapost/repo/martignilas.it/de':
      desc = 'Ferienhaus in Val Resia'
      flagde = ' active'
      lang = 'de'
    elif DST == '/home/lucapost/repo/martignilas.it/en':
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
        	<meta charset="utf-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
       	<meta name="author" content="''' + AUTHOR + '''" />
	    <meta name="description" content="''' + description + '''" />
      	<title>''' + title + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="/css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" />
  		<script src="/js/modernizr.js"></script>
	</head>
	<body id="top">
		<div class="container_24">
			<header class="push_3 grid_18">
					<div class="grid_1 alpha">&nbsp;</div>
					<a href="/" title="home page">
						<hgroup class="grid_8">
							<h1>''' + SITE_NAME + '''</h1>
							<h2>''' + desc + '''</h2>
						</hgroup>
					</a>
					<nav class="grid_4 suffix_1">
						''' + menu(node) + '''
					</nav>
					<figure class="flag">
						<a href="/" title="italiano">
							<img src="/images/flag_ita.png" alt="lingua italiana" class="grid_1''' + flagit + '''">
						</a>
						<a href="/en" title="english">
							<img src="/images/flag_eng.png" alt="english language" class="grid_1''' + flagen + '''">
						</a>
						<a href="/de" title="deutsch">
							<img src="/images/flag_deu.png" alt="deutch" class="grid_1''' + flagde + '''">
						</a>
					</figure>
					<div class="grid_1 omega">&nbsp;</div>
			</header>
			<div class="clear"></div>
		</div>		
		<div class="container_24">
			<section class="push_3 grid_18">
				<div class="grid_1 alpha">&nbsp;</div>
				<article class="grid_10'''+ imagebg +'''">
'''
def footer(node):
    """Build the footer and return it to a string."""

    (title, description, linkname) = get_page_contents(node)

    html = '''\n</article>'''
    if linkname == 'casa' or linkname == 'haus' or linkname == 'home':
	html += '''<figure class="grid_6"><img alt="ingresso della casa" src="/images/pages/casa_fronte.jpg" title="casa martignilas" class="casa"/></figure>'''
    elif linkname == 'alloggi' or linkname == 'unterkunft' or linkname == 'accomodation':
	html += '''<nav class="grid_3 gallery">
    <ul>
      <li><a href="#pic00"><img src="/images/pages/pic00.jpg" alt=""></a></li>
      <li><a href="#pic01"><img src="/images/pages/pic01.jpg" alt=""></a></li>
      <li><a href="#pic02"><img src="/images/pages/pic02.jpg" alt=""></a></li>
      <li><a href="#pic07"><img src="/images/pages/pic07.jpg" alt=""></a></li>
      <li><a href="#pic08"><img src="/images/pages/pic08.jpg" alt=""></a></li>
      <li><a href="#pic11"><img src="/images/pages/pic11.jpg" alt=""></a></li>
      <li><a href="#pic10"><img src="/images/pages/pic10.jpg" alt=""></a></li>
    </ul>
	</nav>
	<nav class="grid_3 gallery">
    <ul>
      <li><a href="#pic03"><img src="/images/pages/pic03.jpg" alt=""></a></li>
      <li><a href="#pic04"><img src="/images/pages/pic04.jpg" alt=""></a></li>
      <li><a href="#pic05"><img src="/images/pages/pic05.jpg" alt=""></a></li>
      <li><a href="#pic06"><img src="/images/pages/pic06.jpg" alt=""></a></li>
      <li><a href="#pic09"><img src="/images/pages/pic09.jpg" alt=""></a></li>
      <li><a href="#pic12"><img src="/images/pages/pic12.jpg" alt=""></a></li>
      <li><a href="#pic13"><img src="/images/pages/pic13.jpg" alt=""></a></li>
    </ul>
</nav>
<figure>
<ul>
      <li id="pic00"><a href="#home"><img src="/images/pages/pic00.jpg" alt=""></a></li>
      <li id="pic01"><a href="#home"><img src="/images/pages/pic01.jpg" alt=""></a></li>
      <li id="pic02"><a href="#home"><img src="/images/pages/pic02.jpg" alt=""></a></li>
      <li id="pic03"><a href="#home"><img src="/images/pages/pic03.jpg" alt=""></a></li>
      <li id="pic04"><a href="#home"><img src="/images/pages/pic04.jpg" alt=""></a></li>
      <li id="pic05"><a href="#home"><img src="/images/pages/pic05.jpg" alt=""></a></li>
      <li id="pic06"><a href="#home"><img src="/images/pages/pic06.jpg" alt=""></a></li>
      <li id="pic07"><a href="#home"><img src="/images/pages/pic07.jpg" alt=""></a></li>
      <li id="pic08"><a href="#home"><img src="/images/pages/pic08.jpg" alt=""></a></li>
      <li id="pic09"><a href="#home"><img src="/images/pages/pic09.jpg" alt=""></a></li>
      <li id="pic10"><a href="#home"><img src="/images/pages/pic10.jpg" alt=""></a></li>
      <li id="pic11"><a href="#home"><img src="/images/pages/pic11.jpg" alt=""></a></li>
      <li id="pic12"><a href="#home"><img src="/images/pages/pic12.jpg" alt=""></a></li>
      <li id="pic13"><a href="#home"><img src="/images/pages/pic13.jpg" alt=""></a></li>
</ul>
</figure>'''
    elif linkname == 'info':
	html += '''<figure class="grid_6"> <img class="logo" src="/images/pages/mappa_info.png" alt="mappa informazioni"/><img class="logo" src="/images/pages/logo_resia.jpg" alt="logo del comune di resia"/><img class="logo" src="/images/pages/logo_parco.jpg" alt="logo del comune di resia"/></figure>'''
    elif linkname == 'contatti' or linkname == 'kontacte' or linkname == 'contacts':
	html += '''<figure class="grid_6"><iframe width="230px" height="230px" src="https://maps.google.it/maps?q=Resia+UD&amp;hl=it&amp;ie=UTF8&amp;view=map&amp;ftid=0x477a3e21c3cfb9bd:0x8f976dec79701aef&amp;ftt=37&amp;geocode=FR5WwwIdmtvKAA&amp;split=0&amp;sll=46.355998,13.294490&amp;sspn=0.000000,0.000000&amp;hq=&amp;hnear=Resia,+Udine,+Friuli-Venezia+Giulia&amp;ll=46.355998,13.29449&amp;spn=0.015403,0.032015&amp;t=h&amp;output=embed"></iframe></figure>'''
    html += '''<div class="grid_1 omega">&nbsp;</div>
			</section>
			<div class="clear"></div>
		</div>
		<div class="container_24">
			<div class="push_3 grid_18">
				<footer class="prefix_1 grid_16 suffix_1 alpha omega">
				<p>&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name" title="lucapost blog">lucapost</a> | <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license</a> | <a href="/privacy.html">privacy</a> | edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
				</footer>
			</div>
			<div class="clear"></div>
		</div>	
	  	<script src="/js/jquery.js"></script> 
  		<script src="/js/hashgrid.js"></script>
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
