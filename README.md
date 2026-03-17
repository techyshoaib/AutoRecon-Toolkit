# AutoRecon Toolkit

> For Educational Purposes Only — Use only on systems you own or have permission to test.

---

## About the Author

> *"Still in college, already breaking systems — ethically."*

A 2nd Year Computer Engineering Student and Certified Ethical Hacker who goes
beyond textbooks and builds real-world security tools from scratch.

**Instagram:** [@root.ascend](https://www.instagram.com/root.ascend)

---

## Legal Disclaimer

By using this tool, you agree that:

- You will only use this tool on systems you own or have explicit written permission to test
- The author holds absolutely no responsibility for any misuse or damage caused
- You are solely responsible for all your actions
- Unauthorized scanning is a criminal offense under cybercrime laws worldwide
- If you use this tool for illegal activities, you alone are responsible for all legal consequences

---

## Features

- WHOIS Lookup
- DNS Records
- SSL Certificate Details
- HTTP Headers Analyzer
- Port Scanner (8 scan types)
- Subdomain Enumeration
- Directory Bruteforce
- Vulnerability Checker
- Technology Detector
- IDOR Finder
- HTML Report Generator

---

## Requirements

- Kali Linux / Ubuntu
- Python 3.8+
- Nmap

---

## Installation

Clone the repository and install dependencies:

    git clone https://github.com/YOUR_USERNAME/AutoRecon-Toolkit.git
    cd AutoRecon-Toolkit
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    sudo apt install nmap -y

---

## Usage

    python3 main.py -t TARGET -m MODULE [OPTIONS]

Flags:
    -t   Target domain or IP       e.g: -t google.com
    -m   Module to run             e.g: -m all
    -o   Output report name        e.g: -o myreport
    -s   Nmap scan type            e.g: -s os
    -p   Custom ports              e.g: -p 80,443
    -a   Custom nmap args          e.g: -a '-sV -T4'
    -h   Show manual

---

## Modules

    whois      Domain registration info
    dns        All DNS records
    ssl        SSL certificate details
    http       HTTP headers and cookies
    portscan   Open ports and services
    subdomain  Active subdomains
    dirbrute   Hidden directories
    vuln       Security headers check
    tech       Technology stack detection
    idor       IDOR parameters finder
    all        Run all modules

---

## Scan Types

    quick        Top 100 ports          no sudo needed
    full         All 65535 ports        no sudo needed
    os           OS Detection           needs sudo
    udp          UDP ports              needs sudo
    vuln         NSE Vuln scripts       needs sudo
    script       NSE default scripts    no sudo needed
    aggressive   Full aggressive scan   needs sudo
    firewall     Firewall detection     needs sudo

---

## Examples

    python3 main.py -t google.com -m whois
    python3 main.py -t google.com -m dns
    python3 main.py -t google.com -m ssl
    python3 main.py -t google.com -m http
    python3 main.py -t google.com -m tech
    python3 main.py -t google.com -m idor
    sudo python3 main.py -t 192.168.1.1 -m portscan -s os
    python3 main.py -t google.com -m portscan -p 22,80,443
    sudo python3 main.py -t google.com -m all -o myreport

---

## Allowed Use

- Your own systems and networks
- CTF challenges
- Systems with explicit written permission
- Educational lab environments

## Prohibited Use

- Scanning without permission
- Government or military systems
- Financial or banking systems
- Any system you do not own

---

AutoRecon Toolkit - Learn. Hack. Protect.
