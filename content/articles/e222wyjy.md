---
title: Compositionality
slug: e222wyjy
date: '2024-11-06'
doi: 10.21428/e2759450.494deacd
authors:
- Ryan M. Nefdt
- Christopher Potts
section_editors:
- Evan Kidd
---

Compositionality is a central concept in cognitive science, with applications in linguistic, visual, and general cognition. In studies on language, the principle says that the meaning of a syntactically complex phrase is a function of the meanings of its constituent parts and the way they are combined. One can think of this as specifying a recursive process in which lexical items (e.g., words ) have atomic meanings, and these come together to form phrasal meanings (e.g., noun phrase), which are themselves inputs to more complex phrase meanings (e.g., sentences), and so forth. The principle can be seen as offering an explanation of why and how people are able to produce and interpret novel well-formed expressions: the meanings of such expressions are taken to be fully determined by their syntax and the lexical items they contain.

# History

Precedents for the principle of compositionality can be found in the work of Gottlob Frege (Frege, 1884; Janssen, 1997). However, the modern form of the principle is due to Richard Montague. One of Montague’s central tenets was that there is “no important theoretical difference between natural languages and the artificial languages of logicians” (Montague, 1970). Logical languages are the prototypical examples of compositional systems, and so Montague’s tenet creates an expectation that natural languages will be compositional as well.

Ever since Montague’s work, the principle of compositionality has profoundly shaped linguistic theory. It is used to explain core properties of natural languages, it guides linguists in their analytical choices, and it arguably even influences the kinds of phenomena that linguists seek to explain. Versions of the principle have also been proposed for other areas of cognition, including vision, planning, and abstract reasoning.

# Core concepts

## *Intuitive compositional analysis*

At its core, the principle of compositionality is a mereological process that breaks complex structures into meaningful constituents or parts. For example, the sentence “the kitten sleeps quietly” contains two phrases, a noun phrase (the kitten) and a verb phrase (sleeps quietly), that come together to form a sentence: [[the kitten] [sleeps quietly]]. The meanings of the lexical items are stipulated. The meaning of the subject “the kitten”—call it α—is determined by a function applied to the meanings of “the” and “kitten.” The same logic applies to “sleeps quietly” to produce a meaning β, and the meaning of the entire structure is then determined by a function applied to α and β.

Compositionality itself does not dictate what the parts are. The example assumes that “sleeps” and “quietly” were atomic units, but they could be decomposed into smaller meaningful (but perhaps more abstract) parts, like “sleep” plus present tense and “quiet” plus an adverbial meaning. It is similarly possible to treat frozen expressions like “a lot of” as atomic units. The compositionality claim can thus be seen as conditional: if the syntactic analysis breaks an expression down into parts, then some compositional analysis of the parts must be correct.

## *Productivity, systematicity, and infinity*

Theoretical arguments for compositionality have generally involved three distinct properties: productivity, infinity, and systematicity.

The argument for productivity relies on the fact that humans can produce countless sentences with a limited lexicon and memory storage. Thus, semantic theory needs to explain this capability in finite terms (Katz & Fodor, 1963), and compositional systems are candidates for such explanations.

The phenomenon of productivity is sometimes described in terms of human’s “infinite” capacity to use language (Chomsky et al., 2023). The sense in which this is an infinite capacity is highly idealized and depends on many assumptions about language and cognition, but the space of expressions people can use is so vast that it cannot possibly reduce to memorization, so the question of infinity can be set aside here.

Finally, a related notion to compositionality is systematicity (Fodor & Pylyshyn, 1988). This idea can be expressed in distributional terms: if (1) you know what “the kitten sleeps” means and (2) you know that “kitten” and “puppy” are related in relevant ways, then (3) you know what “the puppy sleeps” means. In a sense, 1 and 2 seem to fully determine 3. Compositionality can be seen as an explanation for this systematicity, but the observations alone do not entail compositionality (Szabó, 2000).

## *Locality*

It is a hallmark of the way linguists think about compositionality that they tend to focus on the meanings of the immediate parts of constituents (Dowty, 2007). One sees this in the “sleeping kitten” example: for the final sentence meaning, there are only the meanings α and β and not their constituent parts. To see the potential consequences of this, assume (at least for purposes of illustration) that “the kitten ate the treat” and “the treat was eaten by the kitten” are synonymous—call their shared meaning ɣ. Then no subsequent meaning operation can distinguish these two sentences. It follows, for example, that no compositional rule operating on this sentence meaning could depend on the identity of the subject of the sentence because the rule can see only ɣ. That is, because the rule can only see ɣ, it is insensitive as to whether the subject is “the kitten” or “the treat.”

# Questions, controversies, and new developments

## *Salient challenges*

