class Task:
    def __init__(self, id, description, status, createdAt, updateAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updateAt = updateAt

    def __str__(self):
        return f"id: {self.id}, \ndescription: {self.description}, \nstatus: {self.status}, \ncreatedAt: {self.createdAt} \nupdateAt: {self.updateAt}"
