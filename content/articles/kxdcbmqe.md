---
title: Syntactic Priming
slug: kxdcbmqe
date: '2025-07-08'
doi: 10.21428/e2759450.fea3a130
authors:
- Franklin Chang
section_editors:
- Evan Kidd
---

Language allows us to communicate various meanings, including novel messages (e.g., “The engineer airdropped 24GB of prototype designs to his wife’s laptop”). This ability depends on syntactic structures in the language system, but it can be difficult to study these representations, as most people are not explicitly aware of them. One phenomenon that has been used to study them is called *syntactic priming*, which is a tendency for people to reuse previously experienced structures. This phenomenon allows researchers to implicitly manipulate and probe syntactic representations during normal sentence processing, providing a window into the mechanisms used in language to convey meaning.

# History

Priming refers to the influence of one stimulus on another, and its application to sentence planning can be traced to Karl Lashley (1951, p. 128), who posited, “The priming of aggregates of words before a sentence is formulated from them.” Early studies found evidence for structural repetition in experiments (Levelt & Kelter, 1982) and corpora (Schenkein, 1980). Kathryn Bock (1986) provided the standard production paradigm for studying syntactic priming. Typically, it is tested using sentence structures with similar meanings like “The woman gave the book to the man” (*prepositional dative*, PD) and “The woman gave the man the book” (*double object dative*, DO). When a PD prime sentence like “A dog brought a bone to a girl” is presented to a participant before they describe a target picture as in Figure 1, they will be more likely to describe the picture with the same PD structure over the alternative DO structure.

![](images/articles/kxdcbmqe/figure_1.png)

**Figure 1.** Prime-target trial for a priming study.

Initially, syntactic structures were just one of many possible explanations for priming. By controlling other possible factors like function word overlap (prepositions), prosody, and meaning (Bock & Loebell, 1990), it was possible to isolate a unique role for abstract syntactic structures (structures independent of lexical or meaning elements) in priming.

# Core concepts

Early theories posited that production involved activation spreading between concepts, words, and structures [see [Language Production](/articles/e9aapok3)]. If activation was left over in structures (e.g., PD in Figure 1), then this could increase their likelihood of being selected again, and this would create abstract syntactic priming. Then, if activation is used for processing other sentences with unrelated structures after the prime is processed, the residual activation for the prime should be reduced, and priming could disappear. However, empirically, priming persists even when there is a lag of 10 intervening sentences between prime and target, which suggests that abstract priming does not use an activation mechanism (Bock & Griffin, 2000).

To explain the persistence of priming, Chang et al. (2006) proposed that abstract priming was due to the same implicit learning mechanism used to acquire the syntactic representations in the first place. They developed a computational model that could acquire abstract syntactic representations using prediction error–based learning, which is a learning mechanism that uses the difference between the input and the predictions of the system (error). By leaving learning on during the processing of the prime sentence, the model made subtle changes to the syntactic system that created priming effects. This account suggests that priming is a side effect of the fact that the brain is constantly adapting to the input, even in adulthood.

If syntactic priming is a type of learning, then biases should accumulate with every structure that is experienced (*cumulativity*; Figure 2; Kaschak & Borreggine, 2008). This cumulative bias for structures seems to influence priming, in which the mismatch between the preference and the prime structure (*error* or *surprisal*) is associated with larger priming effects (Jaeger & Snider, 2013).

![](images/articles/kxdcbmqe/figure_2.png)

**Figure 2.** A schematic of the relationship between cumulativity, error, and priming.

When content words such as verbs are the same between prime and target (the verb “gave” in Figure 3), the magnitude of syntactic priming can increase, and this is called the *lexical boost* (Pickering & Branigan, 1998). Studies have examined whether the boost and abstract priming with different verbs depend on the same mechanism by increasing the lag between prime and target by using intervening filler sentences, with the results showing that abstract priming persisted over various lags, but the boost quickly dissipated (Figure 3; Hartsuiker et al., 2008). This result suggested that the boost was not due to implicit learning but rather residual activation in explicit memory, which is known to decay rapidly.

![](images/articles/kxdcbmqe/figure_3.png)

**Figure 3.** Lexical boost and abstract priming over lag.

