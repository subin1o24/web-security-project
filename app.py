from flask import Flask, request, redirect
from markupsafe import escape

app = Flask(__name__)

posts = []


@app.route('/')
def index():

    html = """
    <h1>게시판</h1>

    <form action="/write" method="POST">
        <input type="text" name="content" style="width:300px;">
        <button type="submit">작성</button>
    </form>

    <hr>

    <h3>게시글 목록</h3>
    """

    for post in posts:
        html += f"<p>{escape(post)}</p>"

    return html


@app.route('/write', methods=['POST'])
def write():

    content = request.form['content']
    posts.append(content)
    return redirect('/')


@app.route('/admin')
def admin():

    html = """
    <h1>관리자 페이지</h1>

    <hr>

    <h3>저장된 게시글 확인</h3>
    """

    for post in posts:
        html += f"<p>{post}</p>"

    return html


if __name__ == '__main__':
    app.run(debug=True)
