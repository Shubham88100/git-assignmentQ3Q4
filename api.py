from flask import Flask, redirect, render_template , request
from dotenv import load_dotenv 
import os
import pymongo


load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client=pymongo.MongoClient(MONGO_URI)
db=client.test
collection = db['new_repo1']
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def form():
    error=""
    
    if request.method=="POST":
        name=request.form.get("name")
        description=request.form.get("description")
        
        if not name or not description:
            error="Name or description required"
            return render_template("form.html",error=error)
        try:
            collection.insert_one({
                "name":name,
                "description":description
            })
            
            return redirect("/submittodoitem")
        
        except Exception as e:
            error=str(e)
    return render_template("form.html",error=error)

@app.route('/submittodoitem')
def success():
    return "Data submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)