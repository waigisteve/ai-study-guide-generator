# 🧠 AI Study Guide Generator

[![GitHub](https://img.shields.io/github/license/waigisteve/ai-study-guide-generator)](https://github.com/waigisteve/ai-study-guide-generator/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/gradio-4.44.0-orange.svg)](https://gradio.app/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com/)

An intelligent, interactive web application that automatically generates comprehensive study guides for any topic using OpenAI's GPT-4o-mini model. Built with Gradio for a seamless user experience.

## 🌟 Features

- **🤖 AI-Powered Generation**: Leverages OpenAI's GPT-4o-mini for intelligent content creation
- **📚 Comprehensive Study Guides**: Generates structured guides with:
  - Topic overview and key concepts
  - Detailed explanations with examples
  - Action steps for learning
  - Practice questions and exercises
- **🌐 Web Interface**: Clean, intuitive Gradio-based UI
- **⚡ Fast Response**: Optimized with 800 token limit for quick generation
- **🔧 Error Handling**: Robust error management with user-friendly messages
- **🚀 Multi-Platform**: Works locally and on Hugging Face Spaces
- **📱 Responsive Design**: Accessible on desktop and mobile devices

## 🎯 Use Cases

- **Students**: Create study materials for exams and coursework
- **Educators**: Generate teaching materials and lesson plans
- **Professionals**: Develop training guides for new skills
- **Self-Learners**: Structure learning paths for personal development
- **Content Creators**: Generate educational content outlines

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/waigisteve/ai-study-guide-generator.git
   cd ai-study-guide-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   PORT=7860
   ```

   Or set environment variables directly:
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="your_openai_api_key_here"
   
   # Windows Command Prompt
   set OPENAI_API_KEY=your_openai_api_key_here
   
   # Linux/Mac
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the app**
   
   Open your browser and navigate to `http://localhost:7860`

## 🛠️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | None | ✅ Yes |
| `PORT` | Port for the Gradio server | 7860 | ❌ No |

### API Settings

The application uses the following OpenAI API configuration:
- **Model**: GPT-4o-mini
- **Max Tokens**: 800
- **Temperature**: 0.3 (for consistent, focused responses)

## 📖 Usage

1. **Enter a Topic**: Type any subject you want to study in the input field
   
   Examples:
   - "PostgreSQL indexing"
   - "Machine Learning algorithms"
   - "React.js hooks"
   - "Spanish conjugation"

2. **Generate Study Guide**: Click the "Generate Study Guide" button

3. **Review Results**: The AI will create a structured study guide including:
   - Overview of the topic
   - Key concepts and definitions
   - Practical examples
   - Learning action steps

## 🏗️ Project Structure

```
ai-study-guide-generator/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (create this)
└── .gitignore           # Git ignore rules (recommended)
```

## 🔧 Dependencies

- **gradio** (4.44.0): Web interface framework
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management

## 🌐 Live Demo

Try the application without installation:

**🤗 Hugging Face Space**: [AI Study Guide Generator](https://huggingface.co/spaces/waigisteve/ai-study-guide-generator)

## 🔒 Security & Privacy

- **API Key Protection**: Environment variables prevent accidental exposure
- **No Data Storage**: User inputs and generated content are not stored
- **Secure Communication**: All API calls use HTTPS
- **Rate Limiting**: Inherits OpenAI's built-in rate limiting

## 🐛 Troubleshooting

### Common Issues

1. **"Error contacting OpenAI API"**
   - Verify your OpenAI API key is correct
   - Check your internet connection
   - Ensure you have sufficient API credits

2. **"Module not found" errors**
   - Run `pip install -r requirements.txt`
   - Verify Python version (3.8+)

3. **Port already in use**
   - Change the PORT environment variable
   - Kill existing processes on port 7860

### Getting Help

If you encounter issues:
1. Check the [Issues](https://github.com/waigisteve/ai-study-guide-generator/issues) page
2. Create a new issue with:
   - Error message
   - Steps to reproduce
   - System information

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 🔮 Roadmap

Future enhancements planned:

- [ ] **Multiple AI Models**: Support for different LLMs
- [ ] **Export Options**: PDF, Word, and Markdown export
- [ ] **Template System**: Customizable study guide templates
- [ ] **User Accounts**: Save and manage study guides
- [ ] **Collaborative Features**: Share and edit guides
- [ ] **Mobile App**: Native mobile application
- [ ] **Offline Mode**: Local model support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing the GPT-4o-mini API
- **Gradio** team for the excellent web framework
- **Hugging Face** for hosting and platform support
- **Python Community** for the amazing ecosystem

## 📞 Contact

**Steve Waigi** - [@waigisteve](https://github.com/waigisteve)

**Project Link**: [https://github.com/waigisteve/ai-study-guide-generator](https://github.com/waigisteve/ai-study-guide-generator)

---

⭐ **Star this repository if you found it helpful!**

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/waigisteve/ai-study-guide-generator?style=social)
![GitHub forks](https://img.shields.io/github/forks/waigisteve/ai-study-guide-generator?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/waigisteve/ai-study-guide-generator?style=social)

*Last updated: October 2025*