Since most people do not have explicit awareness of the syntactic structures they use, these structures are thought to depend on implicit memory. However, because some aspects of language are available to conscious awareness (e.g., words) and could depend on explicit declarative memory, it was important to determine which memory systems are involved in priming. These memory systems can be differentiated in individuals with anterograde amnesia, who have deficits in explicit memory (e.g., newly learned facts are forgotten quickly) but retain implicit learning abilities (e.g., learning to play new piano pieces). These patients exhibit abstract syntactic priming, even though they have impaired explicit memory for the prime sentences (Ferreira et al., 2008). This finding demonstrates that syntactic priming mostly depends on implicit memory without a substantial role for explicit memory.

Since priming has been argued to be supported by language learning mechanisms, priming has been used to examine syntactic structures in development [see [Language Acquisition](/articles/xohbfbix)]. Item-based theories of language acquisition have argued that children start initially with lexically specific syntactic representations and only later develop abstract syntax (Figure 4) [see [Compositionality](/articles/e222wyjy)]. However, several studies have found evidence for abstract structural priming early in development (Kumarage et al., 2024; Rowland et al., 2012). Priming in children exhibits persistence, cumulativity, and error sensitivity in ways that are similar to adults (Branigan & Messenger, 2016; Peter et al., 2015), and these findings are consistent with the idea that language acquisition and syntactic priming involve the same prediction error–based learning mechanism [see [Computational Models of Language Learning](/articles/hexmhaj8)].

![](images/articles/kxdcbmqe/figure_4.png)

**Figure 4.** Priming based on item-based or abstract syntactic representations in development.

# Questions, controversies, and new developments

Most priming studies use language production measures (Mahowald et al., 2016). Syntactic priming has also been studied with comprehension measures like reading times, but abstract priming is not always found using these measures, and priming often depends on verb overlap (Tooley & Traxler, 2010). Thus, there are substantial differences in priming with comprehension and production measures, and further research is needed to see if there is a shared component [see [Psycholinguistics](/articles/y1uhdz0y)].

Syntactic priming has been mostly studied in a small set of languages (e.g., English, Dutch, German, Chinese). Because priming involves learned syntactic structures, it is possible that priming can vary greatly across typologically different languages (e.g., Tagalog; Garcia et al., 2023) [see [Linguistic Variation](/articles/5wqto9iq)].

# Broader connections

Syntactic priming is an example of learning over the lifetime (Dell & Chang, 2014). Understanding this mechanism may provide insight into similar mechanisms that support adaptation in response to various influences such as education, work, technology, sports, and social situations over the whole of development [see [Neuroplasticity](/articles/t5j0qv3d)].

The error-based learning mechanisms used to explain priming are related to the learning algorithms used by artificial intelligence systems like ChatGPT to acquire their language representations [see [Large Language Models](/articles/zp5n8ivs)]. Priming can be used to examine how closely these systems mirror the abstract syntactic representations used by human language users.

# Further reading

