import asyncio
from dotenv import load_dotenv

from conversation_manager import ConversationManager

if __name__ == "__main__":
    load_dotenv()
    manager = ConversationManager()
    asyncio.run(manager.main())
