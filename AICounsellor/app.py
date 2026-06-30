from flask import Flask, render_template, request
import google.generativeai as genai
app=Flask(__name__)
genai.configure(api_key="AIzaSyDuMq19zP8AXK6DT-pdQfGWX33YLpSZ-tA")
model=genai.GenerativeModel("gemini-3.1-flash-lite")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/career", methods=["POST"])
def career():
    career_goal=request.form["career"]
    prompt=f""" I want to become a {career_goal}. Please provide followingi nformation .1. REquired Skills, 2. Learning RoadMap, 3. Recommended projects 4. Certifications 5. Career Opportunities 6. Salary Expectations 7. Tips for fresher"""
    try:
        response=model.generate_content(prompt)
        answer=response.text
    except Exception as e:
        answer=f"Error: {e}"
    return render_template("result.html", career=career_goal, response=answer)
if __name__ == "__main__":
    app.run(debug=True)
