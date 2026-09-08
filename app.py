import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="Planificador de Menús", page_icon="🥗")

# Estilos personalizados en tonos tierra y beige
st.markdown("""
    <style>
    .main { background-color: #FDFBF7; }
    .stButton>button { background-color: #8C7A6B; color: white; border-radius: 8px; }
    h1, h2, h3 { color: #5C4D42; }
    </style>
""", unsafe_allow_html=True)

recetas_desayunos = ["Gachas de avena con bayas", "Tostada de aguacate", "Yogur con nueces", "Tortilla de espinacas"]
recetas_comidas = {
    "Lentejas estofadas con verduras": ["Lentejas", "Zanahoria", "Cebolla", "Pimiento"],
    "Pechuga de pollo con arroz integral": ["Pechuga de pollo", "Arroz integral", "Ajo"],
    "Salmón al horno con patatas": ["Lomo de salmón", "Patatas", "Romero"],
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

st.title("🥗 Planificador de Menús Saludables")
st.write("Genera tu menú semanal relajante en tonos calma.")

if st.button("🎲 Generar Nuevo Menú de Calma"):
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
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(texto_menu)
    with col2:
        st.subheader("🛒 Lista de la Compra")
        for ing in sorted(lista_compra):
            st.write(f"• {ing}")
