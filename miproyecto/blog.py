from flask import(
    render_template,Blueprint,flash,g,redirect,request,url_for
)
from werkzeug.exceptions import abort
from miproyecto.models.post import Post
from miproyecto.models.user import User
from miproyecto.views.auth import login_required
from miproyecto import db

blog=Blueprint('blog',__name__)
#obtener un usuario 
def get_user(id):
    user=User.query.get_or_404(id)
    return user

 