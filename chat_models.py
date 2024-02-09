from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models.ollama import ChatOllama

messags = [
    SystemMessage(content="You're a helpful assistant, your answers to questions must not be more than 50 words."),
    HumanMessage(content="What is the purpose of model regularization?")
]

chat = ChatOllama(model="llama2")

# output = chat.invoke(messags)

async def run_async():
    async for chunk in chat.astream(messags):
        print(chunk.content, end="", flush=True )

import asyncio
asyncio.run(run_async() )