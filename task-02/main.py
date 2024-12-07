


def get_cats_info(path):
    result = []
    
    try:
        with open(path, "r") as data:
            cat_list = [data.strip() for data in data.readlines()]
    except FileNotFoundError:
        print("ERROR MESSAGE: File not found")
       
    for i in cat_list:
        item = i.split(",")
        cat = {"id": item[0], "name": item[1], "age": int(item[2])}
        result.append(cat)

    return result


cats_info = get_cats_info("task-02/cats_file.txt")
print("cats_info >>", cats_info)