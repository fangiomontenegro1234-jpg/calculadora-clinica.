import streamlit as st

def calcular():
    st.title("📊 Monitor Fisiológico Clínico")
    st.sidebar.header("Entrada de Datos")

    # Entradas en la barra lateral para que se vea limpio en el móvil
    pvo2 = st.sidebar.number_input("PvO2 (B2)", value=40.0)
    po2 = st.sidebar.number_input("PaO2 (B3)", value=90.0)
    fio2 = st.sidebar.slider("FiO2 (B4)", 0.21, 1.0, 0.21)
    pvco2 = st.sidebar.number_input("PvCO2 (B5)", value=45.0)
    pco2 = st.sidebar.number_input("PaCO2 (B6)", value=40.0)
    hco3 = st.sidebar.number_input("HCO3 (B7)", value=24.0)
    sao2 = st.sidebar.slider("SaO2 (B8)", 0.0, 1.0, 0.98)
    svo2 = st.sidebar.slider("SvO2 (B9)", 0.0, 1.0, 0.75)
    hb = st.sidebar.number_input("Hb (B10)", value=15.0)
    gc = st.sidebar.number_input("GC (B32)", value=5.0)

    # Cálculos
    p_alv = (513 * fio2) - (pco2 / 0.8)
    cao2 = (1.34 * hb * sao2) + (po2 * 0.003)
    cvo2 = (1.34 * hb * svo2) + (pvo2 * 0.003)
    cap_o2 = (1.34 * hb * 1) + (p_alv * 0.003)
    dav_o2 = cao2 - cvo2
    shunt = ((cap_o2 - cao2) / (cap_o2 - cvo2) * 100) if (cap_o2 - cvo2) != 0 else 0
    ido2 = gc * cao2 * 10
    vo2 = gc * dav_o2 * 10

    # Mostrar Resultados en tarjetas visuales
    col1, col2 = st.columns(2)
    col1.metric("CaO2 (Arterial)", f"{cao2:.2f}")
    col2.metric("CvO2 (Venoso)", f"{cvo2:.2f}")

    st.subheader("Análisis Hemodinámico")
    st.write(f"**Shunt Pulmonar:** {shunt:.2f}%")
    st.write(f"**Entrega de O2 (IDO2):** {ido2:.2f} ml/min")
    st.write(f"**Consumo de O2 (VO2):** {vo2:.2f} ml/min")

    if shunt > 20:
        st.error("⚠️ Alerta: Shunt elevado detectado.")

if __name__ == "__main__":
    calcular()
