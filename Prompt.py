# Prompt Refine Engine Example
# This project refines basic user inputs into structured, highly effective LLM prompts.
#or
#description of project
#refine input prompts to effectively guide generative AI models in producing desired output.
#techniques used:
#1.role prompting:
#Assigns a specfic "System Role" like domain expert to set context.
#2.step-by-step instructions
#adds "execution steps and rules" to guide the AI's reasoning.
# #3.output format specification
#specifies the "desired output format" like markdown with examples
# #4.Task Definition:
# Clearly states the "Core Task" from the user's input
#Implementation:
# # A python function 'refine_prompt()' takes a basic prompt and wraps it in the optimized template
# three test cases were run to show how vogue inputs become structured prompts.
#sample input 1:"explain machine learning  to a begineer"
#sample output 1:A structured prompt with role,task,4 execution steps, and markdown format requirement.
#sample input 2:"write a python code to sort a list of numbers"
# sample output 2:same structured template applied to a coding task.
#sample input 3:"summarize the impact of renewable energy on climate change"
#sample output 3:same strutured template applied to a research task.
#conclusion:
# By refining prompts,we reduce ambiguity and improve the quality of responses from generative AI models.This approach can be used for education,coding,research,and business applications. 
#Advantages of prompt refinement
#1.Better Accuracy:
#structured prompts reduce ambiguity.AI understands exactly what to do and gives more accurate answers.
#2.consistent output:
# #by defining role+steps+format,responses follow the same structure every time.
#3.saves time:
#users don't need to manually write along detailed prompts.the engine does it automatically.
#4.improved reasoning:
#adding "execution steps" forces the AI to think step_by-step,reducing errors in coding/logic tasks.
#5.begineer friendly:
#non-technical users can get expert-level outputs without knowing prompt engineering.
#disadvanatges
#1.token usage increases:
#refined prompts are longers,so they use more tokens+higher cost for API calls.
# #2.over-structing risk:
#too much structure can make the AI sound robotic and less creative for storytelling/brainstorming tasks.
#3.not one-size-fits-all:
#some tasks like casual chat or creative writing work better better with short,open prompts.
#4.dependency:
#users may rely on the engine and not learn how to write good prompts themselves.
#5.template bias:
#if the template is bad,all outputs will follow that same bas patterns.
# #real-world applications
# #1.education:
#convert "explain photosynthesis"->structured lesson with examples,steps, and summary for students.
#2.software development:
#convert "write code to sort list"_> prompt that asks for code+explanation+time complexity +test cases.
#3.content creation:
#convert "write blog" prompt with target audience,tone,headings,SEO keywords, and word count.
#4.bussiness and research:
#convert "summarize renewable energy"-> prompt that asks for data,impact,pros/cons in structured markdown tables.
#5.customer support:
#auto-refine customer queries into internal prompts for AI chatbots to give professionals,step-by-step solutions.
#6.prompt marketplaces:
#can be used as a base engine in tools like promptlayer,langchain,etc.
#summary line for submission:
#the prompt refine engine birdges the gap between vague human intent and structured AI execution,making generative AI more reliable for real-world use.

### *Process of the Prompt Refine Engine*

#### *1. Input Stage: Raw User Prompt*
#The user gives a basic, vague instruction.  
#Example: `"Explain machine learning to a beginner"`  
#Problem: Such prompts are too short and can lead to incomplete or random AI answers.

#### *2. Processing Stage: Prompt Structuring*
#the engine takes that raw input and passes it through a fixed template. This template adds 4 key components:

#1. *System Role Assignment*  
#   The AI is given a specific identity like `Domain Expert & Technical Communicator`.  
 #  _Why_: This sets the tone, expertise level, and knowledge depth of the response.

#2. *Core Task Definition*  
#   The user's original input is placed clearly under "Core Task".  
#   _Why_: Removes ambiguity about what the AI should actually do.

#3. *Execution Steps & Rules*  
#  The template adds step-by-step instructions:  
#   - Analyze requirements  
#   - Break down answer step-by-step  
#   - Be accurate and avoid vague explanations  
#   - Follow the given output format  
#   _Why_: This forces the AI to use chain-of-thought reasoning and improves accuracy.

#4. *Output Format Specification*  
#   We specify how the answer should look: `Structured Markdown with Examples`.  
#   _Why_: Ensures the response is organized, readable, and consistent every time.

#### *3. Output Stage: Optimized Prompt*
#After combining all 4 parts, the engine produces a new, detailed prompt.  
#This refined prompt is now ready to be sent to any generative AI model like ChatGPT, Gemini, etc.

#### *4. Result Stage: Better AI Response*
#When the optimized prompt is given to an LLM, it returns:  
#- More accurate answers  
#- Step-by-step explanations  
#- Consistent formatting with headings and examples  
#- Less hallucination and vagueness

### *In Simple Words:*
#Basic Prompt  →  [Add Role + Task + Steps + Format]  →  Refined Prompt  →  Better AI Output
### *Analogy*
#Think of it like this:  
#Giving a raw prompt to AI is like telling a student: "Do homework"  
#Giving a refined prompt is like telling: "You are a Science Teacher. Explain photosynthesis to a 5th grader. Use 3 steps, give 2 examples, and format in bullet points."

#The second one will always get a better result.



#### *1. Project Overview*
#The `Prompt Refine Engine` is a tool that transforms vague, basic user instructions into structured, optimized prompts.  
#Instead of the user having to think about "how to ask AI", the engine does it automatically using a fixed template.  
#The main goal is to make Generative AI more reliable, accurate, and easy to use for everyone, even non-technical people.

