# Beyond Single Prompts: Engineering a Multi-Agent Workgroup for End-to-End Tabular Data Science

**Author:** Shashank Kumar
**Date:** February 2026

## Abstract
Traditional automated machine learning (AutoML) frameworks fundamentally rely on static pipelines and brute-force search strategies. While functional, this approach incurs prohibitive computational overhead and lacks the adaptive contextual reasoning provided by human data scientists. Recent methodologies have attempted to process intact datasets through singular Large Language Models (LLMs) to automatically generate predictive scripts. However, empirical evidence demonstrates that this single-agent approach consistently fails due to context degradation, hallucinated schema parameters, and failure to detect target leakage during sustained execution chains. 

This paper introduces a decentralized, role-based multi-agent orchestration framework designed to autonomously execute end-to-end tabular data science workflows. By distributing discrete computational tasks across three specialized LLM personas (a Data Engineer, a Modeler, and an Evaluator), the proposed system physically enforces independent logic verification and self-correction prior to final output. We benchmarked this architecture against standardized Kaggle environments, generating definitive empirical proof that collaborative agentic debate systematically mitigates data leakage, optimizes feature selection, and outperforms single-shot LLM prompts by statistically significant margins.

## 1. Introduction

### 1.1 The Automation Bottleneck
The end-to-end automation of data science pipelines remains a substantial engineering challenge. While predictive algorithms are largely commoditized, the operational difficulty resides in the precise manipulation of raw data: rectifying non-standard missing values, encoding high-cardinality strings, and isolating target-variable leakage. 

Historically, AutoML frameworks such as H2O and TPOT addressed this via exhaustive grid searches. While mathematically valid given unlimited computational resources, brute-forcing all potential feature permutations is highly inefficient in production applications. An experienced human engineer relies on heuristic logic, immediately recognizing a `PassengerId` column as stochastic noise and dropping it. Developing algorithmic systems that emulate this specific deductive intuition is imperative. 

### 1.2 The Failure of Single-Agent LLMs
The proven capability of LLMs to generate functional Python syntax initiated immediate attempts to fully automate predictive modeling platforms. The standard protocol involves passing the schema of an unknown dataset (e.g., `train.csv`) to a single LLM to generate the entire algorithm matrix. 

Subsequent execution logs demonstrate a high statistical failure rate. 

The primary structural flaw is catastrophic context collapse. A singular LLM attempting to retain the variable schema, preprocessing sequencing, hyperparameter constraints, and evaluation metrics within one continuous prompt context experiences logical degradation. Empirical observations consistently show single agents hallucinating non-existent column names or applying a `StandardScaler` to the training matrix while omitting the uniform transformation on the test matrix. While human review detects sequence errors immediately, a solitary agent commits the erroneous code and induces catastrophic pipeline failure.

### 1.3 Proposed System Architecture and Contribution
To resolve this instability, we analyze the operational structure of professional engineering teams. Quality assurance protocols prohibit a single engineer from writing, reviewing, and deploying production code without supervision. A robust system requires strict separation of concerns.

This research proposes a multi-agent orchestration framework engineered specifically for tabular data science. We compartmentalize the computational workflow into three distinct, specialized state machines. The Data Engineer executes strict data sanitization and Pandas transformations. The Modeler dictates algorithm geometry and hyperparameter grids. The Evaluator executes out-of-fold metric validation and rigorously audits the Modeler’s logic, issuing rejections for substandard architectures. 

By constraining agents to debate and transfer data exclusively via validated JSON contracts, we establish an automated self-correcting loop that mathematically mimics human peer review.

## 2. Literature Review & Background

### 2.1 The Evolution of AutoML
The pursuit of removing human intervention from the machine learning lifecycle has established precedent. Early frameworks relied entirely on Bayesian optimization, maximizing hyperparameter discovery but proving deficient at automated feature engineering. Subsequent systems deployed evolutionary algorithms to construct pipelines recursively. While mathematically complex, these essentially function as black boxes. When an evolutionary AutoML pipeline underperforms, diagnosing the logic failure is nearly impossible due to the unreadable procedural code it generates.

### 2.2 LLMs in Data Science
The migration from grid-search AutoML to LLM-driven automation has accelerated proportionally to the increase in transformer context windows. Researchers established that LLMs implicitly retain extensive data science heuristics derived from parsing vast repositories of open-source modeling code during pre-training. 

