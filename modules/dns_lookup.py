import dns.resolver
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA", "PTR", "SRV", "CAA"]

def run_dns(target):
    console.print(f"\n[bold cyan][ DNS Records Lookup: {target} ][/bold cyan]\n")

    for record in RECORD_TYPES:
        try:
            answers = dns.resolver.resolve(target, record)
            table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
            table.add_column("Type", style="cyan", width=8)
            table.add_column("Value", style="white")
            table.add_column("TTL", style="yellow", width=10)

            for rdata in answers:
                table.add_row(record, str(rdata), str(answers.ttl))

            console.print(table)
        except Exception:
            pass