#### *2. Motivation / Why this project?*
#Generative AI models like ChatGPT, Gemini, Claude are very powerful but they follow the "garbage in, garbage out" principle.  
#Most people write short prompts like: "write essay" or "explain ML" and get poor, incomplete results.  
#This project bridges that gap by applying prompt engineering principles automatically so that every input becomes a high-quality instruction for the AI.

#### *3. Key Components of the Engine*
#The engine is built on 4 pillars that every good prompt should have:

#*Persona / System Role*  
#This tells the AI what expertise to use. Examples: Teacher, Coder, Researcher, Analyst.  
#Impact: It changes the tone, depth, and vocabulary of the answer and makes it more domain-specific.

#*Task Clarity / Core Task*  
#This states the exact thing the AI needs to do without any confusion.  
#Impact: It removes ambiguity from the user’s raw input.

#*Process Guidance / Execution Rules*  
#This forces the AI to follow steps instead of guessing. It is based on Chain-of-Thought prompting research.  
#Rules like "analyze first, then break down step-by-step, ensure accuracy" are added here.  
#Impact: It improves logic, accuracy, and reduces mistakes in math and coding tasks.

#*Output Control / Desired Format*  
#This defines how the answer should look: in tables, markdown, bullet points, or with examples.  
#Impact: It makes the output directly usable for reports, assignments, and documentation.

#### *4. Working Workflow*
#Step 1: User gives a basic input like "Explain ML to beginner"  
#Step 2: Engine processes it and injects it into a template with Role, Steps, and Format  
#Step 3: The engine produces a refined, detailed prompt ready for any LLM  
#Step 4: When this refined prompt is given to AI, it returns a structured, accurate answer with examples

#### *5. Types of Problems It Solves*
#Problem with raw prompts is that they are vague. The engine fixes this by adding a clear Core Task.  
#Problem is no structure. The engine fixes this by adding Output Format rules.  
#Problem is one-line answers. The engine fixes this by adding "step-by-step" and "give examples" rules.  
#Problem is inconsistent tone. The engine fixes this by fixing the tone using the System Role.

#### *6. Advantages for Different Users*
#For Students: They can get well-structured notes, explanations, and examples instantly without spending time framing prompts.  
#For Developers: They can get code along with explanation, time complexity analysis, and test cases in one go.  
#For Business Professionals: They can get reports, emails, and summaries in a proper professional format.  
#For Researchers: They can get literature summaries with pros, cons, and key data points in a structured way.

#### *7. Scalability & Extensions*
#This basic engine can be extended in many ways.  
#We can build Domain-Specific Engines like Legal Refine Engine, Medical Refine Engine, or Coding Refine Engine.  
#We can add Multi-language Support so users can refine prompts in Hindi, Telugu, etc.  
#We can add Auto-Role Detection where AI automatically picks the best role based on the input.  
#We can also integrate this engine with ChatGPT API, LangChain, or any chatbot to make it production-ready.

#### *8. Comparison: Before vs After Refinement*
#Before Refinement example: `Write python code to sort list`  
#In this case AI might just give one line of code without explanation.

#After Refinement example:  
#Role becomes Expert Python Developer.  
#Task becomes Write python code to sort a list.  
# 3Steps become Explain logic, give code, give time complexity, give 2 test cases.  
#Format becomes Structured Markdown with Examples.  
#Result: The final output is complete, production-ready, and easy to understand.

#### *9. Future Scope*
#In future we can add AI to automatically choose the best target role and output format.  
#We can build a simple UI where users just type and instantly get the refined prompt.  
#We can add a feedback loop where users rate the output and the template improves automatically.  
#This engine can also be used as the base for building full AI Agents.

#### *10. Final Conclusion*
#The Prompt Refine Engine demonstrates a core idea of Generative AI:  
#The intelligence is not just in the model, it is also in how you talk to the model.  
#By standardizing and structuring prompts, we make AI outputs consistent, professional, and useful for real-world tasks in education, business, and development.

def refine_prompt(basic_prompt: str, target_role: str = "Expert AI Assistant", output_format: str = "Markdown") -> str:
    """
    Refines a raw user prompt into an optimized prompt using structural engineering techniques.
    """
    structured_prompt = f"""
========================================
[OPTIMIZED PROMPT TEMPLATE]
========================================

### System Role:
You are an {target_role} with deep domain expertise.

### Core Task:
{basic_prompt.strip()}

### Execution Steps & Rules:
1. Analyze the core requirements carefully.
2. Break down the response step-by-step for clarity.
3. Ensure accuracy and avoid vague explanations.
4. Format the final output clearly using {output_format}.

### Desired Output Format:
Provide a clear, structured response adhering to standard {output_format} conventions.
========================================
"""
    return structured_prompt.strip()


def run_prompt_refinements():
    # Test cases: Basic user inputs
    test_inputs = [
        "Explain machine learning to a beginner",
        "Write a python code to sort a list of numbers",
        "Summarize the impact of renewable energy on climate change"
    ]

    print("--- PROMPT REFINEMENT PROCESS ---")
    
    for idx, raw_input in enumerate(test_inputs, start=1):
        refined = refine_prompt(
            basic_prompt=raw_input,
            target_role="Domain Expert & Technical Communicator",
            output_format="Structured Markdown with Examples"
        )
        print(f"\n[EXAMPLE {idx}]")
        print(f"RAW INPUT : '{raw_input}'")
        print("-" * 40)
        print("REFINED PROMPT OUTPUT:")
        print(refined)
        print("=" * 60)

if __name__ == "__main__":
    run_prompt_refinements()