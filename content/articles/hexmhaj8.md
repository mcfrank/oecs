---
title: Computational Models of Language Learning
slug: hexmhaj8
date: '2025-03-31'
doi: 10.21428/e2759450.a23858f4
authors:
- Raquel G. Alhama
- Afra Alishahi
section_editors:
- Evan Kidd
---

A computational model of language learning is a formal description of how linguistic input can be transformed into either mental representations or (linguistic) behavior. For instance, a model may formally describe how a speech signal directed at a child can be processed to learn word-meaning mappings, a problem all human children face. In addition, the model may outline how this leads to subsequent behavioral responses such as looking or pointing at a referent. As they implement formal algorithms, computational models of language learning are theoretical proposals of the mental representations and processes underlying human language acquisition. Although a computational model can refer to any detailed specification of such a cognitive process, most modern computational models are computer programs that implement (some aspect of) language learning. These implementations allow simulation of the linguistic behavior or its developmental trajectory and systematic comparison of the model to that of a human language learner. Such a comparison allows the researcher to assess the success of the underlying theoretical account in explaining empirical findings or observations regarding the linguistic process under study and to facilitate deriving theoretical predictions that may have not yet been empirically investigated.

# History

The process of learning natural languages has historically been discussed and theorized concurrently across several disciplines such as psychology and philosophy [see [Language Acquisition](/articles/xohbfbix)]. Earlier attempts were limited to verbal explanations of these processes, without a formal specification of their input and output or a detailed description of their internal learning mechanisms.

The emergence of formal linguistics as an independent discipline led the way for a new generation of formal models and frameworks for representing linguistic knowledge, such as the Chomsky hierarchy—a classification that categorized grammars according to their complexity (Chomsky, 1956)—and the early models of formal semantics (see Partee, 2011). These mathematical formulations, although limited in scope, offered a direct connection between the linguistic input and the outcome of the language learning process. In this generation of models, the focus was primarily on the formal characteristics of an established language system, and less attention was devoted to the process of acquiring linguistic representations from input. The approach was purely theoretical (i.e., it was not implemented using computers).

With the advent of modern computers and the digitization and expansion of datasets collected by language researchers, the next generation of cognitive models became more explicit and often took the form of computer programs. Inspiring and inspired by the first artificial intelligence systems, these models implemented different aspects of learning a language, often relying on a *symbolic framework* for representing linguistic knowledge (i.e., words as symbols, properties as propositional phrases, linguistic structure as a set of symbolic grammar rules). Although these models were often massively simplified and evaluated on small-scale and fully controlled “toy” languages (i.e., simulated languages with small vocabularies and a small number of grammatical rules), they demonstrated how an implementation of an existing theory can perform in practice and be evaluated based on the similarity of its “behavior” to a human language learner. Examples are the word segmentation model of Harris (1955), word learning model of Siskind (1996), and the symbolic implementation of the principles and parameters framework by Gibson and Wexler (1994).

It soon became clear that models based on the symbolic framework have major limitations when dealing with real-world data. Despite their ease of interpretation and their sound and well-understood mathematical foundation, they were not suitable for dealing with the variability present in the environments in which natural languages are often learned and used. Moreover, the symbolic framework could not capture humans’ sensitivity to the statistical properties of the input and its context.

The shortcomings of the symbolic framework for modeling human cognition motivated some scholars to look for inspiration in the ultimate learning machine, that is, the human brain. The first *connectionist* or artificial neural network models were built with data processing units that imitated the functional behavior of interconnected neurons, which sent signals to each other. These early networks were small in size and straightforward in architecture, but they were radically different from previous models in the way they represented and processed knowledge: a new way of thinking was required to map the linguistic input (often thought of as a sequence of symbols) into a distributed numerical representation that was understandable by an artificial neural network. The models showed an impressive capacity in detecting and learning regular patterns in the data without a need for hand-built rules and schemas, a process that seemed much more similar to how humans learn. Some examples include models of the acquisition of English past tense (Rumelhart & McClelland, 1986; Plunkett & Marchman, 1993), the formation of lexical categories (Elman, 1991), and the learning of word-meaning associations (Regier, 2005).

