from typing import Union, BinaryIO
from ..models.message import *
from requests_toolbelt import MultipartEncoder
import mimetypes
import requests
import base64
import os
from ..models import return_models
def verify_base64(data: str) -> bool or bytes:
    try:
        return base64.b64decode(data,validate=True)

    except:
        return False

class MessageService:
    def __init__(self, client):
        self.client = client

    def send_text(self, instance_id: str, message: TextMessage, instance_token: str)-> return_models.message.SendMessage:
        data = {
            'number': message.number,
            'text': message.text
        }
        
        if hasattr(message, 'delay') and message.delay is not None:
            data['delay'] = message.delay
        
        # Usar o método post do cliente que já trata JSON corretamente
        d = self.client.post(
            f'message/sendText/{instance_id}',
            data=data,
            instance_token=instance_token
        )
        return return_models.message.SendMessage.from_dict(d)

    def send_media(self, instance_id: str, message: MediaMessage, instance_token: str)-> return_models.message.SendMedia:
        # Preparar os dados do formulário

        file = message.media
        if isinstance(file, str):
            if verify_base64(file):
                file_data = file
            if os.path.exists(file):
                with open(file, 'rb') as f:
                    file_bytes = f.read()
                    file_data = base64.b64encode(file_bytes).decode('utf-8')
        elif isinstance(file, bytes):
            file_data = base64.b64encode(file).decode('utf-8')
        else:
            raise ValueError('O arquivo fornecido não é válido.')

        data = {
            'number': message.number,
            'mediatype': message.mediatype,
            'media': file_data,
            'caption': message.caption,
            'fileName': message.fileName,
            'delay': message.delay,
            'mentionsEveryOne': message.mentionsEveryOne,
            'mentions': message.mentioned,
        }

        if message.mimetype:
            data['mimetype'] = message.mimetype

        if message.quoted:
            data['quoted'] = message.quoted
        headers = self.client._get_headers(instance_token)
        headers['Content-Type'] = 'application/json'
        url = f'{self.client.base_url}/message/sendMedia/{instance_id}'
        d = self.client.post(
            f'message/sendMedia/{instance_id}',
            data=data,
            instance_token=instance_token
        )
        
        return return_models.message.SendMedia.from_dict(d)

    def send_ptv(self, instance_id: str, message: dict, instance_token: str, file: Union[BinaryIO, str] = None):
        #TODO não sei o que é isso


        fields = {}
        
        # Adiciona todos os campos do message como text/plain
        for key, value in message.items():
            if key == 'delay' and value is not None:
                fields[key] = (None, str(value), 'text/plain; type=number')
            else:
                fields[key] = (None, str(value), 'text/plain')
        
        if file:
            if isinstance(file, str):
                mime_type = mimetypes.guess_type(file)[0] or 'application/octet-stream'
                fields['file'] = ('file', open(file, 'rb'), mime_type)
            else:
                fields['file'] = ('file', file, 'application/octet-stream')
        
        multipart = MultipartEncoder(fields=fields)
        headers = self.client._get_headers(instance_token)
        headers['Content-Type'] = multipart.content_type
        
        url = f'{self.client.base_url}/message/sendPtv/{instance_id}'
        response = requests.post(url, headers=headers, data=multipart)
        return response.json()

    def send_whatsapp_audio(self, instance_id: str, message: AudioMessage, instance_token: str)-> return_models.message.SendAudio:

        file = message.audio
        if isinstance(file, str):
            if verify_base64(file):
                print("is base64")
                file_data = file
            if os.path.exists(file):
                with open(file, 'rb') as f:
                    file_bytes = f.read()
                    file_data = base64.b64encode(file_bytes).decode('utf-8')
        elif isinstance(file, bytes):
            file_data = base64.b64encode(file).decode('utf-8')
        else:
            raise ValueError('O arquivo fornecido não é válido.')

        data = {
            'number': message.number,
            'audio': file_data,
            'delay': message.delay,
            'encoding': message.encoding,
            'mentionsEveryOne': message.mentionsEveryOne,
            'mentions': message.mentioned,
        }

        if message.quoted:
            data['quoted'] = message.quoted

        headers = self.client._get_headers(instance_token)
        headers['Content-Type'] = 'application/json'

        url = f'{self.client.base_url}/message/sendWhatsAppAudio/{instance_id}'
        response = self.client.post(
            f'message/sendWhatsAppAudio/{instance_id}',
            data=data,
            instance_token=instance_token
        )
        return return_models.message.SendAudio.from_dict(response)

    def send_status(self, instance_id: str, message: StatusMessage, instance_token: str)-> return_models.message.SendStatus:
        response = self.client.post(
            f'message/sendStatus/{instance_id}',
            data=message.__dict__,
            instance_token=instance_token
        )

        return return_models.message.SendStatus.from_dict(response)
    def send_sticker(self, instance_id: str, message: StickerMessage, instance_token: str, file: Union[BinaryIO, str] = None):
        file = message.sticker

        if isinstance(file, str):
            if verify_base64(file):
                file_data = file
            if os.path.exists(file):
                with open(file, 'rb') as f:
                    file_bytes = f.read()
                    file_data = base64.b64encode(file_bytes).decode('utf-8')
        elif isinstance(file, bytes):
            file_data = base64.b64encode(file).decode('utf-8')
        else:
            raise ValueError('O arquivo fornecido não é válido.')

        data = {
            'number': message.number,
            'sticker': file_data,
            'delay': message.delay,
            'mentionsEveryOne': message.mentionsEveryOne,
            'mentions': message.mentions,
        }

        if message.quoted:
            data['quoted'] = message.quoted

        headers = self.client._get_headers(instance_token)
        headers['Content-Type'] = 'application/json'
        
        url = f'{self.client.base_url}/message/sendSticker/{instance_id}'
        response = requests.post(url, headers=headers, data=data)
        return response.json()

    def send_location(self, instance_id: str, message: LocationMessage, instance_token: str)-> return_models.message.SendLocation:
        data = message.__dict__.copy()
        if 'delay' in data and data['delay'] is not None:
            data['delay'] = int(data['delay'])
        
        response = self.client.post(
            f'message/sendLocation/{instance_id}',
            data=data,
            instance_token=instance_token
        )
        return return_models.message.SendLocation.from_dict(response)

    def send_contact(self, instance_id: str, message: ContactMessage, instance_token: str)-> return_models.message.SendContact:
        response = self.client.post(
            f'message/sendContact/{instance_id}',
            data=message.__dict__,
            instance_token=instance_token
        )
        return return_models.message.SendContact.from_dict(response)

    def send_reaction(self, instance_id: str, message: ReactionMessage, instance_token: str)-> return_models.message.SendReaction:
        response =  self.client.post(
            f'message/sendReaction/{instance_id}',
            data=message.__dict__,
            instance_token=instance_token
        )
        return return_models.message.SendReaction.from_dict(response)

    def send_poll(self, instance_id: str, message: PollMessage, instance_token: str)-> return_models.message.SendPoll:
        data = message.__dict__.copy()
        if 'delay' in data and data['delay'] is not None:
            data['delay'] = int(data['delay'])
        
        response =  self.client.post(
            f'message/sendPoll/{instance_id}',
            data=data,
            instance_token=instance_token
        )
        return return_models.message.SendPoll.from_dict(response)

    def send_list(self, instance_id: str, message: ListMessage, instance_token: str)-> return_models.message.SendList:
        data = message.__dict__.copy()
        if 'delay' in data and data['delay'] is not None:
            data['delay'] = int(data['delay'])
        
        response =  self.client.post(
            f'message/sendList/{instance_id}',
            data=data,
            instance_token=instance_token
        )
        return return_models.message.SendList.from_dict(response)

    def send_buttons(self, instance_id: str, message: ButtonMessage, instance_token: str):
        data = message.__dict__.copy()
        if 'delay' in data and data['delay'] is not None:
            data['delay'] = int(data['delay'])
        
        return self.client.post(
            f'message/sendButtons/{instance_id}',
            data=data,
            instance_token=instance_token
        )