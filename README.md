```🗡️ Ultimate Pentest Commander```
Are you tired of writing commands in the terminal? Solution is here!!
This script will make your pentesting accuracy at another level.
Now, it's just just selecting your target. Finished ⚠️.

📦 Installation

Quick Start (30 seconds)

```bash
# 1. Clone the repository
git clone https://github.com/taieftech/One_attack.git
```
```bash
# 3. Run it
sudo python3 One_attack/oneattack.py

```
😎 HOW IT WORKS
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



⚡ New Quick All-in-One Mode

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
