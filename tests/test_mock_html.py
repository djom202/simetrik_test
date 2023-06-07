import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def mock_html():
    html_content = """
    <html>
        <body>
            <main class="container">
                <h2>When to use</h2>
                <p>This is a paragraph</p>
                <h2>Resources</h2>
                <p>JSONPlaceholder comes with a set of 6 common resources:</p>
            <main>
        </body>
    </html>
    """
    return html_content

def test_mock_html(mock_html, mocker):
    mocker.patch("builtins.open", mocker.mock_open(read_data=mock_html))

    soup = BeautifulSoup(mock_html, "html.parser")

    assert soup.body.find_all("h2")[1].text == "Resources"
    assert soup.body.find_all("p")[1].text == "JSONPlaceholder comes with a set of 6 common resources:"