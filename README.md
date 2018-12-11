# Feedreader-CLI

This is a very simple project, based upon the excellent 
`feedparser` library ( <https://pypi.org/project/feedparser/> ).
It allows a user to download an RSS or atom feed and show it 
on the terminal.

## Example of usage

```bash
$ ./feedreader.py wired.com -l 3


 1. Elon Musk Abuses Tesla Autopilot on *60 Minutes*
    --------------------------------------------------
    By ignoring his company's instructions, Musk
    risked making the public even more confused about
    how to safely use the semi-autonomous system.
    ==================================================

 2. 5 Questions Congress Should Ask Google's Sundar
    Pichai
    --------------------------------------------------
    Google's CEO will testify before the House
    Judiciary Committee in a hearing focused on
    transparency and search practices.
    ==================================================

 3. Earth's Depths Are Teeming With Otherworldly
    Microbes
    --------------------------------------------------
    Scientists have discovered a vast subterranean
    ecosystem of microbial life deep underground,
    stretching our sense of life's limits.
    ==================================================
```