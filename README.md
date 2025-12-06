# 📄 PDF to Word Converter

A simple and efficient **PDF to Word (.docx) converter** that works using a clean folder-based workflow.  
Just drop your PDF files into the `input` folder, run the script, and get editable Word documents in the `output` folder — no complicated UI needed.

---
## 🚀 Features

- 📂 **Folder-based workflow** — works with `input` and `output` directories
- 🧾 **Batch conversion** — converts all PDFs inside the `input` folder
- ✏️ **Editable Word files** — output is generated as `.docx`
- 🧱 **Simple project structure** — easy to understand and modify
- ⚠️ **Basic error handling** — safely skips invalid or corrupted PDFs
- 🖥️ **Command-line based** — lightweight and fast to run locally

---

## 🛠️ Tech Stack

| Category            | Tools / Libraries                                           |
| ------------------- | ----------------------------------------------------------- |
| **Language**        | Python 3.x                                                 |
| **Core Script**     | `pdf_to_word.py`                                           |
| **Dependencies**    | Libraries listed in `requirements.txt` (e.g. pdf/docx libs)|
| **File Handling**   | Standard Python `os` / `pathlib` modules                   |
| **Version Control** | Git & GitHub                                               |
| **Environment**     | Virtualenv / venv (recommended)                            |

---

## 📂 Folder Structure

After setting up, your project structure should look like this:

```bash
pdf-to-word-converter/
├── input/               # Put your PDF files here
│   └── sample.pdf
├── output/              # Converted Word files will be saved here
├── pdf_to_word.py       # Main conversion script
└── README.md

* input/ — all the source PDF files

* output/ — all the generated .docx files

* pdf_to_word.py — the code file you will run


## ⚙️ Setup Instructions

To run this project locally:

# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/pdf-to-word-converter.git

# 2️⃣ Navigate to project directory
cd pdf-to-word-converter

# 3️⃣ (Optional but recommended) Create & activate a virtual environment

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS / Linux
python3 -m venv venv
source venv/bin/activate

# 4️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Use (Step-by-Step)

Follow these steps exactly as your project is designed 👇

1️⃣ Create input and output folders (if not already present)

Inside your project folder:

mkdir input
mkdir output
If you cloned the repo and these folders already exist, you can skip this step.

2️⃣ Add a PDF file into the input folder

* Copy any .pdf file you want to convert

* Paste it inside the input folder
Example: input/my-document.pdf

You can add one or multiple PDFs — the script will convert each of them.

3️⃣ Run the code file

Make sure you are inside the project folder, then run:
# On Windows
python pdf_to_word.py

# On macOS / Linux
python3 pdf_to_word.py

What the script does:

Reads all .pdf files from the input/ folder

Converts each PDF into a .docx Word file

Saves the converted files into the output/ folder with the same file name

Example:

input/sample.pdf ➜ output/sample.docx

4️⃣ Check the output folder

After the script finishes:

* Open the output/ folder

* You will see the generated Word files (e.g., my-document.docx)

* Open them in Microsoft Word, LibreOffice, Google Docs, etc. to edit

🔍 Example Workflow

Place notes.pdf and report.pdf in input/

Run:
python pdf_to_word.py

After successful conversion, you will see:
output/
├── notes.docx
└── report.docx
Open notes.docx and report.docx and edit them as normal Word documents ✅

📬 Contact

If you’d like to give feedback, report bugs, or suggest improvements:

📧 Email: manthankadhare@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/manthankadhare/

🐙 GitHub: https://github.com/ManthanKadhare

🌟 Future Improvements

Possible enhancements you can add to this project:

* GUI interface (using Tkinter / PyQt / web UI)

* Drag-and-drop support

* Progress bar or logs for each file

* Support for selecting a single file via command-line arguments

* Export options (e.g., .txt, .html)

🏁 License

This project is open source and available under the MIT License.
Feel free to fork, use, and improve it⭐
