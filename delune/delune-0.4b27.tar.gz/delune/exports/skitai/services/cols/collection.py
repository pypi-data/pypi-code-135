import delune
import os
from ..helpers import dpath
import codecs
import json

def __mount__ (context, app, opts):
    @app.route ("/<alias>", methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"])
    @app.permission_required (["replica", "index"])
    def collection (context, alias, side_effect = "", **_data):
        fn = dpath.getdir ("config", alias)
        if context.request.method == "GET":
            if not delune.get (alias):
                return context.Fault ("404 Not Found", "resource %s not exist" % alias, 40401)
            status = delune.status (alias)
            conf = dpath.getdir ("config", alias)
            if not os.path.isfile (conf):
                return context.Fault ("404 Not Found", "resource not exist", 40401)
            with codecs.open (conf, "r", "utf8") as f:
                colopt = json.loads (f.read ())
                status ['colopt'] = {
                    'data': colopt,
                    'mtime': os.path.getmtime (conf),
                    'size': os.path.getsize (conf),
                    'path': conf
                }
            return context.API (status)

        if context.request.method == "DELETE":
            if not os.path.isfile (fn):
                return context.Fault ("404 Not Found", "resource not exist", 40401)
            a, b = os.path.split (fn)
            if side_effect.find ("data") != -1:
                newfn = os.path.join (a, "-" + b)
            else:
                newfn = os.path.join (a, "#" + b)
            if os.path.isfile (newfn):
                os.remove (newfn)
            os.rename (fn, newfn)
            context.setlu (delune.SIG_UPD)
            if side_effect.find ("now") != -1:
                delune.close (alias)
                app.emit ('delune:delete', alias)
                return context.API ("204 No Content")
            return context.API ("202 Accepted")

        if context.request.method == "POST" and delune.get (alias):
            return context.Fault ("406 Conflict", "resource already exists", 40601)

        elif context.request.method in ("PUT", "PATCH") and not delune.get (alias):
            return context.Fault ("404 Not Found", "resource not exist", 40401)

        if context.request.method == "PATCH":
            with open (fn) as f:
                config = json.load (f)
            data = context.request.JSON
            section = data ["section"]
            for k, v in data ["data"].items ():
                if k not in config [section]:
                    return context.Fault ("400 Bad Request", "{} is not propety of {}".format (k, section), 40001)
                config [section][k] = v
        else:
            config = context.request.JSON

        with open (fn, "w") as f:
            json.dump (config, f)
        context.setlu (delune.SIG_UPD)
        app.emit ('delune:reconfigure', alias)

        if context.request.method == "POST":
            if side_effect == "now":
                dpath.load_data (alias, app.config.numthreads, context.plock)
                app.emit ('delune:create', alias)
                return context.API ("201 Created", **config)
            return context.API ("202 Accepted", **config)

        return context.API (**config)

    # replica -------------------------------------------------------
    @app.route ("/<alias>/config", methods = ["GET"])
    @app.permission_required (["index", "replica"])
    def config (context, alias):
        fn = dpath.getdir ("config", alias)
        return context.response.file (fn, "application/json")

    @app.route ("/<alias>/locks", methods = ["GET"])
    @app.permission_required ("replica")
    def locks (context, alias):
        return context.API ({"locks": delune.get (alias).si.lock.locks ()})

    @app.route ("/<alias>/locks/<name>", methods = ["POST", "DELETE", "OPTIONS"])
    @app.permission_required ("replica")
    def lock (context, alias, name, **_data):
        if context.request.command == "post":
            delune.get (alias).si.lock.lock (name)
            app.emit ('delune:lock', alias, name)
            return context.API ("201 Created")
        delune.get (alias).si.lock.unlock (name)
        app.emit ('delune:unlock', alias, name)
        return context.API ("205 No Content")

    @app.route ("/<alias>/commit", methods = ["POST"])
    @app.permission_required ("index")
    def commit (context, alias):
        delune.get (alias).queue.commit ()
        app.emit ('delune:commit', alias)
        return context.API ("205 No Content")

    @app.route ("/<alias>/rollback", methods = ["POST"])
    @app.permission_required ("index")
    def rollback (context, alias):
        delune.get (alias).queue.rollback ()
        app.emit ('delune:rollback', alias)
        return context.API ("205 No Content")

    # utilities ------------------------------------------
    @app.route ("/<alias>/stem", methods = ["GET", "POST", "OPTIONS"])
    def stem (context, alias, **args):
        q = args.get ("q")
        if not q:
            return context.Fault ("400 Bad Request", 'parameter q required', 40003)
        if isinstance (q, str):
            q = q.split (",")
        l = args.get ("lang", 'en')
        return context.API (dict ([(eq, " ".join (delune.stem (alias, eq, l))) for eq in q]))

    @app.route ("/<alias>/analyze", methods = ["GET", "POST", "OPTIONS"])
    def analyze (context, alias, **args):
        q = args.get ("q")
        if not q:
            return context.Fault ("400 Bad Request", 'parameter q required', 40003)
        l = args.get ("lang", 'en')
        return context.API (delune.analyze (alias, q, l))

    # segments ------------------------------------------
    @app.route ("/<alias>/devices/<group>/<fn>", methods = ["GET"])
    @app.permission_required ("replica")
    def getfile (context, alias, group, fn):
        s = delune.status (alias)
        if group == "primary":
            path = os.path.join (s ["indexdirs"][0], fn)
        else:
            path = os.path.join (s ["indexdirs"][0], group, fn)
        return context.response.file (path)

    @app.route ("/<alias>/devices/<group>/segments/<fn>", methods = ["GET"])
    @app.permission_required ("replica")
    def getsegfile (context, alias, group, fn):
        s = delune.status (alias)
        seg = fn.split (".") [0]
        if group == "primary":
            if seg not in s ["segmentsizes"]:
                return context.Fault ("404 Not Found", "resource not exist", 40401)
            path = os.path.join (s ["segmentsizes"][seg][0], fn)
        else:
            path = os.path.join (s ["indexdirs"][0], group, fn)
        return context.response.file (path)
