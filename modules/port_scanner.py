import nmap
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

SCAN_TYPES = {
    "quick"      : "--top-ports 100 -T4 --open",
    "full"       : "-p- -T4 --open",
    "os"         : "-O --osscan-guess -T4",
    "udp"        : "--top-ports 20 -sU -T4",
    "vuln"       : "--top-ports 20 --script=vuln -T4",
    "script"     : "--top-ports 20 -sC -T4",
    "aggressive" : "--top-ports 20 -A -T4",
    "firewall"   : "--top-ports 20 -sA -T4",
}

def print_table(title, columns, rows):
    if not rows:
        console.print(f"[red]No results for {title}[/red]")
        return
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED, title=f"[bold cyan]{title}[/bold cyan]")
    for col, style, width in columns:
        table.add_column(col, style=style, width=width)
    for row in rows:
        table.add_row(*row)
    console.print(table)

def run_portscan(target, scan_type="quick", ports=None, custom_args=None):
    console.print(f"\n[bold cyan][ Port Scanner: {target} ][/bold cyan]\n")
    nm = nmap.PortScanner()

    try:
        if custom_args:
            args = custom_args
            console.print(f"[yellow]Running Custom Scan: {args}[/yellow]")
        elif ports:
            args = f"-p {ports} -sV -T4"
            console.print(f"[yellow]Scanning Custom Ports: {ports}[/yellow]")
        else:
            args = SCAN_TYPES.get(scan_type, SCAN_TYPES["quick"])
            console.print(f"[yellow]Running {scan_type.upper()} Scan...[/yellow]")

        nm.scan(target, arguments=args)
        rows = []

        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                for port in sorted(nm[host][proto].keys()):
                    d = nm[host][proto][port]
                    rows.append((
                        str(port),
                        proto.upper(),
                        d.get("name", ""),
                        d.get("state", ""),
                        d.get("product", ""),
                        d.get("version", "")
                    ))

        print_table(
            f"{scan_type.upper()} Scan Results",
            [("Port","cyan",8),("Proto","magenta",8),("Service","green",15),("State","white",10),("Product","yellow",20),("Version","white",15)],
            rows
        )

        # OS info agar available ho
        for host in nm.all_hosts():
            if "osmatch" in nm[host]:
                os_rows = []
                for osmatch in nm[host]["osmatch"][:3]:
                    osclass = osmatch.get("osclass", [{}])[0]
                    os_rows.append((osmatch.get("name","?"), osmatch.get("accuracy","?") + "%", osclass.get("osfamily","?")))
                print_table("OS Detection", [("OS Name","cyan",35),("Accuracy","green",10),("Family","yellow",15)], os_rows)

        # Script output agar available ho
        script_rows = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                for port in sorted(nm[host][proto].keys()):
                    for name, output in nm[host][proto][port].get("script", {}).items():
                        script_rows.append((str(port), name, output[:80]))
        if script_rows:
            print_table("Script Results", [("Port","cyan",8),("Script","yellow",25),("Output","white",50)], script_rows)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
