class Account:
    def __init__(self, user_name, first, last, password, entry, category):
        self.user_name = user_name
        self.first = first
        self.last = last
        self.password = password
        self.entry = entry
        self.category = category
    #entry is like netflix, hulu, chase, walmart, etc        
    def set_entry(self, entry):
        self.entry = entry
    
    def get_user_name(self):
        return self.user_name
    
    def get_first(self):
        return self.first
    
    def get_last(self):
        return self.last
    
    def get_password(self):
        return self.last

    def get_post_id(self):
        return self.post_id
    
'''
    TODO:
        finish out the setters and getters of each of these attributes
'''