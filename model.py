# model.py
from pydantic import BaseModel, Field
from typing import List

class ResearchAgentModel(BaseModel):
    Title: str
    Authors: List[str]
    Summary: str

class SynthesisAgentModel(BaseModel):
    Summary: str
    Methods: str
    Findings: str
    Gaps_and_Future_Work: str
class AggregatedModel(BaseModel):
    research_sub_agent: ResearchAgentModel = Field(..., description="Output of ResearchAgentModel")
    synthesis_sub_agent: SynthesisAgentModel = Field(..., description="Output of SynthesisAgentModel")
