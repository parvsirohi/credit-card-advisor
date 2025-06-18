# agent.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def build_credit_card_agent():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.4)

    memory = ConversationBufferMemory()
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    return conversation

if __name__ == "__main__":
    chat = build_credit_card_agent()

    print("🤖 Agent: Hi! I’ll help you find the best credit card. Type 'exit' to stop.\n")
    
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "exit":
            break
        response = chat.predict(input=user_input)
        print(f"🤖 Agent: {response}\n")