Despite their popularity, the computational inefficiency of connectionist models and their reliance on datasets annotated with linguistic information made them hard to generalize to larger-scale case studies and realistic language input. This coincided with a new generation of statistical and probabilistic models that could efficiently process large collections of noisy data. *Probabilistic* models became widespread as an alternative framework for developing data-driven models that draw on previous experience to build weighted knowledge representations. Principled algorithms based on probabilistic reasoning could use such representations to choose the most likely hypotheses for explaining observations. Most of the new, probabilistic models of language learning and processing were built on the symbolic foundations of earlier models (e.g., probabilistic context-free grammars).

A family of probabilistic models, called (hierarchical) Bayesian models, became particularly popular in formalizing various aspects of human cognition—including language—due to their elegant way of defining and formalizing prior assumptions about different components of a cognitive process and their statistical characteristics and interdependence. Some examples include Frank et al.'s (2009) model of word learning and Goldwater et al.'s (2009) model of word segmentation. Probabilistic models of language learning and processing have enjoyed decades of popularity and dominance in cognitive science. However, with the resurgence of more efficient neural networks, their enhanced architectures and (arguably) human-like behavior, combined with the availability of massive datasets for training them (especially in the domain of language), the attention of the cognitive modeling community has been shifted back to neural network models [see [Large Language Models](/articles/zp5n8ivs)]. Much of the focus of recent discussions is centered on the cognitive plausibility of deep neural models and whether they can tell us anything about the way humans learn and process language.

# Core concepts

## *Why computational modeling?*

Computational models can play different roles in the scientific process of discovering the underpinnings of language learning. As in other areas of cognitive science, we often refer to Marr’s levels of analysis as a useful taxonomy to indicate whether a model is proposed as a formalization of the task to be solved by the learner (i.e., at the *computational level*), a model is proposed as a depiction of the mental processes followed by a human learner (i.e., at the *algorithmic level*), or a model goes as far as to propose which brain circuits play a role in the process (i.e., at the *implementational level*; Marr, 2010).

Marr’s levels of analyses are helpful to clarify the proposed level of realism of a model. Another partially overlapping characterization of models concerns their predictive or explanatory nature. Models can be considered *predictive* when their main goal is to quantitatively reflect an observed behavior as accurately as possible. For example, many models of word learning are used to predict the age at which a learner acquires specific words in a given language (or which words are learnt earlier than others) [see [Word Learning](/articles/dubzy1cd)]. These models are particularly helpful to reveal which input features are most relevant for word learning, for example, a word’s level of concreteness, frequency of usage, or the linguistic context in which it appears (Hansen, 2017; Swingley & Humphrey, 2018; Verhagen et al., 2022; Alhama et al., 2023). Models that focus on different properties of the input may differ in their predictions, so we can claim that the model that better approximates the observed age of acquisition of human learners likely exploits similar input properties. However, these models often abstain from making claims about the representations and processes that mediate learning. That is, it is entirely possible that a model will simulate the human acquisition process accurately but does so using different internal representations and processes.

In contrast, *explanatory* models are used to gain insight into such processes and representations. Accuracy of prediction is not the main goal in this case; although models should still hold some predictive power, a simple model that can only approximate the general trends of an observed pattern may be more revealing than a complex model that accurately predicts every observation. For example, models of word learning (e.g., Siskind, 1996; Fazly et al., 2010) aim to replicate developmental trajectories observed in children such as the so-called vocabulary spurt (i.e., the sudden increase in the rate of acquired words following a slow start; McMurray, 2007), and models of morphological derivation or argument structure acquisition often attempt to explain the so-called U-shaped curve, in which an initial conservative and error-free period of predicting an inflected form (e.g., “went”) is followed by an erroneous application of a general rule (e.g., “goed”), before recovering from these overgeneralization errors (Pinker & Prince, 1988; Alishahi & Stevenson, 2008). The main goal of such models is to examine which combination of information cues and learning mechanisms can yield the same developmental trajectory observed in humans.

