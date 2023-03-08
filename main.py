from PySide2.QtWidgets import QApplication, QMainWindow
import requests
import sys
from main_window import Ui_MainWindow
import speedtest

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
        self.check_internet_connection()

        self.obtendo_lista_servidores()


    # Função que roda a primeira vez o speedtest na chamada do programa
    def first_test(self):
        speedtester = speedtest.Speedtest()
        server = speedtester.get_best_server()
        download_speed = speedtester.download()
        upload_speed = speedtester.upload()
        ping = speedtester.results.ping

        download_speed_txt = "{:.2f} Mbps".format(download_speed / 1000000)
        upload_speed_txt = "{:.2f} Mbps".format(upload_speed / 1000000)
        ping_txt = "{} ms".format(ping)
        server_txt = f"{server['sponsor']} ({server['country']}, {server['name']})"
        operadora_txt = f"{server['cc']} {server['country']} ({server['id']})"

        self.text_download.setText(str(download_speed_txt))
        self.text_upload.setText(str(upload_speed_txt))
        self.text_ping.setText(str(ping_txt))
        self.text_servidor.setText(str(server_txt))
        self.text_operadora.setText(str(operadora_txt))



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
                self.lista_servidores_nomes_ids.append({"Nome: ": dicionario_valor['sponsor'], "id": dicionario_valor['id']})
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

        self.test_speed(self.id_servidor_escolhido)


    # Função que será chamada quando já tiver sido feita uma escolha de servidor
    def test_speed(self, servidor):
        speedtester = speedtest.Speedtest()
        # servers = speedtester.get_servers()
        # print(servers)

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


        download_speed_txt = "{:.2f} Mbps".format(download_speed / 1000000)
        upload_speed_txt = "{:.2f} Mbps".format(upload_speed / 1000000)
        ping_txt = "{} ms".format(ping)
        server_txt = f"{server['sponsor']} ({server['country']}, {server['name']})"
        operadora_txt = f"{server['cc']} {server['country']} ({server['id']})"

        self.text_download.setText(str(download_speed_txt))
        self.text_upload.setText(str(upload_speed_txt))
        self.text_ping.setText(str(ping_txt))
        self.text_servidor.setText(str(server_txt))
        self.text_operadora.setText(str(operadora_txt))

    # Função para testar a conexão com a ‘internet’
    def check_internet_connection(self):
        url = 'https://www.google.com/'
        timeout = 5  # Tempo limite para tentar se conectar
        try:
            _ = requests.get(url, timeout=timeout)
            print('Conexão de internet bem-sucedida')
            self.img_status_da_internet.setPixmap('./images/sinal_verde.png')
            self.lb_online_offline.setText("Online")
            self.enable_buttons()
            self.first_test()
            return True
        except requests.ConnectionError:
            print('Sem conexão de internet disponível.')
            self.img_status_da_internet.setPixmap('./images/sinal_vermelho.png')
            self.lb_online_offline.setText("Offline")
            self.btn_monitora_internet.setEnabled()
            return False

    def enable_buttons(self):
        self.btn_monitora_internet.setEnabled()
        self.text_download.setEnabled()
        self.text_upload.setEnabled()
        self.text_ping.setEnabled()
        self.text_servidor.setEnabled()
        self.text_operadora.setEnabled()


# Precisa de apenas uma instância por aplicação
app = QApplication(sys.argv)
# Criação do qtwidget que será a janela
window = MainWindow()
# Começa o evento loop
window.show()

app.exec_()
