#!/usr/bin/env python3
"""
🌈 WHOIS - Colorful Domain Information Lookup Tool
Created by: Muhammad Hassnain
Version: 1.0.0
"""

import socket
import sys
import argparse
import json
from datetime import datetime
import whois as whois_lib
import time

# ========== EXTENDED COLOR PALETTE ==========
class Colors:
    # Regular Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bold Colors
    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_MAGENTA = '\033[1;35m'
    BOLD_CYAN = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    DIM = '\033[2m'
    
    # Reset
    ENDC = '\033[0m'
    
    # Emoji icons
    INFO_ICON = "ℹ️ "
    SUCCESS_ICON = "✅ "
    ERROR_ICON = "❌ "
    WARNING_ICON = "⚠️ "
    DOMAIN_ICON = "🌐 "
    CALENDAR_ICON = "📅 "
    CLOCK_ICON = "⏰ "
    SERVER_ICON = "🖥️ "
    EMAIL_ICON = "📧 "
    LOCATION_ICON = "📍 "
    LINK_ICON = "🔗 "
    STAR_ICON = "⭐ "
    ROCKET_ICON = "🚀 "
    MAGIC_ICON = "✨ "
    FIRE_ICON = "🔥 "

class ColorfulWHOIS:
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Muhammad Hassnain"
        self.colors = Colors()
        
    def animated_banner(self):
        """Display animated banner"""
        banner_lines = [
            f"{self.colors.BOLD_MAGENTA}╔════════════════════════════════════════════════════════════════╗",
            f"{self.colors.BOLD_CYAN}║{self.colors.BOLD_YELLOW}        🌈 WHOIS DOMAIN LOOKUP TOOL - COLORFUL EDITION 🌈        {self.colors.BOLD_CYAN}║",
            f"{self.colors.BOLD_GREEN}║{self.colors.WHITE}              Professional Domain Information Scanner              {self.colors.BOLD_GREEN}║",
            f"{self.colors.BOLD_BLUE}║{self.colors.BOLD_WHITE}                                                                {self.colors.BOLD_BLUE}║",
            f"{self.colors.BOLD_MAGENTA}║{self.colors.BOLD_CYAN}              Created by: {self.colors.BOLD_YELLOW}{self.author}{self.colors.BOLD_CYAN}                      {self.colors.BOLD_MAGENTA}║",
            f"{self.colors.BOLD_RED}║{self.colors.BOLD_GREEN}              Version: {self.colors.BOLD_WHITE}{self.version}{self.colors.BOLD_GREEN}                                  {self.colors.BOLD_RED}║",
            f"{self.colors.BOLD_BLUE}╚════════════════════════════════════════════════════════════════╝{self.colors.ENDC}"
        ]
        
        # Animated reveal
        for line in banner_lines:
            print(line)
            time.sleep(0.1)
        print()
    
    def loading_animation(self, text, duration=1):
        """Show loading animation"""
        animation = "|/-\\"
        for i in range(20):
            time.sleep(duration/20)
            sys.stdout.write(f"\r{self.colors.CYAN}{self.colors.BOLD}{animation[i % 4]} {text}{self.colors.ENDC}")
            sys.stdout.flush()
        print()
    
    def create_gradient_text(self, text, colors):
        """Create gradient colored text"""
        result = ""
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            result += f"{color}{char}{self.colors.ENDC}"
        return result
    
    def display_domain_header(self, domain):
        """Display colorful domain header"""
        gradient_colors = [self.colors.RED, self.colors.YELLOW, self.colors.GREEN, self.colors.CYAN, self.colors.BLUE, self.colors.MAGENTA]
        styled_domain = self.create_gradient_text(domain, gradient_colors)
        
        header = f"""
{self.colors.BOLD_MAGENTA}┌─{self.colors.BOLD_CYAN}─────────────────────────────────────────────────────{self.colors.BOLD_MAGENTA}─┐
{self.colors.BOLD_MAGENTA}│{self.colors.BOLD_YELLOW}  {self.colors.INFO_ICON} TARGET DOMAIN: {styled_domain}{self.colors.BOLD_YELLOW}{' ' * (30 - len(domain))}{self.colors.BOLD_MAGENTA}│
{self.colors.BOLD_MAGENTA}└─{self.colors.BOLD_CYAN}─────────────────────────────────────────────────────{self.colors.BOLD_MAGENTA}─┘{self.colors.ENDC}"""
        print(header)
    
    def lookup_domain(self, domain):
        """Perform WHOIS lookup with animation"""
        try:
            # Clean domain
            domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
            domain = domain.split('/')[0]
            
            self.display_domain_header(domain)
            self.loading_animation(f"{self.colors.MAGIC_ICON} Performing WHOIS magic on {domain}...")
            
            # Perform lookup
            w = whois_lib.whois(domain)
            
            print(f"{self.colors.GREEN}{self.colors.BOLD}{self.colors.SUCCESS_ICON} WHOIS lookup completed successfully!{self.colors.ENDC}\n")
            return w
            
        except Exception as e:
            print(f"{self.colors.RED}{self.colors.BOLD}{self.colors.ERROR_ICON} Error: {str(e)}{self.colors.ENDC}")
            return None
    
    def format_section_header(self, title, icon):
        """Create colorful section header"""
        return f"\n{self.colors.BOLD_MAGENTA}┌─{self.colors.BOLD_CYAN}[{self.colors.BOLD_YELLOW}{icon} {title}{self.colors.BOLD_CYAN}]{self.colors.BOLD_MAGENTA}─" + "─" * (50 - len(title)) + "┐"
    
    def format_key_value(self, key, value, key_color, value_color, indent=0):
        """Format key-value pair with colors"""
        spaces = "  " * indent
        return f"{spaces}{key_color}▸ {key}:{self.colors.ENDC} {value_color}{value}{self.colors.ENDC}"
    
    def format_list_item(self, item, color, bullet="•"):
        """Format list item with color"""
        return f"  {color}{bullet} {item}{self.colors.ENDC}"
    
    def format_whois_output(self, whois_data, show_extra=True):
        """Format WHOIS data with beautiful colors"""
        if not whois_data:
            return ""
        
        output = []
        
        # Main Information Section
        output.append(self.format_section_header("DOMAIN INFORMATION", self.colors.DOMAIN_ICON))
        
        # Domain Name
        if hasattr(whois_data, 'domain_name') and whois_data.domain_name:
            domain_names = whois_data.domain_name
            if isinstance(domain_names, list):
                output.append(self.format_key_value("Domain Names", ", ".join(domain_names[:2]), 
                                                   self.colors.BOLD_CYAN, self.colors.BOLD_GREEN))
            else:
                output.append(self.format_key_value("Domain Name", domain_names, 
                                                   self.colors.BOLD_CYAN, self.colors.BOLD_GREEN))
        
        # Registrar
        if hasattr(whois_data, 'registrar') and whois_data.registrar:
            output.append(self.format_key_value("Registrar", whois_data.registrar, 
                                               self.colors.BOLD_CYAN, self.colors.BOLD_YELLOW))
        
        # Registrar URL
        if hasattr(whois_data, 'registrar_url') and whois_data.registrar_url:
            output.append(self.format_key_value("Registrar URL", whois_data.registrar_url, 
                                               self.colors.BOLD_CYAN, self.colors.BOLD_BLUE))
        
        # WHOIS Server
        if hasattr(whois_data, 'whois_server') and whois_data.whois_server:
            output.append(self.format_key_value("WHOIS Server", whois_data.whois_server, 
                                               self.colors.BOLD_CYAN, self.colors.BOLD_MAGENTA))
        
        output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
        
        # Dates Section
        output.append(self.format_section_header("IMPORTANT DATES", self.colors.CALENDAR_ICON))
        
        # Creation Date
        if hasattr(whois_data, 'creation_date') and whois_data.creation_date:
            dates = whois_data.creation_date
            if isinstance(dates, list):
                output.append(self.format_key_value("Created", str(dates[0]), 
                                                   self.colors.BOLD_GREEN, self.colors.WHITE))
            else:
                output.append(self.format_key_value("Created", str(dates), 
                                                   self.colors.BOLD_GREEN, self.colors.WHITE))
        
        # Expiration Date
        if hasattr(whois_data, 'expiration_date') and whois_data.expiration_date:
            dates = whois_data.expiration_date
            if isinstance(dates, list):
                output.append(self.format_key_value("Expires", str(dates[0]), 
                                                   self.colors.BOLD_RED, self.colors.WHITE))
            else:
                output.append(self.format_key_value("Expires", str(dates), 
                                                   self.colors.BOLD_RED, self.colors.WHITE))
        
        # Updated Date
        if hasattr(whois_data, 'updated_date') and whois_data.updated_date:
            dates = whois_data.updated_date
            if isinstance(dates, list):
                output.append(self.format_key_value("Updated", str(dates[0]), 
                                                   self.colors.BOLD_YELLOW, self.colors.WHITE))
            else:
                output.append(self.format_key_value("Updated", str(dates), 
                                                   self.colors.BOLD_YELLOW, self.colors.WHITE))
        
        output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
        
        # Name Servers Section
        if hasattr(whois_data, 'name_servers') and whois_data.name_servers:
            output.append(self.format_section_header("NAME SERVERS", self.colors.SERVER_ICON))
            name_servers = whois_data.name_servers
            if isinstance(name_servers, list):
                for ns in name_servers[:5]:
                    output.append(self.format_list_item(ns, self.colors.CYAN, "🖧"))
                if len(name_servers) > 5:
                    output.append(f"  {self.colors.DIM}... and {len(name_servers) - 5} more{self.colors.ENDC}")
            else:
                output.append(self.format_list_item(name_servers, self.colors.CYAN, "🖧"))
            output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
        
        # Domain Status Section
        if hasattr(whois_data, 'status') and whois_data.status:
            output.append(self.format_section_header("DOMAIN STATUS", "🔒"))
            statuses = whois_data.status
            if isinstance(statuses, list):
                for status in statuses[:4]:
                    output.append(self.format_list_item(status, self.colors.YELLOW, "🔹"))
                if len(statuses) > 4:
                    output.append(f"  {self.colors.DIM}... and {len(statuses) - 4} more{self.colors.ENDC}")
            else:
                output.append(self.format_list_item(statuses, self.colors.YELLOW, "🔹"))
            output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
        
        # Contact Information Section
        has_contact = False
        contact_section = []
        
        if hasattr(whois_data, 'emails') and whois_data.emails:
            has_contact = True
            emails = whois_data.emails
            if isinstance(emails, list):
                for email in emails:
                    contact_section.append(self.format_list_item(email, self.colors.GREEN, "📧"))
            else:
                contact_section.append(self.format_list_item(emails, self.colors.GREEN, "📧"))
        
        if hasattr(whois_data, 'org') and whois_data.org:
            has_contact = True
            contact_section.append(self.format_key_value("Organization", whois_data.org, 
                                                        self.colors.BOLD_BLUE, self.colors.BOLD_WHITE, 1))
        
        if hasattr(whois_data, 'country') and whois_data.country:
            has_contact = True
            contact_section.append(self.format_key_value("Country", whois_data.country, 
                                                        self.colors.BOLD_BLUE, self.colors.BOLD_WHITE, 1))
        
        if hasattr(whois_data, 'city') and whois_data.city:
            has_contact = True
            contact_section.append(self.format_key_value("City", whois_data.city, 
                                                        self.colors.BOLD_BLUE, self.colors.BOLD_WHITE, 1))
        
        if has_contact:
            output.append(self.format_section_header("CONTACT INFORMATION", self.colors.EMAIL_ICON))
            output.extend(contact_section)
            output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
        
        # DNS Security Section (if available)
        if hasattr(whois_data, 'dnssec') and whois_data.dnssec:
            output.append(self.format_section_header("DNS SECURITY", "🔐"))
            output.append(self.format_key_value("DNSSEC", whois_data.dnssec, 
                                               self.colors.BOLD_CYAN, self.colors.BOLD_GREEN, 1))
            output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
        
        return "\n".join(output)
    
    def get_ip_information(self, domain):
        """Get IP information with colorful output"""
        try:
            domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
            domain = domain.split('/')[0]
            ip = socket.gethostbyname(domain)
            
            output = []
            output.append(self.format_section_header("IP INFORMATION", "🌍"))
            output.append(self.format_key_value("IPv4 Address", ip, self.colors.BOLD_CYAN, self.colors.BOLD_GREEN, 1))
            
            # Try to get IPv6
            try:
                ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
                if ipv6_info:
                    ipv6 = ipv6_info[0][4][0]
                    output.append(self.format_key_value("IPv6 Address", ipv6, self.colors.BOLD_CYAN, self.colors.BOLD_GREEN, 1))
            except:
                pass
            
            output.append(f"{self.colors.BOLD_MAGENTA}└" + "─" * 58 + "┘" + f"{self.colors.ENDC}")
            return "\n".join(output)
        except:
            return None
    
    def show_summary_stats(self, whois_data):
        """Show colorful summary statistics"""
        stats = []
        stats.append(f"\n{self.colors.BOLD_YELLOW}{self.colors.STAR_ICON} DOMAIN SUMMARY {self.colors.STAR_ICON}{self.colors.ENDC}")
        stats.append(f"{self.colors.CYAN}▰" * 60 + f"{self.colors.ENDC}")
        
        # Calculate days until expiration
        if hasattr(whois_data, 'expiration_date') and whois_data.expiration_date:
            exp_date = whois_data.expiration_date
            if isinstance(exp_date, list):
                exp_date = exp_date[0]
            if isinstance(exp_date, datetime):
                days_left = (exp_date - datetime.now()).days
                if days_left > 0:
                    status = f"{self.colors.GREEN}✓ Active ({days_left} days left){self.colors.ENDC}"
                elif days_left == 0:
                    status = f"{self.colors.YELLOW}⚠ Expires today{self.colors.ENDC}"
                else:
                    status = f"{self.colors.RED}✗ Expired ({abs(days_left)} days ago){self.colors.ENDC}"
                stats.append(f"{self.colors.BOLD_WHITE}Domain Status:{self.colors.ENDC} {status}")
        
        # Count name servers
        if hasattr(whois_data, 'name_servers') and whois_data.name_servers:
            ns_count = len(whois_data.name_servers) if isinstance(whois_data.name_servers, list) else 1
            stats.append(f"{self.colors.BOLD_WHITE}Name Servers:{self.colors.ENDC} {self.colors.CYAN}{ns_count}{self.colors.ENDC}")
        
        # Registrar info
        if hasattr(whois_data, 'registrar') and whois_data.registrar:
            stats.append(f"{self.colors.BOLD_WHITE}Registrar:{self.colors.ENDC} {self.colors.MAGENTA}{whois_data.registrar}{self.colors.ENDC}")
        
        stats.append(f"{self.colors.CYAN}▰" * 60 + f"{self.colors.ENDC}")
        return "\n".join(stats)
    
    def save_to_file(self, data, filename):
        """Save output to file with confirmation"""
        try:
            with open(filename, 'w') as f:
                # Remove ANSI color codes for file save
                import re
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                clean_data = ansi_escape.sub('', data)
                f.write(clean_data)
            
            print(f"\n{self.colors.GREEN}{self.colors.BOLD}{self.colors.SUCCESS_ICON} Results saved to: {self.colors.BOLD_WHITE}{filename}{self.colors.ENDC}")
        except Exception as e:
            print(f"\n{self.colors.RED}{self.colors.BOLD}{self.colors.ERROR_ICON} Error saving file: {str(e)}{self.colors.ENDC}")

