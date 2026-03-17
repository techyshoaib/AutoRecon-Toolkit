import httpx
import asyncio
from rich.console import Console
from rich.table import Table

console = Console()

DIRS = [
    "admin", "login", "dashboard", "uploads", "backup",
    "config", "api", "test", "dev", "staging", "wp-admin",
    "phpmyadmin", "robots.txt", "sitemap.xml", ".env",
    "static", "media", "images", "css", "js", "files",
    "db", "sql", "old", "new", "temp", "tmp", "logs"
]

async def check_dir(client, url):
    try:
        r = await client.get(url, timeout=5)
        return url, r.status_code
    except:
        return url, None

async def scan_dirs(target):
    if not target.startswith("http"):
        target = f"http://{target}"

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("URL", style="cyan", width=45)
    table.add_column("Status", style="yellow", width=10)
    table.add_column("Result", style="green")

    found = 0
    async with httpx.AsyncClient(verify=False) as client:
        tasks = [check_dir(client, f"{target}/{d}") for d in DIRS]
        results = await asyncio.gather(*tasks)

        for url, status in results:
            if status:
                if status == 200:
                    table.add_row(url, str(status), "[green]Found ✓[/green]")
                    found += 1
                elif status in [301, 302]:
                    table.add_row(url, str(status), "[yellow]Redirect →[/yellow]")
                    found += 1
                elif status == 403:
                    table.add_row(url, str(status), "[red]Forbidden ✗[/red]")

    if found == 0:
        console.print("[red]Nothing found![/red]")
    else:
        console.print(table)
        console.print(f"\n[bold green]Total Found: {found}[/bold green]")

def run_dirbrute(target):
    console.print(f"\n[bold cyan]═══ Directory Bruteforce: {target} ═══[/bold cyan]\n")
    asyncio.run(scan_dirs(target))
