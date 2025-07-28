# 🧬 Bioinformatics Web Dashboard Suite
Welcome to your Bioinformatics Web Dashboard Suite! This suite contains three interactive, user-friendly Streamlit apps that allow researchers, clinicians, and students to analyze gene lists for biological insights—no coding or special software required.

## ⭐ How to Use These Apps
1. Get the app files (enrichment_tools_app.py, gene_network_tools_app.py, clinical_relevance_tools_app.py).

2. Install requirements by opening a terminal (command prompt) and running:

```
pip install streamlit pandas requests networkx matplotlib
```
3. Launch an app (for example, the enrichment app) with:
```
streamlit run enrichment_tools_app.py
```
The app will open in your web browser at http://localhost:8501.

4. Paste your gene symbols (comma-separated, e.g. FSHR, LHCGR, CYP19A1) in the sidebar.

5. Click "Run..." and the analysis results will appear.

6. Interact with the outputs, export tables as CSV, and click links for deeper exploration.

## 📊 App Overviews & Instructions
## 1️⃣ Enrichment Dashboard App
### Purpose:
Find out which pathways, biological processes, cellular locations, or disease terms are most relevant to your genes!

### What it does:

- Accepts any human gene list.

- Instantly queries multiple pathway and enrichment analysis tools (like gProfiler, Enrichr).

- Provides links for deep-dive analyses with Metascape, WebGestalt, DAVID, and ClusterProfiler.

- Lets you compare tools and rate them with a built-in evaluation matrix.

### How to use it:

- Paste your gene symbols in the sidebar.

- Click ‘Run Enrichment’.

- See interactive pathway enrichment results, download CSVs, and click "Open" to launch tools like Metascape or WebGestalt for further exploration.

## 2️⃣ Gene Network Dashboard App
### Purpose:
Explore and visualize how your genes or proteins interact in biological networks.

### What it does:

- Takes any list of gene/protein symbols.

- Directly interacts with the STRING-db API to create and visually display interaction networks.

- Provides one-click links to explore each gene individually on GeneMANIA.

- Prepares download-ready edge tables for use in Cytoscape (and ClueGO) for advanced desktop visualization.

- Includes a performance evaluation matrix you can adjust and export.

### How to use it:

- Paste gene symbols in the sidebar.

- Click ‘Run Network Analysis’.

- Browse automatic network visualizations and export tables for Cytoscape.

- For GeneMANIA, click on each gene’s link to view its network online.

## 3️⃣ Clinical Relevance Dashboard App
### Purpose:
Link your genes to real-world clinical data: drugs, diseases, known associations, and pharmacogenomic implications.

### What it does:

- Lets you search your gene list in curated clinical genomics knowledgebases.

- Offers instant web links to results for:

- DGIdb (drug–gene interactions)

- DisGeNET (gene–disease associations)

- Open Targets Platform (multi-omic target evidence)

- PharmGKB (pharmacogenomics and variant-drug links)

- Gives simple step-by-step instructions for using each clinical portal.

- Includes a customizable evaluation matrix for tool comparison.

### How to use it:

- Paste your gene symbols in the sidebar.

- Click 'Run Clinical Search'.

- Click web links for each database to explore your genes’ roles in therapies and diseases.

## 📝 General Tips
- All apps are copy-paste ready and require only free, widely available Python libraries.

- No programming experience required.

- Designed to run locally on your computer; you can share apps via Streamlit Cloud or by sending results (see previous suggestions).

- Interactive help, data export, and evaluation are built in.

- For best results, always use official HGNC gene symbols (case-sensitive, e.g., TP53 not tp53).

## 📦 File Summary
| App File	                          |  Purpose                                                                        |
|-------------------------------------|---------------------------------------------------------------------------------|
| `enrichment_tools_app.py`           | Multi-tool pathway and ontology enrichment dashboard.                           |
| `gene_network_tools_app.py` 	      | Interactive gene/protein network visualization and export, with GeneMANIA links.|
| `clinical_relevance_tools_app.py` 	| Direct links to clinical/therapeutic databases for each gene.                   |

## 🚀 Ready to Discover!
Just install, run, and open the dashboard in your browser.
Paste your list, press a button, and reveal the biological story behind your genes—fast.

### Questions or issues?
Check each app's info boxes, or ask the app author for help.

Happy discovery!
