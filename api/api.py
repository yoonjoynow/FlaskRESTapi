from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datatime
from models import MessageModel
import status
from pytz import utc

class MessageManager():
    last_id = 0
    def __init__(self):
        self.messages = {}

    def insert_message(self, message):
        self.__class__ .last_id += 1
        message.id = self.__class__.last_id
        self.messages[self.__class__.last_id] = message

    def get_message(self, id):
        return self.messages[id]

    def delete_message(self, id):
        del self.messages[id]

message_fields = {
    'id': fields.Integer,
    'uri': fields.Url('message_endpoint'),
    'message': fields.String,
    'duration': fields.Integer,
    'creation_date': fields.DateTime,
    'message_category': fields.String,
    'printed_times': fields.Integer,
    'printed_once': fields.Boolean
}


message_manager = MessageManager()