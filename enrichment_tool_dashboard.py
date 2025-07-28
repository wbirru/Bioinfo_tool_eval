import streamlit as st
import requests
import pandas as pd
import datetime

st.set_page_config(page_title="Gene Set Enrichment Tools", layout="wide")
st.title("🔬 Gene Set Enrichment Tools Dashboard")

# 📅 Current date
st.caption(f"🗓️ Today: {datetime.datetime.now().strftime('%A, %B %d, %Y')}")

# 🧠 Memory/contextual info
st.info("""
This platform integrates genomic enrichemnt tools to understand and evaluate their performace.
It uses tools such as gProfiler, Enrichr, Metascape, WebGestalt, DAVID and ClusterProfiler, emphasizing user-friendly interfaces and transparent data sources.
Developed for advanced genomic analysis and related applications.
""")

# === Sidebar ===
st.sidebar.header("Input Genes")
genes_input = st.sidebar.text_area("Enter gene symbols (comma-separated):", "FSHR, LHCGR, CYP19A1, ESR1, INHBA")
genes = [g.strip() for g in genes_input.split(",") if g.strip()]
run_button = st.sidebar.button("🚀 Run Analysis")

# === gProfiler Integration ===
@st.cache_data
def run_gprofiler(genes):
    url = "https://biit.cs.ut.ee/gprofiler/api/gost/profile/"
    payload = {
        "organism": "hsapiens",
        "query": genes,
        "sources": ["GO:BP", "KEGG", "REAC"],
        "no_evidences": True
    }
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            return pd.json_normalize(r.json().get("result", []))
    except Exception as e:
        st.error(f"gProfiler error: {e}")
    return pd.DataFrame()

# === Enrichr Integration ===
@st.cache_data
def run_enrichr(genes, library="KEGG_2021_Human"):
    try:
        res = requests.post("https://maayanlab.cloud/Enrichr/addList", files={"list": (None, "\n".join(genes))})
        if not res.ok: return pd.DataFrame()
        user_list_id = res.json()['userListId']
        res2 = requests.get("https://maayanlab.cloud/Enrichr/enrich", params={
            "userListId": user_list_id, "backgroundType": library
        })
        data = res2.json().get(library, [])
        if not data: return pd.DataFrame()
        df = pd.DataFrame(data, columns=[
            "Rank", "Term", "P-value", "Z-score", "Combined Score",
            "Overlapping Genes", "Adjusted P-value", "Old P-value", "Old Adjusted P-value"
        ])
        return df.drop(columns=["Old P-value", "Old Adjusted P-value"])
    except Exception as e:
        st.error(f"Enrichr error: {e}")
        return pd.DataFrame()

# === WebGestalt ID Mapping API Integration ===
@st.cache_data
def run_webgestalt_idmapping(genes):
    url = "https://www.webgestalt.org/api/idmapping"
    payload = {
        "organism": "hsapiens",
        "sourceType": "genesymbol",
        "targetType": "entrezgene",
        "ids": genes,
        "standardId": "entrezgene"
    }
    try:
        r = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        data = r.json()
        df = pd.DataFrame(data.get("mapped", []))
        return df
    except Exception as e:
        st.error(f"WebGestalt ID mapping error: {e}")
        return pd.DataFrame()

