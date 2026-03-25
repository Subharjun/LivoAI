# Golden Dataset Methodology

This document outlines the design and methodology behind the 5 Question-Answer pairs forming the RAG Golden Dataset.

## How did you decide which questions made the cut?
I chose questions that proactively test the known limitations and edge cases of Retrieval-Augmented Generation (RAG) systems across all four assigned videos. Instead of simple factual lookups (which any basic vector database can solve), the questions were selected to evaluate:
- **Exact Numeric Extraction:** Forcing the system to retrieve specific, rare numbers accurately without confusing them with other highly prevalent statistics.
- **Scale Contrast:** Testing if the system can accurately pull contrasting statistics located in the same chunk (e.g., 2 vs 175 Billion parameters).
- **Example Extraction:** Verifying if the RAG can link a high-level theoretical concept (Unsupervised Learning) to the exact real-world analog utilized by the speaker.

## How did you actually pull them from the material?
The dataset was constructed exclusively using the raw textual transcripts extracted from the provided YouTube videos. Transcripts were fetched locally and manually reviewed to locate precise, authentic quotes and minute-level timestamps (e.g., 00:09:52, 00:08:31). I ensured that no external knowledge or pre-existing LLM understanding was required; the answers are explicitly grounded in the spoken words of the videos and tagged with their exact timestamps to verify authenticity.

## What are these questions testing — what would a wrong retrieval look like?

Here is a breakdown of what each specific question tests:

- **QA_001 (Reasoning Extraction):** 
  - **Testing:** Strict extraction of explicit numbered reasons directly out of the provided conversational transcript.
  - **Wrong Retrieval:** Since LLMs have strong priors about why Deep Learning is popular, a poor RAG system would fall back to its internal parametric memory and generate a general list (like "GPUs and Big Data") instead of retrieving the exact 2 specific factors mentioned by CampusX.

- **QA_002 (Definitional Precision):** 
  - **Testing:** Direct definition extraction from a designated timestamp.
  - **Wrong Retrieval:** A failure would occur if the model ignores the specific early "simplest terms" definition given by 3Blue1Brown in favor of a complex biological mapping or a mathematical definition from later in the video or an external source.

- **QA_003 (Numeric Scale Contrast):** 
  - **Testing:** Contrastive extraction of model sizes.
  - **Wrong Retrieval:** An aggressive chunking strategy may miss the "two parameters" part of linear regression because "175 billion" dominates semantic searches regarding parameters. A bad response would fail to mention the slope and y-intercept entirely.

- **QA_004 (Explicit Example Mapping):** 
  - **Testing:** Tying a machine learning sub-field to a specific localized example.
  - **Wrong Retrieval:** Since unsupervised learning has hundreds of famous examples (e.g., customer segmentation), a weak RAG might hallucinate a generic example instead of correctly finding CodeWithHarry's specific usage of "Credit Card Fraud Detection" based on IP addresses.

- **QA_005 (Multi-Document Numeric Specificity):** 
  - **Testing:** "Needle in a Haystack" numeric precision, extracting exact spatial and neuron counts for a specific layer.
  - **Wrong Retrieval:** A wrong retrieval would fail to locate the "28x28" and "784" integers, potentially confusing them with other integers like "13,000" stated later in the same video.
