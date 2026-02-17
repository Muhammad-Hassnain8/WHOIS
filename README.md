# WHOIS Domain Lookup Tool

A powerful, colorful command-line WHOIS lookup tool for retrieving comprehensive domain registration information with an beautiful animated interface.

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Output Information](#output-information)
- [Examples](#examples)
- [Requirements](#requirements)

## ✨ Features

- **Colorful Interface**: Beautiful gradient text and emoji-enhanced output
- **Animated Loading**: Visual feedback during WHOIS queries
- **Comprehensive Data**: Retrieves complete domain registration information
- **IP Resolution**: Optional IPv4 and IPv6 address lookup
- **Summary Statistics**: Quick overview of domain status and metrics
- **Multiple Output Formats**: Full details or summary view
- **File Export**: Save results to file (without ANSI colors)
- **Error Handling**: User-friendly error messages
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🔧 Installation

1. **Clone or download** the script:
```bash
git clone <repository-url>
cd whois-tool
```

2. **Install required dependency**:
```bash
pip install python-whois
```

3. **Make the script executable** (Linux/macOS):
```bash
chmod +x main.py
```

## 🚀 Usage

Basic syntax:
```bash
python main.py <domain> [options]
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `domain` | Domain name to lookup (e.g., example.com) |
| `-o, --output FILE` | Save output to specified file |
| `-i, --ip` | Show IP address information |
| `-s, --summary` | Show summary statistics only |
| `-h, --help` | Show help message |

## 📊 Output Information

The tool displays the following information when available:

### Domain Information
- Domain Name(s)
- Registrar
- Registrar URL
- WHOIS Server

### Important Dates
- Creation Date
- Expiration Date
- Last Updated Date

### Technical Details
- Name Servers
- Domain Status
- DNSSEC Information

### Contact Information
- Registrant Email
- Organization
- Country
- City

### Network Information (with `-i` flag)
- IPv4 Address
- IPv6 Address (if available)

### Summary Statistics (with `-s` flag)
- Days until expiration
- Number of name servers
- Registrar information
- Domain status

## 💡 Examples

### Basic WHOIS Lookup
```bash
python main.py example.com
```

### Include IP Information
```bash
python main.py google.com -i
```

### Save Results to File
```bash
python main.py example.com -o domain_info.txt
```

### Summary Statistics Only
```bash
python main.py example.com -s
```

### Multiple Options Combined
```bash
python main.py github.com -i -o github_report.txt
```

## 🖥️ Sample Output

```
╔════════════════════════════════════════════════════════════════╗
║        🌈 WHOIS DOMAIN LOOKUP TOOL - COLORFUL EDITION 🌈        ║
║              Professional Domain Information Scanner              ║
║                                                                  ║
║              Created by: Muhammad Hassnain                      ║
║              Version: 2.0.0                                     ║
╚════════════════════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────┐
│  ℹ️  TARGET DOMAIN: example.com                          │
└────────────────────────────────────────────────────────┘

┌─[ 🌐 DOMAIN INFORMATION ]────────────────────────────────────────┐
▸ Domain Name: EXAMPLE.COM
▸ Registrar: RESERVED
▸ WHOIS Server: whois.iana.org
└──────────────────────────────────────────────────────────┘

┌─[ 📅 IMPORTANT DATES ]──────────────────────────────────────────┐
▸ Created: 1995-08-14 04:00:00
▸ Expires: 2024-08-13 04:00:00
▸ Updated: 2023-08-14 07:01:00
└──────────────────────────────────────────────────────────┘
```

## 📦 Requirements

- **Python**: Version 3.6 or higher
- **Dependencies**:
  - `python-whois` (>= 0.8.0)

## ⚙️ Technical Details

The tool uses:
- `python-whois` library for WHOIS queries
- `socket` for IP resolution
- ANSI escape codes for terminal colors
- `argparse` for command-line argument parsing
- `datetime` for date handling

## 🔄 Version History

**Version 2.0.0**
- Added colorful animated interface
- Implemented gradient text effects
- Added emoji icons for better visualization
- Included summary statistics feature
- Added IPv6 support
- Enhanced error handling

**Version 1.0.0**
- Initial release
- Basic WHOIS functionality
- Simple output formatting

## 🎯 Use Cases

- **System Administrators**: Check domain expiration and status
- **Security Researchers**: Investigate domain ownership
- **Web Developers**: Verify domain availability and details
- **Business Owners**: Monitor domain registration information
- **Students**: Learn about domain registration and DNS

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Submit pull requests

## ⚠️ Notes

- Some WHOIS servers may rate-limit requests
- Not all domains display complete information
- Colors may not display correctly in all terminals
- For Windows, use Command Prompt or PowerShell with VT support

---

**Created by: Muhammad Hassnain**  
**Version: 1.0.0**
