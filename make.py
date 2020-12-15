# 

import os
import os
import time
from pprint import pprint 
t=[]
filearr=[]
for i in os.listdir(r'blogMD/'):
  t = open("blogMD/"+i, "r")
  MDcont=t.read()
  t.close()
  tWrite="""
  <style>@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
  * {
    font-weight:100px;
    font-family: 'Roboto', sans-serif;
  }
  img {
    width:100%;
  }
  hr {
    width:100%;
  }
  .p {
    font-size:10px;
    display: inline-block;
    display: inline;
  }
  span {
    display:inline;
  }</style><style src="/dev/css"></style> <script src="/dev/js"></script>
  <h3><i>a site<span class="p">hello world <a href="update.php">update</a></span></h3></i>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
  <?php
  require '../dev/pd.php';
  $Parsedown = new Parsedown();
  echo $Parsedown->text('"""+MDcont+"""'); 
  """
  i=i.replace(".md","")
  f = open("blogposts/" + i + ".php", "w")
  f.write(tWrite)
  f.close()
  z = open("template.htm", "r")
  template=z.read()
  z.close()
  filearr+=i
  filearr
#for i in os.listdir(r'blogposts/'):
#  #t+=i
#  f = open('index.php', "w")
#  f.write('<link rel="stylesheet" href="/dev/water.css">')
#  f.close()

#for i in t:
#  f=open('')
def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a
blogposts=getfiles("blogMD")
def Reverse(lst): 
    return [ele for ele in reversed(lst)]
#blogposts=Reverse(blogposts) ( this isnt needed )
def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)
f = open("index.php", "w")
f.write("""

<!--

Hi! You won't find that much here, really other
than <a href=, style, scripts, and bad coding 
practices. The code for this is at github.com/mayank1234cmd/phpblog123.
Let me know if you want features!



-->





















<style src="/dev/css"></style> <script src="/dev/js"></script>

<p>Coded by <a href='//glitch.com/@notmayank'>mayank</a>, content by me!</a></p>
<style src="dev/script.js"></script><style src="dev/style.css"></style>

<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css">
<script src="ad.php"></script>
<?php sleep(1); ?>
<!--Main page/template for comments-->
<style>@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
* {
  font-weight:100px;
  font-family: 'Roboto', sans-serif;
}
img {
  width:100%;
}
hr {
  width:100%;
}
.p {
  font-size:10px;
  display: inline-block;
  display: inline;
}
span {
  display:inline;
}</style>
<link rel="stylesheet" href="/dev/water.css" />

<h3><i>a site<span class="p">hello world <a href="update.php">update</a></span></h3></i>
<!--wow you did it-->
""")
f.close()
blogposts=Reverse(blogposts)
for i in blogposts:
  with open("index.php", "a") as myfile:
    myfile.write("<a href='/blogposts/"+i+"'>"+i.replace(".md","")+"</a><br/>")

with open("index.php","a") as f:
  f.write("""<hr/><p>
  CSS from <a href="https://watercss.kognise.dev/"> water.css </a>.
</p>""")
