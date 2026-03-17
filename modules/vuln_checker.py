import requests
import httpx
from rich.console import Console
from rich.table import Table

console = Console()

def check_headers(target):
    if not target.startswith("http"):
        target = f"http://{target}"
    try:
        r = requests.get(target, timeout=5, verify=False)
        headers = r.headers

        security_headers = {
            "X-Frame-Options"           : "Clickjacking Protection",
            "X-XSS-Protection"          : "XSS Protection",
            "X-Content-Type-Options"    : "MIME Sniffing Protection",
            "Strict-Transport-Security" : "HSTS",
            "Content-Security-Policy"   : "CSP",
            "Referrer-Policy"           : "Referrer Policy",
            "Permissions-Policy"        : "Permissions Policy",
        }

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Header", style="cyan", width=35)
        table.add_column("Description", style="white", width=25)
        table.add_column("Status", style="yellow")

        for header, desc in security_headers.items():
            if header in headers:
                table.add_row(header, desc, "[green]Present ✓[/green]")
            else:
                table.add_row(header, desc, "[red]Missing ✗[/red]")

        console.print("\n[bold yellow]── Security Headers Check ──[/bold yellow]")
        console.print(table)

        console.print("\n[bold yellow]── Server Info ──[/bold yellow]")
        console.print(f"[cyan]Server    :[/cyan] {headers.get('Server', 'Hidden')}")
        console.print(f"[cyan]Powered By:[/cyan] {headers.get('X-Powered-By', 'Hidden')}")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def check_ssl(target):
    try:
        r = httpx.get(f"https://{target}", timeout=5)
        console.print("\n[bold yellow]── SSL Check ──[/bold yellow]")
        console.print(f"[green]SSL Certificate: Valid ✓[/green]")
        console.print(f"[cyan]Status Code: {r.status_code}[/cyan]")
    except httpx.ConnectError:
        console.print("\n[red]SSL Certificate: Invalid or Not Found ✗[/red]")
    except Exception as e:
        console.print(f"[bold red]SSL Error:[/bold red] {e}")

def run_vuln(target):
    console.print(f"\n[bold cyan]═══ Vulnerability Checker: {target} ═══[/bold cyan]\n")
    check_headers(target)
    check_ssl(target)
