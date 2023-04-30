from utils import messages
def return_title_for_clockfy():
    try:
        title = str(input(
            messages.error_message(
                "INSIRA O TITULO PARA SEU CLOCKFY: "))).upper()
        print(messages.sucess_message(title))
        return messages.sucess_message(title)
    except Exception as error:
        raise Exception(messages.error_message(
            "HOUVE UM ERRO AO UTILIZAR MENSAGEM:\n"
            +f"{error}"))
return_title_for_clockfy()
