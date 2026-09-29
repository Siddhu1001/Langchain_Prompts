from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core import Prompt_Template
from langchain_core import StrOutputParser

load_dotenv()

prompt=Prompt_Template(
    template='Generate 5 intresting factys about {topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})
print(result)