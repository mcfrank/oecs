---
title: Large Language Models
slug: zp5n8ivs
date: '2024-07-24'
doi: 10.21428/e2759450.2bb20e3c
authors:
- Melanie Mitchell
section_editors:
- Thomas L. Griffiths
---

A *large language model* (LLM) is a computational system, typically a deep neural network with a large number of tunable parameters (i.e., weights), that implements a mathematical function called a *language model*. A *language model* (LM), in its most general form, is a probability distribution over possible sequences of words and other elements in a language. For example, given a sequence *w**1**, w**2**, ..., w**m*, an LM gives the probability *P* of that sequence: *P*(*w**1**, w**2**, ..., w**m*). In a natural language context, sequence elements—referred to as *tokens*—can be words, word parts, punctuation, or other symbols. In practice, LMs can be used to predict unseen tokens in a sequence. For example, given sequence *w**1**, w**2**, ... w**m–1*, the probability that *w* is the *m*th token in this sequence can be computed as the conditional probability *P*(*w *|* w**1**, w**2**, ..., w**m–1*). LMs have been used extensively in many areas of natural language processing, ranging from speech recognition and translation to text generation and chatbots. The neural networks underlying LLMs are trained using broad collections of text typically obtained from websites, digitized books, and other digital resources.

# History

A central concept in language modeling is the *Markov Chain*, a mathematical model of stochastic processes developed by Andrey Markov in the early 1900s (Gagniuc, 2017), in which the probability of a token in a sequence depends only on a fixed number of immediately preceding tokens.

Shannon (1948) adopted a Markov chain framework to propose language modeling with *n*-*grams,* or sequences of length *n*. Given a vocabulary of tokens from which sequences can be formed, a *unigram* model (*n = *1) is a table that gives the probability *P*(*w**i*) of each token independently; a *bigram* (*n = *2) model gives, for each pair of tokens *w**i**, w**j*, the probability that *w**j* will follow *w**i* in a sequence; and a *trigram* model (*n = *3) similarly gives conditional probabilities that each token will follow a particular sequence of two tokens, and so on.

Using a bigram model, for example, the probability of any sequence *w**1**,w**2**, ... w**m* can be estimated as P(w1)P(w2 | w1)...P(wm | *w**m–1*), and given a sequence, the next token can be sampled from the probability distribution over tokens following the previous two tokens. *N*-gram models are the simplest form of language modeling. The probabilities that make up an *n*-gram model are estimated by measuring the frequencies of token co-occurrences in text corpora; these values are then stored in a *probability table*, from which the probability of each possible word following a given sequence can be quickly retrieved. Shannon (1951) showed how *n*-gram models can be used to estimate the entropy of natural languages, where *entropy* measures the average degree to which a word can be predicted from the sequence of words that precedes it.

In the decades following Shannon’s work, *n*-grams and other statistical language models were used extensively in natural language processing. However, among other limitations, *n*-gram models suffer from the “curse of dimensionality”: the size of the model’s probability table increases exponentially with *n*.

In the 1990s and 2000s, several groups showed that neural networks could be trained to implement language models more efficiently and accurately than *n*-gram models. Most notably, Bengio et al. (2000) proposed the basic structure for neural language modeling still used today: given an input sequence of tokens from a text, the neural network is trained to predict the probability that each token in the model’s vocabulary will be the next token in the sequence. Tokens are represented by numerical vectors (*embeddings*) whose values are also learned from data.

Language models based on *n*-grams and on traditional feedforward neural networks allow only a fixed number of tokens—the *context*—to be used in predicting next-token probabilities. The invention of recurrent neural networks (RNNs), in which tokens in a sequence are input to the network over a series of time steps, enabled neural language modeling with unlimited context length. However, such networks have difficulty capturing longer-range relationships between tokens in a sequence. To address this problem, versions of RNNs were created with features that enhanced their short-term memory (Hochreiter & Schmidhuber, 1997; Cho et al., 2014).

In 2017, researchers at Google proposed a novel type of neural network, called a *transformer architecture* (Vaswani et al., 2017), that was entirely feedforward (meaning that it had no recurrence) but captured long-range dependencies among sequence tokens via a mechanism called *attention*. Transformers substantially outperformed previous RNNs on language modeling. Moreover, unlike RNNs, many aspects of the transformer architecture are easily parallelizable on specialized hardware, enabling substantial scaling of training and inference processes. At present, nearly all LLMs use transformer architectures, the largest having one trillion or more parameters.

# Core concepts

