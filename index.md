---
title:  Zombse
layout: default
---

The Zombie Stack Exchanges That Just Won't Die

Zombie Stack Exchanges
----------------------
* [032013 Digital Preservation](032013 Digital Preservation/static/)
* [032013 Digital Preservation Meta](032013 Digital Preservation Meta/static/)
* [062013 Libraries & Information Science](062013 Libraries & Information Science/static/)
* [062013 Libraries & Information Science Meta](062013 Libraries & Information Science Meta/static/)

Notes
-----
 * This calls out to [pandoc][1] to turn HTML snippets into Markdown text, so you'll need to have that installed.
 * The Markdown that pandoc creates seems to upset the Maraku engine, but RDiscount works okay.
 * I'm using [lxml][2], but using lxml.objectify is overkill. Gives little advantage over ElementTree, especially because the objectify wraps start to fail when running XPath queries. I should drop the lxml dependency and switch to a pure ElementTree implementation.


[1]: http://johnmacfarlane.net/pandoc/
[2]: http://lxml.de/