Initial single-agent applications, such as AutoGPT, proved models could chain logical steps autonomously, but suffered from domain ambiguity. Absent strict guardrails, they frequently entered recursive failure loops attempting to resolve arbitrary package dependencies rather than executing the core mathematical task.

### 2.3 Multi-Agent Systems and Recent Breakouts
The deployment of synchronized multi-LLM architectures has demonstrated advanced problem-solving capacity. 

The *AutoKaggle* framework (2024) represented a foundational attempt to structure this protocol, utilizing a five-agent hierarchy (including Planning and Summarizing modules) integrated with Retrieval Augmented Generation (RAG) to dynamically access standard code libraries. Their empirical results on classification tasks validated the core concept. The *DS-Agent* framework subsequently introduced Case-Based Reasoning (CBR), wherein agents analyze historical top-tier modeling scripts and attempt to map proven architectures onto new parameters. 

Another highly cited model, *LightAutoDS-Tab*, utilized the LLM strictly as an administrative router to deploy traditional AutoML grid searches, fusing deterministic search with dynamic logic.

While confirming the efficacy of the multi-agent paradigm, these configurations present inefficiencies. Executing five concurrent LLMs generates massive token overhead and severe API latency. Furthermore, frameworks reliant on historical retrieval (e.g., DS-Agent) express high variance, frequently overfitting on past data structures and failing when executing entirely novel mathematical schemas.

Our framework diverges structurally from *AutoKaggle* by executing severe hierarchical compression. We reduce the operational team to exactly three agents and enforce rigid deterministic state-machine routing rather than open-ended dialogue. Constraining the communication vectors significantly reduces token expenditure and forces the Evaluator agent to execute highly aggressive diagnostic reviews.

## 3. System Architecture and Operational Logic

### 3.1 The Orchestrator Module
The foundation of the architecture is the central Orchestrator. Empirical testing proved that unrestricted communication channels between autonomous agents results in catastrophic topic drift. 

Consequently, the Orchestrator operates as a strict finite state machine (FSM) defining all communication vectors. Lateral communication between the Data Engineer and the Modeler is structurally prohibited. The Data Engineer transmits code solely to the Orchestrator, which executes the syntax within a safe sandbox. Contingent on successful compilation, the Orchestrator forwards the updated dataset schema to the Modeler.

The Orchestrator provides error mitigation via exponential backoff protocols to handle API rate limits (HTTP 429). Furthermore, it governs context window management. When processing high-dimensionality matrices (e.g., >400 features), the Orchestrator compresses the raw data into strict summary statistics arrays before prompt injection, preventing core context overload.

### 3.2 Agent 1: The Data Engineer
The primary persona is isolated for data sanitization. The system prompt configures the LLM exclusively as an engineering resource tasked with tabular matrix preparation. 

The configuration explicitly bans algorithm selection. The instruction set dictates: "Process raw data arrays, execute missing value imputation via median or mode logic, resolve multicollinearity via feature removal, and apply OneHotEncoding or LabelEncoding to categorical parameters. Output strict Python syntax via Pandas and Scikit-Learn libraries."

This extreme specialization demonstrates a proven reduction in hallucination events. Unbounded agents occasionally attempt illogical applications, such as deploying NLP tokenization on numeric ZIP code parameters. Isolating the engineering constraint guarantees output sterility.

### 3.3 Agent 2: The Modeler
Upon verification of a clean data matrix, the Orchestrator transfers the updated schema dictionary to the Modeler.

The Modeler operates as the algorithmic architect. It analyzes the target variable distribution to classify the task (regression vs. classification) and generates the primary training loop. Based on matrix dimensionality, it defaults to XGBoost, LightGBM, or Random Forest architectures. 

It generates the corresponding hyperparameter grid arrays. Crucially, the system imposes hard mathematical caps on parameters (e.g., restricting XGBoost `n_estimators` to a maximum of 500) to preclude infinite compute cycles. The Modeler returns execution scripts designed to compile the model, log training operations, and output definitive error metrics (RMSE or Log-Loss) to the central JSON tracking file.

### 3.4 Agent 3: The Evaluator (Critic)
The Evaluator forms the absolute threshold for quality assurance. The fundamental failure of single-prompt systems is the absence of verification logic. 

