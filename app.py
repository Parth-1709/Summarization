from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
import validators

st.title('Youtube and Video Summarization App')

with st.sidebar:
    groq_api_key = st.text_input(label='Enter Groq Api key',value='',type='password')
    

url = st.text_input('URL',label_visibility='collapsed')

if groq_api_key:
    llm = ChatGroq(model='openai/gpt-oss-120b',api_key=groq_api_key)

system_prompt = '''
Summarize the provided text in less than 200 words with a proper title and bullet points for proper info .
if its a youtube video and there is no transcript in that video or there is no text just return no proper transcript 
{text}
'''

prompt = PromptTemplate(input_variables=['text'],template=system_prompt)

if st.button('summarize'):
    if not groq_api_key or not url.strip():
        st.warning('Please provide the necessary details')
    elif not validators.url(url):
        st.warning('Please provide a valid URL')
    else:
        try:
            with st.spinner('Waiting...'):
                if 'youtube.com' in url:
                    loader = YoutubeLoader.from_youtube_url(url)
                else :
                    loader = UnstructuredURLLoader(urls=[url])

                data = loader.load()

                chain = load_summarize_chain(llm=llm,chain_type='stuff',prompt=prompt)

                output = chain.run(data)

                st.success(output)
        except Exception as e:
            st.exception(f'Exception:{e}')