def main():
    tool = ColorfulWHOIS()
    
    # Show animated banner
    tool.animated_banner()
    
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description=f'{tool.colors.BOLD_CYAN}Colorful WHOIS Lookup Tool{tool.colors.ENDC}',
        epilog=f'{tool.colors.BOLD_GREEN}Example: {tool.colors.BOLD_YELLOW}python whois_colorful.py example.com -o report.txt{tool.colors.ENDC}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'domain',
        help=f'{tool.colors.CYAN}Domain name to lookup (e.g., example.com){tool.colors.ENDC}'
    )
    
    parser.add_argument(
        '-o', '--output',
        help=f'{tool.colors.GREEN}Save output to file{tool.colors.ENDC}'
    )
    
    parser.add_argument(
        '-i', '--ip',
        action='store_true',
        help=f'{tool.colors.YELLOW}Show IP address information{tool.colors.ENDC}'
    )
    
    parser.add_argument(
        '-s', '--summary',
        action='store_true',
        help=f'{tool.colors.MAGENTA}Show summary statistics only{tool.colors.ENDC}'
    )
    
    args = parser.parse_args()
    
    # Perform WHOIS lookup
    whois_data = tool.lookup_domain(args.domain)
    
    if whois_data:
        output_data = []
        
        if args.summary:
            # Show only summary
            summary = tool.show_summary_stats(whois_data)
            output_data.append(summary)
            print(summary)
        else:
            # Show full information
            formatted_output = tool.format_whois_output(whois_data)
            output_data.append(formatted_output)
            print(formatted_output)
        
        # Show IP information if requested
        if args.ip:
            ip_info = tool.get_ip_information(args.domain)
            if ip_info:
                output_data.append("\n" + ip_info)
                print("\n" + ip_info)
            else:
                print(f"\n{tool.colors.YELLOW}{tool.colors.WARNING_ICON} Could not resolve IP address{tool.colors.ENDC}")
        
        # Save to file if specified
        if args.output:
            tool.save_to_file("\n".join(output_data), args.output)
        
        # Show footer
        print(f"\n{tool.colors.BOLD_BLUE}{tool.colors.ROCKET_ICON} WHOIS lookup completed {tool.colors.ROCKET_ICON}{tool.colors.ENDC}")
        
    else:
        print(f"\n{tool.colors.RED}{tool.colors.BOLD}{tool.colors.ERROR_ICON} WHOIS lookup failed for {args.domain}{tool.colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{tool.colors.YELLOW}{tool.colors.BOLD}{tool.colors.WARNING_ICON} Operation cancelled by user{tool.colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{tool.colors.RED}{tool.colors.BOLD}{tool.colors.ERROR_ICON} Unexpected error: {str(e)}{tool.colors.ENDC}")
        sys.exit(1)
