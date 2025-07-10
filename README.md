# Nmap Custom Scanning Tool

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

A user-friendly Python wrapper for Nmap that simplifies network scanning with predefined scan profiles, advanced output options, and both interactive and command-line interfaces.

## Features

- 🚀 **Multiple Scan Profiles**: Quick scan, intense scan, full port scan, ping sweep, OS detection, and more
- 📁 **Flexible Output Options**: Save results in normal, grepable, or XML formats
- 🖥️ **Interactive Menu**: Easy-to-use interface for beginners
- 💻 **Command-Line Support**: Scriptable interface for automation
- ⏱️ **Real-time Output**: View scan progress as it happens
- 🛠️ **Custom Scans**: Advanced users can input raw Nmap commands
- 📅 **Automatic Filenaming**: Timestamp-based output filenames by default

## Installation

### Prerequisites
- Python 3.6 or higher
- Nmap installed on your system

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nmap-custom-scanner.git
   cd nmap-custom-scanner
(Optional) Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
Install the requirements:

bash
pip install -r requirements.txt
Make the script executable (Linux/macOS):

bash
chmod +x nmap_scanner.py
Usage
Interactive Mode
bash
./nmap_scanner.py
or

bash
python nmap_scanner.py
Follow the on-screen prompts to select scan type, output format, and target.

Command-Line Mode
bash
./nmap_scanner.py -t 192.168.1.1 -s 2 -o my_scan -f 3
Command-Line Options:
text
-t, --target      Target IP/hostname/subnet (required)
-s, --scan        Scan type (1-8, see --list-scans)
-o, --output      Output filename (without extension)
-f, --format      Output format (1-4, see --list-formats)
--custom          Custom Nmap options (use with -s 8)
--list-scans      List available scan types and exit
--list-formats    List available output formats and exit
Available Scan Types (--list-scans)
Quick Scan (-T4 -F)

Intense Scan (-T4 -A -v)

Full Scan (-p- -T4 -A -v)

Ping Scan (-sn)

OS Detection (-O)

Service Detection (-sV)

Vulnerability Scan (--script vuln)

Custom Scan (specify your own options)

Available Output Formats (--list-formats)
Normal (-oN)

Grepable (-oG)

XML (-oX)

All Formats (-oA)

Examples
Quick scan with default output:

bash
./nmap_scanner.py -t 192.168.1.0/24 -s 1
Full scan with XML output:

bash
./nmap_scanner.py -t example.com -s 3 -f 3 -o full_scan
Custom vulnerability scan:

bash
./nmap_scanner.py -t 10.0.0.5 -s 8 --custom "--script vulners"
Interactive mode with menu:

bash
./nmap_scanner.py
Screenshots
https://screenshots/interactive.png
Interactive mode with menu options

https://screenshots/commandline.png
Command-line mode example

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature-branch)

Create a new Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Nmap and the Nmap community for the amazing network scanning tool

Python developers for the great subprocess and argparse modules

All open source contributors who inspire projects like this

Developed by [Your Name] - [Your GitHub Profile] - [Your Email/Website]

text

## Additional Recommendations for Your Repository:

1. Create a `screenshots` directory and add actual screenshots of your tool in action
2. Add a `.gitignore` file for Python projects
3. Include a simple `requirements.txt` file (even if it's empty or just has optional dependencies)
4. Add a `LICENSE` file (MIT is good for this type of project)
5. Consider adding GitHub Actions for automated testing if you expand the project

This README demonstrates:
- Professional presentation
- Clear documentation
- Understanding of user needs
- Technical writing skills
- Project organization

Would you like me to modify any section or add more details about specific features?
