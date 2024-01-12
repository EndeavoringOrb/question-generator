from llama_cpp import Llama

mistral_path = "C:/Users/aaron/CODING/llms/mistral-7b-v0.1.Q5_K_M.gguf"
ctx_len = 2048

llm = Llama(model_path=mistral_path, n_ctx=ctx_len)

section = input("Enter the section (i.e '3.2'): ")
numProblems = int(input("How many problems do you want to generate?: "))
numLines = int(input("How many lines do you want for the student to do work?: "))

def addWorkSpace(text, numProblems, numLines):
    newLines = "\n" * numLines
    for i in range(1, numProblems + 1):
        text = text.replace(f"\n{i}. ", f"{newLines}\n{i}. ")
    return text

with open(f"prompts/{section}/prompt.txt", "r", encoding="utf-8") as f:
    prompt1 = f.read()

with open(f"prompts/{section}/answerStart.txt", "r", encoding="utf-8") as f:
    answerStart = f.readlines()

answerStart = f"### Section {section} Problem Set: {answerStart[0].strip()}\n\nFor questions 1-{numProblems}, {answerStart[1].strip().strip('.')}.\n\n1. $"
prompt = f"{prompt1}\n\n{answerStart}"

print(f"\n\n{prompt}")

output = llm(
    prompt, # Prompt
    max_tokens=ctx_len, # Generate up to 32 tokens
    stop=[f"{numProblems+1}. ", "### Section", f"For questions {numProblems+1}"], # Stop generating just before the model would generate a new question
    echo=False, # Echo the prompt back in the output
    stream=True,
)
print("\nResponse:")
out_text = ""
for out in output:
    text = out["choices"][0]["text"]
    out_text += text
    print(text, end="")

out_text = addWorkSpace(out_text, numProblems, numLines).strip()
out_text = answerStart + out_text

with open("out.md", "w", encoding="utf-8") as f:
    f.write(out_text)