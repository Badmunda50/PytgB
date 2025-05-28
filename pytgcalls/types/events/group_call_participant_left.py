from typing import Any

class GroupCallParticipantLeft:
    def __init__(self, participant_data: Any):
        self.participant = participant_data

    def __repr__(self):
        return f"<GroupCallParticipantLeft participant={self.participant}>"
