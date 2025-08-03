from langchain_community.document_loaders import  PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GOOGLE_API_KEY"])

# Define all prompts directly in this file
prompt_summary = PromptTemplate(
    template='''You are an intelligent assistant trained to generate a concise and comprehensive summary from the uploaded PDF \n {text}. \nCarefully read and analyze the document.

Summarize the key points, main arguments, and conclusions. Do not include personal opinions or external knowledge. Focus only on the contents of the document.

Use clear, structured paragraphs and mention section headers if present.

If the document appears empty or contains no readable information, respond with: This PDF could not be summarized due to lack of content.''',
    input_variables=['text', 'question']
    )
prompt_mcq = PromptTemplate(
    template='''You are a quiz generation assistant. Based only on the content of the uploaded PDF \n {text} \n, generate multiple-choice questions (MCQs) that reflect the most important facts, definitions, and concepts from the document.

Each question should have 4 options, with one correct answer and three plausible distractors. Highlight the correct answer with a star (*) or any other clear mark.

Generate at least 5 MCQs if the content allows. Ensure all questions are answerable using the document content only.

Format:
Q1. [Question text]
A. Option 1  
B. Option 2  
C. Option 3 *  
D. Option 4

If no meaningful questions can be generated from the content, respond with: Not enough educational content available for MCQ generation.''',
    input_variables=['text', 'question']
)
prompt_qa = PromptTemplate(
    template='''You are an intelligent assistant trained to answer questions based only on the content of the uploaded PDF \n {text} \n. Use the document strictly as your source of truth. Do not guess or add information that is not found in the text.

Question: {question}

Based only on the provided text, give a clear and concise answer. If the answer requires explanation, cite the page or section explicitly.

If the document does not contain the answer, reply with: This information is not available in the provided document.''',
    input_variables=['text', 'question']
)

    # for multiple pdfs
parser = StrOutputParser()
'''loader = DirectoryLoader(
        path='books',
        glob='*.pdf',
        loader_cls=PyPDFLoader
)''' 
    # for single pdf
loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()
    
    # i could have used ruunalbe parallel but that gave me segmentation fault error
parallel_chain = RunnableParallel({
    'summary':  RunnableSequence(prompt_summary, model, parser),
    'mcq': RunnableSequence(prompt_mcq, model, parser),
    'qa': RunnableSequence(prompt_qa, model, parser)
})

if __name__ == '__main__':
   
    '''result = parallel_chain.invoke({'text':docs[0].page_content, 'question':'What is the main topic of the document?'})
    print('summary: ',result['summary'].content)
    print('mcq: ',result['mcq'].content)
    print('Answer: ',result['qa'].content)'''
    parallel_chain.get_graph().print_ascii()