There are a wide range of challenges to compositionality (Partee, 1984). One is the ubiquitous issue of ambiguity. For example, in “I saw a crane pick up a steel beam,” people tend to infer that “crane” refers to a machine rather than a bird because of the content of “pick up a steel beam.” Thus, the process of ambiguity resolution depends on the broader context [see [Psycholinguistics](/articles/y1uhdz0y)].

A second issue is that of discourse-dependent items. In a discourse like “The kitten is sleeping quietly. She had a long day,” the pronoun “she” is very likely to be interpreted as referring to the same entity as “the kitten” in the first sentence. This looks like a highly nonlocal dependency—a reader or listener cannot resolve the meaning of even the entire sentence “She had a long day” in isolation [see [Conversation](/articles/gx9ypm4x)].

In response to these challenges, semanticists have generally invoked a distinction between representations and intended meanings . For example, there are (at least) two representations of “I saw a crane pick up a steel beam,” one in which the text or sound pattern “crane” refers to birds and another in which it refers to machines. Both representations are well formed semantically, but world knowledge leads comprehenders to select one as the likely intended meaning. This pragmatic process goes beyond compositionality.

## *A constraint on theories?*

A common question is whether or not, in adopting compositionality as a requirement for theories, one is ruling out potential analyses. The answer appears to be “no,” at least for the usual range of potential formalizations of the principle (Zadrozny, 1994). Even the assumption made above about the locality of the principle is easily circumvented if the meanings involved are allowed to be suitably abstract. The proof consists in showing that by the standard definition of semantic compositionality, any semantics whatsoever can be encoded as compositional semantics. The precise details are beyond the present scope. However, caution should be applied with this (likely) formal result. Just because one *can* give a compositional treatment does not mean that one *should* give such a treatment (Kazmi & Pelletier, 1998). For example, assume that idiomatic expressions like “pull strings” (meaning “use one’s influence to get ahead”) are non-compositional, and suppose this is deliberately reflected in the semantic analysis constructed. This could be construed as a claim about how idioms work, and the fact that someone can construct an alternative analysis in which idioms work compositionally is not necessarily relevant. From this perspective, compositionality emerges as a flexible working principle and perhaps as a way to distinguish different phenomena.

## *The limits of compositionality*

It seems inevitable that there will be phenomena in language that are not compositional. Idioms are likely candidates. However, it is noteworthy that idioms are not always frozen expressions (Nunberg et al., 1994), and so they might still pose challenges for compositionality. For example, consider again the idiom “pull strings.” A variant of this is “pull legal strings,” in which the modifier “legal” seems to operate systematically on the meaning. This suggests that there are meaningful subparts of the idiom, and yet a fully compositional account seems unlikely to be feasible or accurate.

An alternative interpretation of such phenomena has prompted some cognitive linguists to adopt an entirely distinct framework eschewing the role of compositionality. Specifically, construction grammar and radical construction grammar question what they call the “building block model” of meaning, in which meaningful parts are combined to produce meaningful wholes (Croft, 2013; Goldberg, 2015). Their suggested alternative model is one in which constructions play a larger role in both syntax and semantics. Constructions are usually taken to be pairings of form and meaning such that there are “slots” for the saturation of individual constructions, as in *X takes Y for granted*. Constructions can range from frozen idiomatic phrases to more flexible and abstract (or “schematic”; Fillmore et al., 1988) rule-like patterns. If these phenomena are as ubiquitous as construction grammarians claim, then, in a reversal of fortunes, compositionality might form the periphery and semiflexible idiomatic expressions might form the core of linguistic cognition.

# Broader connections

## *Human language processing*

It is an open question how compositionality relates to human language processing outside of semantics. There are at least three distinct perspectives (Nefdt, 2020): First, a *process compositionality* in which humans actually perform computations corresponding to a compositional analysis—that is, they do something like what is in the semanticists’ idealized theories. Second, a weaker *state compositionality* in which the complex structure can in principle be analyzed in compositional terms, but no claim is made about whether humans actually do that. This may be the case for expressions like “a lot of”: a clever semanticist could find a compositional analysis, but it might seem contrived. Finally, *outcome compositionality* is where input–output behavior appears compositional, but no claim is made about compositionality. Frequently encountered words and phrases, which might be memorized, could fall into this class. For example, “better late than never” can be given a compositional analysis, but actual usage of it might have the characteristics of a memorized phrase.

## *Natural language processing*

Recent developments in natural language processing have begun to offer new perspectives on compositionality. Perhaps the most striking finding is that modern large language models [see [Large Language Models](/articles/zp5n8ivs)] seem to induce partial compositional analysis just from training on large quantities of text, using learning objectives that simply push the model to imitate those texts. In other words, these models seem, at least in some instances, to arrive at process compositional analyses, and this may explain how they are able to successfully generalize to novel expressions. This is an exciting new opportunity for interdisciplinary collaboration, as linguists and computer scientists can collaborate on assessing models using compositional phenomena and on studying the ways in which models perform highly abstract compositional analyses.

## *Compositionality beyond language and humans*

