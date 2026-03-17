import argparse
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich import box
from pyfiglet import figlet_format
from termcolor import colored

console = Console()

def banner():
    ascii_banner = figlet_format("AutoRecon", font="slant")
    print(colored(ascii_banner, "red"))
    console.print(Panel.fit(
        "[bold yellow]  Ethical Hacking Automation Toolkit  [/bold yellow]\n"
        "[bold green]       For Educational Purposes Only      [/bold green]\n"
        "[bold cyan]          Made on Kali Linux               [/bold cyan]",
        border_style="red",
        box=box.DOUBLE
    ))
    print()

def show_manual():
    console.print(Panel(
        "[bold red][ LEGAL DISCLAIMER ][/bold red]\n\n"
        "[white]> Only use on systems you OWN or have PERMISSION to test[/white]\n"
        "[white]> Author holds NO responsibility for any misuse[/white]\n"
        "[white]> You are SOLELY responsible for your actions[/white]\n"
        "[white]> Unauthorized scanning is a CRIMINAL OFFENSE[/white]\n",
        border_style="red", box=box.DOUBLE
    ))

    console.print(Panel(
        "[bold cyan][ USAGE ][/bold cyan]\n\n"
        "[green]python3 main.py -t <TARGET> -m <MODULE> [OPTIONS][/green]\n\n"
        "[bold cyan][ FLAGS ][/bold cyan]\n\n"
        "[yellow]-t[/yellow]   --target      Target domain or IP        [white]e.g: -t google.com[/white]\n"
        "[yellow]-m[/yellow]   --module      Module to run              [white]e.g: -m dns[/white]\n"
        "[yellow]-o[/yellow]   --output      Output report name         [white]e.g: -o myreport[/white]\n"
        "[yellow]-s[/yellow]   --scan-type   Nmap scan type             [white]e.g: -s os[/white]\n"
        "[yellow]-p[/yellow]   --ports       Custom ports               [white]e.g: -p 80,443[/white]\n"
        "[yellow]-a[/yellow]   --args        Custom nmap arguments      [white]e.g: -a '-sV -T4'[/white]\n"
        "[yellow]-h[/yellow]   --help        Show this manual\n",
        border_style="cyan", box=box.ROUNDED
    ))

    console.print(Panel(
        "[bold cyan][ MODULES ][/bold cyan]\n\n"
        "[bold green]whois[/bold green]\n"
        "    Fetches domain registration info\n"
        "    > Registrar, Creation Date, Expiry, Name Servers, Emails\n"
        "    [white]python3 main.py -t google.com -m whois[/white]\n\n"

        "[bold green]dns[/bold green]\n"
        "    Fetches all DNS records of a domain\n"
        "    > A, AAAA, MX, NS, TXT, CNAME, SOA, PTR, SRV, CAA\n"
        "    [white]python3 main.py -t google.com -m dns[/white]\n\n"

        "[bold green]ssl[/bold green]\n"
        "    Shows SSL certificate details\n"
        "    > Owner, Issuer, Valid dates, Days left, Alt Names\n"
        "    [white]python3 main.py -t google.com -m ssl[/white]\n\n"

        "[bold green]http[/bold green]\n"
        "    Analyzes HTTP headers and cookies\n"
        "    > Security headers, Response info, Cookies\n"
        "    [white]python3 main.py -t google.com -m http[/white]\n\n"

        "[bold green]portscan[/bold green]\n"
        "    Scans open ports and running services\n"
        "    > Port, Protocol, Service, State, Version\n"
        "    [white]python3 main.py -t google.com -m portscan[/white]\n\n"

        "[bold green]subdomain[/bold green]\n"
        "    Discovers active subdomains\n"
        "    > Subdomain list with resolved IPs\n"
        "    [white]python3 main.py -t google.com -m subdomain[/white]\n\n"

        "[bold green]dirbrute[/bold green]\n"
        "    Finds hidden directories and files\n"
        "    > URLs, HTTP status codes, redirects\n"
        "    [white]python3 main.py -t google.com -m dirbrute[/white]\n\n"

        "[bold green]vuln[/bold green]\n"
        "    Checks security headers and SSL certificate\n"
        "    > Missing headers, SSL status, server info\n"
        "    [white]python3 main.py -t google.com -m vuln[/white]\n\n"

        "[bold green]all[/bold green]\n"
        "    Runs all modules at once\n"
        "    [white]python3 main.py -t google.com -m all[/white]\n",
        border_style="green", box=box.ROUNDED
    ))

    console.print(Panel(
        "[bold cyan][ SCAN TYPES (-s flag) ][/bold cyan]\n\n"
        "[yellow]quick[/yellow]        Top 100 ports fast scan          [white]default[/white]\n"
        "               python3 main.py -t example.com -m portscan -s quick\n\n"
        "[yellow]full[/yellow]         All 65535 ports scan\n"
        "               python3 main.py -t example.com -m portscan -s full\n\n"
        "[yellow]os[/yellow]           OS Detection                     [white]needs sudo[/white]\n"
        "               sudo python3 main.py -t example.com -m portscan -s os\n\n"
        "[yellow]udp[/yellow]          UDP ports scan                   [white]needs sudo[/white]\n"
        "               sudo python3 main.py -t example.com -m portscan -s udp\n\n"
        "[yellow]vuln[/yellow]         NSE Vulnerability scripts        [white]needs sudo[/white]\n"
        "               sudo python3 main.py -t example.com -m portscan -s vuln\n\n"
        "[yellow]script[/yellow]       NSE default scripts\n"
        "               python3 main.py -t example.com -m portscan -s script\n\n"
        "[yellow]aggressive[/yellow]   Full aggressive scan             [white]needs sudo[/white]\n"
        "               sudo python3 main.py -t example.com -m portscan -s aggressive\n\n"
        "[yellow]firewall[/yellow]     Firewall / ACL detection         [white]needs sudo[/white]\n"
        "               sudo python3 main.py -t example.com -m portscan -s firewall\n",
        border_style="yellow", box=box.ROUNDED
    ))

    console.print(Panel(
        "[bold cyan][ CUSTOM PORTS & ARGS ][/bold cyan]\n\n"
        "[yellow]Specific ports:[/yellow]\n"
        "    python3 main.py -t example.com -m portscan -p 80,443,8080\n\n"
        "[yellow]Port range:[/yellow]\n"
        "    python3 main.py -t example.com -m portscan -p 1-1000\n\n"
        "[yellow]Single port:[/yellow]\n"
        "    python3 main.py -t example.com -m portscan -p 22\n\n"
        "[yellow]Custom nmap args:[/yellow]\n"
        "    python3 main.py -t example.com -m portscan -a '-sV -p 22,80'\n\n"
        "[yellow]Combine scan type + ports:[/yellow]\n"
        "    sudo python3 main.py -t example.com -m portscan -s os -p 80,443\n",
        border_style="magenta", box=box.ROUNDED
    ))

    console.print(Panel(
        "[bold cyan][ EXAMPLES ][/bold cyan]\n\n"
        "[white]WHOIS lookup:[/white]\n"
        "    python3 main.py -t google.com -m whois\n\n"
        "[white]DNS records:[/white]\n"
        "    python3 main.py -t google.com -m dns\n\n"
        "[white]SSL certificate:[/white]\n"
        "    python3 main.py -t google.com -m ssl\n\n"
        "[white]HTTP headers:[/white]\n"
        "    python3 main.py -t google.com -m http\n\n"
        "[white]Quick port scan:[/white]\n"
        "    python3 main.py -t 192.168.1.1 -m portscan\n\n"
        "[white]OS Detection:[/white]\n"
        "    sudo python3 main.py -t 192.168.1.1 -m portscan -s os\n\n"
        "[white]Specific ports:[/white]\n"
        "    python3 main.py -t example.com -m portscan -p 22,80,443\n\n"
        "[white]Subdomain enum:[/white]\n"
        "    python3 main.py -t example.com -m subdomain\n\n"
        "[white]Full scan + report:[/white]\n"
        "    sudo python3 main.py -t example.com -m all -o myscan\n",
        border_style="white", box=box.ROUNDED
    ))

    console.print(Panel(
        "[bold green][ ALLOWED USE ][/bold green]\n\n"
        "[white]+ Your own systems and networks[/white]\n"
        "[white]+ CTF challenges[/white]\n"
        "[white]+ Systems with explicit written permission[/white]\n"
        "[white]+ Educational lab environments[/white]\n\n"
        "[bold red][ PROHIBITED USE ][/bold red]\n\n"
        "[white]- Scanning without permission[/white]\n"
        "[white]- Government or military systems[/white]\n"
        "[white]- Financial or banking systems[/white]\n"
        "[white]- Any system you do not own[/white]\n",
        border_style="yellow", box=box.ROUNDED
    ))

