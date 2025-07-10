#!/usr/bin/env python3
"""
Nmap Custom Scanning Tool
Author: [Your Name]
GitHub: [Your GitHub Profile]

A user-friendly interface for Nmap scans with advanced output options.
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime

# ASCII Art for the tool header
ASCII_ART = """
  _   _                              
 | \ | | __ _ _ __ ___   ___  _ __  
 |  \| |/ _` | '_ ` _ \ / _ \| '_ \ 
 | |\  | (_| | | | | | | (_) | | | |
 |_| \_|\__,_|_| |_| |_|\___/|_| |_|
                                    
 Custom Nmap Scanning Tool v1.0
"""

# Scan types with descriptions
SCAN_TYPES = {
    "1": {"name": "Quick Scan", "command": "-T4 -F"},
    "2": {"name": "Intense Scan", "command": "-T4 -A -v"},
    "3": {"name": "Full Scan", "command": "-p- -T4 -A -v"},
    "4": {"name": "Ping Scan", "command": "-sn"},
    "5": {"name": "OS Detection", "command": "-O"},
    "6": {"name": "Service Detection", "command": "-sV"},
    "7": {"name": "Vulnerability Scan", "command": "--script vuln"},
    "8": {"name": "Custom Scan", "command": ""},
}

# Output formats
OUTPUT_FORMATS = {
    "1": {"name": "Normal", "option": "-oN"},
    "2": {"name": "Grepable", "option": "-oG"},
    "3": {"name": "XML", "option": "-oX"},
    "4": {"name": "All Formats", "option": "-oA"},
}

def print_banner():
    """Print the tool banner"""
    print(ASCII_ART)
    print("=" * 50)

def check_nmap_installed():
    """Check if Nmap is installed on the system"""
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_scan_type():
    """Prompt user to select a scan type"""
    print("\n[+] Select Scan Type:")
    for key, value in SCAN_TYPES.items():
        print(f" {key}. {value['name']}")
    
    while True:
        choice = input("> Enter your choice (1-8): ")
        if choice in SCAN_TYPES:
            if choice == "8":  # Custom scan
                custom_cmd = input("> Enter your custom Nmap options: ")
                SCAN_TYPES[choice]["command"] = custom_cmd
            return SCAN_TYPES[choice]
        print("Invalid choice. Please try again.")

def get_output_options():
    """Prompt user for output options"""
    print("\n[+] Output Options:")
    for key, value in OUTPUT_FORMATS.items():
        print(f" {key}. {value['name']}")
    
    while True:
        choice = input("> Select output format (1-4): ")
        if choice in OUTPUT_FORMATS:
            output_option = OUTPUT_FORMATS[choice]["option"]
            break
        print("Invalid choice. Please try again.")
    
    filename = input("> Enter output filename (without extension): ") or f"nmap_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    return output_option, filename

def get_target():
    """Prompt user for target"""
    while True:
        target = input("\n> Enter target (IP, hostname, or subnet): ").strip()
        if target:
            return target
        print("Target cannot be empty. Please try again.")

def build_nmap_command(scan_type, output_option, filename, target):
    """Build the Nmap command"""
    base_cmd = ["nmap"]
    
    # Add scan options
    if scan_type["command"]:
        base_cmd.extend(scan_type["command"].split())
    
    # Add output options
    base_cmd.extend([output_option, filename])
    
    # Add target
    base_cmd.append(target)
    
    return base_cmd

def run_scan(command):
    """Execute the Nmap scan"""
    print("\n[+] Starting Nmap scan...")
    print(f"Command: {' '.join(command)}")
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        
        # Check for errors
        stderr = process.stderr.read()
        if stderr:
            print("\n[!] Errors occurred during scan:")
            print(stderr)
        
        return process.returncode == 0
    
    except Exception as e:
        print(f"\n[!] Error executing Nmap: {str(e)}")
        return False

def main():
    """Main function"""
    print_banner()
    
    # Check if Nmap is installed
    if not check_nmap_installed():
        print("[!] Nmap is not installed or not in PATH. Please install Nmap first.")
        sys.exit(1)
    
    # Get scan parameters
    target = get_target()
    scan_type = get_scan_type()
    output_option, filename = get_output_options()
    
    # Build and run command
    command = build_nmap_command(scan_type, output_option, filename, target)
    success = run_scan(command)
    
    # Display results
    if success:
        print("\n[+] Scan completed successfully!")
        print(f"Results saved to: {filename}.*")
    else:
        print("\n[!] Scan encountered errors")
    
    print("\nThank you for using Nmap Custom Scanning Tool!")

if __name__ == "__main__":
    # Also support command-line arguments
    parser = argparse.ArgumentParser(description="Nmap Custom Scanning Tool")
    parser.add_argument("-t", "--target", help="Target IP/hostname/subnet")
    parser.add_argument("-s", "--scan", type=int, choices=range(1, 9), 
                        help="Scan type (1-8, see --list-scans)")
    parser.add_argument("-o", "--output", help="Output filename (without extension)")
    parser.add_argument("-f", "--format", type=int, choices=range(1, 5),
                        help="Output format (1-4, see --list-formats)")
    parser.add_argument("--list-scans", action="store_true", 
                        help="List available scan types and exit")
    parser.add_argument("--list-formats", action="store_true",
                        help="List available output formats and exit")
    parser.add_argument("--custom", help="Custom Nmap options (use with -s 8)")
    
    args = parser.parse_args()
    
    if args.list_scans:
        print("Available scan types:")
        for key, value in SCAN_TYPES.items():
            print(f" {key}. {value['name']}")
            if value['command']:
                print(f"    Command: nmap {value['command']} <target>")
        sys.exit(0)
    
    if args.list_formats:
        print("Available output formats:")
        for key, value in OUTPUT_FORMATS.items():
            print(f" {key}. {value['name']} (option: {value['option']})")
        sys.exit(0)
    
    if args.target or args.scan or args.output or args.format:
        # Command-line mode
        if not args.target:
            print("Error: Target is required in command-line mode")
            parser.print_help()
            sys.exit(1)
        
        scan_type = SCAN_TYPES.get(str(args.scan or "1"), SCAN_TYPES["1"])
        if args.scan == 8 and args.custom:
            scan_type["command"] = args.custom
        
        output_option = OUTPUT_FORMATS.get(str(args.format or "1"), OUTPUT_FORMATS["1"])["option"]
        filename = args.output or f"nmap_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        command = build_nmap_command(scan_type, output_option, filename, args.target)
        success = run_scan(command)
        
        if success:
            print("\n[+] Scan completed successfully!")
            print(f"Results saved to: {filename}.*")
        else:
            print("\n[!] Scan encountered errors")
    else:
        # Interactive mode
        main()
