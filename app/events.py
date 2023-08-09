from flask import request
from flask_socketio import SocketIO, emit
from .routes import dummy_data
socketio = SocketIO()

@socketio.on("connect")
def handle_connect():
    print("connected")


@socketio.on("edit_code")
def handle_edit_code(id, new_code):
    requested_code_block = dummy_data[int(id)]
    emit("code_change", {"codeBlockId": id, "newCode": new_code}, broadcast=True)
    requested_code_block.set_code(new_code)
    print(f"code changed to: {new_code}")