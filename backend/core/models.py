from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text of the option presented to the reader.")   
    node_id: Dict[str, Any] = Field(description="The next node that this option leads to.")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="The content or situation described at this node of the story.")
    is_ending: bool = Field(description="Indicates if this node is an ending of the story.")
    is_winning_ending: bool = Field(description="Indicates if this ending is a winning ending.")
    options: Optional[List[StoryOptionLLM]] = Field(
        default=None,
        description="A list of options available at this node, each leading to another node."
    )

    class StoryLLMResponse(BaseModel):
        title: str = Field(description="The title of the story.")
        root_node: StoryNodeLLM = Field(description="The root node of the story from which it begins.")