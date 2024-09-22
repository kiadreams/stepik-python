def make_header(text: str, level: int = 1):
    return f'<h{level}>{text}</h{level}>'

print(make_header('gfdf'))