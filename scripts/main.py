from datetime import datetime

with open("reports/Daily_Report.md","w",encoding="utf8") as f:

    f.write("# ETF Guardian\n\n")

    f.write(datetime.now().isoformat())