It has been suggested that the alleged failures of compositionality in language point to the compositionality of thought as the dominant interpretation of the principle in cognitive science (Fodor & Lepore, 2022). Compositional interpretations have been offered in a number of nonlinguistic domains including planning, music, and visual perception. In addition, the application of compositional analysis to general cognition opens up the possibility of applications outside of human cognition including bird-song, planning in chimpanzees, and other primate gestural systems [see [Primate Communication](/articles/suwgvzqg)]. Some of these avenues have been fruitfully explored (see Dautriche et al., 2022). However, it should be noted that many of these proposals start from the linguistic principle as their basis.

# Acknowledgments

We would like to thank Asida Majid, Evan Kidd, and Michael Frank for their advice and direction on the content of the entry. We would also like to thank Ahmad Jabbar for early input on what is useful to include for such a broad topic.

# Further reading

- Fodor, J. A., & Lepore, E. (2002). *The compositionality papers*. Oxford University Press.
- Janssen, T. M. V. (1997). Compositionality. In J. van Benthem & A. ter Meulen (Eds.), *Handbook of logic and language* (pp. 417–473). Elsevier.
- Partee, B. H. (1984). Compositionality. In F. Landman & F. Veltman (Eds.), *Varieties of formal semantics* (pp. 281–311). Foris.
- Szabó, Z. G. (2012). Compositionality. In E. N. Zalta (Ed.), *The Stanford encyclopedia of philosophy.* Stanford University. [http://plato.stanford.edu/archives/win2012/entries/compositionality/](http://plato.stanford.edu/archives/win2012/entries/compositionality/)

# References

Frege, G. (1884). *Die grundlagen der arithmetik: Eine logisch-mathematische untersuchung ueber den begriff der zahl*. Wilhelm Koebner.

Janssen, T. M. V. (1997). Compositionality. In J. van Benthem & A. ter Meulen (Eds.), *Handbook of logic and language* (pp. 417–473). Elsevier.

Montague, R. (1970). Universal grammar. *Theoria*, *36*(3), 373–398. <https://doi.org/10.1111/j.1755-2567.1970.tb00434.x>

Katz, J. J., & Fodor, J. A. (1963). The structure of semantic theory. *Language*, *39*(2), 170–210. <https://doi.org/10.2307/411200>

Chomsky, N., Seely, T. D., Berwick, R. C., Fong, S., Huybregts, M. A. C., Kitahara, H., McInnerney, A., & Sugimoto, Y. (2023). *Merge and the strong minimalist thesis*. Cambridge University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, *28*(1-2), 3–71. [https://doi.org/10.1016/0010-0277(88)90031-5](https://doi.org/10.1016/0010-0277(88)90031-5 "Persistent link using digital object identifier")

Szabó, Z. G. (2000). *Problems of compositionality.* Routledge Press.

Dowty, D. (2007). Compositionality as an empirical problem. In C. Barker & P. Jacobson (Eds.), *Direct compositionality* (pp. 23–101). Oxford University Press.

Partee, B. H. (1984). Compositionality. In F. Landman & F. Veltman (Eds.), *Varieties of formal semantics* (pp. 281–311). Foris.

Zadrozny, W. (1994). From compositional to systematic semantics. *Linguistics and Philosophy*, *17*(4), 329–342. <https://doi.org/10.1007/BF00985572>

Kazmi, A., & Pelletier, F. J. (1998). Is compositionality formally vacuous? *Linguistics and Philosophy*, *21*(6), 629–633. <https://doi.org/10.1023/A:1005388721969>

Nunberg, G., Sag, I. A., & Wasow, T. (1994). Idioms. In S. Everson (Ed.), *Language: Companions to ancient thought* (pp. 491–538). Cambridge University Press.

Croft, W. (2013). Radical construction grammar. In T. Hoffmann & G. Trousdale (Eds.), *The Oxford handbook of construction grammar* (pp. 211–232). Oxford University Press.

Goldberg, A. (2015). Compositionality. In N. Reimer (Ed.), *The Routledge handbook of semantics* (pp. 419-433). Routledge Press.

Fillmore, C., Kay, P., & O’Connor, M. (1988). Regularity and idiomaticity in grammatical constructions: The case of let alone. *Language*, *64*(3), 501–538. <https://doi.org/10.2307/414531>

Nefdt, R. M. (2020). A puzzle concerning compositionality in machines. *Minds and Machines*, *30*(1), 47–75. <https://doi.org/10.1007/s11023-020-09519-6>

Fodor, J. A., & Lepore, E. (2002). *The compositionality papers*. Oxford University Press.

Dautriche, I., Buccola, B., Berthet, M., Fagot, J., & Chemla, E. (2022). Evidence for compositionality in baboons (*Papio papio*) through the test case of negation. *Nature Scientific Reports*, *12*, 19181. <https://doi.org/10.1038/s41598-022-21143-1>