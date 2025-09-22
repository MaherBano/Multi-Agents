# Homework Triage System
## Overview

This project implements a homework triage system using Python and the agents library. The system processes user queries to determine if they are homework-related and routes them to specialized tutor agents (Math, Physics, or Computer Science) for appropriate responses. It includes a guardrail mechanism to filter out non-homework questions.

## Features





- Guardrail Agent: Checks if the input query is a homework-related question.



- Triage Agent: Routes homework questions to the appropriate tutor agent based on the query content.



- Specialized Tutor Agents:





  - Math Tutor: Assists with math problems, providing step-by-step reasoning and examples.



  - Physics Tutor: Helps with physics concepts and problem-solving, offering clear explanations and examples.



  - Computer Tutor: Supports computer science concepts and programming tasks with code examples.



- Asynchronous Processing: Uses Python's asyncio for efficient handling of agent interactions.



- Pydantic Integration: Ensures structured output validation using the HomeworkOutput model.


# Code Explanation

## Agents





- Guardrail Agent (guardrail_agent):





  - Name: "Guardrail Check"



  - Purpose: Validates if the user input is a homework-related question.



  - Output: HomeworkOutput (Pydantic model with is_homework boolean and reasoning string).



- Triage Agent (triage_agent):





  - Name: "Triage Agent"



  - Purpose: Analyzes the input query and delegates it to the appropriate tutor agent (Math, Physics, or Computer Science).



  - Input Guardrail: Uses homework_guardrail to filter non-homework queries.



  - Handoffs: Supports routing to math_tutor_agent, physics_tutor_agent, or computer_tutor_agent.



- Tutor Agents:





  - Math Tutor: Handles math-related homework with detailed explanations.



  - Physics Tutor: Addresses physics queries with clear examples.



  - Computer Tutor: Assists with programming and computer science concepts, including code snippets.

### Key Components





- HomeworkOutput Model: A Pydantic model to structure the guardrail agent's output, ensuring type safety and validation.



- Guardrail Function (homework_guardrail): Asynchronously checks if the input is homework-related and returns a GuardrailFunctionOutput to control routing.



- Main Function: Demonstrates the system by running sample queries through the triage agent.