The Evaluator agent parses the generated Python syntax and cross-references the resultant JSON metric logs. It is programmed to identify statistical impossibilities. For example, if a classification script logs an exact 1.0 (100%) accuracy vector on a validation fold, the Evaluator recognizes the mathematical probability of target leakage. 

The Evaluator triggers a rejection cascade, transmitting a specific diagnostic to the Orchestrator: "CRITICAL ALERT: Target leakage confirmed. The explicit `Survived` vector remains in the `X_train` matrix. Rerun Modeler generation and forcefully execute `X.drop('Survived')`."

This deterministic debate loop consistently iterates two to three cycles before the final script passes structural validation.

## 4. Methodology and Implementation Parameters

### 4.1 Dataset Selection and Benchmarks
To secure actionable empirical data, we benchmarked the architecture against complex, mathematically deceptive datasets standard in the Kaggle ecosystem.

The model was subjected to the *Titanic Classification* array and the *House Prices Advanced Regression Techniques* matrix. The Titanic dataset contains structurally ambiguous null values within demographic parameters, while the House Prices array contains approximately eighty cross-dependent variables requiring complex categorical encoding schemes. 

Execution runs were divided into three comparative frameworks:
1. **Human Novice Baseline:** A deterministic Random Forest utilizing Scikit-Learn default parameters and mean-imputation without advanced feature engineering.
2. **Zero-Shot LLM Architecture:** Providing rules documentation to a single Llama-3 parameter model, logging the unverified compilation output.
3. **The Multi-Agent Workgroup:** The proposed orchestrator architecture, configured to allow a maximum loop limit of five rejections from the Evaluator before forcing final submission.

### 4.2 Enforcing Pydantic Data Contracts
A definitive engineering challenge involved parsing unstructured LLM output nodes. If the Modeler generated valid syntax surrounded by conversational natural language, the Python execution module failed immediately with parsing tracebacks.

We integrated `pydantic` to enforce strict type-safe JSON schema constraints on all LLM responses. The output must strictly adhere to a pre-defined generic structure containing `python_code` and `reasoning` keys. Failure to validate against the Pydantic schema forces the Orchestrator to resubmit the prompt. This protocol successfully transforms probabilistic linguistic generation into a deterministic computational component.

### 4.3 Secure Code Execution Environment
Executing autonomous LLM code on primary host infrastructure presents severe security vulnerabilities. An agent failure could construct infinite recursive loops or inadvertently execute system deletion commands during workspace generation.

To guarantee system stability, the Orchestrator isolates all agent-generated Python strings within restricted `subprocess` environments. Execution timelines are strictly enforced. Should an anomaly cause execution to exceed 180 seconds, a `SIGKILL` terminal command is sent, the module logs a failure, and the Evaluator informs the Modeler of a core timeout constraint. This logic physically forces the Modeler to utilize highly optimized vectorized operations rather than iterating via inefficient `.apply()` loops.

## 5. Experimental Results and Empirical Proof

### 5.1 Baseline Comparisons on Objective Datasets
To definitively measure the impact of the synchronized multi-agent framework, we aggregated statistical performance across 50 independent execution cycles on both benchmark datasets. Evaluation metrics were strictly defined: Accuracy for classification and Root Mean Squared Error (RMSE) for regression, aligning with Kaggle evaluation standards.

#### Table 1: Performance Benchmarks (Averages over 50 Runs)

| Framework Architecture | Titanic Accuracy (Higher is optimal) | House Prices RMSE (Lower is optimal) | Compilation Success Rate |
| :--- | :--- | :--- | :--- |
| **Novice Random Forest** | 0.765 | 34,500 | 100% |
| **Zero-Shot LLM** | 0.741 | 48,200 | 42% |
| **Multi-Agent Workgroup** | **0.822** | **23,150** | **94%** |

The data confirms a statistically significant advantage for the Multi-Agent framework, yielding a nearly 8% absolute increase in classification accuracy and reducing regression error by 32% compared to standard human-baseline benchmarks.

### 5.2 Compilation Analysis and Execution Observations
The underlying execution logs reveal the operational causality of these metrics. The Zero-Shot LLM exhibited an unacceptably high catastrophic failure rate, compiling valid code in only 42% of attempts. The primary failure mode involved schema misalignment post-transformation. A singular agent consistently failed to align the dimensionality of test set matrices with training set matrices post-One-Hot Encoding. This dimension mismatch immediately triggers terminal crashes in Scikit-Learn execution.

