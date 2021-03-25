from flask import Flask, request, render_template, redirect, flash, session, url_for
from blog import app
from blog.models import Entry, db
from faker import Faker
from blog.forms import EntryForm

@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())


    return render_template("homepage.html", all_posts=all_posts)

@app.route("/new/", methods=["GET", "POST"])
def create_entry():
   form = EntryForm()
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           entry = Entry(title=form.title.data, body=form.body.data, is_published=form.is_published.data)
           db.session.add(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    form = EntryForm(obj=entry)
    errors = None
    if request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(entry)
            db.session.commit()
            flash("Twój wpis został zmieniony", "info")
            return redirect("/")
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)

##@app.shell_context_processor


##if __name__ == "__main__":
  ##  app.run(debug=True)