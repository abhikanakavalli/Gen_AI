from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

from openai import OpenAI
# from groq import Groq
# from google import genai

from api.core.config import config

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_llm(provider, model_name, messages, max_tokens=500):

    logger.info("Provider: %s", provider)
    logger.info("Model: %s", model_name)

    if provider == "OpenAI":

        logger.info("Initializing OpenAI client")

        client = OpenAI(api_key=config.OPENAIKEY)

        logger.info("Sending request to OpenAI")

        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_completion_tokens=max_tokens,
            reasoning_effort="minimal"
        )

        logger.info("OpenAI API request completed")

        logger.info("Response: %s", response)

        result = response.choices[0].message.content

        logger.info("Generated content: %s", result)

        if result is None:
            raise ValueError("OpenAI returned empty message content")

        return result

    raise ValueError(f"Unsupported provider: {provider}")


# def run_llm(provider, model_name, messages, max_tokens=500):

#     if provider == "OpenAI":
#         client = OpenAI(api_key=config.OPENAIKEY)

#     # elif provider == "Groq":
#     #     client = Groq(api_key=config.GROQ_API_KEY)

#     # else:
#     #     client = genai.Client(api_key=config.GOOGLE_API_KEY)

#     # if provider == "Google":
#     #     return client.models.generate_content(
#     #         model=model_name,
#     #         contents=[message["content"] for message in messages],
#     #     ).text

#     if provider == "OpenAI":
#         return client.chat.completions.create(
#             model=model_name,
#             messages=messages,
#             max_completion_tokens=max_tokens,
#             reasoning_effort="minimal"
#         ).choices[0].message.content 

class ChatRequest(BaseModel):
    provider: str
    models_name: str
    messages: list[dict]


class ChatResponse(BaseModel):
    message: str


app = FastAPI()


@app.post("/chat")
@app.post("/chat")
def chat(request: Request, payload: ChatRequest):

    try:
        result = run_llm(
            payload.provider,
            payload.models_name,
            payload.messages
        )

        return ChatResponse(message=result)

    except Exception:
        logger.exception("Chat API failed")

        raise HTTPException(
            status_code=500,
            detail="Failed to generate response. Check server logs."
        )