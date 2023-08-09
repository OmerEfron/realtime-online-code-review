from flask import Blueprint, render_template, session
from .code_block import CodeBlock, DBCodeBlock


lobby_blueprint = Blueprint("lobby", __name__)
code_block_blueprint = Blueprint("code_block", __name__)

mentor_assigned = False

@lobby_blueprint.route("/lobby")
def lobby_route():
    validate_mentor()
    user_role = session.get("role")
    data = DBCodeBlock.query.all()
    return render_template("lobby.html", code_blocks=data, user_role=user_role)


@code_block_blueprint.route("/code-block/<id>")
def code_block_route(id):
    validate_mentor()
    user_role = session.get("role")
    from app import db
    code_block_from_db = db.get_or_404(DBCodeBlock, id)
    return render_template("code-block.html", code_block=code_block_from_db, user_role=user_role)

def validate_mentor():
    global mentor_assigned
    user_role = session.get("role")
    if user_role is None:
        if mentor_assigned:
            session["role"] = "student"
        else:
            session["role"] = "mentor"
            mentor_assigned = True
    elif user_role == "mentor" and not mentor_assigned:
        mentor_assigned = True