log_file = "logs.txt"
report_file = "report.txt"

info = 0
error = 0
warning = 0

with open(log_file, "r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
        elif "ERROR" in line:
            error += 1
        elif "WARNING" in line:
            warning += 1

with open(report_file, "w") as file:
    file.write("Log Summary Report\n")
    file.write("-------------------\n")
    file.write(f"INFO: {info}\n")
    file.write(f"ERROR: {error}\n")
    file.write(f"WARNING: {warning}\n")

print("Report Generated")
