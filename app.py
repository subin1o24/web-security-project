from flask import Flask, request, redirect
from markupsafe import escape

app = Flask(__name__)

# 게시글 저장 리스트
posts = []


# 메인 페이지
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

    # 메인 페이지는 안전하게 출력
    for post in posts:
        html += f"<p>{escape(post)}</p>"

    return html


# 게시글 저장
@app.route('/write', methods=['POST'])
def write():

    content = request.form['content']

    # 입력값 저장
    posts.append(content)

    return redirect('/')


# 관리자 페이지
@app.route('/admin')
def admin():

    html = """
    <h1>관리자 페이지</h1>

    <hr>

    <h3>저장된 게시글 확인</h3>
    """

    # 관리자 페이지는 취약하게 출력
    for post in posts:
        html += f"<p>{post}</p>"

    return html


if __name__ == '__main__':
    app.run(debug=True)
