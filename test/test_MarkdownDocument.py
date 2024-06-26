from src.DocGenerator import MarkdownDocument


def test_render_small_heading3():
    doc = MarkdownDocument()
    doc.add_heading3("Heading 3")
    expecting = "### Heading 3\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_render_paragraph():
    doc = MarkdownDocument()
    doc.add_paragraph("Testing nineteen four seven")
    expecting = "Testing nineteen four seven\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_render_codeblock():
    doc = MarkdownDocument()
    doc.add_codeblock("print(Dogs) {...}")
    expecting = "```\nprint(Dogs) {...}\n```\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_escape_markdown():
    doc = MarkdownDocument()
    doc.add_paragraph("# Testing")
    expecting = "\\# Testing\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting

def test_merge_indices():
    doc = MarkdownDocument()
    doc.add_paragraph("Testing 1").add_paragraph("Testing 2").add_paragraph("Testing 3")
    doc.merge_indices(0,1)
    expecting = "Testing 1\nTesting 2\n\nTesting 3\n\n"
    rendered = doc.render()
    rendered = ''.join(rendered)
    assert rendered == expecting