- Bock, K., & Loebell, H. (1990). Framing sentences. *Cognition*, *35*(1), 1–39. [https://doi.org/10.1016/0010-0277(90)90035-I](https://doi.org/10.1016/0010-0277(90)90035-I)
- Branigan, H. (2007). Syntactic priming. *Language and Linguistics Compass*, 1(1–2), 1–16. [https://doi.org/10.1111/j.1749-818X.2006.00001.x](https://doi.org/10.1111/j.1749-818X.2006.00001.x)
- Pickering, M. J., & Ferreira, V. S. (2008). Structural priming: A critical review. *Psychological Bulletin*, *134*(3), 427–459. [https://doi.org/10.1037/0033-2909.134.3.427](https://psycnet.apa.org/doi/10.1037/0033-2909.134.3.427)

# References

Lashley, K. S. (1951). The problem of serial order in behavior. In L. A. Jeffress (Ed.), *Cerebral mechanisms in behavior* (pp. 112–136). Wiley.

Levelt, W. J., & Kelter, S. (1982). Surface form and memory in question answering. *Cognitive Psychology*, *14*(1), 78–106. <https://doi.org/10.1016/0010-0285(82)90005-6>

Schenkein, J. (1980). A taxonomy for repeating action sequences in natural conversation. In B. Butterworth (Ed.), *Language production* (Vol. 1, pp. 21–47). Academic Press.

Bock, K. (1986). Syntactic persistence in language production. *Cognitive Psychology*, *18*(3), 355–387. <https://doi.org/10.1016/0010-0285(86)90004-6>

Bock, K., & Loebell, H. (1990). Framing sentences. *Cognition*, *35*(1), 1–39. <https://doi.org/10.1016/0010-0277(90)90035-I>

Bock, K., & Griffin, Z. M. (2000). The persistence of structural priming: Transient activation or implicit learning? *Journal of Experimental Psychology: General*, *129*(2), 177–192. <https://doi.org/10.1037//0096-3445.129.2.177>

Chang, F., Dell, G. S., & Bock, K. (2006). Becoming syntactic. *Psychological Review*, *113*(2), 234–272. <https://doi.org/10.1037/0033-295X.113.2.234>

Kaschak, M. P., & Borreggine, K. L. (2008). Is long-term structural priming affected by patterns of experience with individual verbs? *Journal of Memory and Language*, *58*(3), 862–878. <https://doi.org/10.1016/j.jml.2006.12.002>

Jaeger, T. F., & Snider, N. E. (2013). Alignment as a consequence of expectation adaptation: Syntactic priming is affected by the prime’s prediction error given both prior and recent experience. *Cognition*, *127*(1), 57–83. <https://doi.org/10.1016/j.cognition.2012.10.013>

Pickering, M. J., & Branigan, H. P. (1998). The representation of verbs: Evidence from syntactic priming in language production. *Journal of Memory and Language*, *39*(4), 633–651. <https://doi.org/10.1006/jmla.1998.2592>

Hartsuiker, R. J., Bernolet, S., Schoonbaert, S., Speybroeck, S., & Vanderelst, D. (2008). Syntactic priming persists while the lexical boost decays: Evidence from written and spoken dialogue. *Journal of Memory and Language*, *58*(2), 214–238. <https://doi.org/10.1016/j.jml.2007.07.003>

Ferreira, V. S., Bock, K., Wilson, M. P., & Cohen, N. J. (2008). Memory for syntax despite amnesia. *Psychological Science*, *19*(9), 940–946. <https://doi.org/10.1111/j.1467-9280.2008.02180.x>

Kumarage, S., Donnelly, S., & Kidd, E. (2024). A meta-analysis of syntactic priming experiments in children. *Journal of Memory and Language*, *138*, 104532. <https://doi.org/10.1016/j.jml.2024.104532>

Rowland, C. F., Chang, F., Ambridge, B., Pine, J. M., & Lieven, E. V. M. (2012). The development of abstract syntax: Evidence from structural priming and the lexical boost. *Cognition*, *125*(1), 49–63. <https://doi.org/10.1016/j.cognition.2012.06.008>

Branigan, H. P., & Messenger, K. (2016). Consistent and cumulative effects of syntactic experience in children’s sentence production: Evidence for error-based implicit learning. *Cognition*, *157*, 250–256. <https://doi.org/10.1016/j.cognition.2016.09.004>

Peter, M., Chang, F., Pine, J. M., Blything, R., & Rowland, C. F. (2015). When and how do children develop knowledge of verb argument structure? Evidence from verb bias effects in a structural priming task. *Journal of Memory and Language*, *81*, 1–15. <https://doi.org/10.1016/j.jml.2014.12.002>

Mahowald, K., James, A., Futrell, R., & Gibson, E. (2016). A meta-analysis of syntactic priming in language production. *Journal of Memory and Language*, *91*, 5–27. <https://doi.org/10.1016/j.jml.2016.03.009>

Tooley, K. M., & Traxler, M. J. (2010). Syntactic priming effects in comprehension: A critical review. *Language and Linguistics Compass*, *4*(10), 925–937. <https://doi.org/10.1111/j.1749-818X.2010.00249.x>

Garcia, R., Roeser, J., & Kidd, E. (2023). Finding your voice: Voice-specific effects in Tagalog reveal the limits of word order priming. *Cognition*, *236*, 105424. <https://doi.org/10.1016/j.cognition.2023.105424>

Dell, G. S., & Chang, F. (2014). The P-chain: Relating sentence production and its disorders to comprehension and acquisition. *Philosophical Transactions of the Royal Society B: Biological Sciences*, *369*(1634), 1–9. <https://doi.org/10.1098/rstb.2012.0394>