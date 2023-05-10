# Obsidian-Cornell-Notes-Generator
Use LLM to generate Obsidian timeline style Cornell notes


<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
Obsidian-Cornell-Notes-Generator
</h1>
<h3 align="center">📍 Make Note-Taking Effortless with Obsidian-Cornell Notes Generator!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="template" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="idx" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

Obsidian-Cornell-Notes-Generator is an open source project that provides an automated way to generate Cornell-style notes from Obsidian notes. Using the powerful Obsidian graph engine

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
repo
├── gpt_notes.py
├── LICENSE
├── main.py
├── __pycache__
│   ├── gpt_notes.cpython-311.pyc
│   └── main.cpython-311.pyc
├── README.md
└── templates
    └── index.html

2 directories, 7 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Root</summary>

| File         | Summary                                                                                                                                                                                                           | Module       |
|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| gpt_notes.py | This code imports the OpenAI API and dotenv library , loads the dotenv file , and sets the OpenAI API key . It then defines two functions : split_prompt ( ) which splits a text into parts and sends them to the | gpt_notes.py |
| main.py      | This code creates a Flask web application that takes in text input from a user , processes it using the generate_notes function from the gpt_notes module , and returns the processed text as a JSON response .   | main.py      |

</details>

<details closed><summary>Templates</summary>

| File       | Summary                                                                                                                                                          | Module               |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
| index.html | This code creates a web app using Flask that takes in text from a textarea and processes it using an AJAX call . The output is then displayed in a pre element . | templates/index.html |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the Obsidian-Cornell-Notes-Generator repository:
```sh
git clone https://github.com/KenWuqianghao/Obsidian-Cornell-Notes-Generator
```

2. Change to the project directory:
```sh
cd Obsidian-Cornell-Notes-Generator
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Using Obsidian-Cornell-Notes-Generator

```sh
python main.py
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `Apache License 2.0` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.