LLMs are *generative models*, which, given a prompt (decomposed into tokens), compute a probability distribution over the model’s vocabulary and probabilistically select the next token to generate. This process can be iterated by appending the generated token to the original prompt and using this new prompt to choose the next token, and so on, to generate new text of any length. LLMs typically have a fixed-length *context window* for their input, in which the original prompt and added tokens are stored; when the context window is full, a token is dropped from the beginning in order to add a new token at the end.

LLMs are built on the transformer architecture, which consists of layers of *transformer blocks*. Each block contains an *attention layer* that feeds into a traditional multilayer perceptron. Each attention layer can have multiple *attention heads*, each of which computes new token embeddings that incorporate some aspect of the context of other tokens in the sequence. The final output of the network is a probability distribution over all tokens in the vocabulary, from which new tokens can be probabilistically selected. As an example of the scale of LLMs, OpenAI’s GPT-3 model has 96 layers of transformer blocks, each of which contains 96 attention heads, with a total of 175 billion tunable parameters (Brown et al., 2020). More recent models have one trillion or more parameters (Minaee et al., 2024).

LLMs are trained on large corpora of text data. A masked training method was used for the early LLM BERT (Devlin et al., 2018): certain tokens in the input text are omitted, and the training objective is to predict these “masked” tokens. OpenAI’s GPT models use an autoregressive training method: the last token in an input text is omitted, and the model’s objective is to predict that token.

Such *self*-*supervised* training, without any specific task objective, is called *pre-training*. The pre-trained model is called a *base model* or a *foundation model*. For many applications, the model must be fine-tuned (i.e., additionally trained) on data that is designed or collected for a specific task. Such fine-tuning takes several forms. *Supervised fine-tuning* uses curated texts with human-created labels that are relevant to specific tasks an LLM might be adapted for, such as summarization or sentiment analysis. *Instruction tuning* uses datasets with human-created examples in which prompts contain instructions and the desired responses show the model how to carry out the instructions. Similar curated datasets are also used to train LLMs to engage in conversation (e.g., become chatbots). Other fine-tuning methods include *reinforcement learning from human feedback*, often used to train LLMs to avoid biased, inappropriate, or other unwanted outputs. Like pre-training, all such fine-tuning methods result in a model that predicts new tokens in response to a prompt, but by tuning weights to create a friendly, nontoxic chatbot that obeys instructions (e.g., OpenAI’s ChatGPT), they go beyond the language-modeling objective that simply relies on statistics of natural language found in general text corpora.

# Questions, controversies, and new developments

## *Successes and limitations of LLMs*

LLMs have been remarkably successful, both in their abilities to model and generate natural language and in their benefits as foundations on which more general AI systems can be built (hence the term *foundation models*). LLMs now dominate applications in natural language processing and have been applied to many areas beyond language, including computer code generation (Poldrack et al., 2023; Roziere et al., 2023), medical applications (Zhou et al., 2023), robotics (Vemprala et al., 2023), financial prediction (Yu et al., 2023), and other diverse applications.

However, in spite of their successes, these models have several weaknesses that have limited their widespread deployment. Because their pretraining objective is to generate statistically likely next tokens, they are prone to what have been called *hallucinations*: generating (often plausible-sounding) untrue statements or information (Xu et al., 2024). LLMs have also absorbed human-like biases concerning race, gender, and other attributes. In spite of fine-tuning designed to mitigate such biases, models built on LLMs have exhibited such biases in both explicit and subtle ways (Weidinger et al., 2022). Other liabilities of LLMs include the possibly illegal inclusion of copyrighted materials in their training data and their outputs (Karamolegkou et al., 2023), the possibility of security risks and privacy violations by such models (Yao et al., 2024), the use of such models to spread disinformation (Jiang et al., 2024), and the requirement for unsustainable amounts of electricity, water, and other resources needed for their operation (Luccioni et al., 2023).

## *Evaluation of LLMs*

The quality of pre-trained LLMs is often evaluated in terms of *perplexity*, an information-theoretic measure that captures how well LLMs perform at predicting tokens that follow given sequences (Rosenfeld, 2000). However, perplexity does not always correlate well with the capability of LLMs (and their fine-tuned versions) to perform specific tasks. Thus, these models are typically tested on standard benchmarks that assess abilities to perform diverse tasks involving language and reasoning as well as on standardized tests designed for humans (Chang et al., 2023). There has been considerable controversy over how informative such evaluations are. Some issues with benchmark-based evaluations are (1) the possibility of *data contamination*—whether parts of these benchmarks (or very similar items) are contained in the models’ training data, which is often impossible to determine, as commercial companies typically don’t reveal training data; (2) the possibility of *shortcuts*—unintended statistical associations in tests that might be used by the model to predict answers without actually performing the underlying general ability being tested; and (3) the issue of *test validity*—whether scoring high on a benchmark translates into similar performance in real-world tasks.

