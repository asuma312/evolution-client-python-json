from enum import Enum
from typing import List, Optional, Union, Required
from evolution_wrapper.evolutionapi.utils.hex_colors import HexColors

class QuotedKey:
    def __init__(self, remoteJid: Required[str], id: Required[str], fromMe: bool = False):
        if remoteJid is None or id is None:
            raise ValueError("'remoteJid' and 'id' are required and cannot be None")
        self.remoteJid = remoteJid
        self.id = id
        self.fromMe = fromMe

class MediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"

class MimeTypes(Enum):
    VIDEO_MP4 = "video/mp4"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_GIF = "image/gif"
    AUDIO_OGG = "audio/ogg"
    AUDIO_MPEG = "audio/mpeg"
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"
    APPLICATION_PDF = "application/pdf"
    APPLICATION_ZIP = "application/zip"

extensions = {
    "mp4": MimeTypes.VIDEO_MP4,
    "jpg": MimeTypes.IMAGE_JPEG,
    "jpeg": MimeTypes.IMAGE_JPEG,
    "png": MimeTypes.IMAGE_PNG,
    "gif": MimeTypes.IMAGE_GIF,
    "ogg": MimeTypes.AUDIO_OGG,
    "mp3": MimeTypes.AUDIO_MPEG,
    "txt": MimeTypes.TEXT_PLAIN,
    "html": MimeTypes.TEXT_HTML,
    "pdf": MimeTypes.APPLICATION_PDF,
    "zip": MimeTypes.APPLICATION_ZIP
}

class StatusType(Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"

class FontType(Enum):
    SERIF = 1
    NORICAN_REGULAR = 2
    BRYNDAN_WRITE = 3
    BEBASNEUE_REGULAR = 4
    OSWALD_HEAVY = 5

class BaseMessage:
    def __init__(self, **kwargs):
        self.__dict__.update({k: v for k, v in kwargs.items()})

class QuotedMessage(BaseMessage):
    def __init__(self, key: Required[QuotedKey], message: Optional[dict] = None):
        if key is None:
            raise ValueError("'key' is required and cannot be None")
        super().__init__(
            key=key.__dict__,
            message=message)

class TextMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        text: Required[str],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None,
        linkPreview: Optional[bool] = True,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        if number is None or text is None:
            raise ValueError("'number' and 'text' are required and cannot be None")
        super().__init__(
            number=number,
            text=text,
            delay=delay,
            quoted=quoted.__dict__ if quoted else None,
            linkPreview=linkPreview,
            mentionsEveryOne=mentionsEveryOne,
            mentioned=mentioned if mentioned else []
        )

class MediaMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        media: Required[Union[str, bytes]],
        mediatype: Optional[MediaType] = None,
        mimetype: Optional[Union[MimeTypes]] = None,
        caption: str = '',
        fileName: str = 'file',
        delay: Optional[Union[int, float]] = 1200,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        if number is None or media is None:
            raise ValueError("'number' and 'media' are required and cannot be None")
        super().__init__(
            number=number,
            mediatype=mediatype.value if mediatype else None,
            mimetype=mimetype.value if mimetype else None,
            caption=caption,
            fileName=fileName,
            quoted=quoted.__dict__ if quoted else None,
            mentionsEveryOne=mentionsEveryOne,
            mentioned=mentioned if mentioned else [],
            delay=delay,
            media=media
        )

class AudioMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        audio: Required[Union[str, bytes]],
        delay: Optional[int] = 1200,
        encoding: Optional[bool] = True,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        if number is None or audio is None:
            raise ValueError("'number' and 'audio' are required and cannot be None")
        super().__init__(
            number=number,
            audio=audio,
            delay=delay,
            encoding=encoding,
            quoted=quoted.__dict__ if quoted else None,
            mentionsEveryOne=mentionsEveryOne,
            mentioned=mentioned if mentioned else []
        )

class StatusMessage(BaseMessage):
    def __init__(
        self,
        type: Required[StatusType],
        content: Required[str],
        statusJidList: Required[Union[List[str]]],
        caption: Optional[str] = '',
        backgroundColor: Optional[HexColors] = HexColors.WHITE,
        font: Optional[FontType] = FontType.SERIF,
        allContacts: bool = False
    ):
        if type is None or content is None or not statusJidList:
            raise ValueError("'type', 'content', and 'statusJidList' are required and cannot be None")
        super().__init__(
            type=type.value,
            content=content,
            caption=caption,
            backgroundColor=backgroundColor,
            font=font.value if font else None,
            allContacts=allContacts,
            statusJidList=statusJidList
        )

class LocationMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        name: Required[str],
        address: Required[str],
        latitude: Required[float],
        longitude: Required[float],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None
    ):
        if number is None or name is None or address is None or latitude is None or longitude is None:
            raise ValueError("'number', 'name', 'address', 'latitude', and 'longitude' are required and cannot be None")
        super().__init__(
            number=number,
            name=name,
            address=address,
            latitude=latitude,
            longitude=longitude,
            delay=delay,
            quoted=quoted.__dict__ if quoted else None
        )

