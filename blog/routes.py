from flask import Flask, request, render_template, redirect
from blog import app
from blog.models import Entry

 
@app.route("/")
def blog_base():
    return render_template("base.html")

##@app.route("/")
##def index():
  ##    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
   ##return render_template("homepage.html", all_posts=all_posts)

##@app.shell_context_processor


##if __name__ == "__main__":
  ##  app.run(debug=True)