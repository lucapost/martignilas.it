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
SRC_EXT = {"markdown": "md", "textile": "tt"}
DST_EXT = "html"
HIDDEN = set(["404.md", "privacy.md"])
menu_code = ''
PAGES = {SRC + "/01_index.md": ("home", "sito internet della casa vacanze Martignilas"),
	 SRC + "/10_alloggi.md": ("alloggi", "descrizione della casa"),
	 SRC + "/20_informazioni.md": ("informazioni", "eventi e cose da visitare"),
	 SRC + "/30_contatti.md": ("contatti", "comunicare con il propietario")}

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

    global menu_code

    menu_code += indent + '<ul>\n'
    for child in sorted(node.children, key=lambda n: n.page.src_pathname):
        if child.page.src_file in HIDDEN:
            continue
        menu_code += indent + '<li class="level-' + str(child.page.level)
        if(child == cur_node
        or (cur_node.page.dst_file.startswith("index.") and child == cur_node.parent)):
            menu_code += ' current'
        menu_code += '"><a href="' + node_prefix + child.page.dst_file
        if child.children:
            menu_code += "/index." + DST_EXT + '">'    + child.page.name + '</a>\n'
            menu_(child, cur_node, node_prefix + child.page.dst_file + '/', indent + '\t')
            menu_code += indent + '</li>\n'
	else:
	    if child.page.name == 'index':
	        menu_code += '">casa</a></li>\n'
            else:
	        menu_code += '">'   + child.page.name + '</a></li>\n'
    menu_code += indent + '</ul>\n'

def header(node):
    """Build the header and return it to a string."""

    (title, description, linkname) = get_page_contents(node)

    return '''<!DOCTYPE html>
	<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="it"> <![endif]-->
	<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="it"> <![endif]-->
	<!--[if IE 8]>    <html class="no-js lt-ie9" lang="it"> <![endif]-->
	<!--[if gt IE 8]><!--> <html class="no-js" lang="it"> <!--<![endif]-->
	<head>
        	<meta charset="utf-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
		<meta name="googlebot" content="nofollow">
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
		<div class="container_24">
			<header class="push_3 grid_18">
				<hgroup class="prefix_1 grid_7 alpha">
						<a href="/" title="home page">
							<h1>''' + SITE_NAME + '''</h1>
							<h2>''' + DESC + '''</h2>
						</a>
				</hgroup>
				<nav class="suffix_1 grid_9 omega">
						''' + menu(node) + '''
				</nav>
			</header>
			<div class="clear"></div>
		</div>		
		<div class="container_24">
			<div class="push_3 grid_18 '''+ linkname +''' id="box"">
				<section>
					<article class="prefix_1 grid_9 alpha">
'''
def footer(node):
    """Build the footer and return it to a string."""

    return '''				
				</section>
			</div>
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
	  	<script src="'''+ PREFIX +'''js/jquery.js"></script> 
  		<script src="'''+ PREFIX +'''js/hashgrid.js"></script>
	</body>
</html>'''	
