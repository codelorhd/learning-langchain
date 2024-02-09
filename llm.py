from langchain_community.llms.ollama import Ollama
from langchain.callbacks import get_openai_callback

llm = Ollama(model="llama2")

question = "What are some theories about the relationship between unemployment and inflation? Your answer should not be more than 50 words."
question = "Write a 100 words story about King Solomon in the Bible."

# for chunk in llm.stream(question):
#     print(chunk, end="", flush=True)

# output = llm.batch(
#     [
#         "What are some theories about the relationship between unemployment and inflation? Your answer should not be more than 50 words."
#     ]
# )
# print(output)

# Async Invoke
async def ask_async_question():
    for chunk in llm.stream(question):
        print(chunk, end="", flush=True)

import asyncio
asyncio.run(ask_async_question())