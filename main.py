from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QCoreApplication
import requests
import pygame
import sys
from main_window import Ui_MainWindow
import speedtest
from PySide2.QtCore import QThread
import time


# Classe que trabalha com Thread, que é a execução de funções sem travar o programa. Se quiser que uma função seja
# executada sem travar o sistema, deve-se criar uma isntância dessa classe para rodar a função.
class SpeedTestThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.func = None

    def __del__(self):
        self.wait()

    def set_function(self, func, param=None):
        self.func = func
        self.param = param

    def run(self):
        if self.param == None:
            # print("Sem parâmetro!")
            if self.func:
                self.func()
        else:
            if self.func:
                # print("Com parâmetro!")
                self.func(self.param)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
        self.check_internet_connection()



        # Se clicado, o botão de selecionar servidor chama uma função que libera o combobox e o botão ok pra testar
        # Com o servidor escolhido
        self.btn_selecionar_servidor.clicked.connect(self.enable_with_btn_seleciona_servidor)
        self.btn_parar_monitoramento.clicked.connect(self.parar_monitora_internet)
        self.btn_monitora_internet.clicked.connect(self.inicia_monitora_internet)


    def inicia_monitora_internet(self):
        self.teste = True
        self.btn_monitora_internet.setDisabled(True)
        self.btn_parar_monitoramento.setEnabled(True)
        ##################################################
        self.bloco2 = SpeedTestThread()                  #
        self.bloco2.set_function(self.monitora_internet) #
        self.bloco2.start()                              #
        ##################################################

    def parar_monitora_internet(self):
        self.btn_monitora_internet.setEnabled(True)
        self.btn_parar_monitoramento.setDisabled(True)
        self.teste = False

    def monitora_internet(self):
        url = 'https://www.google.com/'
        timeout = 5  # Tempo limite para tentar se conectar


        self.internet_status = ""

        try:
            _ = requests.get(url, timeout=timeout)
            # print("Internet Ok")
            self.internet_status = "ok"
        except requests.ConnectionError:
            # print("Internet Ruim!")
            self.internet_status = "not_ok"



        if self.internet_status == "ok":
            i = 0
            while self.teste:
                try:
                    test = requests.get(url, timeout=timeout)
                    if test.status_code == 200:
                        print("Internet Ok!")
                        if i == 0:
                            self.internet_online()
                            i += 1
                            pass
                        time.sleep(2)
                        pass
                except:
                    self.internet_offline()
                    print("Internet caiu!")
                    break
                QApplication.processEvents()

        print("Entramos no else do sem internet")
        if self.teste == True:
            a = 0
            print("Entramos no IFFFF")
            while self.teste:
                try:
                    test = requests.get(url, timeout=timeout)
                    if test.status_code == 200:
                        if a == 1:
                            self.internet_online()
                            a = 0
                        print("Internet Voltou!!!")
                        time.sleep(2)
                        pass
                except:
                    if a == 0:
                        self.internet_offline()
                        a += 1
                    print("Internet fora!")
                    time.sleep(2)
                    pass

        if self.teste == True:
            self.monitora_internet()
        else:
            self.teste = True
            pass



    def definindo_sons(self):
        # inicia a entrada de sons no programa
        pygame.mixer.init()
        self.musica = pygame.mixer.Channel(7)
        self.musica_online = pygame.mixer.Sound("./sounds/internet_online.mp3")
        self.musica_offline = pygame.mixer.Sound("./sounds/internet_offline.mp3")

    def internet_offline(self):
        self.definindo_sons()
        text = self.lb_online_offline.text()
        if "Online" or "Testando" in text:
            self.musica.play(self.musica_offline, loops=0)
            self.musica.set_volume(0.5)
            self.lb_online_offline.setText(QCoreApplication.translate("MainWindow",
                                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Offline</span></p></body></html>",
                                                                      None))
            self.img_status_da_internet.setPixmap('./images/sinal_vermelho.png')
    def internet_online(self):
        self.definindo_sons()
        text = self.lb_online_offline.text()
        if "Offline" or "Testando" in text:
            self.musica.play(self.musica_online, loops=0)
            self.musica.set_volume(0.5)
            self.lb_online_offline.setText(QCoreApplication.translate("MainWindow",
                                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Online</span></p></body></html>",
                                                                      None))
            self.img_status_da_internet.setPixmap('./images/sinal_verde.png')

    # Função que roda a primeira vez o speedtest na chamada do programa
    def first_test(self):

        self.lb_teste_de_velocidade_loading.setText("Executando primeiro teste...")
        speedtester = speedtest.Speedtest()
        server = speedtester.get_best_server()
        download_speed = speedtester.download()
        upload_speed = speedtester.upload()
        ping = speedtester.results.ping

        self.download_speed_txt = "{:.2f} Mbps".format(download_speed / 1000000)
        self.upload_speed_txt = "{:.2f} Mbps".format(upload_speed / 1000000)
        self.ping_txt = "{} ms".format(ping)
        self.server_txt = f"{server['sponsor']} ({server['country']}, {server['name']})"
        self.operadora_txt = f"{server['cc']} {server['country']} ({server['id']})"

        self.lb_download_velocidade.setText(str(self.download_speed_txt))
        self.lb_upload_velocidade.setText(str(self.upload_speed_txt))
        self.lb_ping_velocidade.setText(str(self.ping_txt))
        self.lb_servidor_velocidade.setText(str(self.server_txt))
        self.lb_operadora_velocidade.setText(str(self.operadora_txt))

        self.btn_selecionar_servidor.setEnabled(True)

        self.lb_teste_de_velocidade_loading.setText("Primeiro teste concluído!")
        self.btn_monitora_internet.setEnabled(True)
        self.inicia_monitora_internet()

    # Função para obter a lista dos servidores disponíveis para o teste de velocidade
    def obtendo_lista_servidores(self):
        speedtester = speedtest.Speedtest()

        # Obtendo um dicionário com os servidores disponíveis
        self.servidores_speedtest_json = speedtester.get_servers()
        print(self.servidores_speedtest_json)

        # Criando listas para obter nomes dos servidores disponíveis para testar a velocidade da conexão e os IDs
        self.lista_servidores_nomes_ids = []
        self.lista_servidores_nomes = []

        # iternando sobre a lista obtida acima para criar um dicionário somente com o nome do servidor e com o ID
        # e logo após criando uma lista com o nome do servidor para ser usado no combobox
        for key in self.servidores_speedtest_json:
            for dicionario_valor in self.servidores_speedtest_json[key]:
                self.lista_servidores_nomes_ids.append(
                    {"Nome: ": dicionario_valor['sponsor'], "id": dicionario_valor['id']})
                self.lista_servidores_nomes.append((str(dicionario_valor['sponsor'])))

        # Usando a lista de nomes de servidores obtida pela iteração acima para aparecer na combobox
        self.cb_servidores.addItems(self.lista_servidores_nomes)

        # Inicia a função que está entre parenteses quando o botão for clicado
        self.btn_testar_internet_servidor_selecionado.clicked.connect(self.test_with_selected_server)

    # Função na chamada do botão para testar com o servidor selecinado
    def test_with_selected_server(self):
        # Cria a variável self.texto_atual_cb que recebe o valor atual do combobox
        self.texto_atual_cb = self.cb_servidores.currentText()

        # Cria a variável self.id_servidor_escolhido
        self.id_servidor_escolhido = ""
        # Iteração para obter o ID referente ao nome do servidor obtido da variável criada acima
        for server in self.lista_servidores_nomes_ids:
            # Se a nome na variável acima for o mesmo da chave que está sendo iterada, a variável
            # self.id_servidor_escolhido recebe o valor que tiver na chave 'id' nessa iteração
            if server['Nome: '] == self.texto_atual_cb:
                self.id_servidor_escolhido = server['id']

        # Instância da classe SpeedTestThread para executar a função test_speed com parâmetro do ID do servidor.
        #######################################################################
        self.bloco = SpeedTestThread()  #
        self.bloco.set_function(self.test_speed, self.id_servidor_escolhido)  #
        self.bloco.start()  #
        #######################################################################

    # Função que será chamada quando já tiver sido feita uma escolha de servidor
    def test_speed(self, servidor):
        self.btn_testar_internet_servidor_selecionado.setDisabled(True)
        self.cb_servidores.setDisabled(True)
        self.lb_teste_de_velocidade_loading.setText("Testando com servidor selecionado...")
        speedtester = speedtest.Speedtest()
        # servers = speedtester.get_servers()
        # print(servers)

        # Laço que pega o id do servidor passado para essa função (test_speed) como parâmetro e extrai todo o
        # dicionário referente a esse servidor, para passar pra função get_best_server, da classe speedtester, que
        # setará como servidor de testes o servidor escolhido
        for ping, servers in self.servidores_speedtest_json.items():
            for server in servers:
                if server['id'] == servidor:
                    if not isinstance(server, dict):
                        print("Não é um dicionário!")
                    else:
                        speedtester.get_best_server([server])
                        break

        download_speed = speedtester.download()
        upload_speed = speedtester.upload()
        ping = speedtester.results.ping

        self.download_speed_txt = "{:.2f} Mbps".format(download_speed / 1000000)
        self.upload_speed_txt = "{:.2f} Mbps".format(upload_speed / 1000000)
        self.ping_txt = "{} ms".format(ping)
        self.server_txt = f"{server['sponsor']} ({server['country']}, {server['name']})"
        self.operadora_txt = f"{server['cc']} {server['country']} ({server['id']})"

        self.lb_download_velocidade.setText(str(self.download_speed_txt))
        self.lb_upload_velocidade.setText(str(self.upload_speed_txt))
        self.lb_ping_velocidade.setText(str(self.ping_txt))
        self.lb_servidor_velocidade.setText(str(self.server_txt))
        self.lb_operadora_velocidade.setText(str(self.operadora_txt))

        self.btn_testar_internet_servidor_selecionado.setEnabled(True)
        self.cb_servidores.setEnabled(True)
        self.lb_teste_de_velocidade_loading.setText("Teste com servidor selecionado concluido!")

    # Função para testar a conexão com a ‘internet’
    def check_internet_connection(self):
        url = 'https://www.google.com/'
        timeout = 5  # Tempo limite para tentar se conectar
        try:
            _ = requests.get(url, timeout=timeout)
            print('Conexão de internet bem-sucedida')
            self.obtendo_lista_servidores()
            self.internet_online()

            # Criando thread para exdcutar a função first_test
            ##############################################
            self.bloco = SpeedTestThread()               #
            self.bloco.set_function(self.first_test)     #
            self.bloco.start()                           #
            ##############################################
            return True

        except requests.ConnectionError:
            # print('Sem conexão de internet disponível.')
            self.internet_offline()
            return False

    # Função acionada pelo butão de selecionar servidor. Libera os o combobox com os servidores disponíveis e o botão ok
    def enable_with_btn_seleciona_servidor(self):
        self.btn_selecionar_servidor.setDisabled(True)
        self.btn_testar_internet_servidor_selecionado.setEnabled(True)
        self.cb_servidores.setEnabled(True)


# Precisa de apenas uma instância por aplicação
app = QApplication(sys.argv)
# Criação do qtwidget que será a janela
window = MainWindow()
# Começa o evento loop
window.show()

app.exec_()