class Contact(BaseMessage):
    def __init__(
        self,
        fullName: Required[str],
        wuid: Required[str],
        phoneNumber: Required[str],
        organization: Optional[str] = '',
        email: Optional[str] = '',
        url: Optional[str] = ''
    ):
        if fullName is None or wuid is None or phoneNumber is None:
            raise ValueError("'fullName', 'wuid', and 'phoneNumber' are required and cannot be None")
        super().__init__(
            fullName=fullName,
            wuid=wuid,
            phoneNumber=phoneNumber,
            organization=organization,
            email=email,
            url=url
        )

class ContactMessage(BaseMessage):
    def __init__(self, number: Required[str], contact: Required[List[Contact]]):
        if number is None or not contact:
            raise ValueError("'number' and 'contact' are required and cannot be None")
        super().__init__(
            number=number,
            contact=[c.__dict__ for c in contact]
        )

class ReactionMessage(BaseMessage):
    def __init__(self, key: Required[QuotedKey], reaction: Required[str]):
        if key is None or reaction is None:
            raise ValueError("'key' and 'reaction' are required and cannot be None")
        super().__init__(
            key=key.__dict__,
            reaction=reaction)

class PollMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        name: Required[str],
        selectableCount: Required[int],
        values: Required[List[str]],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        if number is None or name is None or selectableCount is None or not values:
            raise ValueError("'number', 'name', 'selectableCount', and 'values' are required and cannot be None")
        super().__init__(
            number=number,
            name=name,
            selectableCount=selectableCount,
            values=values,
            delay=delay,
            quoted=quoted.__dict__ if quoted else None,
            mentionsEveryOne=mentionsEveryOne,
            mentioned=mentioned if mentioned else []
        )

class ListRow(BaseMessage):
    def __init__(self, title: Required[str], description: Required[str], rowId: Required[str]):
        if title is None or description is None or rowId is None:
            raise ValueError("'title', 'description', and 'rowId' are required and cannot be None")
        super().__init__(
            title=title,
            description=description,
            rowId=rowId
        )

class ListSection(BaseMessage):
    def __init__(self, title: Required[str], rows: Required[List[ListRow]]):
        if title is None or not rows:
            raise ValueError("'title' and 'rows' are required and cannot be None")
        super().__init__(
            title=title,
            rows=[r.__dict__ for r in rows]
        )

class ListMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        title: Required[str],
        description: Required[str],
        buttonText: Required[str],
        footerText: Required[str],
        sections: Required[List[ListSection]],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None
    ):
        if number is None or title is None or description is None or buttonText is None or footerText is None or not sections:
            raise ValueError("'number', 'title', 'description', 'buttonText', 'footerText', and 'sections' are required and cannot be None")
        super().__init__(
            number=number,
            title=title,
            description=description,
            buttonText=buttonText,
            footerText=footerText,
            sections=[s.__dict__ for s in sections],
            delay=delay,
            quoted=quoted.__dict__ if quoted else None
        )

class Button(BaseMessage):
    def __init__(
        self,
        type: Required[str],
        displayText: Required[str],
        id: Required[str],
        copyCode: Optional[str] = None,
        url: Optional[str] = None,
        phoneNumber: Optional[str] = None,
        currency: Optional[str] = None,
        name: Optional[str] = None,
        keyType: Optional[str] = None,
        key: Optional[str] = None
    ):
        if type is None or displayText is None or id is None:
            raise ValueError("'type', 'displayText', and 'id' are required and cannot be None")
        super().__init__(
            type=type,
            displayText=displayText,
            id=id,
            copyCode=copyCode,
            url=url,
            phoneNumber=phoneNumber,
            currency=currency,
            name=name,
            keyType=keyType,
            key=key
        )

class ButtonMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        title: Required[str],
        description: Required[str],
        footer: Required[str],
        buttons: Required[List[Button]],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None
    ):
        if number is None or title is None or description is None or footer is None or not buttons:
            raise ValueError("'number', 'title', 'description', 'footer', and 'buttons' are required and cannot be None")
        super().__init__(
            number=number,
            title=title,
            description=description,
            footer=footer,
            buttons=[b.__dict__ for b in buttons],
            delay=delay,
            quoted=quoted.__dict__ if quoted else None
        )

class StickerMessage(BaseMessage):
    def __init__(
        self,
        number: Required[str],
        sticker: Required[Union[str ,bytes]],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        if number is None or sticker is None:
            raise ValueError("'number' and 'sticker' are required and cannot be None")
        super().__init__(
            number=number,
            sticker=sticker,
            delay=delay,
            quoted=quoted.__dict__ if quoted else None,
            mentionsEveryOne=mentionsEveryOne,
            mentioned=mentioned if mentioned else []
        )
