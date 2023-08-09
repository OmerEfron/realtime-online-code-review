from flask import Blueprint, render_template, request, session, redirect
from modules.code_block import CodeBlock
lobby_blueprint = Blueprint("lobby", __name__)
code_block_blueprint = Blueprint("code_block", __name__)

async_example = CodeBlock("Async Example", """
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

array_manipulation = CodeBlock("Array Manipulation", """
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
const sum = doubledNumbers.reduce((acc, curr) => acc + curr, 0);
console.log('Doubled Numbers:', doubledNumbers);
console.log('Sum:', sum);
""")

dummy_data = {async_example.get_id(): async_example, array_manipulation.get_id():array_manipulation}

user_roles = {}

mentor_assigned = False

@lobby_blueprint.route("/lobby")
def lobby_route():
    validate_mentor()
    return render_template("lobby.html", code_blocks=dummy_data)


@code_block_blueprint.route("/code-block/<id>")
def code_block_route(id):
    validate_mentor()
    user_role = session.get("role")
    requested_code_block = dummy_data[int(id)]
    return render_template("code-block.html", code_block=requested_code_block, user_role=user_role)

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
