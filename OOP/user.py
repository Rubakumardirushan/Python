class user:
    user_name= None
    user_password= None
   
    def resgiter(self):
        print("enter your name")
        self.user_name=input()
        print("enter your password")
        self.user_password=input()
        print("user registered")
        print("user name is "+self.user_name)
        print("user password is "+self.user_password)