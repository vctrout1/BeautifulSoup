from bs4 import BeautifulSoup

html_doc = '''<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>HTML - Simple English Wikipedia, the free encyclopedia</title>
<script>document.documentElement.className = document.documentElement.className.replace( /(^|\s)client-nojs(\s|$)/, "$1client-js$2" );</script>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"HTML","wgTitle":"HTML","wgCurRevisionId":6284187,"wgRevisionId":6284187,"wgArticleId":3032,"wgIsArticle":true,"wgIsRedirect":false,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Markup languages","Internet","Web design"],"wgBreakFrames":false,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"HTML","wgRelevantArticleId":3032,"wgRequestId":"W-sLgwpAICsAAKJsQ-MAAAAY","wgCSPNonce":false,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":[],"wgCategoryTreePageCategoryOptions":"{\"mode\":0,\"hideprefix\":20,\"showcount\":true,\"namespaces\":false}","wgWikiEditorEnabledModules":[],"wgBetaFeaturesFeatures":[],"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsShouldSendModuleToUser":true,"wgPopupsConflictsWithNavPopupGadget":false,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en","usePageImages":true,"usePageDescriptions":true},"wgMFExpandAllSectionsUserOption":true,"wgMFEnableFontChanger":true,"wgMFDisplayWikibaseDescriptions":{"search":true,"nearby":true,"watchlist":true,"tagline":true},"wgRelatedArticles":null,"wgRelatedArticlesUseCirrusSearch":true,"wgRelatedArticlesOnlyUseCirrusSearch":false,"wgWMESchemaEditAttemptStepOversample":false,"wgULSCurrentAutonym":"English","wgNoticeProject":"wikipedia","wgCentralNoticeCookiesToDelete":[],"wgCentralNoticeCategoriesUsingLegacy":["Fundraising","fundraising"],"wgWikibaseItemId":"Q8811","wgScoreNoteLanguages":{"arabic":"العربية","catalan":"català","deutsch":"Deutsch","english":"English","espanol":"español","italiano":"italiano","nederlands":"Nederlands","norsk":"norsk","portugues":"português","suomi":"suomi","svenska":"svenska","vlaams":"West-Vlams"},"wgScoreDefaultNoteLanguage":"nederlands","wgCentralAuthMobileDomain":false,"wgCodeMirrorEnabled":true,"wgVisualEditorToolbarScrollOffset":0,"wgVisualEditorUnsupportedEditParams":["undo","undoafter","veswitched"],"wgEditSubmitButtonLabelPublish":true});mw.loader.state({"ext.globalCssJs.user.styles":"ready","ext.globalCssJs.site.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","ext.globalCssJs.site":"ready","user":"ready","user.options":"ready","user.tokens":"loading","ext.cite.styles":"ready","ext.pygments":"ready","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","mediawiki.toc.styles":"ready","wikibase.client.init":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","ext.3d.styles":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready"});mw.loader.implement("user.tokens@0tffind",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});RLPAGEMODULES=["ext.cite.a11y","site","mediawiki.page.startup","mediawiki.user","mediawiki.page.ready","jquery.tablesorter","mediawiki.toc","mediawiki.searchSuggest","ext.gadget.ReferenceTooltips","ext.gadget.switcher","ext.centralauth.centralautologin","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging.subscriber","ext.wikimediaEvents","ext.navigationTiming","ext.uls.eventlogger","ext.uls.init","ext.uls.compactlinks","ext.uls.interface","ext.centralNotice.geoIP","ext.centralNotice.startUp","skins.vector.js"];mw.loader.load(RLPAGEMODULES);});</script>
<link rel="stylesheet" href="/w/load.php?debug=false&amp;lang=en&amp;modules=ext.3d.styles%7Cext.cite.styles%7Cext.pygments%2CwikimediaBadges%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cmediawiki.legacy.commonPrint%2Cshared%7Cmediawiki.skinning.interface%7Cmediawiki.toc.styles%7Cskins.vector.styles%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"/>
<script async="" src="/w/load.php?debug=false&amp;lang=en&amp;modules=startup&amp;only=scripts&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/w/load.php?debug=false&amp;lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/>
<meta name="generator" content="MediaWiki 1.33.0-wmf.4"/>
<meta name="referrer" content="origin"/>
<meta name="referrer" content="origin-when-crossorigin"/>
<meta name="referrer" content="origin-when-cross-origin"/>
<link rel="alternate" href="android-app://org.wikipedia/http/simple.m.wikipedia.org/wiki/HTML"/>
<link rel="alternate" type="application/x-wiki" title="change this page" href="/w/index.php?title=HTML&amp;action=edit"/>
<link rel="edit" title="change this page" href="/w/index.php?title=HTML&amp;action=edit"/>
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png"/>
<link rel="shortcut icon" href="/static/favicon/wikipedia.ico"/>
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (en)"/>
<link rel="EditURI" type="application/rsd+xml" href="//simple.wikipedia.org/w/api.php?action=rsd"/>
<link rel="license" href="//creativecommons.org/licenses/by-sa/3.0/"/>
<link rel="canonical" href="https://simple.wikipedia.org/wiki/HTML"/>
<link rel="dns-prefetch" href="//login.wikimedia.org"/>
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<!--[if lt IE 9]><script src="/w/load.php?debug=false&amp;lang=en&amp;modules=html5shiv&amp;only=scripts&amp;skin=vector&amp;sync=1"></script><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-HTML rootpage-HTML skin-vector action-view">		<div id="mw-page-base" class="noprint"></div>
		<div id="mw-head-base" class="noprint"></div>
		<div id="content" class="mw-body" role="main">
			<a id="top"></a>
			<div id="siteNotice" class="mw-body-content"><!-- CentralNotice --></div><div class="mw-indicators mw-body-content">
</div>
<h1 id="firstHeading" class="firstHeading" lang="en">HTML</h1>			<div id="bodyContent" class="mw-body-content">
				<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>				<div id="contentSub"></div>
				<div id="jump-to-nav"></div>				<a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
				<a class="mw-jump-link" href="#p-search">Jump to search</a>
				<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><table class="infobox" style="width:22em"><caption style="font-size:130%; padding-bottom:0.15em;">HTML<br /><span style="font-size:85%;"><span class="nowrap">(HyperText Markup Language)</span></span></caption><tbody><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;"><a href="/wiki/Filename_extension" class="mw-redirect" title="Filename extension">Filename extension</a></th><td style="line-height:1.35em;"><code>.html, .htm</code></td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;"><a href="/w/index.php?title=Media_type&amp;action=edit&amp;redlink=1" class="new" title="Media type (not yet started)">Internet media&#160;type</a></th><td style="line-height:1.35em;"><code>text/html</code></td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;"><a href="/w/index.php?title=Type_code&amp;action=edit&amp;redlink=1" class="new" title="Type code (not yet started)">Type code</a></th><td style="line-height:1.35em;">TEXT</td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;"><a href="/w/index.php?title=Uniform_Type_Identifier&amp;action=edit&amp;redlink=1" class="new" title="Uniform Type Identifier (not yet started)">Uniform Type Identifier&#160;(UTI)</a></th><td style="line-height:1.35em;">public.html</td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;">Developed&#160;by</th><td style="line-height:1.35em;"><a href="/wiki/World_Wide_Web_Consortium" title="World Wide Web Consortium">World Wide Web Consortium</a> &amp; <a href="/w/index.php?title=WHATWG&amp;action=edit&amp;redlink=1" class="new" title="WHATWG (not yet started)">WHATWG</a></td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;">Type of format</th><td style="line-height:1.35em;"><a href="/wiki/Markup_language" title="Markup language">Markup language</a></td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;">Extended&#160;from</th><td style="line-height:1.35em;"><a href="/w/index.php?title=Standard_Generalized_Markup_Language&amp;action=edit&amp;redlink=1" class="new" title="Standard Generalized Markup Language (not yet started)">SGML</a></td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;">Extended&#160;to</th><td style="line-height:1.35em;"><a href="/wiki/XHTML" title="XHTML">XHTML</a></td></tr><tr><th scope="row" style="padding:0.2em 0;line-height:1.2em; padding-right:0.65em;"><a href="/wiki/International_standard" title="International standard">Standard</a></th><td style="line-height:1.35em;">ISO/IEC 15445<br /><a rel="nofollow" class="external text" href="http://www.w3.org/TR/1999/REC-html401-19991224/">W3C HTML 4.01</a><br />
<a rel="nofollow" class="external text" href="http://dev.w3.org/html5/spec/">W3C HTML 5</a> (draft)</td></tr></tbody></table>
<p><br />
<b>HyperText Markup Language</b> (<b>HTML</b>) is a <a href="/wiki/Markup_language" title="Markup language">markup language</a><sup id="cite_ref-1" class="reference"><a href="#cite_note-1">&#91;1&#93;</a></sup> for creating a <a href="/wiki/Webpage" title="Webpage">webpage</a>. Webpages are usually viewed in a <a href="/wiki/Web_browser" title="Web browser">web browser</a>. They can include writing, links, pictures, and even sound and <a href="/wiki/Video" title="Video">video</a>. HTML is used to mark and describe each of these kinds of content so the web browser can display them correctly. HTML can also be used to add meta information to a webpage. Meta information is usually not shown by web browsers and is data <i>about</i> the web page, e.g., the name of the person who created the page. <a href="/wiki/Cascading_Style_Sheets" title="Cascading Style Sheets">Cascading Style Sheets</a> (CSS) is used to style HTML elements while <a href="/wiki/JavaScript" title="JavaScript">JavaScript</a> is used to manipulate HTML elements and CSS styles.
</p><p>HTML was made by the <a href="/wiki/World_Wide_Web_Consortium" title="World Wide Web Consortium">World Wide Web Consortium</a> (W3C). There are several versions of HTML. As of September 2018, the current standard of HTML is dubbed <a href="/wiki/HTML5" class="mw-redirect" title="HTML5">HTML 5</a> and is specifically at version 5.2.
</p>
<div id="toc" class="toc"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none" /><div class="toctitle" lang="en" dir="ltr"><h2>Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Tags"><span class="tocnumber">1</span> <span class="toctext">Tags</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Example"><span class="tocnumber">2</span> <span class="toctext">Example</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Basic_HTML_tags"><span class="tocnumber">3</span> <span class="toctext">Basic HTML tags</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#Other_websites"><span class="tocnumber">4</span> <span class="toctext">Other websites</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#References"><span class="tocnumber">5</span> <span class="toctext">References</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Tags">Tags</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=HTML&amp;veaction=edit&amp;section=1" class="mw-editsection-visualeditor" title="Change section: Tags">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=HTML&amp;action=edit&amp;section=1" title="Change section: Tags">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>HTML uses special bits of programming language called "tags" to let the browser know how a webpage should look. The tags <i>usually</i> come in pairs: an <u>opening</u> tag defines the start of a block of content and an <i>ending</i> tag defines the end of that block of content. There are many different kinds of tags, and each one has a different purpose. See <b>Basic HTML Tags</b> below for tag examples.
</p><p>Some tags only work in certain browsers. For example, the <code>&lt;marquee&gt;</code> tag, which is used to make a bit of writing slide across the page, only works in the <a href="/wiki/Internet_Explorer" title="Internet Explorer">Internet Explorer</a> and <a href="/wiki/Mozilla_Firefox" title="Mozilla Firefox">Mozilla Firefox</a> browsers. Other browsers simply ignore this tag and display the writing normally. Many web page creators avoid using these "non-standard" tags because they want their pages to look the same with all browsers.
</p>
<h2><span class="mw-headline" id="Example">Example</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=HTML&amp;veaction=edit&amp;section=2" class="mw-editsection-visualeditor" title="Change section: Example">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=HTML&amp;action=edit&amp;section=2" title="Change section: Example">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Here is an example page in HTML.
</p>
<div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="lineno"> 1 </span><span class="cp">&lt;!DOCTYPE html&gt;</span>
<span class="lineno"> 2 </span><span class="p">&lt;</span><span class="nt">html</span><span class="p">&gt;</span>
<span class="lineno"> 3 </span>  <span class="p">&lt;</span><span class="nt">head</span><span class="p">&gt;</span>
<span class="lineno"> 4 </span>    <span class="p">&lt;</span><span class="nt">title</span><span class="p">&gt;</span>This is the title of the page.<span class="p">&lt;/</span><span class="nt">title</span><span class="p">&gt;</span>
<span class="lineno"> 5 </span>  <span class="p">&lt;/</span><span class="nt">head</span><span class="p">&gt;</span>
<span class="lineno"> 6 </span>  <span class="p">&lt;</span><span class="nt">body</span> <span class="na">bgcolor</span><span class="o">=</span><span class="s">&quot;gray&quot;</span><span class="p">&gt;</span>
<span class="lineno"> 7 </span>    <span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>This is a paragraph.<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
<span class="lineno"> 8 </span>    <span class="p">&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;https://www.domain.com&quot;</span><span class="p">&gt;</span>This is a link.<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
<span class="lineno"> 9 </span>    <span class="p">&lt;</span><span class="nt">img</span> <span class="na">src</span><span class="o">=</span><span class="s">&quot;image.jpg&quot;</span> <span class="na">alt</span><span class="o">=</span><span class="s">&quot;Image&quot;</span><span class="p">&gt;</span>
<span class="lineno">10 </span>  <span class="p">&lt;/</span><span class="nt">body</span><span class="p">&gt;</span>
<span class="lineno">11 </span><span class="p">&lt;/</span><span class="nt">html</span><span class="p">&gt;</span>
</pre></div>
<h2><span class="mw-headline" id="Basic_HTML_tags">Basic HTML tags</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=HTML&amp;veaction=edit&amp;section=3" class="mw-editsection-visualeditor" title="Change section: Basic HTML tags">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=HTML&amp;action=edit&amp;section=3" title="Change section: Basic HTML tags">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<table class="wikitable sortable">
<tbody><tr>
<th>Tag name
</th>
<th>Name
</th>
<th>Function
</th>
<th>Code Example
</th></tr>
<tr>
<td><code>&lt;!DOCTYPE&gt;</code>
</td>
<td>Doctype
</td>
<td>Defines the Document type
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="cp">&lt;!DOCTYPE html&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;html&gt;</code>
</td>
<td>HTML
</td>
<td>Defines an HTML document
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">html</span><span class="p">&gt;</span>All code<span class="p">&lt;/</span><span class="nt">html</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;head&gt;</code>
</td>
<td>Head
</td>
<td>Contains any code that is not used to display elements on the webpage
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">head</span><span class="p">&gt;&lt;/</span><span class="nt">head</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;title&gt;</code>
</td>
<td>Title
</td>
<td>Defines the title of the webpage (shown on the tab) and is entered within the &lt;head&gt;
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">title</span><span class="p">&gt;</span>Webpage<span class="p">&lt;/</span><span class="nt">title</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;body&gt;</code>
</td>
<td>Body
</td>
<td>Contains the visible elements of the webpage
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">body</span><span class="p">&gt;</span>Html tags<span class="p">&lt;/</span><span class="nt">body</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;h1&gt; to &lt;h6&gt;</code>
</td>
<td>Headings
</td>
<td>Headings of various sizes (&lt;h1&gt; being the largest)
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">h1</span><span class="p">&gt;</span>Heading<span class="p">&lt;/</span><span class="nt">h1</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;p&gt;</code>
</td>
<td>Paragraph
</td>
<td>Defines a paragraph of text
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">p</span><span class="p">&gt;</span>TEXT<span class="p">&lt;/</span><span class="nt">p</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;a&gt;</code>
</td>
<td>Anchor
</td>
<td>Creates active links to other web pages
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">a</span> <span class="na">href</span><span class="o">=</span><span class="s">&quot;www.domain.com&quot;</span><span class="p">&gt;</span>Visit our site<span class="p">&lt;/</span><span class="nt">a</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;img&gt;</code>
</td>
<td>Image
</td>
<td>Displays an image on the page
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">img</span> <span class="na">src</span><span class="o">=</span><span class="s">&quot;ImageUrl&quot;</span> <span class="na">alt</span><span class="o">=</span><span class="s">&quot;Text displayed if image is not available&quot;</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;br&gt;</code>
</td>
<td>Break
</td>
<td>Inserts a single line break
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span>Text <span class="p">&lt;</span><span class="nt">br</span><span class="p">&gt;</span> Text
</pre></div>&#160;
</td></tr>
<tr>
<td><code>&lt;center&gt;</code>
</td>
<td>Center
</td>
<td>Moves content to the center of the page
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">center</span><span class="p">&gt;</span>Code<span class="p">&lt;/</span><span class="nt">center</span><span class="p">&gt;</span>
</pre></div>
</td></tr>
<tr>
<td><code>&lt;script&gt;</code>
</td>
<td>Script
</td>
<td>Creates a script in the webpage, usually written in JavaScript
</td>
<td><div class="mw-highlight mw-content-ltr" dir="ltr"><pre><span></span><span class="p">&lt;</span><span class="nt">script</span><span class="p">&gt;</span><span class="nb">document</span><span class="p">.</span><span class="nx">write</span><span class="p">(</span><span class="s2">&quot;Hello World!&quot;</span><span class="p">)&lt;/</span><span class="nt">script</span><span class="p">&gt;</span>
</pre></div>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Other_websites">Other websites</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=HTML&amp;veaction=edit&amp;section=4" class="mw-editsection-visualeditor" title="Change section: Other websites">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=HTML&amp;action=edit&amp;section=4" title="Change section: Other websites">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a rel="nofollow" class="external text" href="http://www.yourhtmlsource.com/">HTML Source: Beginner's HTML Tutorial</a> - a site of tutorials aimed at web design advanced.</li>
<li><a rel="nofollow" class="external text" href="http://www.htmldog.com/">HTML Dog</a> is a site that helps new writers write good, simple HTML and make it look good with <a href="/wiki/Cascading_Style_Sheets" title="Cascading Style Sheets">CSS</a>.</li>
<li><a rel="nofollow" class="external text" href="http://www.w3schools.com/html/">w3schools</a> a site of web technologies tutorials</li>
<li><a rel="nofollow" class="external text" href="https://digitaldefynd.com/best-html5-css3-certification-course-class-training-tutorial/">HTML5 Certification</a></li></ul>
<h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=HTML&amp;veaction=edit&amp;section=5" class="mw-editsection-visualeditor" title="Change section: References">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=HTML&amp;action=edit&amp;section=5" title="Change section: References">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="reflist" style="list-style-type: decimal;">
<div class="mw-references-wrap"><ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><a href="#cite_ref-1">↑</a></span> <span class="reference-text"><cite class="citation web"><a rel="nofollow" class="external text" href="http://infospace.ischool.syr.edu/2012/04/05/why-html-is-not-a-programming-language/">"Why HTML is Not a Programming Language"</a>. Syracuse University<span class="reference-accessdate">. Retrieved <span class="nowrap">27 June</span> 2016</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Why+HTML+is+Not+a+Programming+Language&amp;rft.pub=Syracuse+University&amp;rft_id=http%3A%2F%2Finfospace.ischool.syr.edu%2F2012%2F04%2F05%2Fwhy-html-is-not-a-programming-language%2F&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3AHTML" class="Z3988"></span><style data-mw-deduplicate="TemplateStyles:r6274847">.mw-parser-output cite.citation{font-style:inherit}.mw-parser-output q{quotes:"\"""\"""'""'"}.mw-parser-output code.cs1-code{color:inherit;background:inherit;border:inherit;padding:inherit}.mw-parser-output .cs1-lock-free a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/6/65/Lock-green.svg/9px-Lock-green.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .cs1-lock-limited a,.mw-parser-output .cs1-lock-registration a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Lock-gray-alt-2.svg/9px-Lock-gray-alt-2.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .cs1-lock-subscription a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lock-red-alt-2.svg/9px-Lock-red-alt-2.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration{color:#555}.mw-parser-output .cs1-subscription span,.mw-parser-output .cs1-registration span{border-bottom:1px dotted;cursor:help}.mw-parser-output .cs1-hidden-error{display:none;font-size:100%}.mw-parser-output .cs1-visible-error{font-size:100%}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration,.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left,.mw-parser-output .cs1-kern-wl-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right,.mw-parser-output .cs1-kern-wl-right{padding-right:0.2em}</style></span>
</li>
</ol></div></div>

<!--
NewPP limit report
Parsed by mw1249
Cached time: 20181125171118
Cache expiry: 1900800
Dynamic content: false
CPU time usage: 0.108 seconds
Real time usage: 0.150 seconds
Preprocessor visited node count: 456/1000000
Preprocessor generated node count: 0/1500000
Post‐expand include size: 7866/2097152 bytes
Template argument size: 615/2097152 bytes
Highest expansion depth: 7/40
Expensive parser function count: 0/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 8534/5000000 bytes
Number of Wikibase entities loaded: 0/400
Lua time usage: 0.051/10.000 seconds
Lua memory usage: 1.47 MB/50 MB
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  121.183      1 -total
 59.36%   71.933      1 Template:Reflist
 50.68%   61.414      1 Template:Cite_web
 35.07%   42.500      1 Template:Infobox_file_format
 31.95%   38.712      1 Template:Infobox
  3.22%    3.904      1 Template:Small
  2.47%    2.989      1 Template:Template_other
  2.25%    2.721      1 Template:Main_other
  1.62%    1.962      1 Template:Nowrap
-->

<!-- Saved in parser cache with key simplewiki:pcache:idhash:3032-0!canonical and timestamp 20181125171118 and revision id 6284187
 -->
</div><noscript><img src="//simple.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" title="" width="1" height="1" style="border: none; position: absolute;" /></noscript></div>					<div class="printfooter">
						Retrieved from "<a dir="ltr" href="https://simple.wikipedia.org/w/index.php?title=HTML&amp;oldid=6284187">https://simple.wikipedia.org/w/index.php?title=HTML&amp;oldid=6284187</a>"					</div>
				<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Special:Categories" title="Special:Categories">Categories</a>: <ul><li><a href="/wiki/Category:Markup_languages" title="Category:Markup languages">Markup languages</a></li><li><a href="/wiki/Category:Internet" title="Category:Internet">Internet</a></li><li><a href="/wiki/Category:Web_design" title="Category:Web design">Web design</a></li></ul></div></div>				<div class="visualClear"></div>
							</div>
		</div>
		<div id="mw-navigation">
			<h2>Navigation menu</h2>
			<div id="mw-head">
									<div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label">
						<h3 id="p-personal-label">Personal tools</h3>
						<ul>
							<li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a href="/wiki/Special:MyTalk" title="Discussion about changes from this IP address [n]" accesskey="n">Talk</a></li><li id="pt-anoncontribs"><a href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]" accesskey="y">Contributions</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=HTML" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=HTML" title="You are encouraged to log in; however, it is not mandatory [o]" accesskey="o">Log in</a></li>						</ul>
					</div>
									<div id="left-navigation">
										<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
						<h3 id="p-namespaces-label">Namespaces</h3>
						<ul>
							<li id="ca-nstab-main" class="selected"><span><a href="/wiki/HTML" title="View the content page [c]" accesskey="c">Page</a></span></li><li id="ca-talk"><span><a href="/wiki/Talk:HTML" rel="discussion" title="Discussion about the content page [t]" accesskey="t">Talk</a></span></li>						</ul>
					</div>
										<div id="p-variants" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-variants-label">
												<input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-variants-label" />
						<h3 id="p-variants-label">
							<span>Variants</span>
						</h3>
						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
									</div>
				<div id="right-navigation">
										<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
						<h3 id="p-views-label">Views</h3>
						<ul>
							<li id="ca-view" class="collapsible selected"><span><a href="/wiki/HTML">Read</a></span></li><li id="ca-ve-edit" class="collapsible"><span><a href="/w/index.php?title=HTML&amp;veaction=edit" title="Edit this page [v]" accesskey="v">Change</a></span></li><li id="ca-edit" class="collapsible"><span><a href="/w/index.php?title=HTML&amp;action=edit" title="You can change this page. Please use the preview button before saving. [e]" accesskey="e">Change source</a></span></li><li id="ca-history" class="collapsible"><span><a href="/w/index.php?title=HTML&amp;action=history" title="Past revisions of this page [h]" accesskey="h">View history</a></span></li>						</ul>
					</div>
										<div id="p-cactions" role="navigation" class="vectorMenu emptyPortlet" aria-labelledby="p-cactions-label">
						<input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-cactions-label" />
						<h3 id="p-cactions-label"><span>More</span></h3>
						<div class="menu">
							<ul>
															</ul>
						</div>
					</div>
										<div id="p-search" role="search">
						<h3>
							<label for="searchInput">Search</label>
						</h3>
						<form action="/w/index.php" id="searchform">
							<div id="simpleSearch">
								<input type="search" name="search" placeholder="Search Wikipedia" title="Search Wikipedia [f]" accesskey="f" id="searchInput"/><input type="hidden" value="Special:Search" name="title"/><input type="submit" name="fulltext" value="Search" title="Search the pages for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton"/><input type="submit" name="go" value="Go" title="Go to a page with this exact name if it exists" id="searchButton" class="searchButton"/>							</div>
						</form>
					</div>
									</div>
			</div>
			<div id="mw-panel">
				<div id="p-logo" role="banner"><a class="mw-wiki-logo" href="/wiki/Main_Page"  title="Visit the main page"></a></div>
						<div class="portal" role="navigation" id="p-navigation" aria-labelledby="p-navigation-label">
			<h3 id="p-navigation-label">Getting around</h3>
			<div class="body">
								<ul>
					<li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li><li id="n-portal"><a href="/wiki/Wikipedia:Simple_start" title="About the project, what you can do, where to find things">Simple start</a></li><li id="n-Simple-talk"><a href="/wiki/Wikipedia:Simple_talk">Simple talk</a></li><li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="The list of new changes in the wiki. [r]" accesskey="r">New changes</a></li><li id="n-randompage"><a href="/wiki/Special:Random" title="Show any page [x]" accesskey="x">Show any page</a></li><li id="n-help"><a href="/wiki/Help:Contents" title="The place to get help">Help</a></li><li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_simple.wikipedia.org&amp;uselang=en" title="Support us">Give to Wikipedia</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-coll-print_export" aria-labelledby="p-coll-print_export-label">
			<h3 id="p-coll-print_export-label">Print/export</h3>
			<div class="body">
								<ul>
					<li id="coll-create_a_book"><a href="/w/index.php?title=Special:Book&amp;bookcmd=book_creator&amp;referer=HTML">Make a book</a></li><li id="coll-download-as-rdf2latex"><a href="/w/index.php?title=Special:ElectronPdf&amp;page=HTML&amp;action=show-download-screen">Download as PDF</a></li><li id="t-print"><a href="/w/index.php?title=HTML&amp;printable=yes" title="Printable version of this page [p]" accesskey="p">Page for printing</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-wikibase-otherprojects" aria-labelledby="p-wikibase-otherprojects-label">
			<h3 id="p-wikibase-otherprojects-label">In other projects</h3>
			<div class="body">
								<ul>
					<li class="wb-otherproject-link wb-otherproject-commons"><a href="https://commons.wikimedia.org/wiki/Category:HTML" hreflang="en">Wikimedia Commons</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-tb" aria-labelledby="p-tb-label">
			<h3 id="p-tb-label">Tools</h3>
			<div class="body">
								<ul>
					<li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/HTML" title="A list of all wiki pages that link here [j]" accesskey="j">What links here</a></li><li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/HTML" rel="nofollow" title="New changes in pages linked from this page [k]" accesskey="k">Related changes</a></li><li id="t-upload"><a href="//commons.wikimedia.org/wiki/Special:UploadWizard" title="Upload files [u]" accesskey="u">Upload file</a></li><li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li><li id="t-permalink"><a href="/w/index.php?title=HTML&amp;oldid=6284187" title="Permanent link to this revision of the page">Permanent link</a></li><li id="t-info"><a href="/w/index.php?title=HTML&amp;action=info" title="More information about this page">Page information</a></li><li id="t-wikibase"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q8811" title="Link to connected data repository item [g]" accesskey="g">Wikidata item</a></li><li id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=HTML&amp;id=6284187" title="Information on how to cite this page">Cite this page</a></li>				</ul>
							</div>
		</div>
			<div class="portal" role="navigation" id="p-lang" aria-labelledby="p-lang-label">
			<h3 id="p-lang-label">In other languages</h3>
			<div class="body">
								<ul>
					<li class="interlanguage-link interwiki-af"><a href="https://af.wikipedia.org/wiki/HTML" title="HTML – Afrikaans" lang="af" hreflang="af" class="interlanguage-link-target">Afrikaans</a></li><li class="interlanguage-link interwiki-als"><a href="https://als.wikipedia.org/wiki/HTML" title="HTML – Alemannisch" lang="gsw" hreflang="gsw" class="interlanguage-link-target">Alemannisch</a></li><li class="interlanguage-link interwiki-ang"><a href="https://ang.wikipedia.org/wiki/Oferwrit_mearc_gereord" title="Oferwrit mearc gereord – Old English" lang="ang" hreflang="ang" class="interlanguage-link-target">Ænglisc</a></li><li class="interlanguage-link interwiki-ar"><a href="https://ar.wikipedia.org/wiki/%D9%84%D8%BA%D8%A9_%D8%AA%D8%B1%D9%85%D9%8A%D8%B2_%D8%A7%D9%84%D9%86%D8%B5_%D8%A7%D9%84%D9%81%D8%A7%D8%A6%D9%82" title="لغة ترميز النص الفائق – Arabic" lang="ar" hreflang="ar" class="interlanguage-link-target">العربية</a></li><li class="interlanguage-link interwiki-an"><a href="https://an.wikipedia.org/wiki/HTML" title="HTML – Aragonese" lang="an" hreflang="an" class="interlanguage-link-target">Aragonés</a></li><li class="interlanguage-link interwiki-ast"><a href="https://ast.wikipedia.org/wiki/HTML" title="HTML – Asturian" lang="ast" hreflang="ast" class="interlanguage-link-target">Asturianu</a></li><li class="interlanguage-link interwiki-az"><a href="https://az.wikipedia.org/wiki/HTML" title="HTML – Azerbaijani" lang="az" hreflang="az" class="interlanguage-link-target">Azərbaycanca</a></li><li class="interlanguage-link interwiki-azb"><a href="https://azb.wikipedia.org/wiki/%D8%A7%DA%86_%D8%AA%DB%8C_%D8%A7%D9%85_%D8%A7%D9%84" title="اچ تی ام ال – South Azerbaijani" lang="azb" hreflang="azb" class="interlanguage-link-target">تۆرکجه</a></li><li class="interlanguage-link interwiki-bn"><a href="https://bn.wikipedia.org/wiki/%E0%A6%8F%E0%A6%87%E0%A6%9A%E0%A6%9F%E0%A6%BF%E0%A6%8F%E0%A6%AE%E0%A6%8F%E0%A6%B2" title="এইচটিএমএল – Bangla" lang="bn" hreflang="bn" class="interlanguage-link-target">বাংলা</a></li><li class="interlanguage-link interwiki-zh-min-nan"><a href="https://zh-min-nan.wikipedia.org/wiki/HTML" title="HTML – Chinese (Min Nan)" lang="nan" hreflang="nan" class="interlanguage-link-target">Bân-lâm-gú</a></li><li class="interlanguage-link interwiki-ba"><a href="https://ba.wikipedia.org/wiki/HTML" title="HTML – Bashkir" lang="ba" hreflang="ba" class="interlanguage-link-target">Башҡортса</a></li><li class="interlanguage-link interwiki-be"><a href="https://be.wikipedia.org/wiki/HTML" title="HTML – Belarusian" lang="be" hreflang="be" class="interlanguage-link-target">Беларуская</a></li><li class="interlanguage-link interwiki-be-x-old"><a href="https://be-x-old.wikipedia.org/wiki/HTML" title="HTML – Belarusian (Taraškievica orthography)" lang="be-tarask" hreflang="be-tarask" class="interlanguage-link-target">Беларуская (тарашкевіца)‎</a></li><li class="interlanguage-link interwiki-bg"><a href="https://bg.wikipedia.org/wiki/HTML" title="HTML – Bulgarian" lang="bg" hreflang="bg" class="interlanguage-link-target">Български</a></li><li class="interlanguage-link interwiki-bar"><a href="https://bar.wikipedia.org/wiki/HTML" title="HTML – Bavarian" lang="bar" hreflang="bar" class="interlanguage-link-target">Boarisch</a></li><li class="interlanguage-link interwiki-bs"><a href="https://bs.wikipedia.org/wiki/HTML" title="HTML – Bosnian" lang="bs" hreflang="bs" class="interlanguage-link-target">Bosanski</a></li><li class="interlanguage-link interwiki-br"><a href="https://br.wikipedia.org/wiki/HTML" title="HTML – Breton" lang="br" hreflang="br" class="interlanguage-link-target">Brezhoneg</a></li><li class="interlanguage-link interwiki-ca"><a href="https://ca.wikipedia.org/wiki/Hyper_Text_Markup_Language" title="Hyper Text Markup Language – Catalan" lang="ca" hreflang="ca" class="interlanguage-link-target">Català</a></li><li class="interlanguage-link interwiki-cv"><a href="https://cv.wikipedia.org/wiki/HTML" title="HTML – Chuvash" lang="cv" hreflang="cv" class="interlanguage-link-target">Чӑвашла</a></li><li class="interlanguage-link interwiki-cs"><a href="https://cs.wikipedia.org/wiki/Hypertext_Markup_Language" title="Hypertext Markup Language – Czech" lang="cs" hreflang="cs" class="interlanguage-link-target">Čeština</a></li><li class="interlanguage-link interwiki-co"><a href="https://co.wikipedia.org/wiki/HTML" title="HTML – Corsican" lang="co" hreflang="co" class="interlanguage-link-target">Corsu</a></li><li class="interlanguage-link interwiki-cy"><a href="https://cy.wikipedia.org/wiki/HTML" title="HTML – Welsh" lang="cy" hreflang="cy" class="interlanguage-link-target">Cymraeg</a></li><li class="interlanguage-link interwiki-da"><a href="https://da.wikipedia.org/wiki/HTML" title="HTML – Danish" lang="da" hreflang="da" class="interlanguage-link-target">Dansk</a></li><li class="interlanguage-link interwiki-se"><a href="https://se.wikipedia.org/wiki/HTML" title="HTML – Northern Sami" lang="se" hreflang="se" class="interlanguage-link-target">Davvisámegiella</a></li><li class="interlanguage-link interwiki-de"><a href="https://de.wikipedia.org/wiki/Hypertext_Markup_Language" title="Hypertext Markup Language – German" lang="de" hreflang="de" class="interlanguage-link-target">Deutsch</a></li><li class="interlanguage-link interwiki-dsb"><a href="https://dsb.wikipedia.org/wiki/HTML" title="HTML – Lower Sorbian" lang="dsb" hreflang="dsb" class="interlanguage-link-target">Dolnoserbski</a></li><li class="interlanguage-link interwiki-et"><a href="https://et.wikipedia.org/wiki/HTML" title="HTML – Estonian" lang="et" hreflang="et" class="interlanguage-link-target">Eesti</a></li><li class="interlanguage-link interwiki-el"><a href="https://el.wikipedia.org/wiki/HTML" title="HTML – Greek" lang="el" hreflang="el" class="interlanguage-link-target">Ελληνικά</a></li><li class="interlanguage-link interwiki-en"><a href="https://en.wikipedia.org/wiki/HTML" title="HTML – English" lang="en" hreflang="en" class="interlanguage-link-target">English</a></li><li class="interlanguage-link interwiki-es"><a href="https://es.wikipedia.org/wiki/HTML" title="HTML – Spanish" lang="es" hreflang="es" class="interlanguage-link-target">Español</a></li><li class="interlanguage-link interwiki-eo"><a href="https://eo.wikipedia.org/wiki/HTML" title="HTML – Esperanto" lang="eo" hreflang="eo" class="interlanguage-link-target">Esperanto</a></li><li class="interlanguage-link interwiki-eu"><a href="https://eu.wikipedia.org/wiki/HTML" title="HTML – Basque" lang="eu" hreflang="eu" class="interlanguage-link-target">Euskara</a></li><li class="interlanguage-link interwiki-fa"><a href="https://fa.wikipedia.org/wiki/%D8%A7%DA%86%E2%80%8C%D8%AA%DB%8C%E2%80%8C%D8%A7%D9%85%E2%80%8C%D8%A7%D9%84" title="اچ‌تی‌ام‌ال – Persian" lang="fa" hreflang="fa" class="interlanguage-link-target">فارسی</a></li><li class="interlanguage-link interwiki-hif"><a href="https://hif.wikipedia.org/wiki/HTML" title="HTML – Fiji Hindi" lang="hif" hreflang="hif" class="interlanguage-link-target">Fiji Hindi</a></li><li class="interlanguage-link interwiki-fo"><a href="https://fo.wikipedia.org/wiki/HTML" title="HTML – Faroese" lang="fo" hreflang="fo" class="interlanguage-link-target">Føroyskt</a></li><li class="interlanguage-link interwiki-fr"><a href="https://fr.wikipedia.org/wiki/Hypertext_Markup_Language" title="Hypertext Markup Language – French" lang="fr" hreflang="fr" class="interlanguage-link-target">Français</a></li><li class="interlanguage-link interwiki-fy"><a href="https://fy.wikipedia.org/wiki/HTML" title="HTML – Western Frisian" lang="fy" hreflang="fy" class="interlanguage-link-target">Frysk</a></li><li class="interlanguage-link interwiki-fur"><a href="https://fur.wikipedia.org/wiki/HTML" title="HTML – Friulian" lang="fur" hreflang="fur" class="interlanguage-link-target">Furlan</a></li><li class="interlanguage-link interwiki-ga"><a href="https://ga.wikipedia.org/wiki/HTML" title="HTML – Irish" lang="ga" hreflang="ga" class="interlanguage-link-target">Gaeilge</a></li><li class="interlanguage-link interwiki-gd"><a href="https://gd.wikipedia.org/wiki/HTML" title="HTML – Scottish Gaelic" lang="gd" hreflang="gd" class="interlanguage-link-target">Gàidhlig</a></li><li class="interlanguage-link interwiki-gl"><a href="https://gl.wikipedia.org/wiki/HTML" title="HTML – Galician" lang="gl" hreflang="gl" class="interlanguage-link-target">Galego</a></li><li class="interlanguage-link interwiki-glk"><a href="https://glk.wikipedia.org/wiki/%D8%A6%DA%86.%D8%AA%D9%8A.%D8%A6%D9%85.%D8%A6%D9%84" title="ئچ.تي.ئم.ئل – Gilaki" lang="glk" hreflang="glk" class="interlanguage-link-target">گیلکی</a></li><li class="interlanguage-link interwiki-ko"><a href="https://ko.wikipedia.org/wiki/HTML" title="HTML – Korean" lang="ko" hreflang="ko" class="interlanguage-link-target">한국어</a></li><li class="interlanguage-link interwiki-hy"><a href="https://hy.wikipedia.org/wiki/HTML" title="HTML – Armenian" lang="hy" hreflang="hy" class="interlanguage-link-target">Հայերեն</a></li><li class="interlanguage-link interwiki-hi"><a href="https://hi.wikipedia.org/wiki/%E0%A4%8F%E0%A4%9A%E0%A4%9F%E0%A5%80%E0%A4%8F%E0%A4%AE%E0%A4%8F%E0%A4%B2" title="एचटीएमएल – Hindi" lang="hi" hreflang="hi" class="interlanguage-link-target">हिन्दी</a></li><li class="interlanguage-link interwiki-hsb"><a href="https://hsb.wikipedia.org/wiki/HTML" title="HTML – Upper Sorbian" lang="hsb" hreflang="hsb" class="interlanguage-link-target">Hornjoserbsce</a></li><li class="interlanguage-link interwiki-hr"><a href="https://hr.wikipedia.org/wiki/HTML" title="HTML – Croatian" lang="hr" hreflang="hr" class="interlanguage-link-target">Hrvatski</a></li><li class="interlanguage-link interwiki-id"><a href="https://id.wikipedia.org/wiki/HTML" title="HTML – Indonesian" lang="id" hreflang="id" class="interlanguage-link-target">Bahasa Indonesia</a></li><li class="interlanguage-link interwiki-ia"><a href="https://ia.wikipedia.org/wiki/HTML" title="HTML – Interlingua" lang="ia" hreflang="ia" class="interlanguage-link-target">Interlingua</a></li><li class="interlanguage-link interwiki-is"><a href="https://is.wikipedia.org/wiki/HTML" title="HTML – Icelandic" lang="is" hreflang="is" class="interlanguage-link-target">Íslenska</a></li><li class="interlanguage-link interwiki-it"><a href="https://it.wikipedia.org/wiki/HTML" title="HTML – Italian" lang="it" hreflang="it" class="interlanguage-link-target">Italiano</a></li><li class="interlanguage-link interwiki-he"><a href="https://he.wikipedia.org/wiki/HTML" title="HTML – Hebrew" lang="he" hreflang="he" class="interlanguage-link-target">עברית</a></li><li class="interlanguage-link interwiki-jv"><a href="https://jv.wikipedia.org/wiki/Hypertext_markup_language" title="Hypertext markup language – Javanese" lang="jv" hreflang="jv" class="interlanguage-link-target">Basa Jawa</a></li><li class="interlanguage-link interwiki-ka"><a href="https://ka.wikipedia.org/wiki/%E1%83%B0%E1%83%98%E1%83%9E%E1%83%94%E1%83%A0%E1%83%A2%E1%83%94%E1%83%A5%E1%83%A1%E1%83%A2%E1%83%A3%E1%83%A0%E1%83%98_%E1%83%9B%E1%83%90%E1%83%A0%E1%83%99%E1%83%98%E1%83%A0%E1%83%94%E1%83%91%E1%83%98%E1%83%A1_%E1%83%94%E1%83%9C%E1%83%90" title="ჰიპერტექსტური მარკირების ენა – Georgian" lang="ka" hreflang="ka" class="interlanguage-link-target">ქართული</a></li><li class="interlanguage-link interwiki-kk"><a href="https://kk.wikipedia.org/wiki/HTML" title="HTML – Kazakh" lang="kk" hreflang="kk" class="interlanguage-link-target">Қазақша</a></li><li class="interlanguage-link interwiki-sw"><a href="https://sw.wikipedia.org/wiki/HTML" title="HTML – Swahili" lang="sw" hreflang="sw" class="interlanguage-link-target">Kiswahili</a></li><li class="interlanguage-link interwiki-ku"><a href="https://ku.wikipedia.org/wiki/HTML" title="HTML – Kurdish" lang="ku" hreflang="ku" class="interlanguage-link-target">Kurdî</a></li><li class="interlanguage-link interwiki-ky"><a href="https://ky.wikipedia.org/wiki/HTML" title="HTML – Kyrgyz" lang="ky" hreflang="ky" class="interlanguage-link-target">Кыргызча</a></li><li class="interlanguage-link interwiki-ltg"><a href="https://ltg.wikipedia.org/wiki/HTML" title="HTML – Latgalian" lang="ltg" hreflang="ltg" class="interlanguage-link-target">Latgaļu</a></li><li class="interlanguage-link interwiki-lv"><a href="https://lv.wikipedia.org/wiki/HTML" title="HTML – Latvian" lang="lv" hreflang="lv" class="interlanguage-link-target">Latviešu</a></li><li class="interlanguage-link interwiki-lb"><a href="https://lb.wikipedia.org/wiki/Hypertext_Markup_Language" title="Hypertext Markup Language – Luxembourgish" lang="lb" hreflang="lb" class="interlanguage-link-target">Lëtzebuergesch</a></li><li class="interlanguage-link interwiki-lt"><a href="https://lt.wikipedia.org/wiki/HTML" title="HTML – Lithuanian" lang="lt" hreflang="lt" class="interlanguage-link-target">Lietuvių</a></li><li class="interlanguage-link interwiki-lij"><a href="https://lij.wikipedia.org/wiki/HTML" title="HTML – Ligurian" lang="lij" hreflang="lij" class="interlanguage-link-target">Ligure</a></li><li class="interlanguage-link interwiki-lfn"><a href="https://lfn.wikipedia.org/wiki/HTML" title="HTML – Lingua Franca Nova" lang="lfn" hreflang="lfn" class="interlanguage-link-target">Lingua Franca Nova</a></li><li class="interlanguage-link interwiki-lmo"><a href="https://lmo.wikipedia.org/wiki/HTML" title="HTML – Lombard" lang="lmo" hreflang="lmo" class="interlanguage-link-target">Lumbaart</a></li><li class="interlanguage-link interwiki-hu"><a href="https://hu.wikipedia.org/wiki/HTML" title="HTML – Hungarian" lang="hu" hreflang="hu" class="interlanguage-link-target">Magyar</a></li><li class="interlanguage-link interwiki-mk"><a href="https://mk.wikipedia.org/wiki/HTML" title="HTML – Macedonian" lang="mk" hreflang="mk" class="interlanguage-link-target">Македонски</a></li><li class="interlanguage-link interwiki-mg"><a href="https://mg.wikipedia.org/wiki/Hypertext_Markup_Language" title="Hypertext Markup Language – Malagasy" lang="mg" hreflang="mg" class="interlanguage-link-target">Malagasy</a></li><li class="interlanguage-link interwiki-ml"><a href="https://ml.wikipedia.org/wiki/%E0%B4%8E%E0%B4%9A%E0%B5%8D.%E0%B4%9F%E0%B4%BF.%E0%B4%8E%E0%B4%82.%E0%B4%8E%E0%B5%BD." title="എച്.ടി.എം.എൽ. – Malayalam" lang="ml" hreflang="ml" class="interlanguage-link-target">മലയാളം</a></li><li class="interlanguage-link interwiki-mr"><a href="https://mr.wikipedia.org/wiki/%E0%A4%8F%E0%A4%9A.%E0%A4%9F%E0%A5%80.%E0%A4%8F%E0%A4%AE.%E0%A4%8F%E0%A4%B2." title="एच.टी.एम.एल. – Marathi" lang="mr" hreflang="mr" class="interlanguage-link-target">मराठी</a></li><li class="interlanguage-link interwiki-ms"><a href="https://ms.wikipedia.org/wiki/HTML" title="HTML – Malay" lang="ms" hreflang="ms" class="interlanguage-link-target">Bahasa Melayu</a></li><li class="interlanguage-link interwiki-cdo"><a href="https://cdo.wikipedia.org/wiki/HTML" title="HTML – Min Dong Chinese" lang="cdo" hreflang="cdo" class="interlanguage-link-target">Mìng-dĕ̤ng-ngṳ̄</a></li><li class="interlanguage-link interwiki-mn"><a href="https://mn.wikipedia.org/wiki/HTML" title="HTML – Mongolian" lang="mn" hreflang="mn" class="interlanguage-link-target">Монгол</a></li><li class="interlanguage-link interwiki-my"><a href="https://my.wikipedia.org/wiki/HTML" title="HTML – Burmese" lang="my" hreflang="my" class="interlanguage-link-target">မြန်မာဘာသာ</a></li><li class="interlanguage-link interwiki-nl"><a href="https://nl.wikipedia.org/wiki/HyperText_Markup_Language" title="HyperText Markup Language – Dutch" lang="nl" hreflang="nl" class="interlanguage-link-target">Nederlands</a></li><li class="interlanguage-link interwiki-ne"><a href="https://ne.wikipedia.org/wiki/%E0%A4%8F%E0%A4%9A.%E0%A4%9F%E0%A5%80.%E0%A4%8F%E0%A4%AE.%E0%A4%8F%E0%A4%B2." title="एच.टी.एम.एल. – Nepali" lang="ne" hreflang="ne" class="interlanguage-link-target">नेपाली</a></li><li class="interlanguage-link interwiki-new"><a href="https://new.wikipedia.org/wiki/%E0%A4%8F%E0%A4%9A_%E0%A4%9F%E0%A5%80_%E0%A4%8F%E0%A4%AE%E0%A5%8D_%E0%A4%8F%E0%A4%B2%E0%A5%8D" title="एच टी एम् एल् – Newari" lang="new" hreflang="new" class="interlanguage-link-target">नेपाल भाषा</a></li><li class="interlanguage-link interwiki-ja"><a href="https://ja.wikipedia.org/wiki/HyperText_Markup_Language" title="HyperText Markup Language – Japanese" lang="ja" hreflang="ja" class="interlanguage-link-target">日本語</a></li><li class="interlanguage-link interwiki-ce"><a href="https://ce.wikipedia.org/wiki/HTML" title="HTML – Chechen" lang="ce" hreflang="ce" class="interlanguage-link-target">Нохчийн</a></li><li class="interlanguage-link interwiki-no"><a href="https://no.wikipedia.org/wiki/HTML" title="HTML – Norwegian" lang="no" hreflang="no" class="interlanguage-link-target">Norsk</a></li><li class="interlanguage-link interwiki-nn"><a href="https://nn.wikipedia.org/wiki/HTML" title="HTML – Norwegian Nynorsk" lang="nn" hreflang="nn" class="interlanguage-link-target">Norsk nynorsk</a></li><li class="interlanguage-link interwiki-mhr"><a href="https://mhr.wikipedia.org/wiki/HTML" title="HTML – Eastern Mari" lang="mhr" hreflang="mhr" class="interlanguage-link-target">Олык марий</a></li><li class="interlanguage-link interwiki-uz"><a href="https://uz.wikipedia.org/wiki/HTML" title="HTML – Uzbek" lang="uz" hreflang="uz" class="interlanguage-link-target">Oʻzbekcha/ўзбекча</a></li><li class="interlanguage-link interwiki-pa"><a href="https://pa.wikipedia.org/wiki/%E0%A8%90%E0%A8%9A.%E0%A8%9F%E0%A9%80.%E0%A8%90%E0%A8%AE.%E0%A8%90%E0%A8%B2" title="ਐਚ.ਟੀ.ਐਮ.ਐਲ – Punjabi" lang="pa" hreflang="pa" class="interlanguage-link-target">ਪੰਜਾਬੀ</a></li><li class="interlanguage-link interwiki-km"><a href="https://km.wikipedia.org/wiki/HTML" title="HTML – Khmer" lang="km" hreflang="km" class="interlanguage-link-target">ភាសាខ្មែរ</a></li><li class="interlanguage-link interwiki-pl"><a href="https://pl.wikipedia.org/wiki/HTML" title="HTML – Polish" lang="pl" hreflang="pl" class="interlanguage-link-target">Polski</a></li><li class="interlanguage-link interwiki-pt"><a href="https://pt.wikipedia.org/wiki/HTML" title="HTML – Portuguese" lang="pt" hreflang="pt" class="interlanguage-link-target">Português</a></li><li class="interlanguage-link interwiki-kaa"><a href="https://kaa.wikipedia.org/wiki/HTML" title="HTML – Kara-Kalpak" lang="kaa" hreflang="kaa" class="interlanguage-link-target">Qaraqalpaqsha</a></li><li class="interlanguage-link interwiki-ro"><a href="https://ro.wikipedia.org/wiki/HyperText_Markup_Language" title="HyperText Markup Language – Romanian" lang="ro" hreflang="ro" class="interlanguage-link-target">Română</a></li><li class="interlanguage-link interwiki-rue"><a href="https://rue.wikipedia.org/wiki/HTML" title="HTML – Rusyn" lang="rue" hreflang="rue" class="interlanguage-link-target">Русиньскый</a></li><li class="interlanguage-link interwiki-ru"><a href="https://ru.wikipedia.org/wiki/HTML" title="HTML – Russian" lang="ru" hreflang="ru" class="interlanguage-link-target">Русский</a></li><li class="interlanguage-link interwiki-sco"><a href="https://sco.wikipedia.org/wiki/HTML" title="HTML – Scots" lang="sco" hreflang="sco" class="interlanguage-link-target">Scots</a></li><li class="interlanguage-link interwiki-sq"><a href="https://sq.wikipedia.org/wiki/HTML" title="HTML – Albanian" lang="sq" hreflang="sq" class="interlanguage-link-target">Shqip</a></li><li class="interlanguage-link interwiki-si"><a href="https://si.wikipedia.org/wiki/%E0%B6%91%E0%B6%A0%E0%B7%8A%E0%B6%A7%E0%B7%93%E0%B6%91%E0%B6%B8%E0%B7%8A%E0%B6%91%E0%B6%BD%E0%B7%8A" title="එච්ටීඑම්එල් – Sinhala" lang="si" hreflang="si" class="interlanguage-link-target">සිංහල</a></li><li class="interlanguage-link interwiki-sd"><a href="https://sd.wikipedia.org/wiki/%D9%87%D8%A7%D8%A6%D9%BE%D8%B1_%D9%BD%D9%8A%DA%AA%D8%B3%D9%BD_%D9%85%D8%A7%D8%B1%DA%AA_%D8%A7%D9%BE_%D9%84%D9%8A%D9%86%DA%AF%D9%88%D9%8A%D8%AC" title="هائپر ٽيڪسٽ مارڪ اپ لينگويج – Sindhi" lang="sd" hreflang="sd" class="interlanguage-link-target">سنڌي</a></li><li class="interlanguage-link interwiki-sk"><a href="https://sk.wikipedia.org/wiki/Hypertextov%C3%BD_zna%C4%8Dkov%C3%BD_jazyk" title="Hypertextový značkový jazyk – Slovak" lang="sk" hreflang="sk" class="interlanguage-link-target">Slovenčina</a></li><li class="interlanguage-link interwiki-sl"><a href="https://sl.wikipedia.org/wiki/HTML" title="HTML – Slovenian" lang="sl" hreflang="sl" class="interlanguage-link-target">Slovenščina</a></li><li class="interlanguage-link interwiki-so"><a href="https://so.wikipedia.org/wiki/HTML" title="HTML – Somali" lang="so" hreflang="so" class="interlanguage-link-target">Soomaaliga</a></li><li class="interlanguage-link interwiki-ckb"><a href="https://ckb.wikipedia.org/wiki/%D8%A6%DB%95%DB%8C%DA%86_%D8%AA%DB%8C_%D8%A6%DB%8E%D9%85_%D8%A6%DB%8E%DA%B5" title="ئەیچ تی ئێم ئێڵ – Central Kurdish" lang="ckb" hreflang="ckb" class="interlanguage-link-target">کوردی</a></li><li class="interlanguage-link interwiki-sr"><a href="https://sr.wikipedia.org/wiki/HTML" title="HTML – Serbian" lang="sr" hreflang="sr" class="interlanguage-link-target">Српски / srpski</a></li><li class="interlanguage-link interwiki-sh"><a href="https://sh.wikipedia.org/wiki/HTML" title="HTML – Serbo-Croatian" lang="sh" hreflang="sh" class="interlanguage-link-target">Srpskohrvatski / српскохрватски</a></li><li class="interlanguage-link interwiki-fi"><a href="https://fi.wikipedia.org/wiki/HTML" title="HTML – Finnish" lang="fi" hreflang="fi" class="interlanguage-link-target">Suomi</a></li><li class="interlanguage-link interwiki-sv"><a href="https://sv.wikipedia.org/wiki/HTML" title="HTML – Swedish" lang="sv" hreflang="sv" class="interlanguage-link-target">Svenska</a></li><li class="interlanguage-link interwiki-tl"><a href="https://tl.wikipedia.org/wiki/HTML" title="HTML – Tagalog" lang="tl" hreflang="tl" class="interlanguage-link-target">Tagalog</a></li><li class="interlanguage-link interwiki-ta"><a href="https://ta.wikipedia.org/wiki/%E0%AE%AE%E0%AF%80%E0%AE%AF%E0%AF%81%E0%AE%B0%E0%AF%88%E0%AE%95%E0%AF%8D_%E0%AE%95%E0%AF%81%E0%AE%B1%E0%AE%BF%E0%AE%AF%E0%AE%BF%E0%AE%9F%E0%AF%81_%E0%AE%AE%E0%AF%8A%E0%AE%B4%E0%AE%BF" title="மீயுரைக் குறியிடு மொழி – Tamil" lang="ta" hreflang="ta" class="interlanguage-link-target">தமிழ்</a></li><li class="interlanguage-link interwiki-te"><a href="https://te.wikipedia.org/wiki/%E0%B0%B9%E0%B1%86%E0%B0%9A%E0%B1%8D%E2%80%8C%E0%B0%9F%E0%B0%BF%E0%B0%8E%E0%B0%AE%E0%B1%8D%E0%B0%8E%E0%B0%B2%E0%B1%8D(HTML)" title="హెచ్‌టిఎమ్ఎల్(HTML) – Telugu" lang="te" hreflang="te" class="interlanguage-link-target">తెలుగు</a></li><li class="interlanguage-link interwiki-th"><a href="https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%AD%E0%B8%8A%E0%B8%97%E0%B8%B5%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%A1%E0%B9%81%E0%B8%AD%E0%B8%A5" title="เอชทีเอ็มแอล – Thai" lang="th" hreflang="th" class="interlanguage-link-target">ไทย</a></li><li class="interlanguage-link interwiki-tg"><a href="https://tg.wikipedia.org/wiki/HTML" title="HTML – Tajik" lang="tg" hreflang="tg" class="interlanguage-link-target">Тоҷикӣ</a></li><li class="interlanguage-link interwiki-tr"><a href="https://tr.wikipedia.org/wiki/HTML" title="HTML – Turkish" lang="tr" hreflang="tr" class="interlanguage-link-target">Türkçe</a></li><li class="interlanguage-link interwiki-tk"><a href="https://tk.wikipedia.org/wiki/HTML" title="HTML – Turkmen" lang="tk" hreflang="tk" class="interlanguage-link-target">Türkmençe</a></li><li class="interlanguage-link interwiki-uk badge-Q17437798 badge-goodarticle" title="good article"><a href="https://uk.wikipedia.org/wiki/HTML" title="HTML – Ukrainian" lang="uk" hreflang="uk" class="interlanguage-link-target">Українська</a></li><li class="interlanguage-link interwiki-ur"><a href="https://ur.wikipedia.org/wiki/%D8%A7%DB%8C%DA%86_%D9%B9%DB%8C_%D8%A7%DB%8C%D9%85_%D8%A7%DB%8C%D9%84" title="ایچ ٹی ایم ایل – Urdu" lang="ur" hreflang="ur" class="interlanguage-link-target">اردو</a></li><li class="interlanguage-link interwiki-vi"><a href="https://vi.wikipedia.org/wiki/HTML" title="HTML – Vietnamese" lang="vi" hreflang="vi" class="interlanguage-link-target">Tiếng Việt</a></li><li class="interlanguage-link interwiki-wo"><a href="https://wo.wikipedia.org/wiki/HTML" title="HTML – Wolof" lang="wo" hreflang="wo" class="interlanguage-link-target">Wolof</a></li><li class="interlanguage-link interwiki-yi"><a href="https://yi.wikipedia.org/wiki/HTML" title="HTML – Yiddish" lang="yi" hreflang="yi" class="interlanguage-link-target">ייִדיש</a></li><li class="interlanguage-link interwiki-yo"><a href="https://yo.wikipedia.org/wiki/HTML" title="HTML – Yoruba" lang="yo" hreflang="yo" class="interlanguage-link-target">Yorùbá</a></li><li class="interlanguage-link interwiki-zh-yue"><a href="https://zh-yue.wikipedia.org/wiki/HTML" title="HTML – Cantonese" lang="yue" hreflang="yue" class="interlanguage-link-target">粵語</a></li><li class="interlanguage-link interwiki-bat-smg"><a href="https://bat-smg.wikipedia.org/wiki/HTML" title="HTML – Samogitian" lang="sgs" hreflang="sgs" class="interlanguage-link-target">Žemaitėška</a></li><li class="interlanguage-link interwiki-zh"><a href="https://zh.wikipedia.org/wiki/HTML" title="HTML – Chinese" lang="zh" hreflang="zh" class="interlanguage-link-target">中文</a></li>				</ul>
				<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q8811#sitelinks-wikipedia" title="Edit interlanguage links" class="wbc-editpage">Change links</a></span></div>			</div>
		</div>
				</div>
		</div>
				<div id="footer" role="contentinfo">
						<ul id="footer-info">
								<li id="footer-info-lastmod"> This page was last changed on 21 October 2018, at 21:09.</li>
								<li id="footer-info-copyright">Text is available under the <a href="//simple.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License">Creative Commons Attribution/Share-Alike License</a> and the <a href="//simple.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License">GFDL</a>; additional terms may apply. See <a href="//wikimediafoundation.org/wiki/Terms_of_Use">Terms of Use</a> for details.</li>
							</ul>
						<ul id="footer-places">
								<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Privacy_policy" class="extiw" title="wmf:Privacy policy">Privacy policy</a></li>
								<li id="footer-places-about"><a href="/wiki/Wikipedia:About" title="Wikipedia:About">About Wikipedia</a></li>
								<li id="footer-places-disclaimer"><a href="/wiki/Wikipedia:General_disclaimer" title="Wikipedia:General disclaimer">Disclaimers</a></li>
								<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
								<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Cookie_statement">Cookie statement</a></li>
								<li id="footer-places-mobileview"><a href="//simple.m.wikipedia.org/w/index.php?title=HTML&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Mobile view</a></li>
							</ul>
										<ul id="footer-icons" class="noprint">
										<li id="footer-copyrightico">
						<a href="https://wikimediafoundation.org/"><img src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation"/></a>					</li>
										<li id="footer-poweredbyico">
						<a href="//www.mediawiki.org/"><img src="/static/images/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88" height="31"/></a>					</li>
									</ul>
						<div style="clear: both;"></div>
		</div>

<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.108","walltime":"0.150","ppvisitednodes":{"value":456,"limit":1000000},"ppgeneratednodes":{"value":0,"limit":1500000},"postexpandincludesize":{"value":7866,"limit":2097152},"templateargumentsize":{"value":615,"limit":2097152},"expansiondepth":{"value":7,"limit":40},"expensivefunctioncount":{"value":0,"limit":500},"unstrip-depth":{"value":1,"limit":20},"unstrip-size":{"value":8534,"limit":5000000},"entityaccesscount":{"value":0,"limit":400},"timingprofile":["100.00%  121.183      1 -total"," 59.36%   71.933      1 Template:Reflist"," 50.68%   61.414      1 Template:Cite_web"," 35.07%   42.500      1 Template:Infobox_file_format"," 31.95%   38.712      1 Template:Infobox","  3.22%    3.904      1 Template:Small","  2.47%    2.989      1 Template:Template_other","  2.25%    2.721      1 Template:Main_other","  1.62%    1.962      1 Template:Nowrap"]},"scribunto":{"limitreport-timeusage":{"value":"0.051","limit":"10.000"},"limitreport-memusage":{"value":1540332,"limit":52428800}},"cachereport":{"origin":"mw1249","timestamp":"20181125171118","ttl":1900800,"transientcontent":false}}});});</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"HTML","url":"https:\/\/simple.wikipedia.org\/wiki\/HTML","sameAs":"http:\/\/www.wikidata.org\/entity\/Q8811","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q8811","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2004-03-05T03:39:17Z","dateModified":"2018-10-21T21:09:16Z","headline":"family of markup languages for displaying information viewable in a web browser"}</script>
<script>(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":118,"wgHostname":"mw1322"});});</script>
	</body>
</html> '''

soup = BeautifulSoup(html_doc, 'html.parser')


