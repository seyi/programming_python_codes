#!/usr/bin/python
########################################################
# implement http server in python that knows how to run
# server side CGI scripts; servess files/scripts  from
# current working dir; Python scripts must be stored in
# webdir/cgi-bin or webdir\htbin
#######################################################
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
import os,sys

#current working directory for html fils
webdir = '.'


port = 8006
os.chdir(webdir)
if sys.platform[:3] == 'win':
    CGIHTTPRequestHandler.have_popen2 = False
    CGIHTTPRequestHandler.have_popen3 = False

os.chdir(webdir)

serveraddr = HTTPServer(("",port),CGIHTTPRequestHandler)
serveraddr.serve_forever()