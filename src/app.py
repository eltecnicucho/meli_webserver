from flask import Flask,jsonify,render_template,request
from bson.json_util import dumps
from pymongo import MongoClient

#BASE=MELIDB
#COLLECTION=Coleccion_2022
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.MELIDB
@app.route('/',methods=['GET','POST'])
def menu():
    if request.method=='POST':
        doc_name = request.form['archivo']
        term = request.form['palabra']
        #return redirect('/buscar')
        return (jsonify("Frecuencia:", dumps(db.Coleccion_2022.count_documents({"Archivo" : doc_name, "Palabra" : term}))))
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)