

def student_entity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }
    
    
def list_0f_student_entity(db_item_list) -> list:
    list_0f_student = []
    for item in db_item_list:
        list_0f_student.append(student_entity(item))
        
    return list_0f_student