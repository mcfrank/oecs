---
title: Hidden Markov Models
slug: bq8p3lmb
date: '2025-10-10'
doi: 10.21428/e2759450.528dddc3
authors:
- Ingmar Visser
---

Hidden Markov models are a class of statistical model used to characterize time series and longitudinal data. When applied to longitudinal data, the model is also known as the latent Markov model. Hidden Markov models are very versatile models and have a wide range of applications. The model is appropriate when the underlying process is assumed to be discrete, and measurements are taken at discrete (equally spaced) points in time. In cognitive science, the model is primarily applied to data on learning and cognitive development as well as to psychophysiological data.

# History

Baum and Petrie laid the statistical foundations of hidden Markov models (HMMs) in the 1960s. In their article, (Baum and Petrie (1966)) derived the main equations necessary to efficiently compute the likelihood for these models (informally, the probability of the data under the model as a function of the parameters) as well as outlining methods for parameter estimation. Note that, at the time, the models were not called HMMs but referred to as *probabilistic functions of Markov chains*. The groundwork for latent Markov models was done by Wiggins around the same time, presenting models for the analysis of longitudinal panel data (see (Wiggins, 1973)).

Early applications of time series analysis with HMMs were developed in engineering and economics. A key paper in the engineering literature is (Rabiner (1989)). In this work, Rabiner applied the HMM to the problem of speech recognition; a continuous stream of speech data needs to be parsed into discrete segments—words. In economic time series, HMMs have been (and continue to be) applied to characterize and predict different phases of the economy. For example, so-called “bear” and “bull” markets (with average stock prices going up or down) on the stock exchange are modeled by (Kim (1994)). In the context of economics, these models are often referred to as regime-switching models.

The latent Markov model (LMM) for longitudinal data was popularized in the social sciences by Langeheine and Van de Pol in the 1980s and 1990s (e.g., (Langeheine & Van de Pol, 1990)). The aim was to characterize groups of people and societal change. Applications in learning and developmental psychology are first presented in (Visser et al. (2002)) and (Schmittmann et al. (2006)). In these and later applications, the discrete states of the HMM or LMM are seen as cognitive states or strategies that people use to answer items or solve problems in (experimental) psychology tasks.

# Core concepts

Two main assumptions characterize HMMs. First, the underlying process of interest is discrete, meaning that there are only a finite number of discrete states that the process can be in. Second, the evolution of the process (or development) is Markovian, meaning that the current state only depends on the previous state—and not on earlier states. In cognitive science, the primary use of HMMs and LMMs is in the areas of learning and cognitive development and in the area of psychophysiological data. HMMs capture sudden changes in a system and are therefore very suitable for analyzing *phase transitions* in complex systems [see [Complex Dynamical Systems](/articles/00hsw4x2)].

## *HMMs and LMMs in learning and development*

The theoretical perspective of stages in developmental psychology has been very influential ((Inhelder & Piaget, 1958)). In this framework, cognitive development proceeds through several discrete stages, which cannot be directly observed [see [Cognitive Development](/articles/zw60p83x)]. Such stages are visible in typical Piagetian tasks such as the conservation of liquid task and the balance scale task. When children engage in such tasks repeatedly, a developmental sequence may be observed in which they switch from one strategy to the next. In the balance scale task, a typical switch concerns including the distance dimension instead of only considering the number of weights. In such situations, the LMM is an appropriate model for the data and can help detect the switches the children go through ((Jansen et al., 2007)).

Similarly, participants in experimental paradigms may switch between different strategies. A typical case in category learning is the switch between rule-based and exemplar-based categorization ((Johansen & Palmeri, 2002)), which was analyzed using HMMs ((Raijmakers et al., 2014)). Another application is the analysis of *regime switches* in response times in experimental tasks ((Van der Maas et al., 2008)), in which a discrete switch occurs between different settings of the speed–accuracy trade-off.

In all these examples, the construct of interest is assumed to be a discrete state, in particular, a cognitive state or a developmental stage, which is observed through a set of measurements that have a probabilistic or noisy relationship with the underlying state. In this context, the probabilistic relationship is also referred to as the *measurement model,* as it measures the underlying states.

## *Example: Learning in the Dimensional Change Card Sorting task*

In , data is presented from the Dimensional Change Card Sorting task ((van Bers et al., 2011)). In this task, six trials are presented in which children have to make a choice where to sort a particular card using a different rule than they used previously, for example, shifting from sorting on color to sorting on shape. The results show the performance over the six trials averaged within three age groups (93 children ranging from 3 to 5 years old were tested). Overall, performance is higher as the children are older. Moreover, as  indicates, the probability correct is not constant across trials, certainly in the 3- and 4-year-old children.

![]()

