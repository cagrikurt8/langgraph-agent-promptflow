from promptflow.core import tool
from promptflow.connections import CustomConnection
from LangGraphAssistant import LangGraphAssistant


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def answer_with_agent(question: str, user_id: str, oai_conn: CustomConnection) -> str:
    assistant = LangGraphAssistant(oai_conn, user_id, user_id)
    answer = assistant.get_answer(question)

    return answer['messages'][-1].content
