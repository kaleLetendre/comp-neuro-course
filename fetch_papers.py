#!/usr/bin/env python3
"""Fetch the lesson-plan reading list into papers/ (which is gitignored).

This file doubles as the bibliography: every entry below was resolved against
Europe PMC, so the DOIs and PMIDs are verified even for papers we cannot
download. Re-run any time; it skips what is already on disk.

    python3 fetch_papers.py

Resolution order per entry: a known open-access publisher URL, then Semantic
Scholar's open-access index by DOI, then Europe PMC full text (saved as .xml
plus a tags-stripped .txt). Anything left needs institutional access — the
script says so rather than failing quietly. Defensive try/except throughout is
deliberate: this runs unattended against a dozen third-party endpoints, and one
publisher being down should not stop the rest.
"""
import json, os, re, ssl, sys, time, urllib.parse, urllib.request

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "papers")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
REST = "https://www.ebi.ac.uk/europepmc/webservices/rest"

# name, lesson, citation, doi, pmcid (or None), open-access URL candidates
PAPERS = [
 ("izhikevich_2006_polychronization","A1","Izhikevich 2006, Polychronization: Computation with Spikes, Neural Computation",
  "10.1162/089976606775093882",None,["https://www.izhikevich.org/publications/spnet.pdf"]),
 ("hopfield_1982_neural_networks","A2","Hopfield 1982, Neural networks and physical systems with emergent collective computational abilities, PNAS",
  "10.1073/pnas.79.8.2554","PMC346238",[]),
 ("fries_2005_coherence","A3","Fries 2005, A mechanism for cognitive dynamics: neuronal communication through neuronal coherence, TICS",
  "10.1016/j.tics.2005.08.011",None,[]),
 ("wang_2010_cortical_rhythms","A3","Wang 2010, Neurophysiological and computational principles of cortical rhythms in cognition, Physiol Rev",
  "10.1152/physrev.00035.2008","PMC2923921",[]),
 ("tsodyks_markram_1997_release_probability","A4","Tsodyks & Markram 1997, The neural code between neocortical pyramidal neurons depends on neurotransmitter release probability, PNAS",
  "10.1073/pnas.94.2.719","PMC19580",[]),
 ("attwell_laughlin_2001_energy_budget","A5","Attwell & Laughlin 2001, An energy budget for signaling in the grey matter of the brain, JCBFM",
  "10.1097/00004647-200110000-00001",None,[]),
 ("roy_2019_spike_based_machine_intelligence","A5","Roy, Jaiswal & Panda 2019, Towards spike-based machine intelligence with neuromorphic computing, Nature",
  "10.1038/s41586-019-1677-2",None,[]),
 ("schultz_1997_prediction_and_reward","B1","Schultz, Dayan & Montague 1997, A neural substrate of prediction and reward, Science",
  "10.1126/science.275.5306.1593",None,[]),
 ("yu_dayan_2005_uncertainty_neuromodulation","B1","Yu & Dayan 2005, Uncertainty, neuromodulation, and attention, Neuron",
  "10.1016/j.neuron.2005.04.026",None,[]),
 ("bastos_2012_canonical_microcircuits","B2","Bastos et al. 2012, Canonical microcircuits for predictive coding, Neuron",
  "10.1016/j.neuron.2012.10.038","PMC3777738",[]),
 ("hertag_sprekeler_2020_prediction_error_neurons","B2","Hertag & Sprekeler 2020, Learning prediction error neurons in a canonical interneuron circuit, eLife",
  "10.7554/eLife.57541","PMC7442488",["https://cdn.elifesciences.org/articles/57541/elife-57541-v2.pdf"]),
 ("poirazi_2003_two_layer_neuron","B3","Poirazi, Brannon & Mel 2003, Pyramidal neuron as two-layer neural network, Neuron",
  "10.1016/S0896-6273(03)00149-1",None,[]),
 ("larkum_2013_cellular_mechanism","B3","Larkum 2013, A cellular mechanism for cortical associations, TINS",
  "10.1016/j.tins.2012.11.006",None,[]),
 ("london_hausser_2005_dendritic_computation","B3","London & Hausser 2005, Dendritic computation, Annu Rev Neurosci",
  "10.1146/annurev.neuro.28.061604.135703",None,[]),
 ("schafer_2012_microglia_sculpt","B4","Schafer et al. 2012, Microglia sculpt postnatal neural circuits in an activity and complement-dependent manner, Neuron",
  "10.1016/j.neuron.2012.03.026","PMC3528177",[]),
 ("hensch_2005_critical_period","B4","Hensch 2005, Critical period plasticity in local cortical circuits, Nat Rev Neurosci",
  "10.1038/nrn1787",None,[]),
 ("huttenlocher_1997_synaptogenesis","B4","Huttenlocher & Dabholkar 1997, Regional differences in synaptogenesis in human cerebral cortex, J Comp Neurol",
  "10.1002/(SICI)1096-9861(19971020)387:2<167::AID-CNE1>3.0.CO;2-Z",None,[]),
 ("mcclelland_1995_complementary_learning_systems","B5","McClelland, McNaughton & O'Reilly 1995, Why there are complementary learning systems in the hippocampus and neocortex, Psych Review",
  "10.1037/0033-295X.102.3.419",None,[]),
 ("foster_wilson_2006_reverse_replay","B5","Foster & Wilson 2006, Reverse replay of behavioural sequences in hippocampal place cells during the awake state, Nature",
  "10.1038/nature04587",None,[]),
 ("olafsdottir_2018_replay_memory_planning","B5","Olafsdottir, Bush & Barry 2018, The role of hippocampal replay in memory and planning, Current Biology",
  "10.1016/j.cub.2017.10.073","PMC5847173",[]),
 ("bogacz_2017_free_energy_tutorial","C1","Bogacz 2017, A tutorial on the free-energy framework for modelling perception and learning, J Math Psychol",
  "10.1016/j.jmp.2015.11.003","PMC5341759",[]),
 ("rao_ballard_1999_predictive_coding","C1","Rao & Ballard 1999, Predictive coding in the visual cortex, Nat Neurosci",
  "10.1038/4580",None,[]),
 ("millidge_2021_predictive_coding_review","C2","Millidge, Seth & Buckley 2021, Predictive Coding: a Theoretical and Experimental Review, arXiv",
  "10.48550/arXiv.2107.12979",None,["https://arxiv.org/pdf/2107.12979"]),
 ("feldman_friston_2010_attention_uncertainty","C3","Feldman & Friston 2010, Attention, uncertainty, and free-energy, Front Hum Neurosci",
  "10.3389/fnhum.2010.00215","PMC3001758",["https://www.frontiersin.org/articles/10.3389/fnhum.2010.00215/pdf"]),
 ("salvatori_2022_arbitrary_graph_topologies","C4","Salvatori et al. 2022, Learning on Arbitrary Graph Topologies via Predictive Coding, arXiv",
  "10.48550/arXiv.2201.13180",None,["https://arxiv.org/pdf/2201.13180"]),
 ("friston_2009_active_inference","C5","Friston, Daunizeau & Kiebel 2009, Reinforcement Learning or Active Inference?, PLoS ONE",
  "10.1371/journal.pone.0006421","PMC2713351",
  ["https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0006421&type=printable"]),
 ("whittington_bogacz_2017_backprop_approximation","C6","Whittington & Bogacz 2017, An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity, Neural Computation",
  "10.1162/NECO_a_00949","PMC5467749",[]),
 ("song_2020_exact_backprop_in_pc","C6","Song, Lukasiewicz, Xu & Bogacz 2020, Can the Brain Do Backpropagation?, NeurIPS 33",
  "10.5555/3495724.3497617",None,
  ["https://proceedings.neurips.cc/paper/2020/file/fec87a37cdeec1c6ecf8181c0aa2d3bf-Paper.pdf"]),
]

