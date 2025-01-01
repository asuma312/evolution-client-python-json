from enum import Enum
from typing import List, Optional, Union
from evolutionapi.utils.hex_colors import HexColors

class QuotedKey:
    def __init__(self,remoteJid:str,id:str,fromMe:bool=False):
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
        self.__dict__.update({k: v for k, v in kwargs.items() if v is not None})

class QuotedMessage(BaseMessage):
    def __init__(self, key: QuotedKey, message: Optional[dict] = None):
        super().__init__(
            key=key.__dict__,
            message=message)

class TextMessage(BaseMessage):
    def __init__(
        self,
        number: str,
        text: str,
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None,
        linkPreview: Optional[bool] = True,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
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
        number: str,
        media: Union[str,bytes],
        mediatype: Union[MediaType],
        mimetype: MimeTypes,
        caption: str = '',
        fileName: str = 'file',
        delay: Optional[Union[int, float]] = 1200,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        super().__init__(
            number=number,
            mediatype=mediatype.value,
            caption=caption,
            mimetype=mimetype.value,
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
            number: str,
            audio: Union[str, bytes],
            delay: Optional[int] = 1200,
            encoding: Optional[bool] = True,
            quoted: Optional[QuotedMessage] = None,
            mentionsEveryOne: Optional[bool] = False,
            mentioned: Optional[List[str]] = None
    ):
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
        type: StatusType,
        content: str,
        statusJidList: Union[List[str]],
        caption: Optional[str] = '',
        backgroundColor: Optional[HexColors] = HexColors.WHITE,
        font: Optional[FontType] = FontType.SERIF,
        allContacts: bool = False
    ):
        statusJidList = statusJidList if statusJidList else []
        if len(statusJidList) == 0:
            raise ValueError("statusJidList must have at least one contact")


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
        number: str,
        name: str,
        address: str,
        latitude: float,
        longitude: float,
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None
    ):
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
        fullName: str,
        wuid: str,
        phoneNumber: str,
        organization: Optional[str] = '',
        email: Optional[str] = '',
        url: Optional[str] = ''
    ):
        super().__init__(
            fullName=fullName,
            wuid=wuid,
            phoneNumber=phoneNumber,
            organization=organization,
            email=email,
            url=url
        )

class ContactMessage(BaseMessage):
    def __init__(self, number: str, contact: List[Contact]):
        super().__init__(
            number=number,
            contact=[c.__dict__ for c in contact]
        )

class ReactionMessage(BaseMessage):
    def __init__(self, key: QuotedKey, reaction: str):
        super().__init__(
            key=key.__dict__,
            reaction=reaction)

class PollMessage(BaseMessage):
    def __init__(
        self,
        number: str,
        name: str,
        selectableCount: int,
        values: List[str],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
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
    def __init__(self, title: str, description: str, rowId: str):
        super().__init__(
            title=title,
            description=description,
            rowId=rowId
        )

class ListSection(BaseMessage):
    def __init__(self, title: str, rows: List[ListRow]):
        super().__init__(
            title=title,
            rows=[r.__dict__ for r in rows]
        )

class ListMessage(BaseMessage):
    def __init__(
        self,
        number: str,
        title: str,
        description: str,
        buttonText: str,
        footerText: str,
        sections: List[ListSection],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None
    ):
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
        type: str,
        displayText: str,
        id: str,
        copyCode: Optional[str] = None,
        url: Optional[str] = None,
        phoneNumber: Optional[str] = None,
        currency: Optional[str] = None,
        name: Optional[str] = None,
        keyType: Optional[str] = None,
        key: Optional[str] = None
    ):
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
        number: str,
        title: str,
        description: str,
        footer: str,
        buttons: List[Button],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None
    ):
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
        number: str,
        sticker: Union[str ,bytes],
        delay: Optional[int] = 1200,
        quoted: Optional[QuotedMessage] = None,
        mentionsEveryOne: Optional[bool] = False,
        mentioned: Optional[List[str]] = None
    ):
        super().__init__(
            number=number,
            sticker=sticker,
            delay=delay,
            quoted=quoted.__dict__ if quoted else None,
            mentionsEveryOne=mentionsEveryOne,
            mentioned=mentioned if mentioned else []
        )