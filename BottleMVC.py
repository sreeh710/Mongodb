import bottle
@bottle.route('/')
def homepage():
    mythings=['apple','mango','pine','blueberry']
    return bottle.template('hello.tpl',{'username':'hari','things':mythings})
@bottle.post('/fav_fruit')
def fav_fruit():
    fruit=bottle.request.forms.get("fruit")
    if fruit==None:
        fruit="Not Selectd"
    return bottle.template('fruitselect.tpl',{'fruit':fruit})
bottle.debug=True
bottle.run(host="localhost",pot=8080)
