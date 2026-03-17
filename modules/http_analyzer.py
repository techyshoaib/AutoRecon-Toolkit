import requests
import httpx
from rich.console import Console
from rich.table import Table
from rich import box
import urllib3
urllib3.disable_warnings()

console = Console()

SECURITY_HEADERS = {
    "Strict-Transport-Security" : "HSTS",
    "Content-Security-Policy"   : "CSP",
    "X-Frame-Options"           : "Clickjacking Protection",
    "X-XSS-Protection"          : "XSS Protection",
    "X-Content-Type-Options"    : "MIME Sniffing Protection",
    "Referrer-Policy"           : "Referrer Policy",
    "Permissions-Policy"        : "Permissions Policy",
    "Cache-Control"             : "Cache Control",
    "X-Powered-By"              : "Tech Stack Info",
    "Server"                    : "Server Info",
    "Access-Control-Allow-Origin": "CORS Policy",
}

def run_http(target):
    if not target.startswith("http"):
        target = f"https://{target}"

    console.print(f"\n[bold cyan][ HTTP Headers Analyzer: {target} ][/bold cyan]\n")

    try:
        r = requests.get(target, timeout=10, verify=False)
        headers = r.headers

        # Security Headers
        sec_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED, title="[bold cyan]Security Headers[/bold cyan]")
        sec_table.add_column("Header", style="cyan", width=35)
        sec_table.add_column("Description", style="white", width=25)
        sec_table.add_column("Status", style="yellow", width=12)
        sec_table.add_column("Value", style="green")

        for header, desc in SECURITY_HEADERS.items():
            if header in headers:
                sec_table.add_row(header, desc, "[green]Present[/green]", headers[header][:50])
            else:
                sec_table.add_row(header, desc, "[red]Missing[/red]", "-")

        console.print(sec_table)

        # Response Info
        info_table = Table(show_header=False, box=box.ROUNDED, title="[bold cyan]Response Info[/bold cyan]")
        info_table.add_column("Field", style="cyan", width=20)
        info_table.add_column("Value", style="white")

        info_table.add_row("Status Code",    str(r.status_code))
        info_table.add_row("Response Time",  f"{r.elapsed.total_seconds():.2f}s")
        info_table.add_row("Content Type",   headers.get("Content-Type", "?"))
        info_table.add_row("Content Length", headers.get("Content-Length", "?"))
        info_table.add_row("Encoding",       r.encoding or "?")
        info_table.add_row("Cookies",        str(len(r.cookies)) + " found")

        console.print(info_table)

        # Cookies detail
        if r.cookies:
            cookie_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED, title="[bold cyan]Cookies[/bold cyan]")
            cookie_table.add_column("Name", style="cyan", width=20)
            cookie_table.add_column("Value", style="white", width=30)
            cookie_table.add_column("Secure", style="yellow", width=10)
            for cookie in r.cookies:
                cookie_table.add_row(cookie.name, cookie.value[:30], str(cookie.secure))
            console.print(cookie_table)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
