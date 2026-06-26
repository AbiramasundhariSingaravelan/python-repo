# I want to become a data scientiest
import google.generativeai as genai
#Configuring API Key
#genai.configure(api_key="abc")
#Loading Gemini Model
print("AI CAREER GUIDANCE ASSISTANT")
model=genai.GenerativeModel("gemini-3-flash-preview")
career=input("Enter your dream career")
prompt = f"""
You are a career mentor.

Provide:
1. Required Skills
2. Learning Roadmap
3. Suggested Projects
4. Job Opportunities

for a student who wants to become a {career}.
"""
response=model.generate_content(prompt)
print("\n==================")
print(response.text)