## *Scaling and emergent capabilities in LLMs*

Many studies have shown that the quality of LLMs, measured both in terms of perplexity and in improvement on benchmarks, scales in predictable ways with model size (number of parameters), amount of pre-training data, and computational resources for training (Kaplan et al., 2020). Other studies have shown that certain capabilities in LLMs seem to emerge only at certain scales (Wei et al., 2022a). However, other studies have proposed that the apparent abrupt emergence of such capabilities is an artifact of the evaluation metrics used, not an intrinsic property of scaling (Schaeffer et al., 2024).

## *Reasoning and planning in LLMs*

The abilities of fine-tuned LLMs to reason and plan have been widely debated and remain controversial. Numerous studies have claimed that LLMs can perform sophisticated mathematical and other types of reasoning (Huang & Chang, 2023) and that their abilities can be improved via *Chain-of-Thought* *prompting*, in which they are prompted with examples of reasoning patterns and are prompted to “think step-by-step” (Wei et al., 2022b; Kojima et al., 2022). However, other studies have pointed to many limitations in LLMs’ capacity for reasoning and planning and have questioned the generality and robustness of such abilities in LLMs (McCoy, 2023; Wu et al., 2023), hypothesizing that these systems’ performance on certain problems is due to “approximate retrieval” of similar reasoning patterns in their training data (Kambhampati, 2024) rather than abstract reasoning abilities.

## *Extensions to LLMs*

In order to improve and increase their capabilities, LLMs are being extended in many ways, such as being given the ability to call on “scratchpads” (Nye et al., 2021), code interpreters, symbolic calculators, and other external tools, to search the web and use the results to back up claims (Gao et al., 2023) and to perform actions on the internet. In addition, LLMs are being extended to be *multimodal—*that is, to integrate language with data in other modalities, such as images and videos (Koh et al., 2023; Liu et al., 2024).

# Broader connections

LLMs have touched on nearly all areas of cognitive science and have played many roles, including (among others) as proof of principle for or against linguistic hypotheses [see [Language Acquisition](/articles/xohbfbix)] (Mahowald et al., 2024; Piantadosi, 2023), as models of neuroscientific and cognitive processes (Hardy et al., 2023; Schrimpf et al., 2020), as proposed replacements for human participants in experiments (Crockett & Messeri, 2023; Dillion et al., 2023), and as foils for showing how humans and machines differ (Mitchell et al., 2023; West et al., 2023; Yiu et al., 2023).

# Further reading

- Child, R. Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark, J., Berner, C. McCandlish, S., Radford, A., Sutskever, I., & Amodei, D. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems*, *33*, 1877–1901.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L. & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, *31*.

# References

Gagniuc, P. A. (2017). *Markov Chains: From theory to implementation and experimentation*. John Wiley & Sons. <https://doi.org/10.1002/9781119387596>

Shannon, C. E. (1948). A mathematical theory of communication. *The Bell System Technical Journal,* *27*(3), 379–423. <https://doi.org/10.1002/j.1538-7305.1948.tb01338.x>

Shannon, C. E. (1951). Prediction and entropy of printed English. *The Bell System Technical Journal,* *30*(1), 50–64. <https://doi.org/10.1002/j.1538-7305.1951.tb01366.x>

