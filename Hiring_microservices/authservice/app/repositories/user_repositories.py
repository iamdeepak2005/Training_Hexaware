from app.models.user import User

class UserRepository:
    def __init__(self,db):
        self.db=db

    def create_user(self,user:User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self,email:str):
        return self.db.query(User).filter(User.email==email).first()
    
    def get_user_by_id(self,id:int):
        return self.db.query(User).filter(User.id==id).first()
    
    def get_all_users(self):
        return self.db.query(User).all()
    
    def update_user(self,user:User):
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self,user:User):
        self.db.delete(user)
        self.db.commit()
        return user
