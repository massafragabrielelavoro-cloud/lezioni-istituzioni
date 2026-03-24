import streamlit as st
import graphviz

# Configurazione della pagina
st.set_page_config(page_title="Mappa Istituzioni", page_icon="🇮🇹", layout="wide")

st.title("Il Sistema Istituzionale Italiano")
st.markdown("Esplora la mappa concettuale per comprendere l'equilibrio dei poteri, poi apri i moduli sottostanti per approfondire ogni singolo blocco logico.")

# --- LA MAPPA CONCETTUALE VISIVA ---
st.subheader("📌 Mappa delle Relazioni e dei Poteri")

mappa = graphviz.Digraph(engine='dot')
mappa.attr(rankdir='TB', size='8,8')

mappa.node('Costituzione', 'Costituzione Italiana\n(Legge Fondamentale 1948)', shape='box', style='filled', fillcolor='lightblue')
mappa.node('Popolo', 'Cittadini Elettori\n(Sovranità e Democrazia Diretta)', shape='ellipse', style='filled', fillcolor='lightgrey')
mappa.node('Parlamento', 'Parlamento\n(Potere Legislativo)', shape='box', style='filled', fillcolor='lightgreen')
mappa.node('PdR', 'Presidente della Repubblica\n(Garante e Arbitro)', shape='ellipse', style='filled', fillcolor='gold')
mappa.node('Governo', 'Governo\n(Potere Esecutivo)', shape='box', style='filled', fillcolor='lightcoral')
mappa.node('Magistratura', 'Magistratura\n(Potere Giudiziario)', shape='box', style='filled', fillcolor='plum')
mappa.node('Consulta', 'Corte Costituzionale\n(Giudice delle Leggi)', shape='ellipse', style='filled', fillcolor='wheat')

mappa.edge('Costituzione', 'PdR', label=' Definisce i poteri')
mappa.edge('Costituzione', 'Consulta', label=' Difesa da')
mappa.edge('Popolo', 'Parlamento', label=' Elegge direttamente')
mappa.edge('Popolo', 'Costituzione', label=' Referendum Abrogativo', style='dashed')
mappa.edge('Parlamento', 'PdR', label=' Elegge (in seduta comune)')
mappa.edge('Parlamento', 'Governo', label=' Vota la FIDUCIA (Vitale!)', color='red', penwidth='2.0')
mappa.edge('PdR', 'Governo', label=' Nomina il Premier')
mappa.edge('PdR', 'Parlamento', label=' Può sciogliere le Camere')
mappa.edge('Governo', 'Parlamento', label=' Decreti Legge (da convertire)')

st.graphviz_chart(mappa, use_container_width=True)

st.markdown("---")

# --- I MODULI DI LEZIONE (Ora completi al 100% per il quiz) ---
st.subheader("📚 Moduli di Studio (Clicca per espandere)")

with st.expander("1️⃣ Fondamenta, Identità e Collocazione"):
    st.write("""
    **Il Contesto:** L'Italia esce dalla Seconda Guerra Mondiale e dalla dittatura. Nel 1946 sceglie la **Repubblica** (forma di Stato) e adotta una forma di governo **parlamentare**. Nel 1948 entra in vigore la **Costituzione**, la **legge fondamentale** dello Stato.
    * **Identità:** L'Articolo 1 la definisce fondata sul **lavoro**. L'Articolo 3 sancisce la pari dignità **sociale**. L'Articolo 11 ripudia la **guerra** in modo assoluto.
    * **Il Voto:** È un diritto (personale, eguale, libero e **segreto**) e un dovere **civico**.
    * **Simboli e Alleanze:** La Festa della Repubblica è a **giugno**. Il primo colore della bandiera partendo dall'asta è il **verde** e l'Inno è di **Mameli**. L'Italia è fondatrice dell'Unione **Europea**, membro dell'alleanza militare **NATO** e regola i rapporti con la Chiesa tramite i Patti **Lateranensi** (1929).
    """)

with st.expander("2️⃣ Il Parlamento (Chi fa le leggi)"):
    st.write("""
    **Il Contesto:** Unico organo eletto direttamente dai **cittadini** (dai **18** anni in su). Vige il bicameralismo **perfetto**: le due camere hanno gli stessi poteri.
    * **Composizione:** La Camera dei Deputati (Camera bassa) sta a **Montecitorio** (**400** eletti, età minima **25** anni). Il **Senato** della Repubblica (Camera alta) sta a Palazzo **Madama** (**200** eletti, età minima **40** anni), a cui si aggiungono i **senatori a vita** (nominati per altissimi meriti).
    * **Regole:** Una legislatura dura **5** anni. I membri rappresentano l'intera **Nazione**. Quando si riuniscono tutti insieme si chiama seduta **comune**.
    * **Il lavoro:** Detengono il potere **legislativo**. Un testo in bozza è un **disegno** di legge. La legge sui conti pubblici è la legge di **bilancio**.
    """)

