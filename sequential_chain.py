# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import Prompt_Template
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=Prompt_Template(
    template = 'Generate a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2=Prompt_Template(
template='Generate a 5 point summary of the following text\n {text}',
input_variables = ['text']
)

model=ChatGroq(model='llama-3.3-70b-versatile')

parser=StrOutputParser()


chain= prompt1 | model | parser | prompt2 |model |parser

result=chain.invoke({'topic':'Unemployment in india'})

print(result)


#how to see chain
chain.get_graph().print_ascii()