Bengio, Y., Ducharme, R., & Vincent, P. (2000). A neural probabilistic language model. *Advances in Neural Information Processing Systems*, 13 (pp. 893-899).

Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation,* *9*(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735

Cho, K., Van Merriënboer, B., Bahdanau, D., & Bengio, Y. (2014). On the properties of neural machine translation: Encoder-decoder approaches. In D. Wu, M. Carpuat, X. Carreras, & E. M. Vecchi (Eds.), *Proceedings of the eighth workshop on syntax, semantics and structure in statistical translation* (pp. 103–111). Association for Computational Linguistics. <https://doi.org/10.3115/v1/W14-4012>

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems,* 31.

Minaee, S., Mikolov, T., Nikzad, N., Chenaghlu, M., Socher, R., Amatriain, X., & Gao, J. (2024). *Large language models: A survey*. arXiv. https://doi.org/10.48550/arXiv.2402.06196

Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of deep bidirectional transformers for language understanding. In J. Burstein, C. Doran, & T. Solorio (Eds.), *Proceedings of the 2019 conference of the North American chapter of the Association for Computational Linguistics: human language technologies*, *Volume 1* (pp. 4171–4186). Association for Computational Linguistics.

Rozière, B., Gehring, J., Gloeckle, F., Sootla, S., Gat, I., Tan, X. E., Adi, Y., Liu, J., Sauvestre, R., Remez, T., Rapin, J., Kozhevnikov, A., Evtimov, I., Bitton, J., Bhatt, M., Canton Ferrer, C., Grattafiori, A., Xiong, W., Défossez, A., . . . Synnaeve, G. (2023). *Code Llama: Open foundation models for code*. arXiv. https://doi.org/10.48550/arXiv.2308.12950

Zhou, H., Liu, F., Gu, B., Zou, X., Huang, J., Wu, J., Li, Y., Chen, S. S., Zhou, P., Liu, J., Hua, Y., Mao, C., You, C., Wu, X., Zheng, Y., Clifton, L., Li, Z., Luo, J., & Clifton, D. A. (2023). *A survey of large language models in medicine: Progress, application, and challenge*. arXiv. https://doi.org/10.48550/arXiv.2311.05112

Vemprala, S. H., Bonatti, R., Bucker, A., & Kapoor, A. (2023). ChatGPT for robotics: Design principles and model abilities. *Microsoft Autonomous Systems and Robots Research.* https://www.microsoft.com/en-us/research/uploads/prod/2023/02/ChatGPT\_\_\_Robotics.pdf

Yu, X., Chen, Z., Ling, Y., Dong, S., Liu, Z., & Lu, Y. (2023). *Temporal data meets LLM: Explainable financial time series forecasting*. arXiv. https://doi.org/10.48550/arXiv.2306.11025

Xu, Z., Jain, S., & Kankanhalli, M. (2024). *Hallucination is inevitable: An innate limitation of large language models*. arXiv. https://doi.org/10.48550/arXiv.2401.11817

Weidinger, L., Uesato, J., Rauh, M., Griffin, C., Huang, P., Mellor, J., Glaese, A., Cheng, M., Balle, B., Kasirzadeh, A., Biles, C., Brown, S., Kenton, Z., Hawkins, W., Stepleton, T., Birhane, A., Hendricks, L., Rimell, L., Isaac, W., . . . Gabriel, I. (2022). Taxonomy of risks posed by language models. In *Proceedings of the 2022 ACM conference on fairness, accountability, and transparency* (pp. 214–229). Association for Computing Machinery. <https://doi.org/10.1145/3531146.3533088>

Karamolegkou, A., Li, J., Zhou, L., & Søgaard, A. (2023). *Copyright violations and large language models*. arXiv. https://doi.org/10.48550/arXiv.2310.13771

Yao, Y., Duan, J., Xu, K., Cai, Y., Sun, Z., & Zhang, Y. (2024). A survey on large language model (LLM) security and privacy: The good, the bad, and the ugly. *High-Confidence Computing*, *4*(2). https://doi.org/10.1016/j.hcc.2024.100211

Jiang, B., Tan, Z., Nirmal, A., & Liu, H. (2024). Disinformation detection: An evolving challenge in the age of LLMs. *Proceedings of the 2024 SIAM International Conference on Data Mining (SDM)*, 427–435. <https://doi.org/10.1137/1.9781611978032.50>

Luccioni, A. S., Jernite, Y., & Strubell, E. (2023). *Power hungry processing: Watts driving the cost of AI deployment?* arXiv. https://doi.org/10.48550/arXiv.2311.16863

Rosenfeld, R. (2000). Two decades of statistical language modeling: Where do we go from here? *Proceedings of the IEEE,* *88*(8), 1270–1278. <https://doi.org/10.1109/5.880083>

Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). *Scaling laws for neural language models*. arXiv. https://doi.org/10.48550/arXiv.2001.08361

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., & Fedus, W. (2022a). *Emergent abilities of large language models*. arXiv. https://doi.org/10.48550/arXiv.2206.07682

Schaeffer, R., Miranda, B., & Koyejo, S. (2024). A*re emergent abilities of large language models a mirage?* arXiv. https://doi.org/10.48550/arXiv.2304.15004