with st.expander("3️⃣ Il Governo (Chi amministra lo Stato)"):
    st.write("""
    **Il Contesto:** Detiene il potere **esecutivo**.
    * **Il Motore - La Fiducia:** Esiste solo se ottiene la **fiducia** dal Parlamento. Se il Parlamento vota contro, il Governo deve dare le **dimissioni**.
    * **Struttura:** A capo c'è il **Presidente Consiglio** (oggi Giorgia **Meloni**, di **Fratelli d'Italia**, alleata con **Lega** di Salvini, **Forza Italia** di Berlusconi e **Noi Moderati**). Siede a **Palazzo Chigi**. Guida i Ministri (al vertice di ogni singolo **dicastero**; quelli senza portafoglio di spesa sono Ministri senza **portafoglio**). Insieme formano il **Consiglio Ministri**. I Ministri possono essere contemporaneamente parlamentari (**Sì**).
    * **Gli Strumenti:** Il **Decreto Legge** (casi urgenza, da convertire entro **60** giorni) e il **Decreto Legislativo** (su perimetro del Parlamento).
    * **I Ministeri:** **Interno** (polizia), **Esteri** (rapporti altri Paesi), **Economia** (tasse), **Giustizia** (carceri/tribunali), **Salute** (ospedali), **Istruzione** (scuole).
    """)

with st.expander("4️⃣ Il Presidente della Repubblica (Il Garante)"):
    st.write("""
    **Il Contesto:** È il **Garante** della Costituzione e ha un ruolo super partes. 
    * **Chi è e dove sta:** Sergio **Mattarella** (2026), risiede al **Quirinale** e usa la tenuta estiva di **Castelporziano**.
    * **Elezione e Mandato:** Eletto dal **Parlamento** in seduta comune più i **delegati** inviati dalle Regioni. Età minima **50** anni, mandato di **7** anni, può essere rieletto (**Sì**). Se impossibilitato, lo sostituisce il Presidente del **Senato**. A fine mandato diventa automaticamente **senatore a vita**.
    * **I Poteri:** Firma la nomina ufficiale dei Ministri, ha il comando formale delle Forze Armate, ha il potere di cancellare una pena (**grazia**). Ha il potere di sciogliere le Camere in anticipo.
    * **Sulle leggi:** Prima di pubblicarle le **promulga**. Può rifiutarsi di firmarle solo **una** volta.
    """)

with st.expander("5️⃣ Giustizia e Controllo (Magistratura e Consulta)"):
    st.write("""
    * **Magistratura:** Detiene il potere **giudiziario**. I giudici sono soggetti soltanto alla **legge**. L'organo di autogoverno (presieduto dal Capo dello Stato) è il **CSM**. 
    * **Regole penali:** La responsabilità penale è sempre **personale**. Ci sono **3** gradi di giudizio ordinari, il massimo è la **Cassazione**. Chi indaga in tribunale è il Pubblico **Ministero**.
    * **Corte Costituzionale (La Consulta):** Giudica se le leggi rispettano la Costituzione. Composta da **15** giudici con mandato di **9** anni. Può giudicare il Capo dello Stato per alto **tradimento**.
    """)

with st.expander("6️⃣ Enti Locali e Democrazia Diretta"):
    st.write("""
    * **Enti Locali:** L'Italia è divisa in **20** Regioni (di cui **5** a statuto speciale). A capo c'è il **Governatore**, l'organo locale che fa le leggi è il Consiglio **Regionale**. L'ente intermedio è la **Provincia**. Quello più vicino ai cittadini è il **Comune**, amministrato dal **Sindaco**.
    * **Referendum:** Strumento per cancellare una legge (**abrogativo**). Non esiste quello per proporre nuove leggi (**No**). Servono **500000** firme o **5** consigli regionali. È valido solo se si raggiunge la soglia minima di votanti (il **quorum**).
    * **Modifiche:** La Costituzione si cambia solo con legge **costituzionale** approvata a maggioranza **assoluta**.
    """)

st.success("✅ **Finito di ripassare? Sei pronto per il test!**")
