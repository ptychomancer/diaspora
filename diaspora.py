from flask import Flask, render_template, jsonify, request
from json import dump
from colony import Colony

# diaspora.py is a web service that serves space colonies.
# (built with Flask, served with gunicorn, deployed with heroku)

app = Flask(__name__, static_url_path='/static')
app.config["JSON_SORT_KEYS"] = False
    
@app.route("/")
def colony():
    colony = Colony()
    colony.describe()
    return render_template('index.html',
                           title = 'diaspora',
                           colony = colony.description,
                           attributes = colony.attributes)    

# An API for requesting colonies (response type: JSON)
@app.route('/api/v1.0/', methods = ['GET'])
def api():
    if request.method == 'GET':                
        if not request.query_string:
            howMany = 0
        else:
            howMany = int(request.query_string)
        if howMany <= 500:            
            colonies = []
            for i in range(0, howMany):
                colony = Colony()
                colony.describe()
                colonies.append(colony.serialize())        
            to_dump = {'colonies' : colonies}    
            return jsonify(to_dump)
        else:
            return "Too many colonies requested (500 max)."

if __name__ == '__main__':
    app.run()
    