Conversely, the enforced separation of concerns in the Multi-Agent setup eradicated this vector of failure. The specialized Data Engineer agent algorithmically controls schema alignment. During recorded Run #17, an initial misalignment triggered a compiler traceback; the Orchestrator routed the error to the Data Engineer, which autonomously corrected the matrix structure by executing robust `pd.get_dummies()` and `.reindex()` logic prior to Modeler intervention.

### 5.3 Case Study Documenting the Extradition of Target Leakage
Empirical logs generated during House Prices analysis reveal definitive proof of the Evaluator's operational necessity. During a Modeler hyperparameter execution sequence, the agent generated K-Fold cross-validation logic. However, it placed target encoding functions iteratively prior to the cross-validation boundary. 

This sequencing guarantees target leakage. By transforming variables via the entire dataset index before localized splitting, the encoded data absorbs distribution data from the validation split. The compromised script yielded an artificial RMSE of 1,200.

The Evaluator intercepted the JSON output array. The validation constraints correctly flagged the statistical impossibility of the metric. The diagnostic log stated: "METRIC REJECTED. RMSE 1,200 violates standard variance expectations for variable `SalePrice`. The pipeline executes `TargetEncoder` globally before `train_test_split()`, confirming target leakage. The logic is rejected. Modeler must split indices immediately, sequence the encoder exclusively on `X_train`, and subsequently `.transform()` the validation holdout."

The Modeler ingested the critique, generated an updated operational sequence, and yielded a statistically valid RMSE of 24,000. This documented interaction provides empirical proof that adversarial multi-agent architectures identify and resolve internal logical errors previous uncatchable by automated tools.

---

## 6. Discussion and Computational Limitations

### 6.1 Token Expenditure and Latency Constraints
The evaluation of multi-agent architectures must account for computational latency and API expenditure. Executing a zero-shot prompt processes minimal tokens with minor latency. In contrast, operating an FSM orchestrating three specialized agents evaluating recursive JSON contracts demands vast computational bandwidth.

Empirical tracking established that an optimized successful execution of the Multi-Agent Workgroup required an average of 14 sequential API queries. This loop consumed approximately 45,000 input tokens and 8,000 output tokens. While highly beneficial for complex engineering pipelines or high-value modeling environments, scaling this exact configuration for broad application across thousands of minor tables remains computationally prohibitive without localized model hosting.

### 6.2 The Context Window Degradation Problem
A secondary structural limitation involves dimensional scaling. The framework operated flawlessly analyzing feature sets ranging from 12 to 80 variables. However, high-dimensionality schemas (e.g., bioinformatics datasets exhibiting 15,000 continuous variables) introduce substantial context degradation.

The standard Operational protocol of transferring summary arrays (mean, standard deviation, null sums) for absolute columns saturates LLM context limits. Preliminary experiments restricting the Data Engineer to the mathematical top 100 features via Mutual Information successfully bypassed the token limit but effectively blinded the agent to deep non-linear feature interactions. 

Future adaptations of this framework necessitate integration of specialized Vector Databases (RAG optimization for structural schemas), permitting the Data Engineer to query strict localized variables without ingesting the comprehensive global matrix.

### 6.3 Future Expansions: Multi-Modal Contexts
Current architecture validation relies exclusively on objective tabular data structures. The evolution of predictive modeling increasingly requires multi-modal processing, fusing categorical data structures with raw text arrays or image vectors. Developing the Data Engineer protocol to natively process embedding models (e.g., parsing raw text via `sentence-transformers` and appending the dense float matrices prior to Modeler handoff) represents the primary engineering trajectory.

## 7. Operational Conclusion
The transition from conceptualizing Artificial Intelligence as a singular computational endpoint to constructing deterministic, specialized software components represents a definitive upgrade in automated system reliability. 

Permitting a solitary, unconstrained neural network to ingest raw matrices, engineer robust features, and configure algorithms autonomously yields statistically unviable outcomes defined by hallucinations and structural bias. 

This research proves that rigidly assigning discrete operational tasks (enforced via deterministic agentic roles and hostile logic review) guarantees the generation of robust, enterprise-grade Python execution scripts. We have successfully automated standard predictive modeling architectures without sacrificing verification criteria. As API token economy and context parameters evolve, multi-agent frameworks will serve as the mathematical standard for zero-intervention data science execution.
