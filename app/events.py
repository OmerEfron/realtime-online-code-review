from flask_socketio import SocketIO, emit
import app
import app.code_block


# Create a SocketIO instance
socketio = SocketIO()


# The handle_connect function is called when a new client connects to the SocketIO server.
@socketio.on("connect")
def handle_connect():
    print("connected!")


# The handle_edit_code function is called when a client sends an edit_code event. The event data contains the id of the code block to be edited and the new code.
@socketio.on("edit_code")
def handle_edit_code(id, new_code):
    # Get the code block from the database
    requested_code_block = app.db.session.get(app.code_block.DBCodeBlock, id)

    # Update the code block with the new code
    requested_code_block.code = new_code

    # Check the code block to see if it is now fixed
    fixed = requested_code_block.check_code()

    # Commit the changes to the database
    app.db.session.commit()

    # Emit a code_change event to all clients, with the updated code block data
    emit("code_change", {"codeBlockId": id, "newCode": new_code, "isFixed": fixed}, broadcast=True)
