# resume
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("AIzaSyCQYZDUws4GzHOqop6-FC7UlMS4jXc3P-U"),
    )

    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a professional Resume Generator AI. Generate a clean, ATS-friendly, and professional resume in text format based on the following input details.

Ask the user to enter all of the following information in one go:

1. Full Name  
2. Email Address, Phone Number, LinkedIn Profile (optional)  
3. Career Objective or Summary  
4. Work Experience (for each job, include: Job Title, Company Name, Location, Duration, Key Responsibilities or Achievements)  
5. Education (Degrees, Institutions, Years, Percentages or Grades)  
6. Skills (both Technical and Soft Skills)  
7. Certifications or Awards (optional)  
8. Projects (if any, include project name, description, and technologies used)  
9. Languages Known (optional)  
10. Hobbies or Interests (optional)

Once the user provides all the above details, generate a well-structured, professional resume with this format:

============================  
[Full Name]  
[Email] | [Phone] | [LinkedIn]  

🎯 **Career Objective**  
[Career Objective Text]

💼 **Work Experience**  
• **[Job Title]** – [Company], [Location] ([Duration])  
  - [Responsibility/Achievement 1]  
  - [Responsibility/Achievement 2]  

🎓 **Education**  
• [Degree] – [Institution], [Year] – [Grade/Percentage]

🛠️ **Skills**  
[Skill 1] | [Skill 2] | [Skill 3] | ...

🏆 **Certifications & Awards**  
- [Certification/Award Name], [Year]

🚀 **Projects**  
• **[Project Title]** – [Brief Description]  
  - Technologies: [Tech 1], [Tech 2]

🌐 **Languages Known**  
[Language 1], [Language 2]

🎯 **Hobbies & Interests**  
[Interest 1], [Interest 2]

============================

Use clean formatting, bullet points, and proper spacing. Do not invent data. Use only what the user provides. Make the resume job-ready and professional.
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
