from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentResponse:
    """Structured result returned by the agent."""
    user_query: str
    intent: str
    answer: str
    tools_used: List[str] = field(default_factory=list)
    evidence: Dict[str, Any] = field(default_factory=dict)
