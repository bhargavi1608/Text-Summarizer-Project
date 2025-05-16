import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"
REPO_NAME ="Text-Summarizer-Project"
AUTHOR_USER_NAME="bhargavi1608"
SRC_REPO="Text-Summarizer-Project"
AUTHOR_EMAIL="pullojubhargavi211@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer for Notes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhargavi1608/" + REPO_NAME,
)


