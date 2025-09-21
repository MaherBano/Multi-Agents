from agents import Agent , GuardrailFunctionOutput , InputGuardrail , Runner
from pydantic import BaseModel
import asyncio , os

class HomeworkOutput(BaseModel):
    is_homework : bool
    reasoning : str

guardrail_agent = Agent( 
    name = "Guardrail Check",
    instructions= "You're a guadrail check agent. Check if the user is asking about the homework.",
    output_type=HomeworkOutput,
)

math_tutor_agent = Agent( 
    name = "Math Tutor" ,
    instructions="You are a math tutor. You provide help with math problems. Explain your reasoning at each step with examples."
)

physics_tutor_agent = Agent(
    name = "Physics Tutor",
    handoff_description = "Specializes in physics concepts and problem-solving.",
    instructions = "You are a physics tutor. You help students understand physics concepts and solve problems. Provide clear explanations and examples."
)

computer_tutor_agent = Agent(
    name = "Computer Tutor",
    handoff_description = "Specializes in computer science concepts and programming.",
    instructions = "You are a computer tutor. You assist with computer science concepts and programming tasks. Explain your reasoning and provide code examples."
)

async def homework_guardrail(ctx , agent , input_data):
    result = await Runner.run(guardrail_agent , input_data , context = ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info = final_output,
        tripwire_triggered= not final_output.is_homework
    )

triage_agent = Agent(
    name = "Triage Agent",
    instructions="You are a triage agent. You determine which agent to use based on the user's homework question.",
    handoffs = [math_tutor_agent , physics_tutor_agent , computer_tutor_agent],
    input_guardrails=[InputGuardrail(
        guardrail_function=homework_guardrail)
    ],
)

async def main():
    result = await Runner.run(triage_agent, "What is the second law of thermodynamics?")
    print(result.final_output)

    result = await Runner.run(triage_agent, "What is life")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    
# This code defines a system of agents that triage homework questions and route them to the appropriate tutor agent.
