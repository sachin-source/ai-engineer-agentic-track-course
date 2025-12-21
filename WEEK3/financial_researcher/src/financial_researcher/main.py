#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """Run the FinancialResearcher crew"""
    inputs = {
        "company": "OpenAI",
    }
    
    result = FinancialResearcher().crew().kickoff(inputs=inputs)
    print(result.raw)
    
if __name__ == "__main__":
    run()