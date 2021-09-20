from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from faker import Faker
import generator

import time


class CreateUser:

    def __init__(self):
        self.fake = Faker(['pt_BR'])
        self.navegador = webdriver.Chrome("driver/chromedriver.exe")

    def check_response(self):
        try:
            self.navegador.get('https://dev.aluno.cursos.contmatic.com.br/')
        except:
            WebDriverException
            return False
        return True

    def handle_response(self):
        while not self.check_response():
            print('Você precisa estar conectado á rede da Contmatic para continuar.')
            print('Pressione Y para tentar novamente')
            user_input = input()
            if user_input == 'Y':
                self.check_response()

        self.navegador.find_element_by_xpath('//*[@id="navbarDropdownMenuLink"]').click()
        self.navegador.get("https://dev.aluno.cursos.contmatic.com.br/participantes/criarConta")

    def check_exists_by_xpath(self, xpath):
        try:
            self.navegador.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def fake_data(self):
        self.cpf = self.fake.ssn()
        self.userPass = '123456'
        self.name = self.fake.name()
        self.email = self.fake.ascii_free_email()
        self.cargo = self.fake.job()
        self.phone = self.fake.msisdn()
        self.phone = self.phone.replace("55", "")
        self.company = self.fake.company()
        self.cep = generator.gerenate_cep()
        self.numero = generator.random_number(4)

    def fill_form(self):
        self.navegador.execute_script('acceptCookies()')

        input_cpf = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[1]/div/p/input')
        input_cpf.send_keys(self.cpf)

        input_pass = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[2]/div[1]/p/input')
        input_pass.send_keys(self.userPass)

        input_pass_confirm = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[2]/div[2]/p/input')
        input_pass_confirm.send_keys(self.userPass)

        input_name = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[3]/div[1]/p/input')
        input_name.send_keys(self.name)

        input_email = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[3]/div[2]/p/input')
        input_email.send_keys(self.email)

        input_cargo = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[4]/div[1]/p/input')
        input_cargo.send_keys(self.cargo)

        self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[4]/div[3]/p/input').click()
        for digit in self.phone:
            self.navegador.find_element_by_name('celular').send_keys(digit)
            time.sleep(0.1)

        input_empresa = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[5]/div/p/input')
        input_empresa.send_keys(self.company)

        input_cep = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[6]/div/p/input')
        input_cep.send_keys(self.cep)

        self.navegador.find_element_by_xpath('//*[@id="consulta_cep_cep"]').click()
        time.sleep(3)

        if self.check_exists_by_xpath('/html/body/div/div/div[3]/button[1]'):
            while True:
                self.cep = generator.gerenate_cep()
                self.navegador.find_element_by_xpath('/html/body/div/div/div[3]/button[1]').click()
                input_cep.clear()
                input_cep.send_keys(self.cep)
                self.navegador.find_element_by_xpath('//*[@id="consulta_cep_cep"]').click()
                time.sleep(3)
                if not self.check_exists_by_xpath('/html/body/div/div/div[3]/button[1]'):
                    input_numero = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[7]/div[3]/p/input')
                    input_numero.send_keys(self.numero)
                    input_sistema = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[9]/div/p/input')
                    input_sistema.send_keys('Folha Phoenix')
                    break
        else:
            input_numero = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[7]/div[3]/p/input')
            input_numero.send_keys(self.numero)
            input_sistema = self.navegador.find_element_by_xpath('//*[@id="formEdit"]/div[9]/div/p/input')
            input_sistema.send_keys('Folha Phoenix')


createUser = CreateUser()
createUser.check_response()
createUser.handle_response()
createUser.fake_data()
createUser.fill_form()
