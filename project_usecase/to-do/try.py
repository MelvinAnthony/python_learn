def update_task(t_u_id, new_status=None, new_description=None):
    if t_u_id in tasks:
        if new_status in ["Pending", "Done"]:
            tasks[t_u_id]["status"] = new_status
        if new_description:
            tasks[t_u_id]["description"] = new_description
        print("Task updated successfully!")
    else:
        print("Invalid ID")
# Example tasks
tasks = {
    "abc123": {"description": "Buy groceries", "status": "Pending"},
    "xyz789": {"description": "Finish homework", "status": "Pending"}
}

# Update status
update_task("abc123", new_status="Done")