def run_with_progress(label, func, *args):
    with Progress(
        SpinnerColumn(spinner_name="dots", style="bold red"),
        TextColumn(f"[bold cyan]{label}[/bold cyan]"),
        BarColumn(bar_width=30, style="red", complete_style="green"),
        TextColumn("[bold green]{task.percentage:>3.0f}%[/bold green]"),
        TimeElapsedColumn(),
        console=console,
        transient=False
    ) as progress:
        task = progress.add_task(label, total=100)
        for i in range(0, 60, 10):
            time.sleep(0.1)
            progress.update(task, advance=10)
        func(*args)
        progress.update(task, completed=100)

def main():
    banner()
    parser = argparse.ArgumentParser(description="AutoRecon Toolkit", add_help=False)
    parser.add_argument("-t", "--target",    help="Target domain or IP")
    parser.add_argument("-m", "--module",    choices=["portscan","subdomain","dirbrute","whois","vuln","dns","ssl","http","all"])
    parser.add_argument("-o", "--output",    default="report")
    parser.add_argument("-s", "--scan-type", default="quick",
                        choices=["quick","full","os","udp","vuln","script","aggressive","firewall"])
    parser.add_argument("-p", "--ports",     default=None)
    parser.add_argument("-a", "--args",      default=None)
    parser.add_argument("-h", "--help",      action="store_true")
    args = parser.parse_args()

    if args.help or not args.target:
        show_manual()
        return

    console.print(Panel(
        f"[bold green]Target    :[/bold green] [white]{args.target}[/white]\n"
        f"[bold green]Module    :[/bold green] [white]{args.module}[/white]\n"
        f"[bold green]Scan Type :[/bold green] [white]{args.scan_type}[/white]\n"
        f"[bold green]Ports     :[/bold green] [white]{args.ports or 'default'}[/white]\n"
        f"[bold green]Output    :[/bold green] [white]{args.output}[/white]",
        title="[bold red][ Scan Info ][/bold red]",
        border_style="cyan", box=box.ROUNDED
    ))
    print()

    if args.module == "whois" or args.module == "all":
        from modules.whois_lookup import run_whois
        run_with_progress("WHOIS Lookup", run_whois, args.target)

    if args.module == "dns" or args.module == "all":
        from modules.dns_lookup import run_dns
        run_with_progress("DNS Lookup", run_dns, args.target)

    if args.module == "ssl" or args.module == "all":
        from modules.ssl_checker import run_ssl
        run_with_progress("SSL Check", run_ssl, args.target)

    if args.module == "http" or args.module == "all":
        from modules.http_analyzer import run_http
        run_with_progress("HTTP Analyzer", run_http, args.target)

    if args.module == "portscan" or args.module == "all":
        from modules.port_scanner import run_portscan
        run_with_progress("Port Scanning", run_portscan, args.target, args.scan_type, args.ports, args.args)

    if args.module == "subdomain" or args.module == "all":
        from modules.subdomain_enum import run_subdomain
        run_with_progress("Subdomain Enum", run_subdomain, args.target)

    if args.module == "dirbrute" or args.module == "all":
        from modules.dir_bruteforce import run_dirbrute
        run_with_progress("Dir Bruteforce", run_dirbrute, args.target)

    if args.module == "vuln" or args.module == "all":
        from modules.vuln_checker import run_vuln
        run_with_progress("Vuln Checker", run_vuln, args.target)

    from reports.report_generator import generate_report
    generate_report(args.target, args.module, [], args.output)

    console.print(Panel(
        f"[bold green]Scan Complete[/bold green]\n"
        f"[bold cyan]Report saved: {args.output}_{args.target}.html[/bold cyan]",
        border_style="green", box=box.DOUBLE
    ))

if __name__ == "__main__":
    main()
