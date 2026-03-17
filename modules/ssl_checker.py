import ssl
import socket
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def run_ssl(target):
    console.print(f"\n[bold cyan][ SSL Certificate Details: {target} ][/bold cyan]\n")
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=target) as s:
            s.connect((target, 443))
            cert = s.getpeercert()

        table = Table(show_header=False, box=box.ROUNDED)
        table.add_column("Field", style="cyan", width=25)
        table.add_column("Value", style="white")

        subject = dict(x[0] for x in cert.get("subject", []))
        issuer  = dict(x[0] for x in cert.get("issuer", []))

        not_before = cert.get("notBefore", "?")
        not_after  = cert.get("notAfter", "?")

        try:
            expiry = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            days_left = (expiry - datetime.utcnow()).days
            expiry_str = f"{not_after} ({days_left} days left)"
        except:
            expiry_str = not_after

        table.add_row("Common Name",     subject.get("commonName", "?"))
        table.add_row("Organization",    subject.get("organizationName", "?"))
        table.add_row("Issued By",       issuer.get("organizationName", "?"))
        table.add_row("Valid From",      not_before)
        table.add_row("Valid Until",     expiry_str)
        table.add_row("Serial Number",   str(cert.get("serialNumber", "?")))
        table.add_row("Version",         str(cert.get("version", "?")))
        table.add_row("Protocol",        s.version() if hasattr(s, "version") else "TLS")

        sans = []
        for san_type, san_value in cert.get("subjectAltName", []):
            sans.append(san_value)
        table.add_row("Alt Names", ", ".join(sans[:5]))

        console.print(table)

        if days_left < 30:
            console.print(f"[bold red]WARNING: Certificate expires in {days_left} days![/bold red]")
        else:
            console.print(f"[bold green]Certificate is valid for {days_left} more days[/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
