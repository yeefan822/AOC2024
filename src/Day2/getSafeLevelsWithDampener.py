def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    count = 0
    
    if all(1 <= diff <= 3 for diff in differences):
        return True
    elif all(-3 <= diff <= -1 for diff in differences):
        return True
    
    return False
    
    
def can_be_safe_with_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports_with_dampener(file_path):
    with open(file_path, 'r') as file:
        reports = [[int(x) for x in line.split()] for line in file]
    
    safe_count = 0
    for report in reports:
        if is_safe(report) or can_be_safe_with_removal(report):
            safe_count += 1
    return safe_count
    
file_path = "Data.txt"
safe_count = count_safe_reports_with_dampener(file_path)
print(f"Number of safe reports: {safe_count}")


