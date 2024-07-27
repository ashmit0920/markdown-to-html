import markdown2
import re

def markdown_to_html(markdown_text):
    html = markdown2.markdown(markdown_text, extras=["fenced-code-blocks", "tables", "footnotes"])
    return html

def generate_toc(html_content):
    # Generate a table of contents from the headings
    toc = []
    heading_pattern = re.compile(r'<h([1-6])>(.*?)</h\1>')

    def replace_heading(match):
        level = match.group(1)
        title = match.group(2)
        anchor = title.lower().replace(' ', '-')
        toc.append(f'<li class="toc-level-{level}"><a href="#{anchor}">{title}</a></li>')
        return f'<h{level} id="{anchor}">{title}</h{level}>'

    content_with_anchors = re.sub(heading_pattern, replace_heading, html_content)
    toc_html = '<ul class="toc">' + ''.join(toc) + '</ul>'
    return toc_html, content_with_anchors

def wrap_with_template(html_content, title="Markdown to HTML"):
    css = """
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 25px;
            background-color: #0f0f0f;
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
            color: #25c2a0;
        }
        pre {
            background: #333;
            color: white;
            padding: 10px;
            overflow-x: auto;
        }
        code {
            background: #242526;
            color: #25c2a0;
            padding: 2px 4px;
        }
        blockquote {
            border-left: 4px solid #25c2a0;
            padding-left: 10px;
            color: #f08d49;
            margin: 20px 0;
        }
        .toc {
            margin: 20px 0;
            padding: 0;
            list-style: none;
        }
        .toc li {
            margin: 5px 0;
        }
        .toc-level-1 { font-weight: bold; }
        .toc-level-2 { margin-left: 20px; }
        .toc-level-3 { margin-left: 40px; }
    </style>
    """

    toc_html, html_with_anchors = generate_toc(html_content)

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
        <div class="container">
            {toc_html}
            {html_with_anchors}
        </div>
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
    
    return output_file
