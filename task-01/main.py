


def total_salary(path):
    total = 0

    try:
        with open(path, "r") as data:
            salary_list = [data.strip() for data in data.readlines()]

    except FileNotFoundError:
            print("File not found")
            
         
    for item in salary_list:
        person_salary_str = item.split(",")
        person_salary = int(person_salary_str[1])

        total += person_salary

    avg_salary = int(total / len(salary_list))
    return {total, avg_salary}
    
         

total, avg_salary = total_salary("task-01/salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg_salary}")
