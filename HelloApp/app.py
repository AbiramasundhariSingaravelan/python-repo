from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return "<h1>Welcome to About Page</h1>"
@app.route("/service")
def service():
    return "<h1>Welcome to Services Page</h1>"
@app.route("/contact")
def contact():
    return "<h1>Welcome to Contact Page</h1>"
@app.route("/student/<name>")
def student(name):
    return f"<h1>Welcome {name}</h1>"
@app.route("/register",methods=["POST"])
def register():
    name=request.form["name"]
    dept=request.form["dept"]
    mobile=request.form["mobile"]
    city=request.form["city"]
    state=request.form["state"]
    country=request.form["country"]
    return f"""<h2>Registration Successful</h2>
    <hr>
    <table border='1'>
        <tr>
            <th>NAME</th>
            <th>DEPT</th>
            <th>MOBILE</th>
            <th>CITY</th>
            <th>STATE</th>
            <th>COUNTRY</th>
        </tr>
        <tr>
            <td>{name}</td>
            <td>{dept}</td>
            <td>{mobile}</td>
            <td>{city}</td>
            <td>{state}</td>
            <td>{country}</td>
        </tr>
    </table>
    """
app.run(debug=True)