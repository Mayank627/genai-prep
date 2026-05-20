#Python vs Java
#Java code
#public class User{
#    public String name;
#    public User(String name){
#        this.name = name;
#    }
#}

#Python code

class User:
    def __init__(self, name):
        self.name = name        
#In Java, we have to define the type of the variable (String name), and we have to create a constructor to initialize the variable. 
# In Python, we can simply define the variable in the __init__ method, and we don't have to specify the type of the variable.
#Now calling the method
u = User("Alice")
print(u.name)