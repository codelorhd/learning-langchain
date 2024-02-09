""" Entrance to amazing stuff """

from langchain_community.llms.ollama import Ollama
from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# A simple parser to convert the chat message coming from a chain (chat model) to a string.
output_parser = StrOutputParser()

llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a world class technical documentation writer."),
        ("user", "{input}"),
    ]
)
# combine these into a simple LLM chain
chain = prompt | llm | output_parser

# output = chain.invoke({"input": "how can langsmith help with testing?"})
output = chain.ainvoke({"input": "how can langsmith help with testing?"})