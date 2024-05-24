class user:
    user_count=0
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        user.user_count+=1

    # Getter method for user_name
    def get_user_name(self):
        return self.__user_name

    # Setter method for user_name
    def set_user_name(self, user_name):
        self.__user_name = user_name
