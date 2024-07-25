import markdown2

def markdown_to_html(markdown_text):
    html = markdown2.markdown(markdown_text)
    return html

def wrap_with_template(html_content, title="Markdown to HTML"):
    css = """
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 25px;
            background-color: #010020;
            color: #f1f1f1;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #00bec4;
        }

        h4, h5, h6 {
            color: #00ffaa;
        }
        pre {
            background: #333;
            color: white;
            padding: 10px;
            overflow-x: auto;
        }
        code {
            background: #34373c;
            padding: 2px 4px;
        }
        blockquote {
            border-left: 4px solid #4CAF50;
            padding-left: 10px;
            color: #666;
            margin: 20px 0;
        }
    </style>
    """

    template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        {css}
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