In addition to—or in combination with—these goals, models are sometimes used to generate novel predictions for situations that have not been empirically investigated yet. For instance, after ensuring that a model accurately predicts or explains a behavioral pattern in one language, it can be used to make predictions for a different language or for an unexplored population group (e.g., learners of a different age). Although computational models should be used with a clear goal in mind, they become maximally useful when they go beyond their original goal and reveal unexpected and unobserved patterns.

Despite all these possibilities that models offer, it is important to keep in mind that no matter how accurate a model is at predicting the behavior of a group of language learners, it can never be taken as proof that humans employ the same learning mechanisms that the model implements. Mathematically speaking, there is no single way to transform an input into a specific output; for this reason, a successful model can only tell us that a certain behavioral pattern can be explained via applying a learning mechanism on a certain type of input. For example, consider models that learn syntactic structures from child-directed speech, without any prior linguistic knowledge (e.g., Reali & Christiansen, 2005; Perfors et al., 2011). Even when these models demonstrate successful learning, they do not constitute definitive evidence that human language acquisition relies (exclusively) on the same process or data. However, such models do provide support for the possibility that it does, countering the so-called poverty of stimulus arguments that refute the mere possibility that syntax can be learned without innate language-specific structures in place (Chomsky, 1965).

## *The role of input*

For a model to imitate human language learning, it is essential to have access to input data that is representative of what humans receive from their environment. This was a challenge for the first generation of computational models of language learning, since representative samples of such input were simply not available, and many of these early models relied on synthesized data (e.g., Siskind, 1996; Elman, 1990).

Once the CHILDES archive (a collection of naturalistic recordings of linguistic interactions between children and caregivers; MacWhinney, 2000) was released, many computational models used its transcripts of child-directed utterances as their input data. Although this approach was sufficient for models that only relied on textual input (e.g., models of morphology, grammar, or lexical categories), those that focused on learning aspects of meaning (e.g., word learning or argument structure) had to augment these transcriptions with either manually annotated symbols of referents and objects in the scene (e.g., Frank et al., 2009) or reconstruct the meaning of words and utterances with additional resources such as WordNet or VerbNet (e.g., Fazly et al., 2010).

