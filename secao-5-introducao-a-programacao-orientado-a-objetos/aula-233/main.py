from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("E-mail: enviando...", self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print("SMS: enviando...", self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    enviada = notificacao.enviar()

    if enviada:
        print("Notificação enviada!")
    else:
        print("Não foi possível enviar a notifição!")

notificao_email = NotificacaoEmail("Testando e-mail")
notificar(notificao_email)

notificao_sms = NotificacaoSMS("Testando SMS")
notificar(notificao_sms)