# http://localhost:5000/
# http://localhost:5000/read/1
# http://localhost:5000/create
# http://localhost:5000/update/1
# Routing: 이러한 주소와 실제 서비스(index)랑 매핑하는것


from flask import Flask
import random

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '''<!doctype html>
#     <html>
#         <body>
#             <h1><a href="/">WEB</a></h1>
#             <ol>
#                 <li><a href="/read/1/">html</a></li>
#                 <li><a href="/read/2/">css</a></li>
#                 <li><a href="/read/3/">javascript</a></li>
#             </ol>
#             <h2>Welcome</h2>
#             Hello, Web
#         </body>
#     </html>
#     '''

# [
#     {'id':1, 'title':'html', 'body':'html is ...' } # 항목에 대한 제목, ID, 본문 등의 데이터가 있음 > 딕셔너리
#     {'id':2, 'title':'css', 'body':'css is ...' } 
#     ,
#     , # 1. 순서가있는 데이터는 리스트에 담는게 적합
# ]

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
        </body>
    </html>
    '''    

def getContests():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags


# @app.route('/')
# def index():
#     liTags = ''
#     for topic in topics:
#         liTags = liTags + f'<li>{topic["title"]}</li>'
#     return f'''<!doctype html>
#     <html>
#         <body>
#             <h1><a href="/">WEB</a></h1>
#             <ol>
#                 {liTags}
#             </ol>
#             <h2>Welcome</h2>
#             Hello, Web
#         </body>
#     </html>
#     '''

# 텍스트에 링크를 걸기 위해 a tag 추가
@app.route('/')
def index():
    return template(getContests(), '<h2>Welcome</h2>Hello,WEB')


@app.route('/create/')
def create():
    return 'Create'

# @app.route('/read/1/')
# def read():
#     return 'Read 1'

# @app.route('/read/<id>/')
# def read(id):
#     print(id)
#     return 'Read 1'

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