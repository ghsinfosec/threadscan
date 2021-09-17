# Threadscan
### Threaded python port scanner
Threadscan is a threaded port scanner inspired by The Cyber Mentor's course Practical Ethical Hacker. In the course, Heath writes a simple python port scanner and I liked it so I wanted to make a threaded version of it. I had some difficulty with the threading implementation so I took some functionality from [Threader3000](https://github.com/dievus/threader3000) by The Mayor to make it work. Some of the code is my own, though I do not take full credit. This is simply my approach with references where needed.

## Requirements
Python3

Pyperclip

I will not include a requirements.txt since pyperclip is the only special requirement. Install pyperclip by typing:

```bash
pip3 install pyperclip
```

## Installation
```bash
git clone https://github.com/ghsinfosec/threadscan.git
```

You can add a symbolic link to run it from anywhere by typing:

```bash
sudo ln -s $(pwd)/threadscan.py /usr/local/bin/threadscan
```

## Usage
Threadscan takes one arguement, which is the IP or hostname you wish to scan:

```bash
threadscan <ip|hostname>
```

Examples:

```bash
threadscan 10.0.1.10
```
or

```bash
threadscan myhost.mydomain.com
```

## IMPORTANT DISCLAIMER
It is illegal to scan any device or IP address that you do not own or do not have explicit permission to do so. I assume no responsibility for threadscan's use, legal or illegal, nor do I condone, support, or promote unethical behavior in the use of this tool. Please do not scan any device that you do not own or do not have explicit permission to scan. Use this tool at your own risk.
