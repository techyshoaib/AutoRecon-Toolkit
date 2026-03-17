import dns.resolver
import concurrent.futures
from rich.console import Console
from rich.table import Table

console = Console()

SUBDOMAINS = [
    "www", "mail", "ftp", "admin", "blog", "dev",
    "test", "api", "shop", "portal", "vpn", "smtp",
    "staging", "app", "cdn", "static", "secure", "login"
]

def check_sub(sub, target):
    full_domain = f"{sub}.{target}"
    try:
        answers = dns.resolver.resolve(full_domain, "A")
        return full_domain, str(answers[0])
    except:
        return None, None

def run_subdomain(target):
    console.print(f"\n[bold cyan]═══ Subdomain Enumeration: {target} ═══[/bold cyan]\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Subdomain", style="cyan", width=35)
    table.add_column("IP Address", style="green", width=20)

    found = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_sub, sub, target): sub for sub in SUBDOMAINS}
        for future in concurrent.futures.as_completed(futures):
            domain, ip = future.result()
            if domain:
                table.add_row(domain, ip)
                found += 1

    if found == 0:
        console.print("[red]No subdomains found![/red]")
    else:
        console.print(table)
        console.print(f"\n[bold green]Total Found: {found}[/bold green]")
