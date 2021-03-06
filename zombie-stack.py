#!/bin/env python
# -*- coding: utf-8 -*-
#
#
from lxml import etree
from lxml import objectify
from subprocess import Popen, PIPE, STDOUT
import StringIO
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def to_markdown(html_in):
  p = Popen(["pandoc", "-f", "html", "-t", "markdown"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
  stdout = p.communicate(input=html_in)[0]
  return stdout



posts = objectify.parse( "./posts.xml" ).getroot()
users = objectify.parse( "users.xml" ).getroot()
comments = objectify.parse( "./comments.xml" ).getroot()
votes = objectify.parse( "./votes.xml" ).getroot()

objectify.dump(users)

for u in users.iterchildren():
  objectify.dump(u)


def get_user(uid):
  xpath = "row[@Id='" + str(uid) + "']"
  return users.find(xpath)

def get_comments(postId):
  return comments.findall("row[@PostId='" + postId + "']")

def print_comments(md,Id):
    print >>md, "### Comments ###"
    for comment in get_comments(Id):
        cu = get_user(comment.get("UserId"))
        if cu == None:
          print >>md, "* NONE: "+to_markdown(comment.get("Text")).strip()
        else:
          print >>md, "* "+ cu.get("DisplayName") + ": "+to_markdown(comment.get("Text")).strip()
    print >>md, ""

def format_tags( tags ):
    tout = '<ul class="tags">'
    for tag in tags.split("><"):
      tag = tag.strip("<>")
      tout += '<li class="tag">'+tag+'</li>'
    tout += '</ul>'
    return tout


inpage = open("static/index.md","w")
print >>inpage, "---"
print >>inpage, "title: Index"
print >>inpage, "layout: default"
print >>inpage, "---"


for r in posts.row:
  Id = r.get("Id")
  md = open("static/questions/"+Id+".md","w")
  if r.get("ParentId") == None:
    print >>md, "---"
    print >>md, "title: \""+str(r.get("Title"))+"\""
    print >>md, "layout: default"
    print >>md, "---"
    print >>md, str(r.get("Title"))
    print >>md, "====================="
    print >>md, to_markdown(r.get("Body"))
    u = get_user(r.get("OwnerUserId"))
    print >>md, u.get("DisplayName")
    tags = r.get("Tags")
    if tags != None:
      print >>md, ""
      print >>md, format_tags(tags)
    print >>md, ""
    print_comments(md,Id)
    print >>md, ""
    for child in posts.findall("row[@ParentId='" + Id + "']"):
      cu = get_user(child.get("OwnerUserId"))
      if cu == None:
        print >>md, "Answer by NONE"
      else:
        print >>md, "Answer by " + cu.get("DisplayName")
      print >>md, "----------------"
      print >>md, to_markdown(child.get("Body"))
      print_comments(md,child.get("Id"))
    print >>inpage, "* ["+str(r.get("Title"))+"](./questions/"+Id+".html)"




