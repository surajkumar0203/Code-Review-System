from groq import Groq
from decouple import config
import json
# from prompt import user_prompt
from myapp.AIIntelligent.prompt import user_prompt,system_prompt
def code_analysis(file_content,filename):
    prompt=user_prompt(file_content,filename)
    
    client = Groq(
        api_key=config('GRAQ_CLOUD'),
    )
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        
        messages=[
            {
                "role": "system",
                "content": system_prompt()
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
    )
    return chat_completion.choices[0].message.content