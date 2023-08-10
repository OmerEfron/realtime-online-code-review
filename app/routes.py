from flask import Blueprint, render_template, session, jsonify
from .code_block import CodeBlock, DBCodeBlock


# Create two blueprints for the lobby and code_block routes
lobby_blueprint = Blueprint("lobby", __name__)
code_block_blueprint = Blueprint("code_block", __name__)

# A global variable to track if a mentor has been assigned yet
mentor_assigned = False


# The lobby route renders the lobby.html template with a list of all code blocks
@lobby_blueprint.route("/lobby")
def lobby_route():
    validate_mentor()
    user_role = session.get("role")
    data = DBCodeBlock.query.all()
    return render_template("lobby.html", code_blocks=data, user_role=user_role)


# The code_block_route renders the code_block.html template with the code block with the given id
@code_block_blueprint.route("/code-block/<id>")
def code_block_route(id):
    validate_mentor()
    user_role = session.get("role")
    from app import db
    code_block_from_db = db.get_or_404(DBCodeBlock, id)
    return render_template("code-block.html", code_block=code_block_from_db, user_role=user_role)


# The get_code_blocks route returns a JSON list of all code blocks
@lobby_blueprint.route("/get-code-blocks")
def get_code_blocks():
    validate_mentor()
    user_role = session.get("role")
    data = DBCodeBlock.query.all()
    res = []
    for cb in data:
        res.append(cb.to_dict())
    print(res)
    return jsonify(res)


# The get_code_block_by_id route returns a JSON representation of the code block with the given id
@code_block_blueprint.route("/get-code-block/<id>")
def get_code_block_by_id(id):
    validate_mentor()
    user_role = session.get("role")
    from app import db
    code_block_from_db = db.get_or_404(DBCodeBlock, id)
    return code_block_from_db.to_dict()


# The get_user_role route returns the user's role as a JSON object
@lobby_blueprint.route("/get-user-role")
def get_user_role():
    validate_mentor()
    user_role = session.get("role")
    return {'user_role': user_role}


# The validate_mentor function checks if the user has been assigned a role yet. If not, it assigns the user the role of "mentor".
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
