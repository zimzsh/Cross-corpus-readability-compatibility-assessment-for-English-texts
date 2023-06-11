# Cross-corpus-readability-compatibility-assessment-for-English-texts

## Background
Text readability assessment has attracted the attention of international researchers and has been widely applied in various fields. However, different research groups often use the different corpus, and existing research lacks exploration of corpus compatibility. We propose a new evaluation framework for the task of cross-corpus text readability compatibility assessment(**CRCA**). The specific approach includes (1) Corpus: CEFR, CLEC, CLOTH, NES, OSP, and RACE. The linguistic features, GloVe word vector representation, and the fusion features of the two were extracted. (2) Classification model: Machine learning methods (XGBoost, SVM) and deep learning methods (BiLSTM, Attention-BiLSTM) were used; (3) Compatibility metrics: RJSD, RRNSS, and NDCG metrics. We mainly found that: (1) The compatibility of the corpora was validated, with OSP being significantly different from other commonly used datasets. (2) There is an adaptation effect between corpus, feature representation, and classification method. (3) The three metrics get similar results, which verifies the robustness of the compatibility assessment method. The results of this study provide valuable references for corpus selection, feature expression, and classification methods, and benefit research on cross-corpus transfer learning.
  

## PATH

```
PATH
│  
├─data process
│      data_clean.ipynb         :Used to process the source files of the corpus.
│      readability.ipynb        :Evaluate the corpus using traditional readability formulas.
│      corpus_analysis.ipynb    :Analyze the distribution of readability formulas and corpus levels.
│      feature_extract.ipynb    :Extract the linguistic features of six corpora.
│      
├─model
|       ML.ipynb      :Machine learning algorithms: XGBoost, SVM.
|       DL.ipynb      :Deep learning algorithms: Bi-LSTM, ATT-BI-LSTM.
│       Demo_XGBoost.ipynb :XGBoost-based demo for cross-corpus assessment.
│      
└─evaluate
       evaluate.ipynb :Evaluate the compatibility of the model's predicted results using the RJSD, RRNSS, and NDCG metrics.
       heatmap.ipynb  :Visualize the results of compatibility evaluation.
```
   



 ## Content
- [Data](#Data)
- [Frame Work](#FrameWork)
- [Results](#Results)
 
  

## Data
### Corpus
We used six datasets for readability research. The source files can be obtained from Baidu Cloud.


| Dataset | Description                                                                                                                                                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CEFR    | The Common European Framework of Reference for Languages (CEFR) is an internationally recognized standard for describing language proficiency and levels. The standard divides six levels based on language texts of different difficulty levels, from beginner to professional level. |
| CLEC    | Chinese Learner English Corpus (CLEC) is a corpus based on learners' English writing. There are five levels of corpus, including middle school students, college English level 4 and 6, junior and senior professional English.                                                        |
| CLOTH   | CLOTH is a large-scale English cloze test set, which is divided into two grades: junior high school and senior high school.                                                                                                                                                            |
| NES     | Newsela (NES) corpus consists of news articles. It covers articles from grade 2 to grade 12 at different levels, allowing students to practice reading on texts appropriate to their ability level.                                                                                    |
| OSP     | The OneStopEnglish (OSP) corpus contains three levels of reading difficulty (primary, intermediate, and advanced), with 189 texts at each level.                                                                                                                                       |
| RACE    | The Reading Comprehension Dataset From Examination (RACE) is a collection of reading comprehension materials from English exams for middle and high school students in China, divided into two levels based on grades: junior high and senior high.                                    |

### Feature

The features used for readability assessment in our study are divided into three categories: lexical features, syntactic features, and semantic features. These features were extracted from six datasets and used as inputs for training machine learning and deep learning models.

| Code                 | Description                                          |
|----------------------|------------------------------------------------------|
|   Lexical Features                                                          |
| ASPW                 | average syllables per word                           |
| ALPW                 | average letters per word                             |
| DWP                  | percentage of difficult words                        |
| CWP                  | percentage of complex words                          |
| LWP                  | percentage of long words                             |
|  Syntactic Features                                                         |
| LSP                  | percentage of long sentences                         |
| AWPS                 | average number of words per sentence                 |
| NPS                  | average number of noun phrases per sentence          |
| VPS                  | average number of verb phrases per sentence          |
| PPS                  | average number of prepositional phrases per sentence |
| SPS                  | average number of subordinate clauses per sentence   |
| SQS                  | average number of special subordinate clauses average per sentence|
| ANPS                 | average length of noun phrases                       |
| AVPS                 | average length of verb phrases                       |
| APPS                 | average length of prepositional phrases              |
| APT                  | average length of parse tree                         |
| Grammatical Features                                                        |
| NP                   | percentage of nouns                                  |
| PNP                  | percentage of proper nouns                           |
| PP                   | percentage of pronouns                               |
| CoP                  | percentage of conjunctions                           |
| CP                   | percentage of commas                                 |


## Framework
We proposed a method for cross-corpus evaluation that aims to predict the readability of text from different corpora and assess the compatibility of readability systems. The project framework contains six steps: **Feature Extraction**, **Word Vector Representation**, **Feature Fusion**, **Training Model**, **Readability Prediction** and **Readability System Compatibility Assessment**.

<img src=https://github.com/LZZ1212/Cross-corpus-readability-compatibility-assessment-for-English-texts/blob/main/readme_figure/Frame_work.png/>

## Model
We employed both machine learning and deep learning approaches with different feature combinations for experimentation. In the model file, we have written a demo for cross-corpus readability assessment using the XGBoost method.
|    | model                |
|----|----------------------|
| ML | XGBoost, SVM         |
| DL | BI-LSTM, ATT-BI-LSTM |


## Results
We conducted readability assessments on six corpora using three experimental combinations, including machine learning+features, machine learning+GloVe word vectors, deep learning+GloVe word vectors, machine learning+fusion features, and deep learning+fusion features. We used three evaluation metrics to assess the compatibility of the predicted results, and here we show the results of the RJSD evaluation, while the evaluation results of RRNSS and NDCG are detailed in the paper.
  
### Compatibility Assessment Results of RJSD (ML+Feature)
<img src=https://github.com/LZZ1212/Cross-corpus-readability-assessment-compatibility-for-English-texts/blob/main/readme_figure/RJSD_feature.png width=70% />

### Compatibility Assessment Results of RJSD (ML/DL+GloVe)
<img src=https://github.com/LZZ1212/Cross-corpus-readability-assessment-compatibility-for-English-texts/blob/main/readme_figure/RJSD_Glove.png width=70% />

### Compatibility Assessment Results of RJSD (ML/DL+fusion feature)
<img src=https://github.com/LZZ1212/Cross-corpus-readability-assessment-compatibility-for-English-texts/blob/main/readme_figure/RJSD_fusion.png width=70% />



## Contributing
@han @zhen











































