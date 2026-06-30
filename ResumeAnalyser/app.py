from flask import Flask, render_template,request
import google.generativeai as genai
import os
app=Flask(__name__)
UPLOAD_FOLDER="resumes"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
genai.configure(api_key="abc")
model=genai.GenerativeModel("gemini-3.1-flash-lite")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/analyse",methods=["POST"])
def analyse():
    uploaded_file=request.files["resume"]
    if uploaded_file.filename == "":
        return "Please select your resume"
    filepath=os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
    uploaded_file.save(filepath)
    with open(filepath, "r", encoding="utf-8") as file:
        resume=file.read()
    prompt=f"""Can you check and analyse my resume and povide a score out of 10. {resume}"""
    try:
        response=model.generate_content(prompt)
        result=response.text
    except Exception as e:
        result =str(e)
    return render_template("result.html", response=result)
if __name__ == "__main__":
    app.run(debug=True)