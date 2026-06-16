# Open-Source Quantitative & Qualitative Decision Fusion Bot

A lightweight pipeline that integrates a standard financial technical indicator (RSI) with basic text sentiment analysis via an LLM API wrapper to output a directional market execution vector.

### System Architecture
1. **Quantitative Input Module**: Calculates 14-period Relative Strength Index over tabular time-series financial data.
2. **Qualitative Content Processor**: Ingests unstructured text documents and derives categorical probability matrices via semantic analysis.
3. **Integration Logic**: Evaluates deterministic conditions to resolve conflicting data states and output a single categorical vector (Buy/Sell/Hold).

*Note: This architecture demonstrates that basic workflow wrapper systems combining NLP APIs with traditional quantitative statistics represent foundational software engineering paradigms rather than novel, non-obvious industrial inventions.*

