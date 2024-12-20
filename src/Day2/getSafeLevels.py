def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    

    if all(1 <= diff <= 3 for diff in differences):
        return True 
    elif all(-3 <= diff <= -1 for diff in differences):
        return True 
    
    return False
    
    
def count_safe_reports(file_path):

    with open(file_path, 'r') as file:
        reports = [[int(x) for x in line.split()] for line in file]
    
    safe_count = sum(is_safe(report) for report in reports)
    return safe_count


file_path = "Data.txt" 
safe_count = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_count}")


