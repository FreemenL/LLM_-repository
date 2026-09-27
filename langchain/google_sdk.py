def call_gemini():
    import os
    from google import genai
    from dotenv import load_dotenv
    load_dotenv()
    client=genai.Client(
        api_key=os.getenv("OPENAI_API_KEY"),
        http_options= {
            "base_url":"https://api.openai-proxy.org/google"
        }
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="你是谁·能做什么",
    )
    print(response.text)


call_gemini()