def open_url(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                  timeout=timeout, context=ssl.create_default_context())

def grab_pdf(url, path):
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

def semantic_scholar_pdf(doi):
    url = ("https://api.semanticscholar.org/graph/v1/paper/DOI:"
           + urllib.parse.quote(doi, safe="") + "?fields=openAccessPdf")
    try:
        with open_url(url, 30) as r:
            return (json.load(r).get("openAccessPdf") or {}).get("url")
    except Exception:
        return None

def grab_fulltext(pmcid, base):
    try:
        with open_url(f"{REST}/{pmcid}/fullTextXML") as r:
            xml = r.read().decode("utf-8", "replace")
    except Exception:
        return False
    if len(xml) < 5000:
        return False
    open(base + ".xml", "w").write(xml)
    text = re.sub(r"<[^>]+>", " ", xml)
    text = re.sub(r"\s+\n", "\n", re.sub(r"[ \t]{2,}", " ", text))
    open(base + ".txt", "w").write(text)
    return True

def main():
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for name, lesson, citation, doi, pmcid, urls in PAPERS:
        base = os.path.join(OUT, f"{lesson}_{name}")
        if os.path.exists(base + ".pdf") or os.path.exists(base + ".txt"):
            rows.append((lesson, name, "have", "")); continue
        status, detail = "needs-institutional-access", f"doi:{doi}"
        for url in urls:
            try:
                if grab_pdf(url, base + ".pdf"):
                    status, detail = "pdf", url; break
            except Exception:
                continue
        if status != "pdf":
            link = semantic_scholar_pdf(doi)
            time.sleep(1.5)          # be polite; the API rate-limits anonymous callers
            if link:
                try:
                    if grab_pdf(link, base + ".pdf"):
                        status, detail = "pdf", link
                except Exception:
                    pass
        if status != "pdf" and pmcid and grab_fulltext(pmcid, base):
            status, detail = "fulltext-txt", pmcid
        rows.append((lesson, name, status, detail))

    with open(os.path.join(OUT, "_index.tsv"), "w") as f:
        f.write("lesson\tname\tstatus\tdetail\tcitation\n")
        for (lesson, name, status, detail), entry in zip(rows, PAPERS):
            f.write(f"{lesson}\t{name}\t{status}\t{detail}\t{entry[2]}\n")

    for lesson, name, status, detail in rows:
        print(f"{lesson}  {status:<28} {name}")
    got = sum(1 for r in rows if r[2] in ("pdf", "fulltext-txt", "have"))
    print(f"\n{got}/{len(rows)} available locally; the rest need institutional access (see papers/_index.tsv)")

if __name__ == "__main__":
    main()
