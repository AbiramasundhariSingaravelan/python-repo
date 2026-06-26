# I want to become a data scientiest
import google.generativeai as genai
#Configuring API Key
genai.configure(api_key="AQ.Ab8RN6IY1ZVR7ZLHr6dz1U-Yylw3Uj2Cdb6Y25sZc3aCSyMC3w")
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