As available corpora of child–adult interaction become more widespread, their scale and modality also becomes more realistic. [TalkBank](https://talkbank.org/) now offers various datasets containing video recordings of child–adult interactions, which allows fundamental aspects of language learning such as word segmentation and phonology to be modeled directly from the speech signal rather than indirectly through transcripts. Furthermore, grounded models of language learning can now explore the associations between written or spoken utterances and their visual context (e.g., Chrupala et al., 2017; Harwath et al., 2020; Nikolaus et al., 2022).

Although the availability of such video recordings is a step towards building more ecologically valid cognitive models, the choice of which information cues to extract and exploit from the complex, noisy, and multimodal signal available to language learners is a methodological as well as theoretical choice. For example, some argue that semantics to a large extent can be learned from implicit information in the cooccurrences of linguistic units rather than relying on an external modality such as vision, often referred to as the *distributional semantics hypothesis* (Harris, 1954; Firth, 1957).

## *Model evaluation*

One common way to evaluate whether a model of language learning is a good representation of human learning is to compare the output of the model to observations of children’s spontaneous use of language. The emergence of collections of child–adult interactions such as [CHILDES](http://childes.talkbank.org) (MacWhinney, 2000) has strongly fueled the development of models of language acquisition, thanks to allowing for evaluation against human data. A common setup is to train models on caretaker productions (that is, presenting the models with the same input that human learners experience) and then evaluate the models by comparing their output to the children’s productions (e.g., McCauley & Christiansen, 2019). However, language production is only one of the many tasks that a language model can perform and be evaluated on, and often other assumptions need to be made to compare a model’s output to the observed behavior of human learners, an issue to which we return below.

There are other ways to collect empirical observations from human learners. An example is the MacArthur-Bates Communicative Development Inventories (see Fenson et al., 2007), a set of vocabulary checklists that parents complete to estimate which words their child understands and produces at a given age. Databases such as [Wordbank](http://wordbank.stanford.edu) (Frank et al., 2017) use these inventories to estimate the typical age at which a word is acquired, which makes it a prominent resource to evaluate models of vocabulary growth (e.g., Chang & Bergen, 2022).

Other measures may be obtained in less naturalistic settings; for instance, by estimating word knowledge from experimentally derived data. To evaluate models against these observations, it is relevant to recreate the experimental conditions during model simulation; that is, the model should be exposed to the same stimuli and tested in a similar fashion as the human subjects.

Comparison to human data is not only important in assessing a cognitive model, it can also be used as an anchor for comparing the plausibility of competing models. For example, young language learners typically underperform when attempting to segment words from a continuous speech stream (e.g., upon hearing “guitar man,” a young English-acquiring infant may hypothesize that “tarman” is a word because they expect words to have syllable-initial stress; Jusczyk et al., 1993). Hence, models may be used to find out which word segmentation strategy results in the same undersegmentation patterns. Modelers often adhere to goodness-of-fit criteria to differentiate between models; that is, they measure the difference between model predictions and observations. However, it is often not at all easy to distinguish the relative contribution of a model, since a better fit may be achieved by providing a model with more degrees of freedom (and arguably less explanatory power).

## *Cognitive plausibility*

It is a truism to say that all models are wrong. Modeling entails simplifying reality to prevent irrelevant details obscuring the uncovering of the learning principles that we are investigating. However, modelers of human language learning (and cognitive modelers more generally) normally agree that models should meet some minimum requirements of cognitive plausibility.

For most cognitive models, the criteria of cognitive plausibility includes restrictions on memory storage, computing power, and on providing realistic input to the model, such that the model approximates the limitations and experiences of the child. In the case of models of language, an important consideration is the temporal aspect of the input—that is, language is experienced over time, and thus we may not provide all the input to our models in one single batch. This consideration is particularly intuitive for spoken language, given that a listener is exposed to sounds that are produced sequentially, phoneme after phoneme, such that each sound disappears right after it has been emitted. Although written language does not have the ephemeral nature of sound, humans observe letter chunks incrementally, although this process is not perfectly sequential, and readers often skip words or regress back to previous text. For this reason, most models of language learning have some form of sequential presentation of information. We must bear in mind, however, that information may be buffered in memory and therefore processed in larger batches or perhaps revisited later, following a non-strictly incremental order [see [Working Memory](/articles/1rgtz41v)].

Models postulated at Marr’s computational level are typically more relaxed in terms of cognitive plausibility (e.g., Perfors et al., 2006) [see [Rational Analysis](/articles/lurik5dk)]. Memory constraints are one of the most illustrative examples—many if not most computational-level models do not limit the model’s capacity in this regard. This choice is consistent with the goal of the representational level, given that these models are used to formalize the problem at a higher level. Nevertheless, modelers ensure that these models make realistic assumptions about the input and do not receive more information than humans do (Brent, 1999).

# Questions, controversies, and new developments

As is the case in linguistics, one of the most debated topics amongst modelers of language learning is the acquisition of linguistic structure, most prominently syntax. This is one of the crucial milestones of language acquisition, as it is what allows learners to go beyond specific lexical information and acquire the rules to produce any novel sentence (i.e., it enables language’s *generative* capacity) [see [Language](/articles/ho9e9c80)]. Computational models have a role to play in discussions around whether humans must come to the world with linguistic-specific biases (Chomsky, 1965). In particular, weakly biased models (such as neural networks) that do not have any prior linguistic knowledge are often used to provide *learnability proofs*: if a model without an incorporated bias towards a representation of syntax (for example, a preexisting syntactic category) can learn such knowledge from naturalistic input, then the poverty of stimulus argument is weakened (Warstadt & Bowman, 2022; Alhama et al., 2024).

A related controversy is the acquisition of morphological derivation—in particular, the English past tense. To correctly inflect this form, children need to differentiate between regular verbs (which requires appending the “-ed” suffix to the base form to inflect the past tense) and irregular verbs, which do not conform to a well-defined rule (e.g., find-found, sing-sung). This phenomenon has been a testbed for models of morphological learning since Rumelhart and McClelland (1986) presented a neural network model that reproduced children’s U-shaped developmental trajectory. The authors interpreted this result as a demonstration that human learners may not represent knowledge of regular constructions in the shape of symbolic rules—since neural network models do not explicitly represent rules and symbols. This claim sparked a debate, as other authors argued that dual route models that assumed differential learning for regular and irregular verbs were a better fit to the data (Pinker & Prince, 1988; Pinker & Ullman, 2002), whereas others suggested the integration of rules within a connectionist framework (Smolensky, 1990). The discussion has recently reignited, updated with more recent encoder–decoder neural network architectures (Kirov & Cotterell, 2018). Although the latter model shows more accurate learning than previous efforts, the authors acknowledge that some of the early criticisms have not been fully resolved—for example, the treatment of homophones (e.g., “write-wrote” but “right-righted”).

Finally, an omnipresent source of controversy among modelers is what constitutes a valid model. One reason for this lack of consensus is that different modeling goals may require different criteria. In predictive modeling, this issue is somewhat mitigated because accuracy of prediction is an objective measure that facilitates model comparison. Predictive models are most often used to distinguish between competing input features, and for such a goal, goodness of fit may be sufficient to differentiate between models that exploit different features. In explanatory modeling, however, a tradeoff between accuracy and simplicity is often preferred, given that accuracy is often achieved by augmenting the degrees of freedom of the model. Hence, a very accurate model with a large number of parameters may be disfavored against a simpler model that likely represents only general principles of learning (while not fitting to idiosyncrasies of individual learners or tasks), therefore being also more robust and usable for other languages or populations. In addition to these considerations about modeling goals, an unresolved problem is that there is no consensus on the data or measurements against which the models should be evaluated as well as on interpreting the output of a model. Neighboring fields such as natural language processing have well-defined benchmarks for model evaluation, which test the practical applicability of each model in the context of a well-defined task. In contrast, models of human language learning do not come with standard desiderata or benchmarks to evaluate them.

# Broader connections

The neighboring field of natural language processing is concerned with building technology that can be useful for tasks involving language such as translation, summarization, question answering, etc. Undoubtedly, the most successful models in the current times are large language models such as GPT-4 (OpenAI, 2024), Llama, and many others. The fluency of these models is unprecedented, to the extent that some researchers claim that we should see beyond the practical uses of these models and treat them as a basis for constructing proper theories of language (Baroni, 2022; Piantadosi, 2023) and see what lessons these models hold for the study of human language learning (Pater, 2019). However, we must bear in mind that large language models are trained on several orders of magnitude more data than children (Frank, 2023; Warstadt & Bowman, 2022). Initiatives such as the BabyLM challenge (Warstadt et al., 2023) limit the amount of training data such that we can analyze the abilities of these models under constraint and compare model variants that have been trained on the same data.

# Further reading

- Alishahi, A. (2011). *Computational modeling of human language acquisition.* Springer Cham.
- Chater, N., & Manning, C. D. (2006). Probabilistic models of language processing and acquisition. *Trends in Cognitive Sciences*, *10*(7), 335–344. [https://doi.org/10.1016/j.tics.2006.05.006](https://doi.org/10.1016/j.tics.2006.05.006)
- Monaghan, P., & Rowland, C. F. (2017). Combining language corpora with experimental and computational approaches for language acquisition research. *Language Learning*, *67*(S1):14–39. [https://doi.org/10.1111/lang.12221](https://doi.org/10.1111/lang.12221)
- Warstadt, A., & Bowman, S. R. (2022). What artificial neural networks can tell us about human language acquisition. *arXiv*. [https://doi.org/10.48550/arXiv.2208.07998](https://doi.org/10.48550/arXiv.2208.07998)

# References

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory,* *2*(3), 113-124. <https://doi.org/10.1109/TIT.1956.1056813>

Partee, B. H. (2011). Formal semantics: Origins, issues, early impact. *Baltic International Yearbook of Cognition, Logic and Communication*, *6*(1), 13. <https://doi.org/10.4148/biyclc.v6i0.1580>

Harris, Z. S. (1955). From phoneme to morpheme. *Language*, *31*, 190-222. <https://doi.org/10.2307/411036>

Siskind, J. M. (1996). A computational study of cross-situational techniques for learning word-to-meaning mappings. *Cognition*, *61*(1-2), 39–91. <https://doi.org/10.1016/S0010-0277(96)00728-7>

Gibson, E., & Wexler, K. (1994). Triggers. *Linguistic Inquiry*, *25*(3), 407–454.

Rumelhart, D. E., & McClelland, J. L. (1986). On learning the past tenses of English verbs. *Psycholinguistics: Critical Concepts in Psychology*, *4*, 216–271.

Plunkett, K., & Marchman, V. (1993). From rote learning to system building: Acquiring verb morphology in children and connectionist nets. *Cognition*, *48*(1), 21–69. <https://doi.org/10.1016/0010-0277(93)90057-3>

Elman, J. L. (1991). Distributed representations, simple recurrent networks, and grammatical structure. *Machine Learning*, *7*, 195–225. <https://doi.org/10.1007/BF00114844>

Regier, T. (2005). The emergence of words: Attentional learning in form and meaning. *Cognitive Science*, *29*(6), 819–865. <https://doi.org/10.1207/s15516709cog0000_31>

Frank, M. C., Goodman, N. D., & Tenenbaum, J. B. (2009). Using speakers’ referential intentions to model early cross-situational word learning. *Psychological Science*, *20*(5), 578–585. <https://doi.org/10.1111/j.1467-9280.2009.02335.x>

Goldwater, S., Griffiths, T. L., & Johnson, M. (2009). A Bayesian framework for word segmentation: Exploring the effects of context. *Cognition*, *112*(1), 21–54. [https://doi.org/10.1016/j.cognition.2009.03.008](https://doi.org/10.1016/j.cognition.2009.03.008.)

Marr, D. (2010). *Vision: A computational investigation into the human representation and processing of visual information*. MIT Press.

Hansen, P. (2017). What makes a word easy to acquire? The effects of word class, frequency, imageability and phonological neighbourhood density on lexical development. *First Language*, 37(2), 205–225. [https://doi.org/10.1177/0](https://doi.org/10.1177/0142723716679956)

Swingley, D., & Humphrey, C. (2018). Quantitative linguistic predictors of infants’ learning of specific English words. *Child Development*, *89*, 1247–1267. <https://doi.org/10.1111/cdev.12731>

Verhagen, J., van Stiphout, M., & Blom, E. (2022). Determinants of early lexical acquisition: Effects of word- and child-level factors on Dutch children’s acquisition of words. *Journal of Child Languag*e, *49*(6), 1193–1213. <https://doi.org/10.1017/S0305000921000635>

Alhama, R. G., Rowland, C. F., & Kidd, E. (2023). How does linguistic context influence word learning?. *Journal of Child Language*, *50*(6), 1374-1393. <https://doi.org/10.1017/S0305000923000302>

Siskind, J. M. (1996). A computational study of cross-situational techniques for learning word-to-meaning mappings. *Cognition*, *61*(1-2), 39–91. <https://doi.org/10.1016/S0010-0277(96)00728-7>

Fazly, A., Alishahi, A., & Stevenson, S. (2010). A probabilistic computational model of cross-situational word learning. *Cognitive Science*, *34*(6), 1017–1063. <https://doi.org/10.1111/j.1551-6709.2010.01104.x>

McMurray, B. (2007). Defusing the childhood vocabulary explosion. *Science*, *317*(5838), 631-631. <https://doi.org/10.1126/science.1144073>

Pinker, S., & Prince, A. (1988). On language and connectionism: Analysis of a parallel distributed processing model of language acquisition. *Cognition*, *28*(1-2), 73–193. <https://doi.org/10.1016/0010-0277(88)90032-7>

Alishahi, A., & Stevenson, S. (2008). A computational model of early argument structure acquisition. *Cognitive Science*, *32*(5), 789-834. <https://doi.org/10.1080/03640210801929287>

Reali, F., & Christiansen, M. H. (2005). Uncovering the richness of the stimulus: Structure dependence and indirect statistical evidence. *Cognitive Science*, *29*(6), 1007-1028. <https://doi.org/10.1207/s15516709cog0000_28>

Perfors, A., Tenenbaum, J. B., & Regier, T. (2011). The learnability of abstract syntactic principles. *Cognition*, *118*(3), 306-338. <https://doi.org/10.1016/j.cognition.2010.11.001>

Chomsky, N. (1965). *Aspects of the theory of syntax*. MIT Press.

Elman, J. L. (1990). Finding structure in time. *Cognitive Science*, *14*(2), 179–211. <https://doi.org/10.1016/0364-0213(90)90002-E>

MacWhinney, B. (2000). The CHILDES project: Tools for analyzing talk (third edition): Volume I: Transcription format and programs, Volume II: The database. *Computational Linguistics*, *26*(4), 657. <https://doi.org/10.1162/coli.2000.26.4.657>

Frank, M. C., Goodman, N. D., & Tenenbaum, J. B. (2009). Using speakers’ referential intentions to model early cross-situational word learning. *Psychological Science*, *20*(5), 578–585. <https://doi.org/10.1111/j.1467-9280.2009.02335.x>

Chrupala, G., Gelderloos, L., & Alishahi, A. (2017). Representations of language in a model of visually grounded speech signal. In R. Barzilay & M. Y. Kan (Eds.), *Annual Meeting of the Association for Computational Linguistics 2017* (pp. 613-622). Association for Computational Linguistics. <https://doi.org/10.18653/v1/P17-1057>

Harwath, D., Recasens, A., Surís, D., Chuang, G., Torralba, A., & Glass, J. (2020). Jointly discovering visual objects and spoken words from raw sensory input. *International Journal of Computer Vision*, 128, 620-641. <https://doi.org/10.1007/s11263-019-01205-0>

Nikolaus, M., Alishahi, A., & Chrupała, G. (2022). Learning English with Peppa Pig. *Transactions of the Association for Computational Linguistics*, *10*, 922-936. <https://doi.org/10.1162/tacl_a_00498>

Harris. Z. S. (1954). Distributional structure. *Word*, *10*(2-3), 146–162. <https://doi.org/10.1080/00437956.1954.11659520>

Firth, J. R. (1957). A synopsis of linguistic theory, 1930-1955. In J.R. Firth (Ed.), *Studies in linguistic analysis* (pp. 1-31). Basil Blackwell.

McCauley, S. M., & Christiansen, M. H. (2019). Language learning as language use: A cross-linguistic model of child language development. *Psychological Review*, *126*(1), 1–51. <https://doi.org/10.1037/rev0000126>

Fenson, L., Bates, E., Dale, P. S., Marchman, V. A., Reznick, J. S., & Thal, D. J. (2007). MacArthur-Bates communicative development inventories (2nd ed.). Brookes.

Frank, M. C., Braginsky, M., Yurovsky, D., & Marchman, V. A. (2017). Wordbank: An open repository for developmental vocabulary data. *Journal of Child Language*, *44*(3), 677–694. <https://doi.org/10.1017/S0305000916000209>

Chang, T. A., & Bergen, B. K. (2022). Word acquisition in neural language models. *Transactions of the Association for Computational Linguistics*, 10, 1–16. <https://doi.org/10.1162/tacl_a_00444>.

Jusczyk, P. W., Cutler, A., & Redanz, N. J. (1993). Infants' preference for the predominant stress patterns of English words. *Child development*, *64*(3), 675–687.

Perfors, A., Regier, T., & Tenenbaum, J. B. (2006). Poverty of the stimulus? A rational approach. *Proceedings of the Annual Meeting of the Cognitive Science Society*, 28. <https://escholarship.org/uc/item/2qk5c3f6>

Brent, M. R. (1999). An efficient, probabilistically sound algorithm for segmentation and word discovery. *Machine Learnin*g, *34*, 71-105. <https://doi.org/10.1023/A:1007541817488>

Warstadt, A., & Bowman, S. R. (2022). What artificial neural networks can tell us about human language acquisition. *arXiv*. <https://doi.org/10.48550/arXiv.2208.07998>

R.G. Alhama, R. Foushee, D. Byrne, A. Ettinger, A. Alishahi, & S. Goldin-Meadow, Using computational modeling to validate the onset of productive determiner–noun combinations in English-learning children, Proceedings National Academy of Science. U.S.A. 121 (50) e2316527121, https://doi.org/10.1073/pnas.2316527121 (2024).

Rumelhart, D. E., & McClelland, J. L. (1986). On learning the past tenses of English verbs. *Psycholinguistics: Critical Concepts in Psychology*, *4*, 216–271.

Pinker, S., & Ullman, M. T. (2002). The past-tense debate. *Cognitive Processing*, *5*, 7.

Smolensky, P. (1990). Tensor product variable binding and the representation of symbolic structures in connectionist systems. *Artificial Intelligence*, *46*(1-2), 159–216. <https://doi.org/10.1016/0004-3702(90)90007-M>

Kirov, C., & Cotterell, R. (2018). Recurrent neural networks in linguistic theory: Revisiting Pinker and Prince (1988) and the past tense debate. *Transactions of the Association for Computational Linguistics,* *6*, 651–665. <https://doi.org/10.1162/tacl_a_00247>

OpenAI. (2024). GPT-4. <https://chat.openai.com/>

Baroni, M. (2022). On the proper role of linguistically oriented deep net analysis in linguistic theorising. In S. Lappin & J. P. Bernardy (Eds.), *Algebraic structures in natural language* (pp. 1–23). CRC Press.

Piantadosi, S. T. (2023). Modern language models refute Chomsky’s approach to language. *From fieldwork to linguistic theory: A tribute to Dan Everett*, 353-414.

Pater, J. (2019). Generative linguistics and neural networks at 60: Foundation, friction, and fusion. *Language*, *95*(1), e41–e74. <https://doi.org/10.1353/lan.2019.0009>

Frank, M. C. (2023). Bridging the data gap between children and large language models. *Trends in Cognitive Sciences*, *27*(11), 990–992. <https://doi.org/10.1016/j.tics.2023.08.007>

Warstadt, A., Mueller, A., Choshen, L., Wilcox, E., Zhuang, C., Ciro, J., Mosquera, R., Paranjabe, B., Williams, A., Linzen, T., & Cotterell, R. (2023). Findings of the BabyLM challenge: Sample-efficient pretraining on developmentally plausible corpora. In A. Warstadt, A. Mueller, L. Choshen, E. Wilcox, C. Zhuang, J. Ciro, R. Mosquera, B. Paranjabe, A. Williams, T. Linzen, & R. Cotterell (Eds.), *Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning* (pp. 1-34). Association for Computer Linguistics. <https://doi.org/10.18653/v1/2023.conll-babylm.1>