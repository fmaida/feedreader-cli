# Feedreader-CLI

This is a very simple project, based upon the excellent 
`feedparser` library ( <https://pypi.org/project/feedparser/> ).
It allows a user to download an RSS or atom feed and show it 
on the terminal.

*Feedreader* adapts its output to the number of columns 
and rows that your terminal is actually capable of 
displaying. When it has used all the space available
on the screen, it pauses and wait until the user 
press the `ENTER` key to continue, or `q` to quit.

## System requirements

In order to use this app, you'll need to have a copy of 
Python 3.5 or above installed on your computer.

## How to install this app

Install *feedreader* with the following command: 
   `python setup.py install`

## Example of usage

```bash
$ feedreader wired.com -l 3


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