# === Tool Summaries and Outputs ===
if run_button and genes:
    st.subheader("1️⃣ gProfiler")
    st.markdown("**Summary:** GO, KEGG, HPO enrichment with orthology support.  \n**API/Automation:** ✅ Full API supported")
    gp_df = run_gprofiler(genes)
    if not gp_df.empty:
        st.dataframe(gp_df.head(10))
        st.download_button("⬇ Download gProfiler Results", gp_df.to_csv(index=False), "gprofiler.csv")
    else:
        st.info("No enrichment found from gProfiler.")
    st.link_button("🌐 Open gProfiler", "https://biit.cs.ut.ee/gprofiler/gost")
    
    st.subheader("2️⃣ Enrichr")
    st.markdown("**Summary:** Large curated libraries for TFs, drugs, pathways.  \n**API/Automation:** ✅ Full API supported")
    enr_df = run_enrichr(genes)
    if not enr_df.empty:
        st.dataframe(enr_df.head(10))
        st.download_button("⬇ Download Enrichr Results", enr_df.to_csv(index=False), "enrichr.csv")
    else:
        st.info("No enrichment results from Enrichr.")
    st.link_button("🌐 Open Enricher", "https://maayanlab.cloud/Enrichr/")
    
    st.subheader("3️⃣ WebGestalt (ID Mapping API)")
    st.markdown("**Summary:** Map gene symbols to Entrez IDs and explore supported annotations.  \n**API/Automation:** ✅ ID mapping only; enrichment via web UI")
    wg_df = run_webgestalt_idmapping(genes)
    if not wg_df.empty:
        st.dataframe(wg_df)
        st.download_button("⬇ Download WebGestalt Mappings", wg_df.to_csv(index=False), "webgestalt_mapped.csv")
    else:
        st.info("No successful mappings from WebGestalt.")
    st.link_button("🌐 Open WebGestalt", "https://www.webgestalt.org/")
    st.subheader("4️⃣ Metascape")
    st.markdown("**Summary:** Web-based network enrichment with integrated visualization.  \n**API/Automation:** ❌ Web-only")
    st.link_button("🌐 Open Metascape", "https://metascape.org/")

    st.subheader("5️⃣ DAVID")
    st.markdown("**Summary:** Classical GO/KEGG mapping with batch annotation.  \n**API/Automation:** ⚠ Currently not functioning")
    st.link_button("🌐 Open DAVID", "https://david.ncifcrf.gov/")

    st.subheader("6️⃣ ClusterProfiler")
    st.markdown("**Summary:** Programmatic enrichment in R for GO/KEGG with strong visualization.  \n**API/Automation:** ✅ via R package")
    st.link_button("📦 View on Bioconductor", "https://bioconductor.org/packages/clusterProfiler/")

# === Evaluation Matrix ===
st.markdown("---")
st.subheader("📊 Tool Performance Evaluation")

evaluation_criteria = {
    "🧬 Biological Context": "Relevance to FSH, folliculogenesis, endocrine system",
    "🔄 Network Connectivity": "Gene/protein interaction coverage",
    "💊 Clinical Utility": "Drug-related interpretability, PGx targets",
    "🤖 AI-readiness": "Structured SBML, scores, ML readiness",
    "🛠 Interoperability": "API, reproducibility, export support",
    "🧑‍⚕️ Clinical Explainability": "Ease of clinical use in medicine context",
    "🎯 Visual Insight": "Interactive / informative graphics"
}

default_scores = {
    "gProfiler": [5, 3, 2, 4, 5, 3, 3],
    "Enrichr": [4, 3, 3, 5, 5, 2, 3],
    "WebGestalt": [4, 3, 3, 3, 3, 2, 3],
    "Metascape": [4, 4, 3, 3, 2, 3, 5],
    "DAVID": [4, 2, 2, 3, 2, 2, 2],
    "ClusterProfiler": [5, 4, 3, 5, 4, 2, 4]
}

df_eval = pd.DataFrame(default_scores, index=evaluation_criteria).T

# Sliders for each tool's evaluation
for tool in df_eval.index:
    with st.expander(f"🔧 Adjust scores for {tool}"):
        for crit in evaluation_criteria:
            df_eval.loc[tool, crit] = st.slider(
                label=f"{crit}",
                min_value=1,
                max_value=5,
                value=int(df_eval.loc[tool, crit]),
                help=evaluation_criteria[crit],
                key=f"{tool}:{crit}"
            )
df_eval["Total Score"] = df_eval.sum(axis=1)
st.dataframe(df_eval.astype(int))
st.download_button("⬇ Download Evaluation Scores", df_eval.to_csv(), "tool_evaluation.csv")

