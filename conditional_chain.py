from langchain_groq import ChatGroq
# from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain.schema.runnable import RunnableParallel

load_dotenv()

model=ChatGroq(model='llama-3.3-70b-versatile')

parser=StrOutputParser()


prompt1=PromptTemplate(
    template='classify the scentiment of following feedback into positive or negative\n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser

print(classifier_chain.invoke({'feedback':'this is terrible smartphone'}))
