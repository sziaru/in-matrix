# coding: utf-8

from matrix_client import client as Client, api as API

def sign_in_matrix(server, user_id, password):
    client = Client.MatrixClient(server)
    access_token = client.login_with_password(user_id, password)
    return client, access_token

def update_room_details(room):
    room.update_room_name()
    room.update_room_topic()
    room.update_aliases()
