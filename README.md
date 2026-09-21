# 🎥 AI Video & Web Summarizer

An AI-powered Streamlit application that summarizes **YouTube videos and web pages** using **LangChain** and **Groq's LLMs**.

## 🚀 Live Demo

👉 [**AI Video Summarizer · Streamlit**](https://summarization-parth.streamlit.app/)

Simply provide a URL and your Groq API key, and the application extracts the content and generates a concise summary with a title and bullet points.

## ✨ Features

* 🎥 Summarize YouTube videos using their transcripts
* 🌐 Summarize publicly accessible web pages
* 🤖 Powered by Groq LLMs
* 🔗 Built using LangChain
* 📝 Generates concise summaries under 200 words
* 📌 Provides a structured title and bullet points
* 🔐 API key is entered securely through Streamlit's password input
* ⚡ Simple and lightweight Streamlit interface

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — Web application interface
* **LangChain** — LLM orchestration
* **LangChain Community** — Document loaders
* **LangChain Classic** — Summarization chain
* **Groq** — LLM inference
* **YouTube Transcript API** — YouTube transcript extraction
* **Unstructured** — Web content extraction

## 📂 Project Structure

```text
AI-Video-Summarizer/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Parth-1709/Summarization.git
cd AI-Video-Summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a Groq API key

Create a Groq API key from the Groq Console.

The application accepts the API key through the sidebar, so you don't need to hard-code it into the source code.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

The application follows a simple pipeline:

```text
                User
                  │
                  ▼
             Enter URL
                  │
                  ▼
        ┌───────────────────┐
        │ Identify URL Type │
        └─────────┬─────────┘
                  │
          ┌───────┴────────┐
          ▼                ▼
       YouTube           Web Page
          │                │
          ▼                ▼
     YouTube Loader   URL Loader
          │                │
          └───────┬────────┘
                  ▼
             Extract Text
                  │
                  ▼
          LangChain Stuff
          Summarization
                  │
                  ▼
             Groq LLM
                  │
                  ▼
              Summary
```

## 🧠 Summarization

The application currently uses LangChain's **Stuff summarization chain**.

The extracted content is passed to the LLM along with a custom prompt requesting:

* A proper title
* Important information
* Bullet points
* A summary of less than 200 words

## 🔒 API Key Security

The Groq API key is entered using Streamlit's password input:

```python
groq_api_key = st.text_input(
    "Groq API Key",
    type="password"
)
```

The key is provided by the user at runtime rather than being hard-coded into the repository.

**Never commit your API key to GitHub.**

## ⚠️ Limitations

* YouTube videos must have an accessible transcript.
* Some YouTube videos may not have transcripts available.
* Some websites may block automated content extraction.
* The application currently processes one URL at a time.
* Very large pages may exceed the model's context window when using the Stuff summarization strategy.

## 🔮 Future Improvements

* [ ] Add Map-Reduce summarization for larger documents
* [ ] Add Refine-based summarization
* [ ] Support more video platforms
* [ ] Add downloadable summaries
* [ ] Add summary length controls
* [ ] Add multiple language support
* [ ] Add a chat interface for summarized content
* [ ] Add RAG-based question answering
* [ ] Migrate the summarization workflow to LangGraph
* [ ] Add support for multiple URLs
* [ ] Add summary history

## 📜 License

This project is open-source and available under the MIT License.

```


