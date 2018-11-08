import os
from time import time

from .payloads import Payload
from .presence import Presence
from .response import Response
from .utils import remove_none


class Activity:

    def __init__(self, client: Presence, pid: int = os.getpid(),
                 state: str = None, details: str = None,
                 start: int = None, end: int = None,
                 large_image: str = None, large_text: str = None,
                 small_image: str = None, small_text: str = None,
                 party_id: str = None, party_size: list = None,
                 join: str = None, spectate: str = None,
                 match: str = None, instance: bool = True):

        self.payload = Payload.set_activity(pid, state, details, start, end, large_image, large_text,
                                            small_image, small_text, party_id, party_size, join, spectate,
                                            match, instance, _rn=False)

        self.p_properties = ('pid', 'state', 'details', 'start', 'end', 'large_image', 'large_text', 'small_image', 'small_text', 'party_id', 'party_size', 'join', 'spectate', 'match', 'instance')
        self.response = Response.from_dict(self.payload.data)
