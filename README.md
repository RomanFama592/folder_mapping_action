<div align="center">

# Folder Mapping
![Contributions? Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![Maintained? Yes](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg)
[![Pylint](https://github.com/RomanFama592/folder_mapping_action/actions/workflows/pylint.yml/badge.svg)](https://github.com/RomanFama592/folder_mapping_action/actions/workflows/pylint.yml)
[![readme_updated](https://github.com/RomanFama592/folder_mapping_action/actions/workflows/update_readme.yml/badge.svg)](https://github.com/RomanFama592/folder_mapping_action/actions/workflows/update_readme.yml)

</div>

This project is a **CLI tool** that maps the folder structure of a directory and generates an output file with a customizable name based on a template. The main purpose of this tool is to provide a clear and concise representation of the folder structure, taking into account exclusions defined in the `.gitignore` file to avoid displaying specific files. Skip the files until you find another `.gitignore` file. From that path onwards, exclude the files specified in this new file.

<details>
  <summary>📑 <strong>Contents</strong></summary>
  <ol>
    <li><a href="#project-structure">🚀 <strong>Project Structure</strong></a></li>
    <li><a href="#usage">✨ <strong>Usage</strong></a></li>
    <li><a href="#contributions">👋 <strong>Contributions</strong></a></li>
    <li><a href="#license">👨‍⚖️ <strong>License</strong></a></li>
    <li><a href="#contact-me">📬 <strong>Contact me</strong></a></li>
  </ol>
</details>

<br>

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

## 🚀 Project Structure

Folder map and example of use:

```
/
├── .devcontainer/
│     ├── Dockerfile
│     └── devcontainer.json
├── .github/
│     └── workflows/
│          ├── pylint.yml
│          └── update_readme.yml
├── src/
│     ├── args.py
│     ├── exceptions.py
│     ├── map_folders.py
│     └── short_folders.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── README.md.template
├── action.yml
├── index.py
└── requirements.txt

```

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

## ✨ Usage

```yaml
- uses: RomanFama592/folder_mapping_action@v1
  with:
    path-directory:
    description: "Path to the directory for folder mapping."
    default: "./"

    template-output:
    description: "Path to the template file for README.md generation."
    default: "./README.md.template"
    
    path-output:
    description: "Path where the generated README.md file will be saved."
    default: "./README.md"

    search-word:
    description: "Keyword or search term in the template file for folder mapping."
    default: "map_folder"
```

>_In your template put `%{{` + your **search word** + `}}%` to find where you want to put the map folder._

- Example of use in [README.md.template](https://github.com/RomanFama592/folder_mapping_action/blob/main/README.md.template)

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

## 👋 Contributions

Contributions are what make the Open Source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a Pull Request. You can also simply [open an issue](https://github.com/RomanFama592/folder_mapping_action/issues)

Don't forget to **give the project a star ⭐!** Thanks again!

1. Fork the project

2. Clone your fork

```bash
git clone https://github.com/@your_username/folder_mapping_action
```

3. Create your Feature Branch

```bash
git checkout -b feature/AmazingFeature
```

4. Push to the Branch

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

## 👨‍⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right"><a href="#top">Back to top 🔼</a></p>
<br>

## 📬 Contact me

**Famá Román** 
- famaroman@gmail.com
- [Linkedin](https://www.linkedin.com/in/romanfama)

<p align="right"><a href="#top">Back to top 🔼</a></p>