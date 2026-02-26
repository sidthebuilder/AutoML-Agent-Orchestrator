import argparse
from src.orchestrator import Orchestrator
from src.utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Automated Data Science Execution Framework")
    parser.add_argument("--dataset", type=str, required=True, help="Path or name of the dataset to analyze (e.g., 'train.csv')")
    parser.add_argument("--retries", type=int, default=5, help="Maximum number of debate loops before forced submission.")
    
    args = parser.parse_args()
    
    logger = setup_logger("MainExecution")
    logger.info(f"BOOT SEQUENCE INITIATED. Target Dataset: {args.dataset}")
    
    # Initialize the primary finite state machine
    try:
        orchestrator = Orchestrator(max_retries=args.retries)
        final_script = orchestrator.run_pipeline(args.dataset)
        
        if final_script:
            logger.info("FINAL SCRIPT GENERATED:")
            print("\n================ FINAL COMPILED SCRIPT ================\n")
            print(final_script)
            print("\n=======================================================\n")
        else:
            logger.error("SYSTEM HALTED. Failed to generate a mathematically valid pipeline.")
            
    except Exception as e:
        logger.critical(f"FATAL ERROR IN ORCHESTRATOR: {str(e)}")

if __name__ == "__main__":
    main()
