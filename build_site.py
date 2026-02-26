import markdown

# Read markdown
with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Convert to HTML
html_content = markdown.markdown(text, extensions=['tables', 'fenced_code'])

# HTML Template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Autonomous Data Science Workflow</title>
    
    <!-- Open Graph Meta Tags for LinkedIn/Twitter -->
    <meta property="og:title" content="Published Research: Autonomous Multi-Agent Workflows">
    <meta property="og:description" content="Enterprise-grade Python orchestrator utilizing 3 LLM personas to mathematically solve tabular datasets, reducing regression errors by 32%.">
    <meta property="og:image" content="https://raw.githubusercontent.com/sidthebuilder/AutoML-Agent-Orchestrator/main/preview.png">
    <meta property="og:url" content="https://sidthebuilder.github.io/AutoML-Agent-Orchestrator/">
    <meta property="og:type" content="article">

    <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #fdfbf7;
            color: #332f2c;
            font-family: 'Merriweather', serif;
            line-height: 1.8;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 850px;
            margin: 40px auto;
            background: #fff;
            padding: 60px 80px;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(139, 90, 43, 0.08);
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            color: #2c251f;
            margin-top: 1.5em;
        }
        h1 {
            font-size: 2.5em;
            line-height: 1.3;
            text-align: center;
            margin-top: 0;
            border-bottom: 2px solid #e9dfd3;
            padding-bottom: 20px;
        }
        h2 {
            font-size: 1.8em;
            border-bottom: 1px solid #e9dfd3;
            padding-bottom: 10px;
        }
        a {
            color: #8b5a2b;
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: border-bottom 0.2s;
        }
        a:hover {
            border-bottom: 1px solid #8b5a2b;
        }
        code, pre {
            font-family: 'Courier New', Courier, monospace;
            background-color: #f6f3ed;
            border-radius: 4px;
        }
        code {
            padding: 2px 6px;
            font-size: 0.9em;
            color: #8b5a2b;
        }
        pre {
            padding: 20px;
            overflow-x: auto;
            border: 1px solid #e9dfd3;
            border-radius: 8px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            font-family: 'Inter', sans-serif;
            font-size: 0.95em;
        }
        th, td {
            border: 1px solid #e9dfd3;
            padding: 15px;
            text-align: left;
        }
        th {
            background-color: #fdfbf7;
            color: #8b5a2b;
            font-weight: 600;
        }
        tr:nth-child(even) {
            background-color: #faf9f5;
        }
        hr {
            border: 0;
            height: 1px;
            background: #e9dfd3;
            margin: 50px 0;
        }
        strong {
            font-family: 'Inter', sans-serif;
            color: #2c251f;
        }
        @media (max-width: 850px) {
            .container {
                margin: 20px;
                padding: 30px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

# Write to index.html
final_html = html_template.replace('{content}', html_content)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Site built successfully.')
