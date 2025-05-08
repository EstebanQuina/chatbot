import streamlit as st
from openai import OpenAI

# Título y descripción
st.title("📄 Generador de Resúmenes Académicos")
st.write(
    "Este chatbot usa OpenAI para generar resúmenes claros de textos académicos. "
    "Pega el texto que deseas resumir y presiona el botón. Necesitas una API Key de OpenAI."
)

# Ingreso de API key
openai_api_key = st.text_input("🔑 OpenAI API Key", type="password")

# Si no hay API key, no continúa
if not openai_api_key:
    st.info("Por favor ingresa tu API key para continuar.", icon="🔒")
else:
    client = OpenAI(api_key=openai_api_key)

    # Entrada de texto académico
    user_text = st.text_area("📚 Pega tu texto académico aquí:", height=300)

    # Selector de tipo de resumen
    summary_type = st.selectbox("📌 Tipo de resumen", ["Resumen breve", "Puntos clave", "Resumen en lenguaje sencillo"])

    if st.button("📝 Generar resumen") and user_text:
        with st.spinner("Generando resumen..."):

            # Instrucción adaptada según el tipo de resumen
            if summary_type == "Resumen breve":
                instruction = "Resume el siguiente texto académico en un párrafo claro:"
            elif summary_type == "Puntos clave":
                instruction = "Extrae los puntos clave del siguiente texto académico como una lista:"
            else:
                instruction = "Explica el siguiente texto académico en lenguaje sencillo para estudiantes de secundaria:"

            # Llamada a la API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente experto en generar resúmenes académicos."},
                    {"role": "user", "content": f"{instruction}\n\n{user_text}"}
                ]
            )

            summary = response.choices[0].message.content

        st.markdown("### ✨ Resumen generado:")
        st.write(summary)
