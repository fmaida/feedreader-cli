from setuptools import setup

setup(
    name="feedreader",
    version="1.0.0",
    packages=["feedreader"],
    url="https://github.com/fmaida/feedreader-cli",
    license="MIT",
    author="Francesco Maida",
    author_email="fran@cesco.it",
    description="A very simple RSS Feed reader that works from the CLI.",
    install_requires=["click", "feedparser", "newspaper3k", "html2text"],
    entry_points = {
        "console_scripts": ["feedreader = feedreader.__main__:main"],
    }
)
