from typing import Any

class GroupCallParticipantJoined:
    def __init__(self, participant_data: Any):
        # participant_data me aap call ke participant ka data receive karoge
        self.participant = participant_data

    def __repr__(self):
        return f"<GroupCallParticipantJoined participant={self.participant}>"
