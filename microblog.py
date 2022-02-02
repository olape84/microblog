from app import app 
from app.models import User, Post

@app.shell_context_processor    #co to jest? 
def make_shell_context():
   return {
       "db": db,
       "User": User,
       "Post": Post
   }
