from flask import Blueprint, render_template, session
from .code_block import CodeBlock, DBCodeBlock


lobby_blueprint = Blueprint("lobby", __name__)
code_block_blueprint = Blueprint("code_block", __name__)

async_example1 = CodeBlock("Async Example", """
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}""")

array_manipulation1 = CodeBlock("Array Manipulation", """
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
const sum = doubledNumbers.reduce((acc, curr) => acc + curr, 0);
console.log('Doubled Numbers:', doubledNumbers);
console.log('Sum:', sum);
""")

dummy_data1 = {async_example1.get_id(): async_example1, array_manipulation1.get_id():array_manipulation1}


mentor_assigned = False

@lobby_blueprint.route("/lobby")
def lobby_route():
    validate_mentor()
    dummy_data2 = DBCodeBlock.query.all()
    return render_template("lobby.html", code_blocks=dummy_data2)


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