from llm import ask_llm


prompt = """
Explain what a resume is in 3 simple sentences.
"""

response = ask_llm(prompt)

print(response)