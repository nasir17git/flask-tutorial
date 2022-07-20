
from flask import Flask


app = Flask(__name__)

topics = [
    {'id':1, 'title':'html', 'body':'html is ...' }, 
    {'id':2, 'title':'css', 'body':'css is ...' }, 
    {'id':3, 'title':'js', 'body':'js is ...' } 
]

def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''    

def getContests():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getContests(), '<h2>Welcome</h2>Hello,WEB')


@app.route('/create/')
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="type title"></p>
            <p><textarea name="body" placeholder="type body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    return template(getContests(), content)
# URL을 통해서 서버로 데이터를 보내는것을 GET 방식이라고함
# 동적으로 작동하는 웹서비스에서 특정한 페이지를 식별하는 고유주소 > GET
# 값을 변경할때는 POST..?
# Payload 항목에 데이터를 실어서 안전하게 데이터 전송가능

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContests(), f'<h2>{title}</h2>{body}')
    
app.run(debug=True)