def user_prompt(file_content,filename):
    return f"""
            Analyze the following code for:
            - Code style and formatting issues
            - Potential Bugs or errors
            - Performance improvements
            - Best practices
            - Security vulnerabilities
        File : {filename}
        Content : {file_content}

        Provide a detailed JSON output with the structure
        {{
            "issues":[
                {{
                    "type": "<style|bugs|Performance|Best_practices|Security_vulnerabilities">,
                    "line": <line_number>,
                    "description": <description>,
                    "suggestion": <suggestion>
                }},
            ]  
        }}
        ```.json()
        """

def system_prompt():
    return """
        System Message:
            This code review system is designed to analyze code for various issues and provide suggestions for improvements, Potential Bugs or errors, Performance improvements,Best practices, if necessary Security vulnerabilities.
            The output will be a JSON object containing the following structure Here is an example of JSON response:
        ```
        {
            "name":"main.py",

            "issues":[
                {
                    "type": "style",
                    "line": 12,
                    "description": "Line is too long",
                    "suggestion": "Break line into multiple lines"
                },
                {
                    "type": "bugs",
                    "line": 19,
                    "description": "Line is too long",
                    "suggestion": "Break line into multiple lines"
                },
                {
                    "type": "Performance",
                    "line": 19,
                    "description": "Line is too long",
                    "suggestion": "Break line into multiple lines"
                },
                {
                    "type": "Best_practices",
                    "line": 19,
                    "description": "Line is too long",
                    "suggestion": "Break line into multiple lines"
                },
                {
                    "type": "Security_vulnerabilities",
                    "line": 19,
                    "description": "Line is too long",
                    "suggestion": "Break line into multiple lines"
                },
            ]
        }
        ```
        """