from openai import OpenAI
client=OpenAI(api_key="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")
goal = input("Enter your goal")
days=input("dutation")
prompt=f""" Create a {days} study plan for {goal} """
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {
            "role":"user",
            "content":prompt
        }
    ]
)
print(response.choices[0].message.content)
