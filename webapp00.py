# Gabi
import streamlit as st
from ACTlib01 import *

#url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRqsYs1IHpDcqSbn0vd0WhlfBO__UdkEwox69_1zphPFmISLM4BA7YTj7KSvxxHuk3-uMKAuuXAcpJX/pub?gid=270064191&single=true&output=csv"
#db = Ler_GooglePlanilha(url)
#db.columns = ["DataHora", "Nome", "Livro"]
#Escrever(db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Gabi")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("teste")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub teste")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

Divisor()
    
coluna1 = Colunas(3)
with coluna1[0]:
  Escrever("")
with coluna1[1]:
  Escrever("ACTlib Versão 0.1", "titulo")
  nome = Ler(rotulo = "Nome:", nmax=30, tipo="padrao", info="Inserção de Nome", autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder="Não esqueça de preencher seu nome", desabilitada="falso", visibilidade="visivel")
  if nome:     
    Escrever("Seja Bem vinda(o), " + nome + "!")
with coluna1[2]:
  Escrever("")
