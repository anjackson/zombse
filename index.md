---
title:  Zombse
layout: default
---

> The Zombie Stack Exchanges That Just Won't Die

I've taken the data dumps from the Digital Preservation and the Library and Information Science Stack Exchange sites and generated static Markdown pages from them. I've then used GitHub Pages and Jekyll to host these static text files as HTML.

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


### DPSE Data Dump Issues ###

- Readme out of date, c.f. http://meta.stackoverflow.com/a/2678
- No Tags export, so no link between Tag and Tag Wiki Post
- Possibility of missing answers? 
-- Ah-ha! Migrated questions! digitalpreservation.stackexchange.com/questions/65/ 
-- But can you tell? Not 100% reliably due to poor data model. See last entries in post history, and e.g. Comment="to http://superuser.com/questions/568555/most-efficient-way-to-generate-and-validate-file-checksums"
- Post history log appears to return tag and body changes as 'Text changes'. 

http://discuss.area51.stackexchange.com/questions/11057/where-is-the-missing-data-from-the-dumps-of-these-two-closed-beta-sites



[1]: http://johnmacfarlane.net/pandoc/
[2]: http://lxml.de/

