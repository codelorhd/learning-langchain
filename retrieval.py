from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(name="llama2")

embeddings = OllamaEmbeddings()
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents=documents, embedding=embeddings)


prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based only on the provided context


    <context>
    {context}
    <context>

    Question: {input}
    """
)
document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)


retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
response = retrieval_chain.invoke({
    "input": "how can langsmith help with testing?"
})
print(response["answer"])
