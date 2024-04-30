

import datetime

from flask import Flask, render_template, request
app = Flask("cagey-simplex", template_folder="jinja")

from aguirre.integrations.flask import create_blueprint
app.register_blueprint(create_blueprint("package/"), url_prefix="/vendor")

import db


@app.route("/")
def hello():
    #return "Hello world"
    return render_template("hello.html")


#@app.route("/package/htmx.org@1.9.11/htmx.min.js")
#def package():
#    return open("package/htmx.min.js").read()


@app.route("/frag/status/")
def status():
    return "The time is %s" % datetime.datetime.now()


@app.route("/rows.frag")
def rows():
    after = request.args.get("after", "0")
    rows = db.rows_after(int(after))
    next_after = max(r["id"] for r in rows)
    return render_template("rows.frag.html", rows=rows, after=next_after)


import logging
logging.basicConfig(level="DEBUG")
