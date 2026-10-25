import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )




def main():
    print("Hello from langchain course")
    print(os.environ.get("GROQ_API_KEY"))

    model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.0,
    max_retries=2,
    )

    llm = ChatOllama(
    model="gemma3:270m",
    temperature=0,
)
    input_text = "Let the children of Shri Ramakrishna be true to themselves and everything will be all right. We may not live to see the outcome, but as sure as we live, it will come sooner or later. What India wants is a new electric fire to stir up a fresh vigour in the national veins. This was ever, and always will be, slow work. Be content to work, and, above all, be true to yourself. Be pure, staunch, and sincere to the very backbone, and everything will be all right. If you have marked anything in the disciples of Shri Ramakrishna, it is this — they are sincere to the backbone. My task will be done, and I shall be quite content to die, if I can bring up and launch one hundred such men over India. He, the Lord, knows best. Let ignorant men talk nonsense. We neither seek aid nor avoid it — we are the servants of the Most High. The petty attempts of small men should be beneath our notice. Onward! Upon ages of struggle a character is built. Be not discouraged. One word of truth can never be lost; for ages it may be hidden under rubbish, but it will show itself sooner or later. Truth is indestructible, virtue is indestructible, purity is indestructible. Give me a genuine man; I do not want masses of converts. My son, hold fast! Do not care for anybody to help you. Is not the Lord infinitely greater than all human help? Be holy — trust in the Lord, depend on Him always, and you are on the right track; nothing can prevail against you."
    prompt = PromptTemplate.from_template("Understand the given statement: {foo}\n\nWrite the key understanding as points like '1. 2. 3.'.")
    

    chain = prompt | llm
    output = chain.invoke({"foo": input_text})
    print("Output:\n\n", output.content)

if __name__ == "__main__":
    main()
