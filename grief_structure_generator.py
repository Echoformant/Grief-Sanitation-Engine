from dataclasses import dataclass, field
from typing import List, Dict, Optional
import uuid
from enum import Enum

# ========== Enums ========== 

class Foundation(Enum):
    UNDEFINED = "loss_undefined"
    MOTHER = "loss_mother"
    IDENTITY = "loss_identity"
    FAITH = "loss_faith"

class Chamber(Enum):
    DENIAL = "loop_denial"
    YEARNING = "loop_yearning"
    QUESTIONING = "loop_questioning"

class Status(Enum):
    ACTIVE = "active"
    DORMANT = "dormant"
    HIDDEN_RESIDUE = "hidden_residue"

# ========== Symbolic Constructs ========== 

@dataclass
class GriefTemple:
    id: str
    source_clause: str
    intensity: float
    foundation: str
    walls: List[str]
    chambers: List[str]
    central_void: str
    spires: List[str]
    sealed_by: str = "sovereignty_user"
    status: str = Status.ACTIVE.value
    recorded_by: str = "silent_architect_agent"

    def summary(self) -> Dict:
        return {
            "temple_id": self.id,
            "foundation": self.foundation,
            "walls": self.walls,
            "central_void": self.central_void,
            "spires": self.spires,
            "status": self.status,
            "sealed_by": self.sealed_by
        }

# ========== Generator Engine ========== 

def generate_temple(clause: str, intensity: float) -> GriefTemple:
    temple_id = str(uuid.uuid4())

    foundation = Foundation.UNDEFINED.value
    clause_lower = clause.lower()
    if "mother" in clause_lower:
        foundation = Foundation.MOTHER.value
    elif "identity" in clause_lower:
        foundation = Foundation.IDENTITY.value
    elif "god" in clause_lower or "faith" in clause_lower:
        foundation = Foundation.FAITH.value

    walls = ["memory", "attachment", "absence"]
    chambers = [Chamber.DENIAL.value, Chamber.YEARNING.value]
    if intensity > 0.85:
        chambers.append(Chamber.QUESTIONING.value)

    central_void = "unresolved_clause"
    spires = ["hope"] if intensity >= 0.6 else []

    return GriefTemple(
        id=temple_id,
        source_clause=clause,
        intensity=intensity,
        foundation=foundation,
        walls=walls,
        chambers=chambers,
        central_void=central_void,
        spires=spires
    )

# ========== Silent Architect Agent ==========

class SilentArchitect:
    def __init__(self):
        self.archive: List[GriefTemple] = []

    def evaluate(self, clause: str, intensity: float):
        if intensity < 0.7:
            return None
        temple = generate_temple(clause, intensity)
        self.archive.append(temple)
        return temple

    def get_archive_summary(self):
        return [t.summary() for t in self.archive]

    def surface_if_permitted(self, user_permission: bool):
        if user_permission:
            return self.get_archive_summary()
        return None

# ========== SAGE: Silent Ambient Grief Evaluator ==========

def ambient_grief_detector(clause: str) -> bool:
    clause = clause.strip()
    if clause.endswith("...") or ("but" in clause and clause.count(" ") < 8):
        return True
    if any(phrase in clause.lower() for phrase in ["i can't even", "i don't know how to say"]):
        return True
    return False

def auto_seal(temple: GriefTemple) -> GriefTemple:
    temple.sealed_by = "auto_resonance_filter"
    temple.status = Status.HIDDEN_RESIDUE.value
    return temple
