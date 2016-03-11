'''
This program renews the books from UFSM's library.
Copyright (C) 2016 Henrique Mayer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# Renovador de livros da biblioteca UFSM

from splinter import Browser
import time

browser = Browser() # definir browser preferencial 'chrome' or 'firefox'
browser.visit('https://portal.ufsm.br/biblioteca/login.html')
browser.fill('j_username', '') # preencher o segundo campo com a matricula
browser.fill('j_password', '') # preencher o segundo campo com a senha
button = browser.find_by_name('enter')
button.click()
browser.visit('https://portal.ufsm.br/biblioteca/leitor/situacao.html')
# pegar um livro para terminar o código...
