<img width="4032" height="1482" alt="image" src="https://github.com/user-attachments/assets/6996577b-10ca-476d-bf01-9e65d24ebf6a" /># Can Contract Lifecycle Data Support the Monitoring Objectives of the Proposed EU Public Procurement Act? Evidence from Greece

## Abstract
This repository contains the replication code for the empirical findings presented in the paper. The associated anonymized replication dataset is archived separately on Zenodo. Together, the dataset and scripts allow reproduction of the published tables and summary statistics.

## Repository Contents
- `reproduce_results.py`: Script to generate Tables 1-4.
- `dataset_dictionary.md`: Definitions of dataset variables.
- `requirements.txt`: Python package requirements.
- `LICENSE`: Repository license.

## Data Availability

The anonymized replication dataset is archived on Zenodo:

https://doi.org/10.5281/zenodo.23880521

The dataset contains 206,143 direct-award contract lifecycles issued by 123 contracting authorities in the Greek healthcare sector during 2019–2024.

The public dataset supports reproduction of the published empirical findings rather than reconstruction of the original production pipeline.

## Data
The anonymized replication dataset is distributed separately through Zenodo.

The dataset contains anonymized contract-level observations derived from the final production pipeline used in the paper. Direct identifiers, contract references, supplier names, contracting authority names and free-text descriptions have been removed or irreversibly transformed.

The Zenodo record contains:

- `contracts_metadata_anonymized.parquet`
- `dataset_dictionary.md`
- `anonymization_report.md`

## Reproducibility
1. Download the anonymized replication dataset from the associated Zenodo record.
2. Place contracts_metadata_anonymized.parquet in the repository root directory.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python reproduce_results.py`
The script `reproduce_results.py` generates the paper tables (Table 1–Table 4) from the Zenodo replication dataset.

## Scope of Replication

This repository reproduces the published empirical results from the anonymized replication dataset.

The anonymized dataset already contains the final lifecycle monitoring indicators (L1–L5) derived from the production pipeline. Consequently, the replication scripts reproduce the published tables and summary statistics rather than recalculating the indicators from raw procurement records. The public replication package therefore supports results reproducibility rather than full reconstruction of the original production pipeline. The objective of the repository is to reproduce the published statistical findings rather than reconstruct the original administrative data processing workflow.

The full lifecycle reconstruction and indicator-generation pipeline relies on administrative procurement records that are not distributed as part of the public replication package.

## Ethical and Legal Note
- **Contract identifiers removed.**
- **Supplier identifiers removed.**
- **Contracting authority names removed.**
- Original procurement records remain publicly available through the Central Electronic Registry for Public Procurement (KIMDIS).
- **Indicators represent lifecycle monitoring signals.**
- **Indicators are designed for research and monitoring purposes only.**
- **Indicators do not constitute evidence of irregularity, misconduct, corruption, fraud, inefficiency, or legal violations.**

## Citation
If you use the code or dataset, please cite the associated manuscript:

Fountoukidis, I., Antoniou, I., Varsakelis N., Can Contract Lifecycle Data Support the Monitoring Objectives of the Proposed EU Public Procurement Act? Evidence from Greece. Working paper.

Dataset DOI: 10.5281/zenodo.23880521
