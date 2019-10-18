import os

import flask
from canonicalwebteam.flask_base.app import FlaskBase
from flask_wtf.csrf import CSRFProtect
from requests.exceptions import RequestException

from webapp.api import AssetAPI
from webapp.sso import init_sso, login_required


asset_api = AssetAPI(
    os.getenv("ASSET_SERVER_URL"), os.getenv("ASSET_SERVER_TOKEN")
)

app = FlaskBase(
    __name__,
    "manager.assets.ubuntu.com",
    static_folder="../static",
    template_folder="../templates",
    template_404="404.html",
    template_500="500.html",
)

csrf = CSRFProtect()
csrf.init_app(app)

init_sso(app)


@app.route("/")
@login_required
def home():
    query = flask.request.args.get("q", "")
    asset_type = flask.request.args.get("type", "")

    if query:
        assets = asset_api.all(flask.request.args)
    else:
        assets = []

    return flask.render_template(
        "index.html", assets=assets, query=query, type=asset_type
    )


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    created_assets = []
    existing_assets = []
    failed_assets = []

    if flask.request.method == "POST":
        tags = flask.request.form.get("tags", "")
        optimize = flask.request.form.get("optimize", True)

        for asset_file in flask.request.files.getlist("assets"):
            try:
                name = asset_file.filename
                content = asset_file.read()

                response = asset_api.create(content, name, tags, optimize)

                if response.get("code") == 409:
                    file_path = response["file_path"]
                    existing_assets.append(asset_api.get(file_path))
                else:
                    created_assets.append(response)

            except RequestException as error:
                failed_assets.append({"file_path": name, "error": str(error)})

        return flask.render_template(
            "created.html",
            assets=created_assets,
            existing=existing_assets,
            failed=failed_assets,
            tags=tags,
            optimize=optimize,
        )

    return flask.render_template("create.html")


@app.route("/update", methods=["GET", "POST"])
@login_required
def update():
    file_path = flask.request.args.get("file-path")

    if flask.request.method == "GET":
        asset = asset_api.get(file_path)
    elif flask.request.method == "POST":
        tags = flask.request.form.get("tags")
        asset = asset_api.update(file_path, tags)
        flask.flash("Tags updated", "positive")

    return flask.render_template("update.html", asset=asset)
