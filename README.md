# 🤖 Cybersecurity FAQ Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Gemini%20AI-Powered-orange?style=for-the-badge)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

An intelligent, AI-powered chatbot that provides expert answers to all your cybersecurity questions! Built with Google's Gemini AI and Streamlit.

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-example-questions) • [Contributing](#-contributing)

</div>

## ✨ Features

🎯 **Smart Responses**
- Real-time answers powered by Google's Gemini AI
- Expert-level cybersecurity knowledge
- Clear and accessible explanations

🎨 **Modern Interface**
- Sleek dark mode design
- Interactive chat interface
- Message history tracking
- Mobile-responsive layout

🛡️ **Cybersecurity Focus**
- Best practices guidance
- Threat detection and prevention
- Security tool recommendations
- Compliance and regulation info

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Git (for cloning the repository)
- Gemini API key

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd AI-chatbot
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_gemini_api_key_here" > .env
   ```

   To get your Gemini API key:
   1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   2. Create/Select a project
   3. Enable the Gemini API
   4. Generate and copy your API key

## 💻 Usage

1. **Start the Application**
   ```bash
   streamlit run app.py
   ```

2. **Access the Chatbot**
   - Open your browser
   - Navigate to `http://localhost:8501`
   - Start asking questions!

## 🤔 Example Questions

Here are some questions you can ask the chatbot:

### 🔐 Password Security
- "What makes a password strong?"
- "How often should I change my passwords?"
- "What is a password manager and why should I use one?"

### 🌐 Network Security
- "How can I secure my home WiFi network?"
- "What is a VPN and do I need one?"
- "How to detect if someone is using my WiFi?"

### 🦠 Malware Protection
- "How do I know if my computer has a virus?"
- "What's the difference between antivirus and antimalware?"
- "How can I protect against ransomware?"

### 🎣 Phishing Prevention
- "How to identify phishing emails?"
- "What is social engineering?"
- "What should I do if I clicked on a suspicious link?"

## 🛠️ Troubleshooting

### Common Issues and Solutions

1. **API Key Error**
   ```
   Error: API key not found
   ```
   ➡️ Make sure your `.env` file exists and contains the correct API key

2. **Module Not Found**
   ```
   ModuleNotFoundError: No module named 'streamlit'
   ```
   ➡️ Run `pip install -r requirements.txt` again

3. **Port Already in Use**
   ```
   Error: Port 8501 is already in use
   ```
   ➡️ Stop other Streamlit applications or use `streamlit run app.py --server.port 8502`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/AI-chatbot&type=Date)](https://star-history.com/#yourusername/AI-chatbot&Date)

## 📞 Support

Need help? Here's how to get support:

- 📧 Open an issue
- 💬 Start a discussion
- 🌟 Star the repo to show support

---

<div align="center">
Made with ❤️ by Wole

If you find this project helpful, please consider giving it a ⭐
</div> 