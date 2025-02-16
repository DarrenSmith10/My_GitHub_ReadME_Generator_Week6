# Create a GitHub README.md Generator Using Python

## Challenge

This week's challenge is **mandatory**! 🚀

You will put to good use the **new skills** you've learned and create a **README.md generator** that you can use for your real GitHub repositories.

Your Python script should:

1. **Prompt the user** for project details using `InquirerPy`:

   - **Project Title**: A concise and descriptive title.
   - **Project Description**: A brief explanation of what the project does.
   - **Installation Instructions**: Steps to install dependencies and set up the project.
   - **Usage Instructions**: How to run and use the project.
   - **License Selection**: Choose from a list of common licenses.
   - **Contact / Author Information**: Provide ways to contact the author.

2. **Use `Rich`** to enhance the user experience with **colored text and structured output**.
3. **Use Python file operations** to generate a properly formatted `README.md` file.
4. **Provide feedback** to the user once the README is successfully created.

## License Options

The script should allow the user to select a license from the following list using **InquirerPy**:

1. **MIT License** – Permissive, allows modification and distribution with attribution.
2. **Apache License 2.0** – Similar to MIT but includes patent protection.
3. **GNU General Public License (GPL v3)** – Strong copyleft, modifications must remain open-source.
4. **GNU Lesser General Public License (LGPL v3)** – Weak copyleft, allows use in proprietary software.
5. **Mozilla Public License 2.0 (MPL 2.0)** – Hybrid license, modified files must stay open-source.
6. **Creative Commons Licenses (CC0, CC BY, etc.)** – For non-code assets like documentation.
7. **Unlicense** – Public domain dedication, no restrictions.

## Key Learnings

- How to create **interactive prompts** using `InquirerPy`.
- How to format **user-friendly console output** using `Rich`.
- How to **generate markdown files dynamically** using Python.
- How to **write to files** using Python file operations.

## User Story

As a developer,  
I want to generate a well-structured `README.md` file easily,  
So that I can quickly document my GitHub projects.

## Acceptance Criteria

- The script must prompt the user for:
  - Project title, description, installation instructions, usage instructions, license, and author details.
- The script must allow **license selection** using **InquirerPy**.
- The script must use **Rich** to enhance user feedback and display success messages.
- The script must generate a **properly formatted `README.md` file**.
- **Hints for Implementation**:
  - Approach 1: Use a **template file** with placeholder tags.
  - Approach 2: Generate the markdown dynamically using **string literals/concatenation**.

## Setting Up the Environment\*\*

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# Windows:
myenv\Scripts\activate

# macOS/Linux:
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Example

![Week 6 Image](week6.gif)

## Deployment

The application will **not be deployed**, so instead:

- Create a **walkthrough video** demonstrating how the application works.
- You can use **QuickTime + YouTube** or **ScreenCastify** for recording.

## Submission

- Submit a **link to your project's repository**.
- Include a **link to the walkthrough video** (YouTube or ScreenCastify).

## Useful Online Resources

- [InquirerPy Documentation](https://inquirerpy.readthedocs.io/en/latest/)
- [Rich Documentation](https://rich.readthedocs.io/en/latest/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub README Best Practices](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes)
