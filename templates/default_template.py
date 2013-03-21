import time
import datetime

SITE_NAME = "martignilas"
DESC = "Casa vacanze in Val Resia"
AUTHOR = "lucapost"
SRC = "/home/lucapost/repo/martignilas.it/src"
DST = "./"
SITEMAP = "sitemap.xml"
URL = "http://martignilas.it"
PREFIX = "/"
HOME = "home"
PATH_SEPARATOR = '/'
SRC_EXT = {"markdown": "md", "textile": "tt", "plain": "txt"}
DST_EXT = "html"
HIDDEN = set(["404.md"])
menu_code = ''
PAGES = {SRC + "/index.md": ("home page", "wireless mesh network libera e decentralizzata in friuli venezia giulia"),
	 SRC + "/30_rete/index.md": ("rete", "esempi di configurazione dei nodi della rete"),
	 SRC + "/30_rete/30_servizi.md": ("rete", "elenco dei servizi disponibili nelle rete"),
	 SRC + "/70_contatti.md": ("contatti", "contattare via email twitter facebook googleplus irc commenti"),
	 SRC + "/50_links.md": ("links", "collegamenti a siti amici")}

current_time = datetime.datetime.now()

def get_page_contents(node):
    """Return page title and description from the global variable pages if a
    match with current node page.src_file is found.
    """ 

    try:
        return (SITE_NAME + ' | ' + PAGES[node.page.src_pathname][0], \
            PAGES[node.page.src_pathname][1])
    except KeyError:
        return ('%%%TITLE%%%', '')

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

    global menu_code

    menu_code += indent + '<ul>\n'
    for child in sorted(node.children, key=lambda n: n.page.src_pathname):
        if child.page.dst_file.startswith("index.") or child.page.src_file in HIDDEN:
            continue
        menu_code += indent + '<li class="level-' + str(child.page.level) + '"><a '
        if(child == cur_node
        or (cur_node.page.dst_file.startswith("index.") and child == cur_node.parent)):
            menu_code += 'class="current" '
        menu_code += 'href="' + node_prefix + child.page.dst_file
        if child.children:
            menu_code += "/index." + DST_EXT + '">'    + child.page.name + '</a>\n'
            menu_(child, cur_node, node_prefix + child.page.dst_file + '/', indent + '\t')
            menu_code += indent + '</li>\n'
        else:
            menu_code += '">'   + child.page.name + '</a></li>\n'
    menu_code += indent + '</ul>\n'

def header(node):
    """Build the header and return it to a string."""

    (title, description) = get_page_contents(node)
    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
        	<meta charset="utf-8" />
<!--		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /> -->
        	<meta name="author" content="''' + AUTHOR + '''" />
	        <meta name="description" content="''' + description + '''" />
        	<title>''' + title + '''</title>
  		<meta name="viewport" content="width=device-width">
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''css/reset.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''css/text.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''css/960.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''css/hashgrid.css" />
		<link rel="stylesheet" type="text/css" media="all" href="'''+ PREFIX +'''css/style.css" />
  		<script src="'''+ PREFIX +'''js/modernizr.js"></script>
		<link rel="icon" type="image/png" href="'''+ PREFIX +'''img/iuliinetlogo.png">
	</head>
	<body id="top">
		<header class="container_12">
			<div class="grid_7"><a href="/" title="home page">
				<hgroup class="rounded">
					<h1>''' + SITE_NAME + '''</h1>
					<h2>''' + DESC + '''</h2>
				</hgroup>
				</a>
			</div>
			<div class="grid_5 clearfix">
				<section id="contact" class="rounded">
					Fraz. Martignilas n.1 <br/>
					33100 Resia, Udine, IT<br/><br/>
					Tel. +39 1234567890<br/>
					Email. pdilena@tin.it<p>
				</section>
			</div>
			<div class="clear"></div>
		</header>		

		<div class="container_12 clearfix">
			<div class="grid_7">
				<section>
					<article class="opacity rounded">
'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''			
					</article>
				</section>
			</div>
			<div class="grid_5">	
				<nav class="rounded navigator">
					''' + menu(node) + '''
				</nav>
				<div class="opacity rounded twitter">
					<a class="twitter-timeline" href="https://twitter.com/lucapost" data-widget-id="311855027230736384">Tweets by @lucapost</a>
					<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
				</div>
			</div>
			<div class="clear"></div>
		</div>
		<div class="container_12 clearfix">
			<footer class="grid_12 rounded">
					<p>&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name" title="lucapost blog">lucapost</a> | <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/">license</a> | <a href="/privacy.html">privacy</a> | edit: ''' + time.strftime("%Y%m%d %I:%M:%S %p", node.page.last_edit) + '''</p>
			</footer>
			<div class="clear"></div>
		</div>	
	  	<script src="'''+ PREFIX +'''js/jquery.js"></script> 
  		<script src="'''+ PREFIX +'''js/hashgrid.js"></script>
	</body>
</html>'''	
