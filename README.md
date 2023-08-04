# Directory Bee / DIRBEE

![Alt Text](https://i.imgur.com/r7c1KTF.png)

Directory Bee is a simple Python tool for discovering directories on a target website and performing WHOIS lookups. It helps you identify potential hidden or exposed directories on a web server and provides WHOIS information about the target domain.

## Features

- Directory scanning: Discover directories on a target website using a wordlist.
- WHOIS lookup: Perform a WHOIS search for the target domain to retrieve domain registration information.
- User-friendly interface: Interactive command-line interface for ease of use.
- Save reports: Save scan results and WHOIS information to a text file.

## Requirements

- Python 3.7 or higher
- Requests library (`pip install requests`)
- Whois library (`pip install python-whois`)
- Ping3 library (`pip install ping3`)

## Usage

1. Clone this repository or download the ZIP file.
2. Install the required Python libraries using the provided `requirements.txt` file.
3. Run `directory_bee.py` using Python: `python directory_bee.py`.

## How to Use

1. Enter the target URL when prompted. The tool will check if the target is online and provide a response time.
2. Select a wordlist from the available options. The tool will scan the target URL using the selected wordlist.
3. View the found directories and choose whether to perform a WHOIS search.
4. Optionally save the report, including scan results and WHOIS information.

## Terms of Use

Please review and abide by the [Terms of Use](https://github.com/ikilljoy/DirectoryBee/blob/main/Terms%20of%20Use.txt) before using the Directory Bee tool.

## Disclaimer

This tool is provided for educational and ethical purposes only. Unauthorized scanning of websites without proper authorization is illegal. The tool's authors and contributors are not responsible for any misuse or legal consequences resulting from the use of this tool.

## License

DirectoryBee / DIRBEE is released under the [Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

---

![Follow Me on GitHub](https://img.shields.io/github/followers/ikilljoy?label=Follow&style=social)

