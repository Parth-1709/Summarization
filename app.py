from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
import validators

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Video Summarizer",
    page_icon="🎥",
    layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #888;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .result-box {
        padding: 25px;
        border-radius: 12px;
        background-color: rgba(128, 128, 128, 0.08);
        border: 1px solid rgba(128, 128, 128, 0.2);
        margin-top: 25px;
    }

    .footer {
        text-align: center;
        color: #888;
        font-size: 13px;
        margin-top: 50px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🎥 AI Video Summarizer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Summarize YouTube videos and web pages using AI</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    st.markdown("Enter your Groq API key to use the AI summarizer.")

    groq_api_key = st.text_input(
        label="Groq API Key",
        value="",
        type="password",
        placeholder="gsk_..."
    )

    if groq_api_key:
        st.success("API key provided")

    st.divider()

    st.caption(
        "Your API key is used only for this session."
    )

# -----------------------------
# URL Input
# -----------------------------
st.subheader("🔗 Enter Content URL")

url = st.text_input(
    "URL",
    placeholder="Paste a YouTube or webpage URL here...",
    label_visibility="collapsed"
)

st.caption("Supported: YouTube videos and publicly accessible webpages")

# -----------------------------
# LLM
# -----------------------------
if groq_api_key:
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=groq_api_key
    )

# -----------------------------
# Prompt
# -----------------------------
system_prompt = '''
Summarize the provided text in less than 200 words with a proper title and bullet points for proper info .
if its a youtube video and there is no transcript in that video or there is no text just return no proper transcript 
{text}
'''

prompt = PromptTemplate(
    input_variables=["text"],
    template=system_prompt
)

# -----------------------------
# Summarize Button
# -----------------------------
st.markdown("")

if st.button("✨ Summarize Content", use_container_width=True):

    if not groq_api_key or not url.strip():
        st.warning("⚠️ Please provide both your Groq API key and a URL.")

    elif not validators.url(url):
        st.warning("⚠️ Please provide a valid URL.")

    else:

        try:

            with st.spinner("🔄 Fetching content and generating summary..."):

                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[url]
                    )

                data = loader.load()

                chain = load_summarize_chain(
                    llm=llm,
                    chain_type="stuff",
                    prompt=prompt
                )

                output = chain.run(data)

            # -----------------------------
            # Result
            # -----------------------------
            st.markdown(
                '<div class="result-box">',
                unsafe_allow_html=True
            )

            st.subheader("📝 Summary")

            st.write(output)

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

        except Exception as e:

            st.error("❌ Something went wrong.")
            st.exception(e)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    '<div class="footer">Built with Streamlit • LangChain • Groq</div>',
    unsafe_allow_html=True
)
