from abc import ABC, abstractmethod
from typing import Any
from src.utils.logger import setup_logger

class BaseAgent(ABC):
    """
    Abstract Base Class for all specialized agents in the framework.
    Enforces a strict interface for execution and validation.
    """
    def __init__(self, name: str, model_name: str = "llama-3"):
        self.name = name
        self.model_name = model_name
        self.logger = setup_logger(self.name)

    @abstractmethod
    def analyze(self, context: Any) -> str:
        """
        Analyzes the incoming state or data context.
        """
        pass

    @abstractmethod
    def execute(self, prompt: str) -> Any:
        """
        Executes the LLM request and returns a Pydantic-validated object.
        """
        pass
