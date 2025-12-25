🗡️ Ultimate Pentest Commander

Your simple commands, made powerful.
A unified interface for penetration testing that uses only your exact commands - no fancy syntax, no complicated options. Just fill in the blanks and watch it work.

https://img.shields.io/badge/Demo-Live%20Output-brightgreen https://img.shields.io/badge/Python-3.8+-blue https://img.shields.io/badge/License-MIT-yellow https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-purple

✨ Why This Exists

Ever tired of:

· Remembering complex command syntax? ❌
· Manually typing long penetration testing commands? ❌
· Not seeing live progress during attacks? ❌
· Results scattered everywhere? ❌

Ultimate Pentest Commander fixes all that. It's not another pentesting tool - it's YOUR tools made easier.

🚀 Features That Matter

📁 Directory Discovery

```bash
# YOUR Gobuster command - unchanged:
sudo gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt --exclude-length 18979

# YOUR Dirb command - unchanged:
dirb http://target.com /usr/share/wordlists/dirb/common.txt
```

🔓 Wireless Attacks

```bash
# YOUR OneShot command - unchanged:
sudo python3 OneShot/oneshot.py -i wlan0 -K
```

🔐 Login Brute Force

```bash
# YOUR Hydra command - unchanged:
sudo hydra -t 4 -V -f -l admin -P /usr/share/wordlists/rockyou.txt github.com http-post-form "/login:Username or email address=^USER^&Password=^PASS^&Login=Sign in:F=Incorrect username or password."

# Simple Medusa:
medusa -h 192.168.1.1 -u admin -P /usr/share/wordlists/rockyou.txt -M http
```

🎭 Social Engineering

```bash
# Launch SEToolkit:
setoolkit
```

👂 MITM Attacks

```bash
# Bettercap:
sudo bettercap -iface eth0

# MITMproxy:
mitmproxy -p 8080
```

🔍 Reconnaissance

```bash
# Nmap scan:
nmap -sV -sC 192.168.1.1

# SQL injection test:
sqlmap -u 'http://test.com/page?id=1' --batch
```

📦 Installation

Quick Start (30 seconds)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ultimate-pentest-commander.git
cd ultimate-pentest-commander

# 2. Install dependencies
chmod +x simple_attack.py

# 3. Run it
sudo python3 simple_attack.py
```

Required Tools

The commander works with these tools (install what you need):

```bash
# Basic toolkit
sudo apt install gobuster dirb hydra medusa nmap sqlmap

# Wireless tools
git clone https://github.com/drygdryg/OneShot.git
sudo apt install aircrack-ng reaver

# Social engineering
sudo apt install set

# MITM tools
sudo apt install bettercap mitmproxy
```

🎯 How It Works

1. Choose Your Attack

```
ULTIMATE SIMPLE COMMANDER
============================================================
YOUR TOOLS:
 1. 📁 Gobuster (Directory scan)
 2. 📁 Dirb (Directory scan)
 3. 🔓 OneShot (WPS attack)
 4. 🔐 Hydra (Login brute force)
 5. ⚡ Medusa (Fast login attacks)
 6. 🎭 SEToolkit (Social engineering)
 7. 👂 Bettercap (MITM attacks)
 8. 🌐 MITMproxy (Web interception)
 9. 🔍 Nmap (Port scanning)
10. 💉 SQLMap (SQL injection)
11. ⚡ Quick All-in-One Scan
12. 🚪 Exit
```

2. Fill in the Blanks

```
📁 GOBUSTER DIRECTORY SCAN
Target URL (https://example.com): https://target.com
Wordlist [/usr/share/wordlists/dirb/common.txt]: [ENTER]
```

3. Watch Live Progress

```
🚀 Running: sudo gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt --exclude-length 18979
------------------------------------------------------------
===============================================================
Gobuster v3.6
===============================================================
[+] Url:                     https://target.com
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                common.txt
[+] Negative Status codes:   404
===============================================================
/admin                (Status: 403) [Size: 199]
/images               (Status: 301) [Size: 243]
✅ Done! Output saved to: results/20241224_143022/gobuster.txt
```

📊 Results Organization

All results are automatically organized:

```
results/
└── 20241224_143022/                    # Timestamped session
    ├── gobuster_target_com.txt         # Gobuster results
    ├── oneshot_wlan0.txt              # OneShot output
    ├── hydra_github_com.txt           # Hydra results
    ├── nmap_192.168.1.1.txt           # Nmap scan
    └── quick_scan_summary.txt         # Quick scan results
```

⚡ Quick All-in-One Mode

The Quick All-in-One Scan (Option 11) automates everything:

1. Nmap for port/service discovery
2. Gobuster for web directory enumeration
3. Hydra for common login testing
4. All results saved and organized

Perfect for initial reconnaissance!

🔧 Customization

Add Your Own Commands

Edit the script to add your favorite tools:

```python
def run_your_tool(self):
    """Your custom tool"""
    target = input("Target: ").strip()
    # YOUR command here
    cmd = f"your_tool --target {target} --option value"
    self.run_command_live(cmd, "your_tool")
```

Modify Wordlists

Default wordlist paths are easily changeable in the __init__ method.

⚠️ Legal & Ethical Use

IMPORTANT: This tool is for:

· ✅ Testing your own systems
· ✅ Authorized penetration testing
· ✅ Educational purposes
· ✅ CTF challenges

NEVER use for:

· ❌ Unauthorized system access
· ❌ Illegal activities
· ❌ Malicious purposes

By using this tool, you agree to use it only on systems you own or have explicit written permission to test.

🛠️ Troubleshooting

"Command not found"

```bash
# Install missing tools
sudo apt install [tool-name]

# For OneShot:
git clone https://github.com/drygdryg/OneShot.git
cd OneShot
# Make sure oneshot.py is in the commander directory
```

"Permission denied"

```bash
# Some tools need sudo
sudo python3 simple_attack.py
```

No live output

· Make sure you're using Python 3.8+
· Some tools buffer output; use stdbuf -o0 if needed

🌟 Pro Tips

1. Save time with the Quick All-in-One Scan for initial recon
2. Review results in the timestamped directories
3. Combine tools - use Nmap findings to target Gobuster scans
4. Always save output - everything is auto-logged
5. Start simple - use common wordlists first, then go big

🤝 Contributing

Found a bug? Want to add your favorite tool?

1. Fork the repository
2. Create a feature branch
3. Add your tool (keeping commands SIMPLE)
4. Submit a pull request

Guidelines:

· Keep commands simple and user-friendly
· Maintain live output display
· Include error handling
· Document your addition

📄 License

MIT License - see LICENSE for details.

⭐ Support

If this tool saves you time:

· Give it a ⭐ on GitHub
· Share with fellow pentesters
· Report issues or suggest features

---

Remember: With great power comes great responsibility. Use wisely, test ethically, and hack the planet (legally)! 🔒

---

Made with ❤️ for the penetration testing community
