import markdown2
from weasyprint import HTML

# Read the Markdown file
with open('input.md', 'r') as file:
    markdown_content = file.read()

# Convert Markdown to HTML with LaTeX support
html_content = markdown2.markdown(
    markdown_content,
    extras=['fenced-code-blocks', 'mathjax']  # Enable MathJax for LaTeX support
)

# Save HTML to a file
with open('output.html', 'w') as file:
    file.write(html_content)

# Convert HTML to PDF
HTML(string=html_content).write_pdf('output.pdf')
