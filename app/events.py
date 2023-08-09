from flask_socketio import SocketIO, emit
import app
import app.code_block
socketio = SocketIO()

@socketio.on("connect")
def handle_connect():
    print("connected!")

@socketio.on("edit_code")
def handle_edit_code(id, new_code):
    requested_code_block = app.db.session.get(app.code_block.DBCodeBlock, id)
    requested_code_block.code = new_code
    fixed = requested_code_block.check_code()
    app.db.session.commit()
    emit("code_change", {"codeBlockId": id, "newCode": new_code, "isFixed": fixed}, broadcast=True)