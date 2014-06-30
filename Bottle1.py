import bottle
@bottle.route('/')
def home_page():
    return "helloworld\n"
@bottle.route('/testpage')
def test_page():
    return"this is sample\n"
bottle.debug(True)
bottle.run(host='localhost',port=8080)