Huang, J., & Chang, K. C. C. (2023). Towards reasoning in large language models: A survey. In A. Rogers, J. Boyd-Graber, N. Okazaki (Eds.), *Findings of the Association for Computational Linguistics: ACL* (pp. 1049–1065). Association for Computational Linguistics. <https://doi.org/10.18653/v1/2023.findings-acl.67>

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E. H., Le, Q. V., & Zhou, D. (2022b). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems,* *35*, 24824–24837.

Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are zero-shot reasoners. *Advances in Neural Information Processing Systems,* *35*, 22199–22213.

McCoy, R. T., Yao, S., Friedman, D., Hardy, M., & Griffiths, T. L. (2023). *Embers of autoregression: Understanding large language models through the problem they are trained to solve*. arXiv. https://doi.org/10.48550/arXiv.2309.13638

Wu, Z., Qiu, L., Ross, A., Akyürek, E., Chen, B., Wang, B., Kim, N., Andreas, J., & Kim, Y. (2023). *Reasoning or reciting? Exploring the capabilities and limitations of language models through counterfactual tasks*. arXiv. https://doi.org/10.48550/arXiv.2307.02477

Kambhampati, S. (2024). Can large language models reason and plan? *Annals of the New York Academy of Sciences,* *1534*(1), 15–18. <https://doi.org/10.1111/nyas.15125>

Nye, M., Andreassen, A. J., Gur-Ari, G., Michalewski, H., Austin, J., Bieber, D., Dohan, D., Lewkowycz, A., Bosma, M., Luan, D., Sutton, C., & Odena, A. (2021). *Show your work: Scratchpads for intermediate computation with language models*. arXiv. https://doi.org/10.48550/arXiv.2112.00114

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, M., & Wang, H. (2023). *Retrieval-augmented generation for large language models: A survey*. arXiv. https://doi.org/10.48550/arXiv.2312.10997

Koh, J. Y., Salakhutdinov, R., & Fried, D. (2023). Grounding language models to images for multimodal inputs and outputs. *Proceedings of the 40th International Conference on Machine Learning (ICML)*, 17283–17300.

Liu, Y., Zhang, K., Li, Y., Yan, Z., Gao, C., Chen, R., Yuan, Z., Huang, Y., Sun, H., Gao, J., He, L., & Sun, L. (2024). *Sora: A review on background, technology, limitations, and opportunities of large vision models*. arXiv. https://doi.org/10.48550/arXiv.2402.17177

Mahowald, K., Ivanova, A. A., Blank, I. A., Kanwisher, N., Tenenbaum, J. B., & Fedorenko, E. (2024). Dissociating language and thought in large language models. *Trends in Cognitive Sciences,* *28*, 517–540. <https://doi.org/10.1016/j.tics.2024.01.011>

Piantadosi, S. (2023). Modern language models refute Chomsky’s approach to language. <https://lingbuzz.net/lingbuzz/007180>

Hardy, M., Sucholutsky, I., Thompson, B., & Griffiths, T. (2023). Large language models meet cognitive science: LLMs as tools, models, and participants. *Proceedings of the Annual Meeting of the Cognitive Science Society, 45*.

Schrimpf, M., Blank, I., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., Tenenbaum, J., & Fedorenko, E. (2020). *Artificial neural networks accurately predict language processing in the brain*. BioRxiv. https://doi.org/10.1101/2020.06.26.174482

Crockett, M., & Messeri, L. (2023). *Should large language models replace human participants?* PsyArXiv. <https://doi.org/10.31234/osf.io/4zdx9>

Dillion, D., Tandon, N., Gu, Y., & Gray, K. (2023). Can AI language models replace human participants? *Trends in Cognitive Sciences,* *27*(7), 597–600. <https://doi.org/10.1016/j.tics.2023.04.008>

Mitchell, M., Palmarini, A. B., & Moskvichev, A. (2023). *Comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks*. arXiv. https://doi.org/10.48550/arXiv.2311.09247

West, P., Lu, X., Dziri, N., Brahman, F, Li, L., Hwang, J. D., Jiang, L., Fisher, J, Ravichander, A., Raghavi Chandu, K., Newman, B., Koh, P. W., Ettinger, A., and Choi, Y. (2023). The generative AI paradox: “What it can create, it may not understand”. *The Twelfth International Conference on Learning Representations*.

Yiu, E., Kosoy, E., & Gopnik, A. (2023). Transmission versus truth, imitation versus innovation: What children can do that large language and language-and-vision models cannot (yet). *Perspectives on Psychological Science*.<https://doi.org/10.1177/17456916231201401>