An HMM is applied to this data by assuming that participants can be in either of two cognitive states: the perseverator state (P) or the switching state (S). That is, some children switch to the new rule correctly, whereas others have trouble and persevere using the old rule, and there is some mixed behavior. Between trials, they can potentially switch between states—this is assumed to happen only occasionally, and the model is used to estimate these probabilities. In this HMM, the measurement model within the states is straightforward; it represents the probability of sorting an item correctly given the state. In the switching state, this probability is expected to be high (close to 1.0); in the perseverator state, it is expected to be low (close to zero).

A depiction of the fitted model for these data is shown in . The model has two states that are labeled P and S for perseverator and switcher, respectively. Within the nodes, the probabilities correct conditional on those states are provided, and they are, as expected, close to zero and one. The arrows between the states indicate the probabilities of transitioning between the states (from trial to trial). The probability of transitioning from P to S is 0.15; this means that there is some probability for participants to switch from being in the P state to being in the S state. The model parameters can be used to assess which participants switch at which trial (through the posterior probabilities), revealing that, in this case, some participants indeed switch (and that this mostly happens after trial one or two). The developmental interpretation is that children experience a sudden insight after one or two trials and then perform correctly from then on. Reports from children and experimenters corroborate such insights. The probability of switching from the S state to the P state is tiny and negligible in practice; the developmental interpretation is that regression does not occur in this task.

![]()

This HMM representation of the data highlights that cognitive development can progress through sudden insight and as a result of a sudden increase in performance rather than a gradual increase resulting in slight improvements over time.

## *Other applications*

More recently, HMMs have been widely applied to psychophysiological data. An early example is (Flexer et al. (2002)), who aimed to model sleep stages by analysis of electroencephalography data with HMMs. The underlying constructs of interest are the sleep stages, which cannot be directly observed. The electroencephalography signal, however, has typical patterns associated with the sleep stages that can be measured and segmented using HMMs.

Another area of application is that of eye-tracking data. Eye-movement data is typically characterized by eye-movement *events* such as fixations and saccades. To extract such events from raw eye-tracking data, HMMs can be appropriate tools by using as input the sample-to-sample velocity and acceleration as measurements. The states of the HMM correspond to the different events (see, e.g., (Houpt et al., 2018) and (Lüken et al., 2022)).

# Questions, controversies, and new developments

Conceptually, the HMM and LMM are identical; both are characterized by discrete states and probabilistic measurement of those states. In one statistical aspect they are different: although the domain of generalization for the LMM is the population of the individuals (that was measured repeatedly), the domain of generalization in the HMM is time. That is, in a time series model, the aim is to predict future time points of the evolution or development of the system.

HMMs are versatile models as shown by their wide application. An important limitation is the Markov assumption itself, that is, the assumption that the current state of a process only depends on the previous state and not on multiple earlier states. Many extensions of HMMs are concerned with alleviating this, either by adding multiple layers of states such as in the hierarchical HMM ((Fine et al., 1998)) or by adding additional dependency such as in the hidden semi-Markov model ((Bulla & Bulla, 2006)).

In recent years, Bayesian estimation has become much more common and accessible also in the application of HMMs ((Cappe et al., 2005)). As a result, more extensive measurement models are possible than is the case with the classical estimation approaches (e.g., (Kucharskỳ et al., 2021)).

# Broader connections

The concept of Markov models is ubiquitous in mathematics and plays a role in many areas of statistics. Closer to cognitive science and most relevant is the connection between Markov models and linguistic analysis.

(Chomsky (1959)) and (Miller and Chomsky (1963)) developed a framework for the characterization of formal languages. The simplest type of language (in the Chomsky hierarchy) is the *regular* language or *finite state* language. The connection with Markov models becomes clear in comparison with finite state languages; there is a finite number of discrete underlying states that is necessary to (completely) describe the (regular) language. When such a language is stochastic, the class of finite state languages corresponds very closely to the class of HMMs such that each regular language is represented by an HMM. These models have also been implemented in connectionist models of language processing [see [Recurrent Neural Networks](/articles/o3wg9y45)].

Besides playing a role in theoretical discussions in the foundations of cognitive science, finite state languages have also been used in experimental psychology in artificial grammar learning experiments. Participants are exposed to sequences formed by a regular language and then tested on their discrimination and processing of sequences from that language ((Reber, 1967); (Cleeremans & McClelland, 1991)).

# Further reading

- Kaplan, D. (2008). An overview of Markov chain methods for the study of stage-sequential developmental processes. *Developmental Psychology*, *44*(2), 457–467. [https://doi.org/10.1037/0012-1649.44.2.457](https://doi.org/10.1037/0012-1649.44.2.457)
- Visser, I., & Speekenbrink, M. (2022). *Mixture and hidden Markov models with R*. Springer.