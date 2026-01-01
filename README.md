# Exploratory Data Analysis & Benchmarking of Anti-phishing Datasets

## Overview
This repository serves as a **Benchmark Assessment Tool** for researchers in the anti-phishing domain. It provides comprehensive Exploratory Data Analysis (EDA) on five major multimodal datasets: **Phish360**, **PWD2016**, **PhishIntention**, **PILWD-134K**, and **VanNL126k**.

The primary goal is to enable researchers to quantitatively assess the **quality**, **integrity**, and **diversity** of these datasets before selecting them for training or benchmarking their models.

## Key Features

- **Quality vs. Quantity Assessment:** We move beyond simple "sample counts" to analyze the *true* uniqueness of content (HTML, Text, Images) versus URLs.
- **Multimodal Integrity:** Verification of valid data across all modalities (URL validity, HTML parsing success, Screenshot resolution consistency).
- **Comparative Benchmarking:** A dedicated [Comparative Analysis Notebook](Comparative_Analysis.ipynb) aggregates metrics across all datasets to visualize the trade-offs between dataset size and content repetition.
- **Granular Insights:** Detailed breakdown of Language distribution, TLD/Domain diversity, and Text Extraction quality for each dataset.

## Key Findings Summary
Our analysis reveals critical distinctions between datasets:
- **Phish360:** Maintains high content uniqueness (~92%) and linguistic diversity, making it a robust choice for generalization.
- **Benchmarks (e.g., PWD2016):** While containing unique URLs, they often suffer from massive content duplication (low content uniqueness <15%), potentially inflating performance metrics if not accounted for.

## Data Files

Below are links to download Parquet files for the datasets analyzed.

| Dataset Name | Dataset Size |  File Type              | Size in GB   |  Download Link   |
|--------------|---------------|---------|-------------------------------------------|--------------|
| **Phish360 (ours)** | ~11k | Parquet Files    | 0.6 GB | [Download](https://drive.google.com/drive/u/1/folders/1ulQYtb63pZlhgcKMuTeiDze1onsY1yKT)  |
| PWD2016       | 30k | Parquet Files    |  1.1 GB | [Download](https://drive.google.com/drive/folders/1IWip7RW_p8iISYMAT-Db_pFIp4BWb_sn?usp=drive_link)  |
| PhishIntention | ~58k | Parquet Files    | 2.5 GB | [Download](https://drive.google.com/drive/folders/1VsApDC3kYFu7HJ2joYN-klG4jIvOQLkQ?usp=drive_link) | 
| VanNL126k | ~126k| Parquet Files    |  5.12 GB | [Download](https://drive.google.com/drive/folders/1JzcYGREyEewglE-uWWZqdQA8Sz0iBiWh?usp=drive_link) |
| PILWD-134K | ~134k | Parquet Files    |  8.36 GB | [Download](https://drive.google.com/drive/u/2/folders/1TYwUehoq4pFGYnvn8iXQqtSbS788mgLi)  |

## Notebooks
1. **[Phish360 EDA](Phish360%20EDA%20PQ.ipynb)**
2. **[PWD2016 EDA](PWD2016%20EDA%20PQ.ipynb)**
3. **[PhishIntention EDA](PhishIntention%20EDA%20PQ.ipynb)**
4. **[VanNL126k EDA](VanNL126k%20EDA%20PQ.ipynb)**
5. **[PILWD-134K EDA](PILWD-134K%20EDA%20PQ.ipynb)**
6. **[Comparative Analysis](Comparative_Analysis.ipynb)** *(New! Cross-dataset benchmarking)*

## Contact Information

- **Email:** almakhamrehahmad@gmail.com
- **LinkedIn:** [https://www.linkedin.com/in/ahmadalmakhamreh/](https://www.linkedin.com/in/ahmadalmakhamreh/)
- **GitHub:** [https://github.com/almakhamreh](https://github.com/almakhamreh)

## References

Here are some useful resources for further reading:

- [PWD2016](https://www.researchgate.net/profile/Colin-Choon-Lin-Tan/publication/329554848_Building_Standard_Offline_Anti-phishing_Dataset_for_Benchmarking/links/5c0f24374585157ac1b9194e/Building-Standard-Offline-Anti-phishing-Dataset-for-Benchmarking.pdf): In depth description about the PWD2016 dataset by the authors.
  - Chiew, K. L., Chang, E. H., Tan, C. L., Abdullah, J., & Yong, K. S. C. (2018). Building standard offline anti-phishing dataset for benchmarking. International Journal of Engineering & Technology, 7(4.31), 7-14.
- [PhishIntention](https://www.usenix.org/system/files/sec22-liu-ruofan.pdf): The paper that introduced the PhishIntention dataset.
    - Liu, R., Lin, Y., Yang, X., Ng, S. H., Divakaran, D. M., & Dong, J. S. (2022). Inferring phishing intention via webpage appearance and dynamics: A deep vision based approach. In 31st USENIX Security Symposium (USENIX Security 22) (pp. 1633-1650).
- [VanNL126k](https://dl.acm.org/doi/abs/10.1145/3465481.3470112): The paper that introduced the VanNL126k dataset.
  - Van Dooremaal, B., Burda, P., Allodi, L., & Zannone, N. (2021, August). Combining text and visual features to improve the identification of cloned webpages for early phishing detection. In Proceedings of the 16th International Conference on Availability, Reliability and Security (pp. 1-10).
- [PILWD-134K](https://www.sciencedirect.com/science/article/pii/S0957417422012301): The paper that introduced the PILWD-134k dataset.
  - Sánchez-Paniagua, M., Fidalgo, E., Alegre, E., & Alaiz-Rodríguez, R. (2022). Phishing websites detection using a novel multipurpose dataset and web technologies features. Expert Systems with Applications, 207, 118010.

Feel free to explore these references for additional insights and information!
