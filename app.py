from flask import Flask
app=Flask(____name____)
@app.route('/')
def home():
   return"<h1>Hello from Cloud!</h1><p>Deployed on Render</p>"
@app.route('/status')
def status():
   return{
      "statuts":"running",
      "server":"Render"
}
if__name__=="__main__":
   app.run(host="0.0.0.0",port=5000)