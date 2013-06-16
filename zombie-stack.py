#!/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from lxml import objectify
from subprocess import Popen, PIPE, STDOUT
import StringIO

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
  xpath = "row[@Id='" + uid + "']"
  return users.find(xpath)

def get_comments(postId):
  return comments.findall("row[@PostId='" + postId + "']")

def print_comments(md,Id):
    print >>md, "### Comments ###"
    for comment in get_comments(Id):
        cu = get_user(comment.get("UserId"))
        print >>md, "* "+ cu.get("DisplayName") + ": "+to_markdown(comment.get("Text")).strip()
    print >>md, ""


inpage = open("static/index.md","w")
print >>inpage, "---"
print >>inpage, "title: Index"
print >>inpage, "---"


for r in posts.row:
  Id = r.get("Id")
  md = open("static/questions/"+Id+".md","w")
  if r.get("ParentId") == None:
    print >>md, "---"
    print >>md, "title:"+str(r.get("Title"))
    print >>md, "---"
    print >>md, str(r.get("Title"))
    print >>md, "====================="
    print >>md, to_markdown(r.get("Body"))
    u = get_user(r.get("OwnerUserId"))
    print >>md, u.get("DisplayName")
    print >>md, ""
    print_comments(md,Id)
    print >>md, ""
    for child in posts.findall("row[@ParentId='" + Id + "']"):
      cu = get_user(child.get("OwnerUserId"))
      print >>md, "Answer by " + cu.get("DisplayName")
      print >>md, "----------------"
      print >>md, to_markdown(child.get("Body"))
      print_comments(md,child.get("Id"))
    print >>inpage, "* ["+str(r.get("Title"))+"](./questions"+Id+".html)"




