# LP-3

Laboratory Practice III assignments (SPPU, Fourth Year Computer Engineering).

## Design and Analysis of Algorithms: `daa_programs/`

| # | Program | File |
|---|---------|------|
| 1 | Fibonacci, recursive and non-recursive, with complexity analysis | `1_fibonacci.py` |
| 2 | Huffman encoding (greedy) | `2_huffman_encoding.py` |
| 3 | Fractional knapsack (greedy) | `3_fractional_knapsack.py` |
| 4 | 0-1 knapsack (dynamic programming) | `4_knapsack_01_dp.py` |
| 5 | n-Queens with the first queen placed (backtracking) | `5_n_queens.py` |
| 6 | Quick sort analysis, deterministic and randomized | `6_quick_sort_analysis.py` |

Needs only Python 3. Run with `python <file>`.

## Machine Learning: `ml_programs/`

| # | Program | File | Dataset |
|---|---------|------|---------|
| 1 | Uber fare prediction (linear regression, random forest) | `1_uber_fare_prediction.py` | `uber.csv` |
| 2 | Email spam detection (KNN, SVM) | `2_email_spam_knn_svm.py` | `emails.csv` |
| 3 | Bank customer churn (neural network) | `3_bank_churn_neural_network.py` | `Churn_Modelling.csv` |
| 4 | Gradient descent on y = (x + 3)^2 | `4_gradient_descent.py` | none |
| 5 | KNN on the diabetes dataset | `5_knn_diabetes.py` | `diabetes.csv` |
| 6 | K-Means with the elbow method | `6_kmeans_sales.py` | `sales_data_sample.csv` |

```bash
pip install numpy pandas scikit-learn matplotlib
```

Download each dataset from Kaggle (links are in the file headers), place the CSV
next to the program, then run `python <file>` or `python <file> path/to/data.csv`.
The datasets are not stored in this repository.

## Blockchain Technology: `blockchain_programs/`

| # | Assignment | File |
|---|------------|------|
| 1, 2 | MetaMask installation, wallet creation, Ether spent per transaction | `1_2_metamask_wallet_guide.md` |
| 3 | Bank account smart contract (deposit, withdraw, show balance) | `3_Bank.sol` |
| 4 | Student data with structures, arrays and fallback | `4_StudentData.sol` |
| 5 | Survey report on types of blockchains and use cases | `5_blockchain_types_survey_report.md` |
| 6 | Business network using Hyperledger Composer | `6_hyperledger_business_network/` |

The Solidity contracts can be compiled and deployed from <https://remix.ethereum.org>.
