import whois
from rich.console import Console
from rich.table import Table

console = Console()

def run_whois(target):
    console.print(f"\n[bold cyan]═══ WHOIS Lookup: {target} ═══[/bold cyan]\n")
    try:
        w = whois.whois(target)
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field", style="cyan", width=25)
        table.add_column("Value", style="white")
        fields = {
            "Domain Name"   : w.domain_name,
            "Registrar"     : w.registrar,
            "Creation Date" : str(w.creation_date),
            "Expiry Date"   : str(w.expiration_date),
            "Name Servers"  : str(w.name_servers),
            "Country"       : w.country,
            "Emails"        : str(w.emails),
        }
        for field, value in fields.items():
            if value and value != "None":
                table.add_row(field, str(value))
        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
