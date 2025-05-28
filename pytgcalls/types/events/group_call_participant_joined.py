from typing import Any

class GroupCallParticipantJoined:
    def __init__(self, client: Any, participant_data: Any):
        self.client = client
        self.participant = participant_data

    def __repr__(self):
        return f"<GroupCallParticipantJoined participant={self.participant}>"
