import streamlit as st
import random

st.set_page_config(page_title="Planificador de Menús", page_icon="🥗", layout="wide")

# Base de datos de recetas
recetas_desayunos = ["pan con pollo o pavo"]
recetas_comidas = {
    "pollo con patatas y judias" ,
    "ternera con patatas y esparragos",
    "Salmón al horno con patatas y zanahorias",
    "Ensalada completa de atún y aguacate": ["Lechuga", "Atún en lata", "Aguacate", "Tomate"]
}
recetas_cenas = {
    "Crema de calabacín y tortilla": ["Calabacín", "Cebolla", "Huevos"],
    "Pescado blanco con verduras al vapor": ["Filete de merluza", "Brócoli", "Zanahoria"],
    "Ensalada canónigos con queso de cabra y nueces": ["Canónigos", "Queso de cabra", "Nueces"],
    "Revuelto de setas y gambas": ["Setas", "Gambas", "Huevos", "Ajo"]
}
recetas_snacks = ["Frutos secos naturales", "Una pieza de fruta", "Hummus con zanahoria"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

st.title("🥗 PLANIFICADOR DE MENÚS SALUDABLES")
st.write("Genera tu menú semanal de forma relajante.")

if st.button("🎲 Generar Nuevo Menú de Calma", type="primary"):
    texto_menu = ""
    lista_compra = set()
    
    for dia in dias:
        desayuno = random.choice(recetas_desayunos)
        comida = random.choice(list(recetas_comidas.keys()))
        cena = random.choice(list(recetas_cenas.keys()))
        snack = random.choice(recetas_snacks)
        
        for ing in recetas_comidas[comida] + recetas_cenas[cena]:
            lista_compra.add(ing)
            
        texto_menu += f"### 📅 {dia.upper()}\n"
        texto_menu += f"* ☕ **Desayuno:** {desayuno}\n"
        texto_menu += f"* ☀️ **Comida:** {comida}\n"
        texto_menu += f"* 🌙 **Cena:** {cena}\n"
        texto_menu += f"* 🍎 **Snack:** {snack}\n\n"
        texto_menu += "---\n"
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(texto_menu)
    with col2:
        st.markdown("### 🛒 LISTA DE LA COMPRA")
        for ing in sorted(lista_compra):
            st.markdown(f"• {ing}")
