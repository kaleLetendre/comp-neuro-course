#!/usr/bin/env python3
"""Try hard to find free copies of the eighteen papers that publisher routes
refuse. Queries OpenAlex (which indexes repository and author-hosted copies,
not just publisher open access), then Semantic Scholar, then any known
author-hosted URL. Downloads into papers/ (gitignored) and reports honestly
per paper. Defensive try/except throughout: this runs unattended against
several third-party APIs and one being down should not stop the rest."""
import json, os, ssl, sys, time, urllib.parse, urllib.request

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "papers")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}

# name, doi, known author-hosted candidates
CLOSED = [
 ("A2_hopfield_1982_neural_networks", "10.1073/pnas.79.8.2554", []),
 ("A3_fries_2005_coherence", "10.1016/j.tics.2005.08.011", []),
 ("A3_wang_2010_cortical_rhythms", "10.1152/physrev.00035.2008", []),
 ("A4_tsodyks_markram_1997_release_probability", "10.1073/pnas.94.2.719", []),
 ("A5_attwell_laughlin_2001_energy_budget", "10.1097/00004647-200110000-00001", []),
 ("A5_roy_2019_spike_based_machine_intelligence", "10.1038/s41586-019-1677-2", []),
 ("B1_schultz_1997_prediction_and_reward", "10.1126/science.275.5306.1593", []),
 ("B1_yu_dayan_2005_uncertainty_neuromodulation", "10.1016/j.neuron.2005.04.026",
   ["https://www.gatsby.ucl.ac.uk/~dayan/papers/yu-dayan-05.pdf",
    "https://www.gatsby.ucl.ac.uk/~dayan/papers/YuDayan2005.pdf"]),
 ("B2_bastos_2012_canonical_microcircuits", "10.1016/j.neuron.2012.10.038", []),
 ("B3_poirazi_2003_two_layer_neuron", "10.1016/S0896-6273(03)00149-1", []),
 ("B3_larkum_2013_cellular_mechanism", "10.1016/j.tins.2012.11.006", []),
 ("B3_london_hausser_2005_dendritic_computation", "10.1146/annurev.neuro.28.061604.135703", []),
 ("B4_schafer_2012_microglia_sculpt", "10.1016/j.neuron.2012.03.026", []),
 ("B4_hensch_2005_critical_period", "10.1038/nrn1787", []),
 ("B4_huttenlocher_1997_synaptogenesis",
   "10.1002/(SICI)1096-9861(19971020)387:2<167::AID-CNE1>3.0.CO;2-Z", []),
 ("B5_mcclelland_1995_complementary_learning_systems", "10.1037/0033-295X.102.3.419",
   ["https://www.cs.toronto.edu/~hinton/absps/mcclelland95.pdf",
    "https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf"]),
 ("B5_foster_wilson_2006_reverse_replay", "10.1038/nature04587", []),
 ("C1_rao_ballard_1999_predictive_coding", "10.1038/4580",
   ["https://www.cs.utexas.edu/~dana/nn.pdf"]),
]

def open_url(url, timeout=45):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                  timeout=timeout, context=ssl.create_default_context())

def grab(url, path):
    with open_url(url) as r:
        head = r.read(5)
        if not head.startswith(b"%PDF"):
            return False
        with open(path, "wb") as f:
            f.write(head)
            while True:
                chunk = r.read(1 << 16)
                if not chunk:
                    break
                f.write(chunk)
    if os.path.getsize(path) > 20000:
        return True
    os.remove(path)
    return False

def openalex_pdfs(doi):
    """Every open location OpenAlex knows, best first."""
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi, safe="")
    try:
        with open_url(url, 30) as r:
            d = json.load(r)
    except Exception:
        return []
    urls = []
    best = d.get("best_oa_location") or {}
    for loc in [best] + (d.get("locations") or []):
        u = loc.get("pdf_url")
        if u and u not in urls:
            urls.append(u)
        landing = loc.get("landing_page_url") or ""
        if landing.endswith(".pdf") and landing not in urls:
            urls.append(landing)
    return urls

def s2_pdf(doi):
    url = ("https://api.semanticscholar.org/graph/v1/paper/DOI:"
           + urllib.parse.quote(doi, safe="") + "?fields=openAccessPdf")
    try:
        with open_url(url, 30) as r:
            return [(json.load(r).get("openAccessPdf") or {}).get("url")]
    except Exception:
        return []

rows = []
for name, doi, known in CLOSED:
    path = os.path.join(OUT, name + ".pdf")
    if os.path.exists(path) and os.path.getsize(path) > 20000:
        rows.append((name, "already-have", "")); continue
    got = None
    candidates = list(known) + [u for u in openalex_pdfs(doi) if u]
    time.sleep(0.4)
    for u in candidates:
        try:
            if grab(u, path):
                got = u; break
        except Exception:
            continue
    if not got:
        for u in [u for u in s2_pdf(doi) if u]:
            try:
                if grab(u, path):
                    got = u; break
            except Exception:
                continue
        time.sleep(1.0)
    rows.append((name, "FOUND" if got else "no free copy found",
                 (got or f"doi:{doi}")[:70]))

for n, s, d in rows:
    print(f"{s:<22} {n}\n{'':<22} {d}")
found = sum(1 for r in rows if r[1] in ("FOUND", "already-have"))
print(f"\n{found}/{len(rows)} of the previously-paywalled papers now have a local copy")
