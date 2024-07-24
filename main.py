import markdown2

def markdown_to_html(markdown_text):
    html = markdown2.markdown(markdown_text)
    return html

def wrap_with_template(html_content, title="Markdown to HTML"):
    template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return template

def convert_markdown_file(input_file, output_file):
    with open(input_file, 'r') as f:
        markdown_text = f.read()
    html_content = markdown_to_html(markdown_text)
    full_html = wrap_with_template(html_content)
    with open(output_file, 'w') as f:
        f.write(full_html)

input_markdown_file = 'example.md'
output_html_file = 'example.html'
convert_markdown_file(input_markdown_file, output_html_file)
