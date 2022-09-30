from flask import request, render_template, redirect, send_from_directory, make_response, url_for, Blueprint
from werkzeug.exceptions import HTTPException
# from secure import SecureHeaders

from platzky.blog import comment_form, post_formatter



def create_blog_blueprint(db, config, babel):
    url_prefix = config["BLOG_PREFIX"]
    blog = Blueprint('blog', __name__, url_prefix=url_prefix)

    main_domain = config["MAIN_DOMAIN"]

    # secure_headers = SecureHeaders()

    @blog.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', title='404'), 404

    def get_locale():
        return "en"

    @blog.route('/', methods=["GET"])
    def index():
        lang = get_locale()
        return render_template("blog.html", posts=db.get_all_posts(lang))

    @blog.route('/feed', methods=["GET"])
    def get_feed():
        lang = get_locale()

        response = make_response(render_template("feed.xml", posts=db.get_all_posts(lang)))
        response.headers["Content-Type"] = "application/xml"
        return response

    @blog.route('/<post_slug>', methods=["GET", "POST"])
    def get_post(post_slug):
        if request.method == "POST":
            comment = request.form.to_dict()
            db.add_comment(post_slug=post_slug, author_name=comment["author_name"],
                           comment=comment["comment"])
            return redirect(url_for('blog.get_post', post_slug=post_slug, comment_sent=True, language=get_locale()))

        if raw_post := db.get_post(post_slug):
            return render_template("post.html", post=post_formatter.format_post(raw_post), post_slug=post_slug,
                                   form=comment_form.CommentForm(), comment_sent=request.args.get('comment_sent'))
        else:
            return page_not_found("no such page")

    @blog.route('/page/<path:page_slug>', methods=["GET", "POST"])
    def get_page(page_slug):
        if post := db.get_page(page_slug):
            return render_template("page.html", post=post)
        else:
            return page_not_found("no such page")

    @blog.route('/tag/<path:tag>', methods=["GET"])
    def get_posts_from_tag(tag):
        lang = get_locale()
        posts = db.get_posts_by_tag(tag, lang)
        return render_template("blog.html", posts=posts, subtitle=f" - tag: {tag}")

    @blog.route('/icon/<string:name>', methods=["GET"])
    def icon(name):
        return send_from_directory('../static/icons', f"{name}.png")

    return blog
