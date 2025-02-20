# Multilanguage Invoice Extractor 📄🧾

Welcome to **Multilanguage Invoice Extractor**! 🚀 This AI-powered tool helps you extract valuable insights from invoices in multiple languages using **Gemini Pro LLM**. Whether you're dealing with English, Spanish, French, or any other language, this smart extractor gets the job done efficiently. Just upload an invoice and let the AI do the work! 🔥

## ✨ Features
✅ **Multilingual Invoice Understanding** - Extract details from invoices in various languages.  
✅ **AI-Powered Extraction** - Uses Google's **Gemini Pro** for high-accuracy text comprehension.  
✅ **Image & PDF Processing** - Upload images of invoices for seamless analysis.  
✅ **Fast & Lightweight** - Built with **Streamlit** for an interactive and responsive experience.  
✅ **Secure API Handling** - Uses **python-dotenv** to manage API keys safely.  
✅ **Vector Database Support** - Employs **FAISS & ChromaDB** for efficient text retrieval.  

## 🚀 Tech Stack
- **Google Gemini Pro** - State-of-the-art AI model for intelligent document analysis.
- **Streamlit** - A user-friendly web app interface.
- **LangChain** - For structured LLM integration.
- **PyPDF2** - Parses PDF files to extract text.
- **FAISS & ChromaDB** - Vector databases for optimized information retrieval.
- **Python-dotenv** - Manages API keys securely.
- **PIL (Pillow)** - For handling and displaying images.

## 🎯 How It Works
1. **Upload an Invoice Image** 📂 - Select an image file (JPG, PNG, JPEG).
2. **Enter Your Query** 📝 - Ask a question about the invoice.
3. **Get AI-Powered Insights** ⚡ - Receive structured responses instantly.
4. **View Extracted Data** 🔍 - See important details clearly.

## 🛠 Installation & Setup
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```
Set up your **.env** file with the necessary API keys:
```bash
GOOGLE_API_KEY=your_google_api_key
```
Run the Streamlit app:
```bash
streamlit run app.py
```

## 📢 Future Enhancements
🔹 Support for **PDF invoice uploads** 📜  
🔹 Table extraction for structured invoice data 📊  
🔹 Export results to CSV/Excel 📂  


---
Experience the future of invoice processing with **Multilanguage Invoice Extractor!** 🚀📄💡
