import time
from src.utils.logger import setup_logger
from src.agents.data_engineer import DataEngineerAgent
from src.agents.modeler import ModelerAgent
from src.agents.evaluator import EvaluatorAgent

class Orchestrator:
    """
    The finite state machine that routes messages and strictly enforces the separation of concerns.
    """
    def __init__(self, max_retries: int = 5):
        self.logger = setup_logger("StateOrchestrator")
        self.max_retries = max_retries
        self.data_engineer = DataEngineerAgent()
        self.modeler = ModelerAgent()
        self.evaluator = EvaluatorAgent()

    def run_pipeline(self, dataset_path: str):
        self.logger.info(f"INITIALIZING PIPELINE FOR: {dataset_path}")

        # Phase 1: Data Engineer
        try:
            stats = self.data_engineer.analyze(dataset_path)
            engineer_out = self.data_engineer.execute(str(stats))
            self.logger.info("Data Engineering sequence completed successfully.")
        except Exception as e:
            self.logger.critical(f"Pipeline crashed in Data Engineering phase: {str(e)}")
            return

        # Prepare Schema for Modeler
        clean_schema = {"target": engineer_out.target_variable, "features": engineer_out.features}

        # Phase 2 & 3: Modeler and Critic Loop
        retries = 0
        is_valid = False

        while retries < self.max_retries and not is_valid:
            self.logger.info(f"Starting Modeler generation loop (Attempt {retries + 1}/{self.max_retries})")
            
            model_task = self.modeler.analyze(clean_schema)
            model_out = self.modeler.execute(model_task)
            
            # Critic Review
            critique_prompt = self.evaluator.analyze(model_out.metrics, model_out.python_code)
            eval_out = self.evaluator.execute(critique_prompt)

            if eval_out.is_approved:
                self.logger.info("SUCCESS: Evaluator mathematically verified constraints.")
                is_valid = True
                self.logger.info(f"FINAL METRICS: {model_out.metrics}")
                return model_out.python_code
            else:
                self.logger.warning(f"REJECTED BY EVALUATOR: {eval_out.reasoning}")
                self.logger.info("Enforcing exponential backoff interval before retry.")
                time.sleep(2 ** retries)  # Backoff
                retries += 1
                
        self.logger.error("Pipeline failed to generate validated matrix within retry limit.")
        return None
