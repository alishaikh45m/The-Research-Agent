# AI Research Agent 🤖

A powerful automated research assistant built with **LangGraph**, **LangChain**, and **Groq**. This agent autonomously performs deep research on any given topic, analyzes multiple sources, and generates a comprehensive markdown report.

## 🚀 Features

- **Automated Web Search**: Uses Tavily API to find relevant, high-quality articles.
- **Intelligent Analysis**: Aggregates and extracts key insights from multiple sources using Llama 3 models via Groq.
- **Structured Reporting**: Produces a well-formatted Markdown summary of the findings.
- **Agentic Workflow**: distinct roles (Searcher, Analyst, Writer) working together in a linear graph.

## 🛠️ Tech Stack

- **Python**
- **LangGraph** (State management & workflow)
- **LangChain** (LLM orchestration)
- **Groq API** (Llama 3.3 70b inference)
- **Tavily API** (Search engine for LLMs)

## 📋 Prerequisites

Ensure you have the following API keys:
- **Groq API Key**: Get it [here](https://console.groq.com/)
- **Tavily API Key**: Get it [here](https://tavily.com/)

## 📦 Installation

1. **Clone the repository** (if applicable) or verify you have the files.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**:
   Create a `.env` file in the root directory:
   ```ini
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## 🏃 Usage

Run the agent script:

```bash
python research-agent.py
```

1. Enter a topic when prompted (e.g., *"Impact of Quantum Computing on Cryptography"*).
2. Watch as the agent:
   - 🔍 Searches for articles.
   - 📊 Analyzes the content.
   - ✍️ Writes a final summary.
3. The final report will be displayed in the terminal.

## 📂 Project Structure

```
.
├── research-agent.py  # Main agent logic and workflow
├── .env              # API keys (not committed)
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
