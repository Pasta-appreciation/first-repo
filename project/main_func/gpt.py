#from django.test import TestCase

# Create your tests here.

import os
import chromadb

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chains.openai_functions import create_structured_output_chain

from django.conf import settings
from langchain.pydantic_v1 import BaseModel, Field

collection_name = "langchain_test5"

class DefineVariableSenior(BaseModel):
        company_id :int = Field(..., discription="会社のID")
        job_id :int = Field(..., discription="候補者が応募したいと思う案件のID")
        Why_should_applicant_apply_for_the_project :str = Field(..., discription="候補者がこの案件に応募すべきであるという理由について200字程度で記述")

def embedding(document):
    text_splitter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
    is_separator_regex = False,
    )
    
    pages = text_splitter.create_documents([document])
    openai_ef = OpenAIEmbeddings()
    base_dir = settings.BASE_DIR
    print(base_dir)
    print(pages)
    persist_path = os.path.join(settings.BASE_DIR, 'Chroma')
    collection = Chroma(collection_name=collection_name, embedding_function=openai_ef, persist_directory=persist_path)
    vectorstore = collection.from_documents(pages,embedding=openai_ef, persist_directory=persist_path)
    return vectorstore

def make_recommend(query,vectorstore):
    #openai.api_key = os.environ["OPENAI_API_KEY"]
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    openai_ef = OpenAIEmbeddings()


    persist_path = os.path.join(settings.BASE_DIR, 'Chroma')
    client = chromadb.PersistentClient(path=persist_path)
    #vectorstore = Chroma(collection_name=collection_name, client=client, embedding_function=openai_ef)

    retrieved_docs = vectorstore.as_retriever().invoke(query)
    print(f"query{query}")
    print(f"retrieved_docs:{retrieved_docs[0]}")

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a world class algorithm for extracting information in structured formats."),
                ("human", "Use the given format to extract information from the following input: {input}"),
                ("human", "Tip: Make sure to answer in the correct format"),
                ("human", "The canditate profiles are the following data:"+ query),
                ("human", "日本語での回答をお願いします。"),

            ]
        )       

    chain_input = f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(retrieved_docs)])
    max_length = 3000
    trimmed_retrieved_docs = chain_input[:max_length]

    #chain
    chain = create_structured_output_chain(DefineVariableSenior, llm, prompt, verbose=True)
    print("beforechain\n")
    print(chain_input)
    table_of_contents = chain.run(trimmed_retrieved_docs)
    print(table_of_contents)
    return table_of_contents

