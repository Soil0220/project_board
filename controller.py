"""
controller 

"""

import flask as f
import dao as d

app = f.Flask(__name__)

@app.route("/")

def root():
    """
    address : "/", get
    output : root.html , d.list

    루트 화면
    """

    dao_bulletin_board = d.list()

    return f.render_template("root.html",bulletin_board = dao_bulletin_board)

@app.route("/write")
def write():
    """
    address : "/write", get
    output : write.html

    작성 화면
    """

    return f.render_template("write.html")

@app.route("/read")
def read():
    """
    address : "/read", get
    output : read.html, d.read(h_bno)

    읽기 화면
    """

    h_bno = f.request.args.get("bno", type = int)
    dao_board = d.read(h_bno)

    return f.render_template("read.html",board = dao_board)

@app.route("/write", methods=["post"])
def write_in():
    """
    address: "/write", post
    d.save()호출
    output : "/"

    작성 시
    """

    h_title = f.request.form.get("title", type=str)
    h_content = f.request.form.get("content", type=str)
    h_nickname = f.request.form.get("nickname", type=str)
    d.save(title = h_title, content = h_content, nickname = h_nickname)

    return f.redirect("/")

@app.route("/update", methods=["post"])
def update():
    """
    address : "/update ", post
    d.update()호출
    output : "/"

    업데이트
    """

    h_bno = f.request.form.get("bno", type=int)
    h_title = f.request.form.get("title", type=str)
    h_content = f.request.form.get("content", type=str)
    d.update(bno = h_bno, title = h_title, content = h_content)

    return f.redirect("/")

@app.route("/delete", methods=["post"])
def delete():
    """
    address : "/delete", post
    d.delete()호출
    output : "/"

    삭제
    """

    h_bno = f.request.form.get("bno", type=int)
    d.delete(h_bno)

    return f.redirect("/")


app.run(debug=True)