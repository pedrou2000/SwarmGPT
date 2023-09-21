# Metadata:

- Title: Artificial Intelligence: A Modern Approach
- Authors: Stuart J. Russell & Peter Norvig

# TOC Content:

# Root



## Cover Page



cover








## Title




Artificial Intelligence: A Modern Approach














Artificial Intelligence
A Modern Approach
Fourth Edition
Global Edition
Stuart J. Russell and Peter Norvig
Contributing writers:
Ming-Wei Chang
Jacob Devlin
Anca Dragan
David Forsyth
Ian Goodfellow
Jitendra M. Malik
Vikash Mansinghka
Judea Pearl
Michael Wooldridge


...

## Copyright




Artificial Intelligence: A Modern Approach














Pearson Education Limited
KAO Two
KAO Park
Hockham Way
Harlow
CM17 9SR
United Kingdom
and Associated Companies throughout the world
Visit us on the World Wide Web at: www.pearsonglobaleditions.com
©Pearson Education Limited, 2022
The rights of Stuart Russell and Peter Norvig to be identified as the authors of this work have been asserted by them in accordance with the Copyright, Designs and Patents Act 1988.
Authorized adaptation from the United States edition, entitled Artificial Intelligence: A Modern Approach, 4th Edition, ISBN 978-0-13-461099-3 byStuart J. Russell and Peter Norvig, published by Pearson Education © 2021. 
All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without either the prior written permission of the publisher or a license permitting restricted copying...

## Dedication




Artificial Intelligence: A Modern Approach














For Loy, Gordon, Lucy, George, and Isaac — S.J.R.
For Kris, Isabella, and Juliet — P.N.

...

## Preface




Artificial Intelligence: A Modern Approach














Preface
Artificial Intelligence (AI) is a big field, and this is a big book. We have tried to explore the full breadth of the field, which encompasses logic, probability, and continuous mathematics; perception, reasoning, learning, and action; fairness, trust, social good, and safety; and applications that range from microelectronic devices to robotic planetary explorers to online services with billions of users.
The subtitle of this book is “A Modern Approach.” That means we have chosen to tell the story from a current perspective. We synthesize what is now known into a common framework, recasting early work using the ideas and terminology that are prevalent today. We apologize to those whose subfields are, as a result, less recognizable.
New to this edition
This edition reflects the changes in AI since the last edition in 2010:

•We focus more on machine learning rather than hand-crafted knowledge engineering, due to the inc...

## About the Authors




Artificial Intelligence: A Modern Approach














About the Authors
 Stuart Russell was born in 1962 in Portsmouth, England. He received his B.A. with first- class honours in physics from Oxford University in 1982, and his Ph.D. in computer science from Stanford in 1986. He then joined the faculty of the University of California at Berkeley, where he is a professor and former chair of computer science, director of the Center for Human-Compatible AI, and holder of the Smith-Zadeh Chair in Engineering. In 1990, he received the Presidential Young Investigator Award of the National Science Foundation, and in 1995 he was cowinner of the Computers and Thought Award. He is a Fellow of the American Association for Artificial Intelligence, the Association for Computing Machinery, and the American Association for the Advancement of Science, an Honorary Fellow of Wadham College, Oxford, and an Andrew Carnegie Fellow. He held the Chaire Blaise Pascal in Paris from 2012 to 2014. He has pu...

## Contents




Artificial Intelligence: A Modern Approach














Contents
IArtificial Intelligence
1Introduction
1.1What Is AI?
1.2The Foundations of Artificial Intelligence
1.3The History of Artificial Intelligence
1.4The State of the Art
1.5Risks and Benefits of AI
Summary
Bibliographical and Historical Notes
2Intelligent Agents
2.1Agents and Environments
2.2Good Behavior: The Concept of Rationality
2.3The Nature of Environments
2.4The Structure of Agents
Summary
Bibliographical and Historical Notes
IIProblem-solving 
3Solving Problems by Searching
3.1Problem-Solving Agents
3.2Example Problems
3.3Search Algorithms
3.4Uninformed Search Strategies
3.5Informed (Heuristic) Search Strategies
3.6Heuristic Functions
Summary
Bibliographical and Historical Notes
4Search in Complex Environments
4.1Local Search and Optimization Problems
4.2Local Search in Continuous Spaces
4.3Search with Nondeterministic Actions
4.4Search in Partially Observable Environments
4.5Online Search Agents and Unknown Envir...

## I Artificial Intelligence



### 1 Introduction



#### 1.1 What Is AI?




Artificial Intelligence: A Modern Approach














1.1What Is AI?
We have claimed that AI is interesting, but we have not said what it is. Historically, researchers have pursued several different versions of AI. Some have defined intelligence in terms of fidelity to human performance, while others prefer an abstract, formal definition of intelligence called rationality—loosely speaking, doing the “right thing.” The subject matter itself also varies: some consider intelligence to be a property of internal thought processes and reasoning, while others focus on intelligent behavior, an external characterization.1

From these two dimensions—human vs. rational2 and thought vs. behavior—there are four possible combinations, and there have been adherents and research programs for all four. The methods used are necessarily different: the pursuit of human-like intelligence must be in part an empirical science related to psychology, involving observations and hypotheses about actual hum...

#### 1.2 The Foundations of Artificial Intelligence




Artificial Intelligence: A Modern Approach














1.2The Foundations of Artificial Intelligence
In this section, we provide a brief history of the disciplines that contributed ideas, viewpoints, and techniques to AI. Like any history, this one concentrates on a small number of people, events, and ideas and ignores others that also were important. We organize the history around a series of questions. We certainly would not wish to give the impression that these questions are the only ones the disciplines address or that the disciplines have all been working toward AI as their ultimate fruition.
1.2.1Philosophy

•Can formal rules be used to draw valid conclusions?
•How does the mind arise from a physical brain?
•Where does knowledge come from?
•How does knowledge lead to action?

Aristotle (384–322 BCE) was the first to formulate a precise set of laws governing the rational part of the mind. He developed an informal system of syllogisms for proper reasoning, which in principle ...

#### 1.3 The History of Artificial Intelligence




Artificial Intelligence: A Modern Approach














1.3The History of Artificial Intelligence
One quick way to summarize the milestones in AI history is to list the Turing Award winners: Marvin Minsky (1969) and John McCarthy (1971) for defining the foundations of the field based on representation and reasoning; Allen Newell and Herbert Simon (1975) for symbolic models of problem solving and human cognition; Ed Feigenbaum and Raj Reddy (1994) for developing expert systems that encode human knowledge to solve real-world problems; Judea Pearl (2011) for developing probabilistic reasoning techniques that deal with uncertainty in a principled manner; and finally Yoshua Bengio, Geoffrey Hinton, and Yann LeCun (2019) for making “deep learning” (multilayer neural networks) a critical part of modern computing. The rest of this section goes into more detail on each phase of AI history.
1.3.1The inception of artificial intelligence (1943–1956)
The first work that is now generally recogni...

#### 1.4 The State of the Art




Artificial Intelligence: A Modern Approach














1.4 The State of the Art
Stanford University’s One Hundred Year Study on AI (also known as AI100) convenes panels of experts to provide reports on the state of the art in AI. Their 2016 report (Stone et al., 2016; Grosz and Stone, 2018) concludes that “Substantial increases in the future uses of AI applications, including more self-driving cars, healthcare diagnostics and targeted treatment, and physical assistance for elder care can be expected” and that “Society is now at a crucial juncture in determining how to deploy AI-based technologies in ways that promote rather than hinder democratic values such as freedom, equality, and transparency.” AI100 also produces an AI Index at aiindex.org to help track progress. Some highlights from the 2018 and 2019 reports (comparing to a year 2000 baseline unless otherwise stated):


•Publications: AI papers increased 20-fold between 2010 and 2019 to about 20,000 a year. The most popular ...

#### 1.5 Risks and Benefits of AI




Artificial Intelligence: A Modern Approach














1.5 Risks and Benefits of AI
Francis Bacon, a philosopher credited with creating the scientific method, noted in The Wisdom of the Ancients (1609) that the “mechanical arts are of ambiguous use, serving as well for hurt as for remedy.” As AI plays an increasingly important role in the economic, social, scientific, medical, financial, and military spheres, we would do well to consider the hurts and remedies—in modern parlance, the risks and benefits—that it can bring. The topics summarized here are covered in greater depth in Chapters 28 and 29.
To begin with the benefits: put simply, our entire civilization is the product of our human intelligence. If we have access to substantially greater machine intelligence, the ceiling on our ambitions is raised substantially. The potential for AI and robotics to free humanity from menial repetitive work and to dramatically increase the production of goods and services could presage an er...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter defines AI and establishes the cultural background against which it has developed. Some of the important points are as follows:

•Different people approach AI with different goals in mind. Two important questions to ask are: Are you concerned with thinking, or behavior? Do you want to model humans, or try to achieve the optimal results?
•According to what we have called the standard model, AI is concerned mainly with rational action. An ideal intelligent agent takes the best possible action in a situation. We study the problem of building agents that are intelligent in this sense.
•Two refinements to this simple idea are needed: first, the ability of any agent, human or otherwise, to choose rational actions is limited by the computational intractability of doing so; second, the concept of a machine that pursues a definite objective needs to be replaced with that of a machine pursuing objectives to benefit ...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
A comprehensive history of AI is given by Nils Nilsson (2009), one of the early pioneers of the field. Pedro Domingos (2015) and Melanie Mitchell (2019) give overviews of machine learning for a general audience, and Kai-Fu Lee (2018) describes the race for international leadership in AI. Martin Ford (2018) interviews 23 leading AI researchers.
The main professional societies for AI are the Association for the Advancement of Artificial Intelligence (AAAI), the ACM Special Interest Group in Artificial Intelligence (SIGAI, formerly SIGART), the European Association for AI, and the Society for Artificial Intelligence and Simulation of Behaviour (AISB). The Partnership on AI brings together many commercial and nonprofit organizations concerned with the ethical and social impacts of AI. AAAI’s AI Magazine contains many topical and tutorial articles, and its Web site, aaai.org, contains news, tuto...

### 2 Intelligent Agents



#### 2.1 Agents and Environments




Artificial Intelligence: A Modern Approach














2.1Agents and Environments
An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators. This simple idea is illustrated in Figure 2.1. A human agent has eyes, ears, and other organs for sensors and hands, legs, vocal tract, and so on for actuators. A robotic agent might have cameras and infrared range finders for sensors and various motors for actuators. A software agent receives file contents, network packets, and human input (keyboard/mouse/touchscreen/voice) as sensory inputs and acts on the environment by writing files, sending network packets, and displaying information or generating sounds. The environment could be everything—the entire universe! In practice it is just that part of the universe whose state we care about when designing this agent—the part that affects what the agent perceives and that is affected by the agent’s actions.






Des...

#### 2.2 Good Behavior: The Concept of Rationality




Artificial Intelligence: A Modern Approach














2.2Good Behavior: The Concept of Rationality
A rational agent is one that does the right thing. Obviously, doing the right thing is better than doing the wrong thing, but what does it mean to do the right thing?

2.2.1Performance measures
Moral philosophy has developed several different notions of the “right thing,” but AI has generally stuck to one notion called consequentialism: we evaluate an agent’s behavior by its consequences. When an agent is plunked down in an environment, it generates a sequence of actions according to the percepts it receives. This sequence of actions causes the environment to go through a sequence of states. If the sequence is desirable, then the agent has performed well. This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states.


Humans have desires and preferences of their own, so the notion of rationality as applied to humans has to ...

#### 2.3 The Nature of Environments




Artificial Intelligence: A Modern Approach














2.3The Nature of Environments
Now that we have a definition of rationality, we are almost ready to think about building rational agents. First, however, we must think about task environments, which are essentially the “problems” to which rational agents are the “solutions.” We begin by showing how to specify a task environment, illustrating the process with a number of examples. We then show that task environments come in a variety of flavors. The nature of the task environment directly affects the appropriate design for the agent program.

2.3.1Specifying the task environment
In our discussion of the rationality of the simple vacuum-cleaner agent, we had to specify the performance measure, the environment, and the agent’s actuators and sensors. We group all these under the heading of the task environment. For the acronymically minded, we call this the PEAS (Performance, Environment, Actuators, Sensors) description. In designi...

#### 2.4 The Structure of Agents




Artificial Intelligence: A Modern Approach














2.4The Structure of Agents
So far we have talked about agents by describing behavior—the action that is performed after any given sequence of percepts. Now we must bite the bullet and talk about how the insides work. The job of AI is to design an agent program that implements the agent function—the mapping from percepts to actions. We assume this program will run on some sort of computing device with physical sensors and actuators—we call this the agent architecture:

agent = architecture + program.



Obviously, the program we choose has to be one that is appropriate for the architecture. If the program is going to recommend actions like Walk, the architecture had better have legs. The architecture might be just an ordinary PC, or it might be a robotic car with several onboard computers, cameras, and other sensors. In general, the architecture makes the percepts from the sensors available to the program, runs the program, and...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has been something of a whirlwind tour of AI, which we have conceived of as the science of agent design. The major points to recall are as follows:

•An agent is something that perceives and acts in an environment. The agent function for an agent specifies the action taken by the agent in response to any percept sequence.
•The performance measure evaluates the behavior of the agent in an environment. A rational agent acts so as to maximize the expected value of the performance measure, given the percept sequence it has seen so far.
•A task environment specification includes the performance measure, the external environment, the actuators, and the sensors. In designing an agent, the first step must always be to specify the task environment as fully as possible.
•Task environments vary along several significant dimensions. They can be fully or partially observable, single-agent or multiagent, deterministic o...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The central role of action in intelligence—the notion of practical reasoning—goes back at least as far as Aristotle’s Nicomachean Ethics. Practical reasoning was also the subject of McCarthy’s influential paper “Programs with Common Sense” (1958). The fields of robotics and control theory are, by their very nature, concerned principally with physical agents. The concept of a controller in control theory is identical to that of an agent in AI. Perhaps surprisingly, AI has concentrated for most of its history on isolated components of agents—question-answering systems, theorem-provers, vision systems, and so on—rather than on whole agents. The discussion of agents in the text by Genesereth and Nilsson (1987) was an influential exception. The whole-agent view is now widely accepted and is a central theme in recent texts (Padgham and Winikoff, 2004; Jones, 2007; Poole and Mackworth, 2017).

Cha...

## II Problem-solving



### 3 Solving Problems by Searching



#### 3.1 Problem-Solving Agents




Artificial Intelligence: A Modern Approach














3.1Problem-Solving Agents
Imagine an agent enjoying a touring vacation in Romania. The agent wants to take in the sights, improve its Romanian, enjoy the nightlife, avoid hangovers, and so on. The decision problem is a complex one. Now, suppose the agent is currently in the city of Arad and has a nonrefundable ticket to fly out of Bucharest the following day. The agent observes street signs and sees that there are three roads leading out of Arad: one toward Sibiu, one to Timisoara, and one to Zerind. None of these are the goal, so unless the agent is familiar with the geography of Romania, it will not know which road to follow.1
If the agent has no additional information—that is, if the environment is unknown—then the agent can do no better than to execute one of the actions at random. This sad situation is discussed in Chapter 4. In this chapter, we will assume our agents always have access to information about the world, suc...

#### 3.2 Example Problems




Artificial Intelligence: A Modern Approach














3.2Example Problems
The problem-solving approach has been applied to a vast array of task environments. We list some of the best known here, distinguishing between standardized and real-world problems. A standardized problem is intended to illustrate or exercise various problem-solving methods. It can be given a concise, exact description and hence is suitable as a benchmark for researchers to compare the performance of algorithms. A real-world problem, such as robot navigation, is one whose solutions people actually use, and whose formulation is idiosyncratic, not standardized, because, for example, each robot has different sensors that produce different data.


3.2.1Standardized problems
A grid world problem is a two-dimensional rectangular array of square cells in which agents can move from cell to cell. Typically the agent can move to any obstacle-free adjacent cell—horizontally or vertically and in some problems diagonall...

#### 3.3 Search Algorithms




Artificial Intelligence: A Modern Approach














3.3Search Algorithms
A search algorithm takes a search problem as input and returns a solution, or an indication of failure. In this chapter we consider algorithms that superimpose a search tree over the state-space graph, forming various paths from the initial state, trying to find a path that reaches a goal state. Each node in the search tree corresponds to a state in the state space and the edges in the search tree correspond to actions. The root of the tree corresponds to the initial state of the problem.


It is important to understand the distinction between the state space and the search tree. The state space describes the (possibly infinite) set of states in the world, and the actions that allow transitions from one state to another. The search tree describes paths between these states, reaching towards the goal. The search tree may have multiple paths to (and thus multiple nodes for) any given state, but each node in ...

#### 3.4 Uninformed Search Strategies




Artificial Intelligence: A Modern Approach














3.4Uninformed Search Strategies
An uninformed search algorithm is given no clue about how close a state is to the goal(s). For example, consider our agent in Arad with the goal of reaching Bucharest. An uninformed agent with no knowledge of Romanian geography has no clue whether going to Zerind or Sibiu is a better first step. In contrast, an informed agent (Section 3.5) who knows the location of each city knows that Sibiu is much closer to Bucharest and thus more likely to be on the shortest path.
3.4.1Breadth-first search
When all actions have the same cost, an appropriate strategy is breadth-first search, in which the root node is expanded first, then all the successors of the root node are expanded next, then their successors, and so on. This is a systematic search strategy that is therefore complete even on infinite state spaces. We could implement breadth-first search as a call to BEST-FIRST-SEARCH where the evaluation f...

#### 3.5 Informed (Heuristic) Search Strategies




Artificial Intelligence: A Modern Approach














3.5Informed (Heuristic) Search Strategies
This section shows how an informed search strategy—one that uses domain-specific hints about the location of goals—can find solutions more efficiently than an uninformed strategy. The hints come in the form of a heuristic function, denoted h(n):10

h(n) = estimated cost of the cheapest path from the state at node n to a goal state.



For example, in route-finding problems, we can estimate the distance from the current state to a goal by computing the straight-line distance on the map between the two points. We study heuristics and where they come from in more detail in Section 3.6.
3.5.1Greedy best-first search
Greedy best-first search is a form of best-first search that expands first the node with the lowest h(n) value—the node that appears to be closest to the goal—on the grounds that this is likely to lead to a solution quickly. So the evaluation function f(n)= h(n).

Let us see ho...

#### 3.6 Heuristic Functions




Artificial Intelligence: A Modern Approach














3.6Heuristic Functions
In this section, we look at how the accuracy of a heuristic affects search performance, and also consider how heuristics can be invented. As our main example we’ll return to the 8-puzzle. As mentioned in Section 3.2, the object of the puzzle is to slide the tiles horizontally or vertically into the empty space until the configuration matches the goal configuration (Figure 3.25).






Description

A square labeled Start state has three rows and three columns. Row 1: Column 1, 7. Column 2, 2. Column 3, 4. Row 2: Column 1, 5. Column 2, blank. Column 3, 6. Row 3: Column 1, 8. Column 2, 3. Column 3, 1. Another square labeled Goal state has three rows and three columns. Row 1: Column 1, blank. Column 2, 1. Column 3, 2. Row 2: Column 1, 3. Column 2, 4. Column 3, 5. Row 3: Column 1, 6. Column 2, 7. Column 3, 8. 

×
Figure 3.25 A typical instance of the 8-puzzle. The shortest solution is 26 actions long.
There a...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has introduced search algorithms that an agent can use to select action sequences in a wide variety of environments—as long as they are episodic, single-agent, fully observable, deterministic, static, discrete, and completely known. There are tradeoffs to be made between the amount of time the search takes, the amount of memory available, and the quality of the solution. We can be more efficient if we have domain-dependent knowledge in the form of a heuristic function that estimates how far a given state is from the goal, or if we precompute partial solutions involving patterns or landmarks.

•Before an agent can start searching, a well-defined problem must be formulated.
•A problem consists of five parts: the initial state, a set of actions, a transition model describing the results of those actions, a set of goal states, and an action cost function.
•The environment of the problem is represented by a sta...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The topic of state-space search originated in the early years of AI. Newell and Simon’s work on the Logic Theorist (1957) and GPS (1961) led to the establishment of search algorithms as the primary tool for 1960s AI researchers and to the establishment of problem solving as the canonical AI task. Work in operations research by Richard Bellman (1957) showed the importance of additive path costs in simplifying optimization algorithms. The text by Nils Nilsson (1971) established the area on a solid theoretical footing.
The 8-puzzle is a smaller cousin of the 15-puzzle, whose history is recounted at length by Slocum and Sonneveld (2006). In 1880, the 15-puzzle attracted broad attention from the public and mathematicians (Johnson and Story, 1879; Tait, 1880). The editors of the American Journal of Mathematics stated, “The ‘15’ puzzle for the last few weeks has been prominently before the America...

### 4 Search in Complex Environments



#### 4.1 Local Search and Optimization Problems




Artificial Intelligence: A Modern Approach














4.1Local Search and Optimization Problems
In the search problems of Chapter 3 we wanted to find paths through the search space, such as a path from Arad to Bucharest. But sometimes we care only about the final state, not the path to get there. For example, in the 8-queens problem (Figure 4.3), we care only about finding a valid final configuration of 8 queens (because if you know the configuration, it is trivial to reconstruct the steps that created it). This is also true for many important applications such as integrated-circuit design, factory floor layout, job shop scheduling, automatic programming, telecommunications network optimization, crop planning, and portfolio management.
Local search algorithms operate by searching from a start state to neighboring states, without keeping track of the paths, nor the set of states that have been reached. That means they are not systematic—they might never explore a portion of the se...

#### 4.2 Local Search in Continuous Spaces




Artificial Intelligence: A Modern Approach














4.2Local Search in Continuous Spaces
In Chapter 2, we explained the distinction between discrete and continuous environments, pointing out that most real-world environments are continuous. A continuous action space has an infinite branching factor, and thus can’t be handled by most of the algorithms we have covered so far (with the exception of first-choice hill climbing and simulated annealing).
This section provides a very brief introduction to some local search techniques for continuous spaces. The literature on this topic is vast; many of the basic techniques originated in the 17th century, after the development of calculus by Newton and Leibniz.2 We find uses for these techniques in several places in this book, including the chapters on learning, vision, and robotics.
We begin with an example. Suppose we want to place three new airports anywhere in Romania, such that the sum of squared straight-line distances from each ci...

#### 4.3 Search with Nondeterministic Actions




Artificial Intelligence: A Modern Approach














4.3Search with Nondeterministic Actions
In Chapter 3, we assumed a fully observable, deterministic, known environment. Therefore, an agent can observe the initial state, calculate a sequence of actions that reach the goal, and execute the actions with its “eyes closed,” never having to use its percepts.
When the environment is partially observable, however, the agent doesn’t know for sure what state it is in; and when the environment is nondeterministic, the agent doesn’t know what state it transitions to after taking an action. That means that rather than thinking “I’m in state s1 and if I do action a I’ll end up in state s2,” an agent will now be thinking “I’m either in state s1 or s3, and if I do action a I’ll end up in state s2, s4 or s5.” We call a set of physical states that the agent believes are possible a belief state.

In partially observable and nondeterministic environments, the solution to a problem is no longer a...

#### 4.4 Search in Partially Observable Environments




Artificial Intelligence: A Modern Approach














4.4Search in Partially Observable Environments
We now turn to the problem of partial observability, where the agent’s percepts are not enough to pin down the exact state. That means that some of the agent’s actions will be aimed at reducing uncertainty about the current state.
4.4.1Searching with no observation
When the agent’s percepts provide no information at all, we have what is called a sensorless problem (or a conformant problem). At first, you might think the sensorless agent has no hope of solving a problem if it has no idea what state it starts in, but sensorless solutions are surprisingly common and useful, primarily because they don’t rely on sensors working properly. In manufacturing systems, for example, many ingenious methods have been developed for orienting parts correctly from an unknown initial position by using a sequence of actions with no sensing at all. Sometimes a sensorless plan is better even when a co...

#### 4.5 Online Search Agents and Unknown Environments




Artificial Intelligence: A Modern Approach














4.5Online Search Agents and Unknown Environments
So far we have concentrated on agents that use offline search algorithms. They compute a complete solution before taking their first action. In contrast, an online search8 agent interleaves computation and action: first it takes an action, then it observes the environment and computes the next action. Online search is a good idea in dynamic or semi-dynamic environments, where there is a penalty for sitting around and computing too long. Online search is also helpful in nondeterministic domains because it allows the agent to focus its computational efforts on the contingencies that actually arise rather than those that might happen but probably won’t.


Of course, there is a tradeoff: the more an agent plans ahead, the less often it will find itself up the creek without a paddle. In unknown environments, where the agent does not know what states exist or what its actions do, the ...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has examined search algorithms for problems in partially observable, nondeterministic, unknown, and continuous environments.

•Local search methods such as hill climbing keep only a small number of states in memory. They have been applied to optimization problems, where the idea is to find a high-scoring state, without worrying about the path to the state. Several stochastic local search algorithms have been developed, including simulated annealing, which returns optimal solutions when given an appropriate cooling schedule.
•Many local search methods apply also to problems in continuous spaces. Linear programming and convex optimization problems obey certain restrictions on the shape of the state space and the nature of the objective function, and admit polynomial-time algorithms that are often extremely efficient in practice. For some mathematically well-formed problems, we can find the maximum using calc...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Local search techniques have a long history in mathematics and computer science. Indeed, the Newton–Raphson method (Newton, 1671; Raphson, 1690) can be seen as a very efficient local search method for continuous spaces in which gradient information is available. Brent (1973) is a classic reference for optimization algorithms that do not require such information. Beam search, which we have presented as a local search algorithm, originated as a bounded-width variant of dynamic programming for speech recognition in the HARPY system (Lowerre, 1976). A related algorithm is analyzed in depth by Pearl (1984, Ch. 5).
The topic of local search was reinvigorated in the early 1990s by surprisingly good results for large constraint-satisfaction problems such as n-queens (Minton et al., 1992) and Boolean satisfiability (Selman et al., 1992) and by the incorporation of randomness, multiple simultaneous s...

### 5 Constraint Satisfaction Problems



#### 5.1 Defining Constraint Satisfaction Problems




Artificial Intelligence: A Modern Approach














5.1Defining Constraint Satisfaction Problems
A constraint satisfaction problem consists of three components, X, D, and C:

X is a set of variables, (X1,..., Xn}.
D is a set of domains, {D1,..., Dn}, one for each variable.
C is a set of constraints that specify allowable combinations of values.

A domain, Di, consists of a set of allowable values, {v1,..., vk}, for variable Xi. For example, a Boolean variable would have the domain {true, false}. Different variables can have different domains of different sizes. Each constraint Cj consists of a pair 〈scope, rel〉, where scope is a tuple of variables that participate in the constraint and rel is a relation that defines the values that those variables can take on. A relation can be represented as an explicit set of all tuples of values that satisfy the constraint, or as a function that can compute whether a tuple is a member of the relation. For example, if X1 and X2 both have the ...

#### 5.2 Constraint Propagation: Inference in CSPs




Artificial Intelligence: A Modern Approach














5.2Constraint Propagation: Inference in CSPs
An atomic state-space search algorithm makes progress in only one way: by expanding a node to visit the successors. A CSP algorithm has choices. It can generate successors by choosing a new variable assignment, or it can do a specific type of inference called constraint propagation: using the constraints to reduce the number of legal values for a variable, which in turn can reduce the legal values for another variable, and so on. The idea is that this will leave fewer choices to consider when we make the next choice of a variable assignment. Constraint propagation may be intertwined with search, or it may be done as a preprocessing step, before search starts. Sometimes this preprocessing can solve the whole problem, so no search is required at all.

The key idea is local consistency. If we treat each variable as a node in a graph (see Figure 5.1(b)) and each binary constraint as an ...

#### 5.3 Backtracking Search for CSPs




Artificial Intelligence: A Modern Approach














5.3Backtracking Search for CSPs
Sometimes we can finish the constraint propagation process and still have variables with multiple possible values. In that case we have to search for a solution. In this section we cover backtracking search algorithms that work on partial assignments; in the next section we look at local search algorithms over complete assignments.
Consider how a standard depth-limited search (from Chapter 3) could solve CSPs. A state would be a partial assignment, and an action would extend the assignment, adding, say, NSW = red or SA = blue for the Australia map-coloring problem. For a CSP with n variables of domain size d we would end up with a search tree where all the complete assignments (and thus all the solutions) are leaf nodes at depth n. But notice that the branching factor at the top level would be nd because any of d values can be assigned to any of n variables. At the next level, the branching fact...

#### 5.4 Local Search for CSPs




Artificial Intelligence: A Modern Approach














5.4Local Search for CSPs
Local search algorithms (see Section 4.1) turn out to be very effective in solving many CSPs. They use a complete-state formulation (as introduced in Section 4.1.1) where each state assigns a value to every variable, and the search changes the value of one variable at a time. As an example, we’ll use the 8-queens problem, as defined as a CSP on page 167. In Figure 5.8 we start on the left with a complete assignment to the 8 variables; typically this will violate several constraints. We then randomly choose a conflicted variable, which turns out to be Q8, the rightmost column. We’d like to change the value to something that brings us closer to a solution; the most obvious approach is to select the value that results in the minimum number of conflicts with other variables—the min-conflicts heuristic.






Description

Two dice show the numbers 6 and 5. The columns in the top row are numbered from 1 to 1...

#### 5.5 The Structure of Problems




Artificial Intelligence: A Modern Approach














5.5The Structure of Problems
In this section, we examine ways in which the structure of the problem, as represented by the constraint graph, can be used to find solutions quickly. Most of the approaches here also apply to other problems besides CSPs, such as probabilistic reasoning.
The only way we can possibly hope to deal with the vast real world is to decompose it into subproblems. Looking again at the constraint graph for Australia (Figure 5.1(b), repeated as Figure 5.12(a)), one fact stands out: Tasmania is not connected to the mainland.3 Intuitively, it is obvious that coloring Tasmania and coloring the mainland are independent subproblems—any solution for the mainland combined with any solution for Tasmania yields a solution for the whole map.

Independence can be ascertained simply by finding connected components of the constraint graph. Each component corresponds to a subproblem CSPi. If assignment Si is a solution of...

#### Summary




Artificial Intelligence: A Modern Approach














Summary

• Constraint satisfaction problems (CSPs) represent a state with a set of variable/value pairs and represent the conditions for a solution by a set of constraints on the variables. Many important real-world problems can be described as CSPs.
•A number of inference techniques use the constraints to rule out certain variable assignments. These include node, arc, path, and k-consistency.
•Backtracking search, a form of depth-first search, is commonly used for solving CSPs. Inference can be interwoven with search.
•The minimum-remaining-values and degree heuristics are domain-independent methods for deciding which variable to choose next in a backtracking search. The least-constraining-value heuristic helps in deciding which value to try first for a given variable. Backtracking occurs when no legal assignment can be found for a variable. Conflict-directed backjumping backtracks directly to the source of the problem. Const...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The Greek mathematician Diophantus (c. 200–284) presented and solved problems involving algebraic constraints on equations, although he didn’t develop a generalized methodology. We now call equations over integer domains Diophantine equations. The Indian mathematician Brahmagupta (c. 650) was the first to show a general solution over the domain of integers for the equation ax + by = c. Systematic methods for solving linear equations by variable elimination were studied by Gauss (1829); the solution of linear inequality constraints goes back to Fourier (1827).

Finite-domain constraint satisfaction problems also have a long history. For example, graph coloring (of which map coloring is a special case) is an old problem in mathematics. The four-color conjecture (that every planar graph can be colored with four or fewer colors) was first made by Francis Guthrie, a student of De Morgan, in 1852...

### 6 Adversarial Search and Games



#### 6.1 Game Theory




Artificial Intelligence: A Modern Approach














6.1Game Theory
There are at least three stances we can take towards multi-agent environments. The first stance, appropriate when there are a very large number of agents, is to consider them in the aggregate as an economy, allowing us to do things like predict that increasing demand will cause prices to rise, without having to predict the action of any individual agent.

Second, we could consider adversarial agents as just a part of the environment—a part that makes the environment nondeterministic. But if we model the adversaries in the same way that, say, rain sometimes falls and sometimes doesn’t, we miss the idea that our adversaries are actively trying to defeat us, whereas the rain supposedly has no such intention.
The third stance is to explicitly model the adversarial agents with the techniques of adversarial game-tree search. That is what this chapter covers. We begin with a restricted class of games and define the opt...

#### 6.2 Optimal Decisions in Games




Artificial Intelligence: A Modern Approach














6.2Optimal Decisions in Games
MAX wants to find a sequence of actions leading to a win, but MIN has something to say about it. This means that MAX’S strategy must be a conditional plan—a contingent strategy specifying a response to each of MIN’S possible moves. In games that have a binary outcome (win or lose), we could use AND–OR search (page 143) to generate the conditional plan. In fact, for such games, the definition of a winning strategy for the game is identical to the definition of a solution for a nondeterministic planning problem: in both cases the desirable outcome must be guaranteed no matter what the “other side” does. For games with multiple outcome scores, we need a slightly more general algorithm called minimax search.

Consider the trivial game in Figure 6.2. The possible moves for MAX at the root node are labeled a1, a2, and a3. The possible replies to a1 for MIN are b1, b2, b3, and so on. This particular game...

#### 6.3 Heuristic Alpha-Beta Tree Search




Artificial Intelligence: A Modern Approach














6.3Heuristic Alpha–Beta Tree Search
To make use of our limited computation time, we can cut off the search early and apply a heuristic evaluation function to states, effectively treating nonterminal nodes as if they were terminal. In other words, we replace the UTILITY function with EVAL, which estimates a state’s utility. We also replace the terminal test by a cutoff test, which must return true for terminal states, but is otherwise free to decide when to cut off the search, based on the search depth and any property of the state that it chooses to consider. That gives us the formula H-MINIMAX(s, d) for the heuristic minimax value of state s at search depth d:






H-MINIMAX (s, d) =




       {



EVAL (s, MAX)







max

a∈Actions(s) 

H-MINIMAX (RESULT (s, a), d + 1)







min

a∈Actions(s)

 H-MINIMAX (RESULT (s, a), d + 1)


      



if IS-CUTOFF (s, d)





if TO-MOVE (s) = MAX





if TO-MOVE (s) = MIN.


 





6...

#### 6.4 Monte Carlo Tree Search




Artificial Intelligence: A Modern Approach














6.4Monte Carlo Tree Search
The game of Go illustrates two major weaknesses of heuristic alpha–beta tree search: First, Go has a branching factor that starts at 361, which means alpha–beta search would be limited to only 4 or 5 ply. Second, it is difficult to define a good evaluation function for Go because material value is not a strong indicator and most positions are in flux until the endgame. In response to these two challenges, modern Go programs have abandoned alpha–beta search and instead use a strategy called Monte Carlo tree search (MCTS).3

The basic MCTS strategy does not use a heuristic evaluation function. Instead, the value of a state is estimated as the average utility over a number of simulations of complete games starting from the state. A simulation (also called a playout or rollout) chooses moves first for one player, then for the other, repeating until a terminal position is reached. At that point the rules ...

#### 6.5 Stochastic Games




Artificial Intelligence: A Modern Approach














6.5Stochastic Games
Stochastic games bring us a little closer to the unpredictability of real life by including a random element, such as the throwing of dice. Backgammon is a typical stochastic game that combines luck and skill. In the backgammon position of Figure 6.12, Black has rolled a 6–5 and has four possible moves (each of which moves one piece forward (clockwise) 5 positions, and one piece forward 6 positions).





×
Figure 6.12A typical backgammon position. The goal of the game is to move all one’s pieces off the board. Black moves clockwise toward 25, and White moves counterclockwise toward 0. A piece can move to any position unless multiple opponent pieces are there; if there is one opponent, it is captured and must start over. In the position shown, Black has rolled 6–5 and must choose among four legal moves: (5–11,5–10), (5–11,19–24), (5–10,10–16), and (5–11,11–16), where the notation (5–11,11–16) means move one...

#### 6.6 Partially Observable Games




Artificial Intelligence: A Modern Approach














6.6Partially Observable Games
Bobby Fischer declared that “chess is war,” but chess lacks at least one major characteristic of real wars, namely, partial observability. In the “fog of war,” the whereabouts of enemy units is often unknown until revealed by direct contact. As a result, warfare includes the use of scouts and spies to gather information and the use of concealment and bluff to confuse the enemy.
Partially observable games share these characteristics and are thus qualitatively different from the games in the preceding sections. Video games such as StarCraft are particularly challenging, being partially observable, multi-agent, nondeterministic, dynamic, and unknown.
In deterministic partially observable games, uncertainty about the state of the board arises entirely from lack of access to the choices made by the opponent. This class includes children’s games such as Battleship (where each player’s ships are placed i...

#### 6.7 Limitations of Game Search Algorithms




Artificial Intelligence: A Modern Approach














6.7Limitations of Game Search Algorithms
Because calculating optimal decisions in complex games is intractable, all algorithms must make some assumptions and approximations. Alpha–beta search uses the heuristic evaluation function as an approximation, and Monte Carlo search computes an approximate average over a random selection of playouts. The choice of which algorithm to use depends in part on the features of each game: when the branching factor is high or it is difficult to define an evaluation function, Monte Carlo search is preferred. But both algorithms suffer from fundamental limitations.
One limitation of alpha–beta search is its vulnerability to errors in the heuristic function. Figure 6.16 shows a two-ply game tree for which minimax suggests taking the right-hand branch because 100 > 99. That is the correct move if the evaluations are all exactly accurate. But suppose that the evaluation of each node has an error th...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
We have looked at a variety of games to understand what optimal play means, to understand how to play well in practice, and to get a feel for how an agent should act in any type of adversarial environment. The most important ideas are as follows:

•A game can be defined by the initial state (how the board is set up), the legal actions in each state, the result of each action, a terminal test (which says when the game is over), and a utility function that applies to terminal states to say who won and what the final score is.
•In two-player, discrete, deterministic, turn-taking zero-sum games with perfect information, the minimax algorithm can select optimal moves by a depth-first enumeration of the game tree.
•The alpha–beta search algorithm computes the same optimal move as minimax, but achieves much greater efficiency by eliminating subtrees that are provably irrelevant.
•Usually, it is not feasible to consider the wh...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
In 1846, Charles Babbage discussed the feasibility of computer chess and checkers (Morrison and Morrison, 1961). He did not understand the exponential complexity of search trees, claiming “the combinations involved in the Analytical Engine enormously surpassed any required, even by the game of chess.” Babbage also designed, but did not build, a specialpurpose machine for playing tic-tac-toe. The first game-playing machine was built around 1890 by the Spanish engineer Leonardo Torres y Quevedo. It specialized in the “KRK” (king and rook versus king) chess endgame, guaranteeing a win when the side with the rook has the move. The minimax algorithm is traced to a 1912 paper by Ernst Zermelo, the developer of modern set theory.
Game playing was one of the first tasks undertaken in AI, with early efforts by such pioneers as Konrad Zuse (1945), Norbert Wiener in his book Cybernetics (1948), and Al...

## III Knowledge, reasoning, and planning



### 7 Logical Agents



#### 7.1 Knowledge-Based Agents




Artificial Intelligence: A Modern Approach














7.1Knowledge-Based Agents
The central component of a knowledge-based agent is its knowledge base, or KB. A knowledge base is a set of sentences. (Here “sentence” is used as a technical term. It is related but not identical to the sentences of English and other natural languages.) Each sentence is expressed in a language called a knowledge representation language and represents some assertion about the world. When the sentence is taken as being given without being derived from other sentences, we call it an axiom.




There must be a way to add new sentences to the knowledge base and a way to query what is known. The standard names for these operations are TELL and ASK, respectively. Both operations may involve inference—that is, deriving new sentences from old. Inference must obey the requirement that when one ASKs a question of the knowledge base, the answer should follow from what has been told (or TELLed) to the knowledge b...

#### 7.2 The Wumpus World




Artificial Intelligence: A Modern Approach














7.2The Wumpus World
In this section we describe an environment in which knowledge-based agents can show their worth. The wumpus world is a cave consisting of rooms connected by passageways. Lurking somewhere in the cave is the terrible wumpus, a beast that eats anyone who enters its room. The wumpus can be shot by an agent, but the agent has only one arrow. Some rooms contain bottomless pits that will trap anyone who wanders into these rooms (except for the wumpus, which is too big to fall in). The only redeeming feature of this bleak environment is the possibility of finding a heap of gold. Although the wumpus world is rather tame by modern computer game standards, it illustrates some important points about intelligence.

A sample wumpus world is shown in Figure 7.2. The precise definition of the task environment is given, as suggested in Section 2.3, by the PEAS description:






Description

The table has 4 rows and 4 colu...

#### 7.3 Logic




Artificial Intelligence: A Modern Approach














7.3Logic
This section summarizes the fundamental concepts of logical representation and reasoning. These beautiful ideas are independent of any of logic’s particular forms. We therefore postpone the technical details of those forms until the next section, using instead the familiar example of ordinary arithmetic.
In Section 7.1, we said that knowledge bases consist of sentences. These sentences are expressed according to the syntax of the representation language, which specifies all the sentences that are well formed. The notion of syntax is clear enough in ordinary arithmetic: “x + y = 4” is a well–formed sentence, whereas “x4y+ =” is not.

A logic must also define the semantics, or meaning, of sentences. The semantics defines the truth of each sentence with respect to each possible world. For example, the semantics for arithmetic specifies that the sentence “x + y = 4” is true in a world where x is 2 and y is 2, but false in...

#### 7.4 Propositional Logic: A Very Simple Logic




Artificial Intelligence: A Modern Approach














7.4Propositional Logic: A Very Simple Logic
We now present propositiona logic. We describe its syntax (the structure of sentences) and its semantics (the way in which the truth of sentences is determined). From these, we derive a simple, syntactic algorithm for logical inference that implements the semantic notion of entailment. Everything takes place, of course, in the wumpus world.

7.4.1Syntax
The syntax of propositional logic defines the allowable sentences. The atomic sentences consist of a single proposition symbol. Each such symbol stands for a proposition that can be true or false. We use symbols that start with an uppercase letter and may contain other letters or subscripts, for example: P, Q, R, W1,3 and FacingEast. The names are arbitrary but are often chosen to have some mnemonic value—we use W1,3 to stand for the proposition that the wumpus is in [1,3]. (Remember that symbols such as W1,3 are atomic, i.e., W, 1, a...

#### 7.5 Propositional Theorem Proving




Artificial Intelligence: A Modern Approach














7.5Propositional Theorem Proving
So far, we have shown how to determine entailment by model checking: enumerating models and showing that the sentence must hold in all models. In this section, we show how entailment can be done by theorem proving—applying rules of inference directly to the sentences in our knowledge base to construct a proof of the desired sentence without consulting models. If the number of models is large but the length of the proof is short, then theorem proving can be more efficient than model checking.

Before we plunge into the details of theorem-proving algorithms, we will need some additional concepts related to entailment. The first concept is logical equivalence: two sentences α and β are logically equivalent if they are true in the same set of models. We write this as α ≡ β. (Note that ≡ is used to make claims about sentences, while ⇔ is used as part of a sentence.) For example, we can easily show (...

#### 7.6 Effective Propositional Model Checking




Artificial Intelligence: A Modern Approach














7.6Effective Propositional Model Checking
In this section, we describe two families of efficient algorithms for general propositional inference based on model checking: one approach based on backtracking search, and one on local hill-climbing search. These algorithms are part of the “technology” of propositional logic. This section can be skimmed on a first reading of the chapter.
The algorithms we describe are for checking satisfiability: the SAT problem. (As noted in Section 7.5, testing entailment, α ⊨ β, can be done by testing unsatisfiability of α ∧ ¬β.) We mentioned on page 241 the connection between finding a satisfying model for a logical sentence and finding a solution for a constraint satisfaction problem, so it is perhaps not surprising that the two families of propositional satisfiability algorithms closely resemble the backtracking algorithms of Section 5.3 and the local search algorithms of Section 5.4. They are,...

#### 7.7 Agents Based on Propositional Logic




Artificial Intelligence: A Modern Approach














7.7Agents Based on Propositional Logic
In this section, we bring together what we have learned so far in order to construct wumpus world agents that use propositional logic. The first step is to enable the agent to deduce, to the extent possible, the state of the world given its percept history. This requires writing down a complete logical model of the effects of actions. We then show how logical inference can be used by an agent in the wumpus world. We also show how the agent can keep track of the world efficiently without going back into the percept history for each inference. Finally, we show how the agent can use logical inference to construct plans that are guaranteed to achieve its goals, provided its knowledge base is true in the actual world.
7.7.1The current state of the world
As stated at the beginning of the chapter, a logical agent operates by deducing what to do from a knowledge base of sentences about the world....

#### Summary




Artificial Intelligence: A Modern Approach














Summary
We have introduced knowledge-based agents and have shown how to define a logic with which such agents can reason about the world. The main points are as follows:

•Intelligent agents need knowledge about the world in order to reach good decisions.
•Knowledge is contained in agents in the form of sentences in a knowledge representation language that are stored in a knowledge base.
•A knowledge-based agent is composed of a knowledge base and an inference mechanism. It operates by storing sentences about the world in its knowledge base, using the inference mechanism to infer new sentences, and using these sentences to decide what action to take.
•A representation language is defined by its syntax, which specifies the structure of sentences, and its semantics, which defines the truth of each sentence in each possible world or model.
•The relationship of entailment between sentences is crucial to our understanding of reason...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
John McCarthy’s paper “Programs with Common Sense” (McCarthy, 1958, 1968) promulgated the notion of agents that use logical reasoning to mediate between percepts and actions. It also raised the flag of declarativism, pointing out that telling an agent what it needs to know is an elegant way to build software. Allen Newell’s (1982) article “The Knowledge Level” makes the case that rational agents can be described and analyzed at an abstract level defined by the knowledge they possess rather than the programs they run.
Logic itself had its origins in ancient Greek philosophy and mathematics. Plato discussed the syntactic structure of sentences, their truth and falsity, their meaning, and the validity of logical arguments. The first known systematic study of logic was Aristotle’s Organon. His syllogisms were what we now call inference rules, although they lacked the compositionality of our cur...

### 8 First-Order Logic



#### 8.1 Representation Revisited




Artificial Intelligence: A Modern Approach














8.1Representation Revisited
In this section, we discuss the nature of representation languages. Programming languages (such as C++ or Java or Python) are the largest class of formal languages in common use. Data structures within programs can be used to represent facts; for example, a program could use a 4 x 4 array to represent the contents of the wumpus world. Thus, the programming language statement World[2,2] ←Pit is a fairly natural way to assert that there is a pit in square [2,2]. Putting together a string of such statements is sufficient for running a simulation of the wumpus world.
What programming languages lack is a general mechanism for deriving facts from other facts; each update to a data structure is done by a domain-specific procedure whose details are derived by the programmer from his or her own knowledge of the domain. This procedural approach can be contrasted with the declarative nature of propositional lo...

#### 8.2 Syntax and Semantics of First-Order Logic




Artificial Intelligence: A Modern Approach














8.2Syntax and Semantics of First-Order Logic
We begin this section by specifying more precisely the way in which the possible worlds of first-order logic reflect the ontological commitment to objects and relations. Then we introduce the various elements of the language, explaining their semantics as we go along. The main points are how the language facilitates concise representations and how its semantics leads to sound reasoning procedures.
8.2.1Models for first-order logic
Chapter 7 said that the models of a logical language are the formal structures that constitute the possible worlds under consideration. Each model links the vocabulary of the logical sentences to elements of the possible world, so that the truth of any sentence can be determined. Thus, models for propositional logic link proposition symbols to predefined truth values.
Models for first-order logic are much more interesting. First, they have objects in them!...

#### 8.3 Using First-Order Logic




Artificial Intelligence: A Modern Approach














8.3Using First-Order Logic
Now that we have defined an expressive logical language, let’s learn how to use it. In this section, we provide example sentences in some simple domains. In knowl
edge representation, a domain is just some part of the world about which we wish to express some knowledge.

We begin with a brief description of the TELL/ASK interface for first-order knowledge bases. Then we look at the domains of family relationships, numbers, sets, and lists, and at the wumpus world. Section 8.4.2 contains a more substantial example (electronic circuits) and Chapter 10 covers everything in the universe.
8.3.1Assertions and queries in first-order logic
Sentences are added to a knowledge base using TELL, exactly as in propositional logic. Such sentences are called assertions. For example, we can assert that John is a king, Richard is a person, and all kings are persons:








TELL (KB, King(John)) .





TELL (KB, Perso...

#### 8.4 Knowledge Engineering in First-Order Logic




Artificial Intelligence: A Modern Approach














8.4Knowledge Engineering in First-Order Logic
The preceding section illustrated the use of first-order logic to represent knowledge in three simple domains. This section describes the general process of knowledge-base construction— a process called knowledge engineering. A knowledge engineer is someone who investigates a particular domain, learns what concepts are important in that domain, and creates a formal representation of the objects and relations in the domain. We illustrate the knowledge engineering process in an electronic circuit domain. The approach we take is suitable for developing special-purpose knowledge bases whose domain is carefully circumscribed and whose range of queries is known in advance. General-purpose knowledge bases, which cover a broad range of human knowledge and are intended to support tasks such as natural language understanding, are discussed in Chapter 10.

8.4.1The knowledge engineering proce...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has introduced first-order logic, a representation language that is far more powerful than propositional logic. The important points are as follows:

•Knowledge representation languages should be declarative, compositional, expressive, context independent, and unambiguous.
•Logics differ in their ontological commitments and epistemological commitments. While propositional logic commits only to the existence of facts, first-order logic commits to the existence of objects and relations and thereby gains expressive power, appropriate for domains such as the wumpus world and electronic circuits.
•Both propositional logic and first-order logic share a difficulty in representing vague propositions. This difficulty limits their applicability in domains that require personal judgments, like politics or cuisine.
•The syntax of first-order logic builds on that of propositional logic. It adds terms to represent objec...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Although Aristotle’s logic dealt with generalizations over objects, it fell far short of the expressive power of first-order logic. A major barrier to its further development was its concentration on one–place predicates to the exclusion of many-place relational predicates. The first systematic treatment of relations was given by Augustus De Morgan (1864), who cited the following example to show the sorts of inferences that Aristotle’s logic could not handle: “All horses are animals; therefore, the head of a horse is the head of an animal.” This inference is inaccessible to Aristotle because any valid rule that can support this inference must first analyze the sentence using the two–place predicate “x is the head of y.” The logic of relations was studied in depth by Charles Sanders Peirce (Peirce, 1870; Misak, 2004).
True first–order logic dates from the introduction of quantifiers in Gottl...

### 9 Inference in First-Order Logic



#### 9.1 Propositional vs. First-Order Inference




Artificial Intelligence: A Modern Approach














9.1Propositional vs. First-Order Inference
One way to do first-order inference is to convert the first-order knowledge base to propositional logic and use propositional inference, which we already know how to do. A first step is eliminating universal quantifiers. For example, suppose our knowledge base contains the standard folkloric axiom that all greedy kings are evil:



∀x King(x)∧Greedy(x)⇒Evil(x).


From that we can infer any of the following sentences:









King(John)∧Greedy(John)⇒Evil(John)





King(Richard)∧Greedy(Richard)⇒Evil(Richard)





King(Father(John))∧Greedy(Father(John))⇒Evil(Father(John)).







      ⋮





In general, the rule of Universal Instantiation ( UI for short) says that we can infer any sentence obtained by substituting a ground term (a term without variables) for a universally quantified variable.1

To write out the inference rule formally, we use the notion of substitutions introduced in ...

#### 9.2 Unification and First-Order Inference




Artificial Intelligence: A Modern Approach














9.2Unification and First-Order Inference
The sharp-eyed reader will have noticed that the propositionalization approach generates many unnecessary instantiations of universally quantified sentences. We’d rather have an approach that uses just the one rule, reasoning that {x / John} solves the query Evil(x) as follows: given the rule that greedy kings are evil, find some x such that x is a king and x is greedy, and then infer that this x is evil. More generally, if there is some substitution θ that makes each of the conjuncts of the premise of the implication identical to sentences already in the knowledge base, then we can assert the conclusion of the implication, after applying θ. In this case, the substitution θ = {x / John} achieves that aim. Now suppose that instead of knowing Greedy (John), we know that everyone is greedy:







∀y  Greedy (y) .



                   (9.2)





Then we would still like to be able to conc...

#### 9.3 Forward Chaining




Artificial Intelligence: A Modern Approach














9.3Forward Chaining
In Section 7.5 we showed a forward-chaining algorithm for knowledge bases of propositional definite clauses. Here we expand that idea to cover first-order definite clauses.
Of course there are some logical sentences that cannot be stated as a definite clause, and thus cannot be handled by this approach. But rules of the form Antecedent ⇒ Consequent are sufficient to cover a wide variety of interesting real-world systems.
9.3.1First-order definite clauses
First-order definite clauses are disjunctions of literals of which exactly one is positive. That means a definite clause is either atomic, or is an implication whose antecedent is a conjunction of positive literals and whose consequent is a single positive literal. Existential quantifiers are not allowed, and universal quantifiers are left implicit: if you see an x in a definite clause, that means there is an implicit ∀x quantifier. A typical first-order de...

#### 9.4 Backward Chaining




Artificial Intelligence: A Modern Approach














9.4Backward Chaining
The second major family of logical inference algorithms uses backward chaining over definite clauses. These algorithms work backward from the goal, chaining through rules to find known facts that support the proof.
9.4.1A backward-chaining algorithm
Figure 9.6 shows a backward-chaining algorithm for definite clauses. FOL-BC-ASK(KB, goal) will be proved if the knowledge base contains a rule of the form lhs ⇒ goal, where lhs(left-hand side) is a list of conjuncts. An atomic fact like American(West) is considered as a clause whose lhs is the empty list. Now a query that contains variables might be proved in multiple ways. For example, the query Person(x) could be proved with the substitution {x/John} as well as with {x/Richard}. So we implement FOL-BC-ASK as a generator—a function that returns multiple times, each time giving one possible result (see Appendix B).






Description

The horizontal axis is labe...

#### 9.5 Resolution




Artificial Intelligence: A Modern Approach














9.5Resolution
The last of our three families of logical systems, and the only one that works for any knowledge base, not just definite clauses, is resolution. We saw on page 241 that propositional resolution is a complete inference procedure for propositional logic; in this section, we extend it to first-order logic.
9.5.1Conjunctive normal form for first-order logic
The first step is to convert sentences to conjunctive normal form (CNF)—that is, a conjunction of clauses, where each clause is a disjunction of literals.5 In CNF, literals can contain variables, which are assumed to be universally quantified. For example, the sentence



∀x,y,z  American(x)  ∧  Weapon(y)  ∧  Sells(x,y, z)  ∧  Hostile(z)  ⇒  Criminal(x)


becomes, in CNF,



¬American(x)  ∨  ¬Weapon(y)  ∨  ¬Sells(x,y, z)  ∨  ¬Hostile(z)  ∨  Criminal(x).


The key is that Every sentence of first-order logic can be converted into an inferentially equivalent CNF sent...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
We have presented an analysis of logical inference in first-order logic and a number of algorithms for doing it.

•A first approach uses inference rules ( universal instantiation and existential instantiation) to propositionalize the inference problem. Typically, this approach is slow, unless the domain is small.
•The use of unification to identify appropriate substitutions for variables eliminates the instantiation step in first-order proofs, making the process more efficient in many cases.
•A lifted version of Modus Ponens uses unification to provide a natural and powerful inference rule, generalized Modus Ponens. The forward-chaining and backwardchaining algorithms apply this rule to sets of definite clauses.
•Generalized Modus Ponens is complete for definite clauses, although the entailment problem is semidecidable. For Datalog knowledge bases consisting of function-free definite clauses, entailment is decidable.
•...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Gottlob Frege, who developed full first-order logic in 1879, based his system of inference on a collection of valid schemas plus a single inference rule, Modus Ponens. Whitehead and Russell (1910) expounded the so-called rules of passage (the actual term is from Herbrand (1930)) that are used to move quantifiers to the front of formulas. Skolem constants and Skolem functions were introduced, appropriately enough, by Thoralf Skolem (1920). Oddly enough, it was Skolem who introduced the Herbrand universe (Skolem, 1928).
Herbrand’s theorem (Herbrand, 1930) has played a vital role in the development of automated reasoning. Herbrand is also the inventor of unification. Gödel (1930) built on the ideas of Skolem and Herbrand to show that first-order logic has a complete proof procedure. Alan Turing (1936) and Alonzo Church (1936) simultaneously showed, using very different proofs, that validity in...

### 10 Knowledge Representation



#### 10.1 Ontological Engineering




Artificial Intelligence: A Modern Approach














10.1Ontological Engineering
In “toy” domains, the choice of representation is not that important; many choices will work. Complex domains such as shopping on the Internet or driving a car in traffic require more general and flexible representations. This chapter shows how to create these representations, concentrating on general concepts—such as Events, Time, Physical Objects, and Beliefs— that occur in many different domains. Representing these abstract concepts is sometimes called ontological engineering.

We cannot hope to represent everything in the world, even a 1000-page textbook, but we will leave placeholders where new knowledge for any domain can fit in. For example, we will define what it means to be a physical object, and the details of different types of objects—robots, televisions, books, or whatever—can be filled in later. This is analogous to the way that designers of an object-oriented programming framework (su...

#### 10.2 Categories and Objects




Artificial Intelligence: A Modern Approach














10.2Categories and Objects
The organization of objects into categories is a vital part of knowledge representation. Although interaction with the world takes place at the level of individual objects, much reasoning takes place at the level of categories. For example, a shopper would normally have the goal of buying a basketball, rather than a particular basketball such as BB9. Categories also serve to make predictions about objects once they are classified. One infers the presence of certain objects from perceptual input, infers category membership from the perceived properties of the objects, and then uses category information to make predictions about the objects. For example, from its green and yellow mottled skin, one-foot diameter, ovoid shape, red flesh, black seeds, and presence in the fruit aisle, one can infer that an object is a watermelon; from this, one infers that it would be useful for fruit salad.

There are two...

#### 10.3 Events




Artificial Intelligence: A Modern Approach














10.3Events
In Section 7.7.1 we discussed actions: things that happen, such as Shoott; and fluents: aspects of the world that change, such as HaveArrowt. Both were represented as propositions, and we used successor-state axioms to say that a fluent will be true at time t + 1 if the action at time t caused it to be true, or if it was already true at time t and the action did not cause it to be false. That was for a world in which actions are discrete, instantaneous, happen one at a time, and have no variation in how they are performed (that is, there is only one kind of Shootaction, there is no distinction between shooting quickly, slowly, nervously, etc.).
But as we move from simplistic domains to the real world, there is a much richer range of actions or events3 to deal with. Consider a continuous action, such as filling a bathtub. A successor-state axiom can say that the tub is empty before the action and full when the action...

#### 10.4 Mental Objects and Modal Logic




Artificial Intelligence: A Modern Approach














10.4Mental Objects and Modal Logic
The agents we have constructed so far have beliefs and can deduce new beliefs. Yet none of them has any knowledge about beliefs or about deduction. Knowledge about one’s own knowledge and reasoning processes is useful for controlling inference. For example, suppose Alice asks “what is the square root of 1764” and Bob replies “I don’t know.” If Alice insists “think harder,” Bob should realize that with some more thought, this question can in fact be answered. On the other hand, if the question were “Is the president sitting down right now?” then Bob should realize that thinking harder is unlikely to help. Knowledge about the knowledge of other agents is also important; Bob should realize that the president does know.
What we need is a model of the mental objects that are in someone’s head (or something’s knowledge base) and of the mental processes that manipulate those mental objects. The mode...

#### 10.5 Reasoning Systems for Categories




Artificial Intelligence: A Modern Approach














10.5Reasoning Systems for Categories
Categories are the primary building blocks of large-scale knowledge representation schemes. This section describes systems specially designed for organizing and reasoning with categories. There are two closely related families of systems: semantic networks provide graphical aids for visualizing a knowledge base and efficient algorithms for inferring properties of an object on the basis of its category membership; and description logics provide a formal language for constructing and combining category definitions and efficient algorithms for deciding subset and superset relationships between categories.


10.5.1Semantic networks
In 1909, Charles S. Peirce proposed a graphical notation of nodes and edges called existential graphs that he called “the logic of the future.” Thus began a long-running debate between advocates of “logic” and advocates of “semantic networks.” Unfortunately, the deba...

#### 10.6 Reasoning with Default Information




Artificial Intelligence: A Modern Approach














10.6Reasoning with Default Information
In the preceding section, we saw a simple example of an assertion with default status: people have two legs. This default can be overridden by more specific information, such as that Long John Silver has one leg. We saw that the inheritance mechanism in semantic networks implements the overriding of defaults in a simple and natural way. In this section, we study defaults more generally, with a view toward understanding the semantics of defaults rather than just providing a procedural mechanism.
10.6.1Circumscription and default logic
We have seen two examples of reasoning processes that violate the monotonicity property of logic that was proved in Chapter 7.8 In this chapter we saw that a property inherited by all members of a category in a semantic network could be overridden by more specific information for a subcategory. In Section 9.4.4, we saw that under the closed-world assumption, ...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
By delving into the details of how one represents a variety of knowledge, we hope we have given the reader a sense of how real knowledge bases are constructed and a feeling for the interesting philosophical issues that arise. The major points are as follows:

•Large-scale knowledge representation requires a general-purpose ontology to organize and tie together the various specific domains of knowledge.
•A general-purpose ontology needs to cover a wide variety of knowledge and should be capable, in principle, of handling any domain.
•Building a large, general-purpose ontology is a significant challenge that has yet to be fully realized, although current frameworks seem to be quite robust.
•We presented an upper ontology based on categories and the event calculus. We covered categories, subcategories, parts, structured objects, measurements, substances, events, time and space, change, and beliefs.
•Natural kinds cannot b...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Briggs (1985) claims that knowledge representation research began with first millennium BCE Indian theorizing about the grammar of Shastric Sanskrit. Western philosophers trace their work on the subject back to c. 300 BCE in Aristotle’s Metaphysics (literally, what comes after the book on physics). The development of technical terminology in any field can be regarded as a form of knowledge representation.
Early discussions of representation in AI tended to focus on “problem representation” rather than “knowledge representation.” (See, for example, Amarel’s (1968) discussion of the “Missionaries and Cannibals” problem.) In the 1970s, AI emphasized the development of “expert systems” (also called “knowledge-based systems”) that could, if given the appropriate domain knowledge, match or exceed the performance of human experts on narrowly defined tasks. For example, the first expert system, DEN...

### 11 Automated Planning



#### 11.1 Definition of Classical Planning




Artificial Intelligence: A Modern Approach














11.1Definition of Classical Planning
 Classical planning is defined as the task of finding a sequence of actions to accomplish a goal in a discrete, deterministic, static, fully observable environment. We have seen two approaches to this task: the problem-solving agent of Chapter 3 and the hybrid propositional logical agent of Chapter 7. Both share two limitations. First, they both require ad hoc heuristics for each new domain: a heuristic evaluation function for search, and hand-written code for the hybrid wumpus agent. Second, they both need to explicitly represent an exponentially large state space. For example, in the propositional logic model of the wumpus world, the axiom for moving a step forward had to be repeated for all four agent orientations, T time steps, and n2 current locations.

In response to these limitations, planning researchers have invested in a factored representation using a family of languages called P...

#### 11.2 Algorithms for Classical Planning




Artificial Intelligence: A Modern Approach














11.2Algorithms for Classical Planning
The description of a planning problem provides an obvious way to search from the initial state through the space of states, looking for a goal. A nice advantage of the declarative representation of action schemas is that we can also search backward from the goal, looking for the initial state (Figure 11.5 compares forward and backward searches). A third possibility is to translate the problem description into a set of logic sentences, to which we can apply a logical inference algorithm to find a solution.






Description

Part (“a”): A block is labeled At (P subscript 1 BaseLine, "A”), At (P subscript 2 BaseLine, "A”). Lines from the block connect to two blocks labeled Fly (P subscript 1 BaseLine, "A", B) and Fly (P subscript 2 BaseLine, "A", B). An arrow from Fly (P subscript 1 BaseLine, "A", B) block points to a block labeled At (P subscript 1 BaseLine, B), At (P subscript 2 BaseLine, ...

#### 11.3 Heuristics for Planning




Artificial Intelligence: A Modern Approach














11.3Heuristics for Planning
Neither forward nor backward search is efficient without a good heuristic function. Recall from Chapter 3 that a heuristic function h(s) estimates the distance from a state s to the goal, and that if we can derive an admissible heuristic for this distance—one that does not overestimate—then we can use A* search to find optimal solutions.
By definition, there is no way to analyze an atomic state, and thus it requires some ingenuity by an analyst (usually human) to define good domain-specific heuristics for search problems with atomic states. But planning uses a factored representation for states and actions, which makes it possible to define good domain-independent heuristics.
Recall that an admissible heuristic can be derived by defining a relaxed problem that is easier to solve. The exact cost of a solution to this easier problem then becomes the heuristic for the original problem. A search problem...

#### 11.4 Hierarchical Planning




Artificial Intelligence: A Modern Approach














11.4Hierarchical Planning
The problem-solving and planning methods of the preceding chapters all operate with a fixed set of atomic actions. Actions can be strung together, and state-of-the-art algorithms can generate solutions containing thousands of actions. That’s fine if we are planning a vacation and the actions are at the level of “fly from san Francisco to Honolulu,” but at the motorcontrol level of “bend the left knee by 5 degrees” we would need to string together millions or billions of actions, not thousands.
Bridging this gap requires planning at higher levels of abstraction. A high-level plan for a Hawaii vacation might be “Go to san Francisco airport; take flight HA 11 to Honolulu; do vacation stuff for two weeks; take HA 12 back to san Francisco; go home.” Given such a plan, the action “Go to san Francisco airport” can be viewed as a planning task in itself, with a solution such as “Choose a ride-hailing service;...

#### 11.5 Planning and Acting in Nondeterministic Domains




Artificial Intelligence: A Modern Approach














11.5Planning and Acting in Nondeterministic Domains
In this section we extend planning to handle partially observable, nondeterministic, and unknown environments. The basic concepts mirror those in Chapter 4, but there are differences arising from the use of factored representations rather than atomic representations. This affects the way we represent the agent’s capability for action and observation and the way we represent belief states—the sets of possible physical states the agent might be in—for partially observable environments. We can also take advantage of many of the domainindependent methods given in Section 11.3 for calculating search heuristics.
We will cover sensorless planning (also known as conformant planning) for environments with no observations; contingency planning for partially observable and nondeterministic environments; and online planning and replanning for unknown environments. This will allow us to t...

#### 11.6 Time, Schedules, and Resources




Artificial Intelligence: A Modern Approach














11.6Time, Schedules, and Resources
Classical planning talks about what to do, in what order, but does not talk about time: how long an action takes and when it occurs. For example, in the airport domain we could produce a plan saying what planes go where, carrying what, but could not specify departure and arrival times. This is the subject matter of scheduling.

The real world also imposes resource constraints: an airline has a limited number of staff, and staff who are on one flight cannot be on another at the same time. This section introduces techniques for planning and scheduling problems with resource constraints.

The approach we take is “plan first, schedule later”: divide the overall problem into a planning phase in which actions are selected, with some ordering constraints, to meet the goals of the problem, and a later scheduling phase, in which temporal information is added to the plan to ensure that it meets resourc...

#### 11.7 Analysis of Planning Approaches




Artificial Intelligence: A Modern Approach














11.7Analysis of Planning Approaches
Planning combines the two major areas of AI we have covered so far: search and logic. A planner can be seen either as a program that searches for a solution or as one that (constructively) proves the existence of a solution. The cross-fertilization of ideas from the two areas has allowed planners to scale up from toy problems where the number of actions and states was limited to around a dozen, to real-world industrial applications with millions of states and thousands of actions.
Planning is foremost an exercise in controlling combinatorial explosion. If there are n propositions in a domain, then there are 2n states. Against such pessimism, the identification of independent subproblems can be a powerful weapon. In the best case—full decomposability of the problem—we get an exponential speedup. Decomposability is destroyed, however, by negative interactions between actions. SATPLAN can encod...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
In this chapter, we described the PDDL representation for both classical and extended planning problems, and presented several algorithmic approaches for finding solutions. The points to remember:

•Planning systems are problem-solving algorithms that operate on explicit factored representations of states and actions. These representations make possible the derivation of effective domain-independent heuristics and the development of powerful and flexible algorithms for solving problems.
•PDDL, the Planning Domain Definition Language, describes the initial and goal states as conjunctions of literals, and actions in terms of their preconditions and effects. Extensions represent time, resources, percepts, contingent plans, and hierarchical plans.
•State-space search can operate in the forward direction (progression) or the backward direction (regression). Effective heuristics can be derived by subgoal independence assumpt...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
AI planning arose from investigations into state-space search, theorem proving, and control theory. STRIPS (Fikes and Nilsson, 1971, 1993), the first major planning system, was designed as the planner for the Shakey robot at SRI. The first version of the program ran on a computer with only 192 KB of memory. Its overall control structure was modeled on GPS, the General Problem Solver (Newell and Simon, 1961), a state-space search system that used means–ends analysis.
The STRIPS representation language evolved into the Action Description Language, or ADL (Pednault, 1986), and then the Problem Domain Description Language, or PDDL (Ghallab et al., 1998), which has been used for the International Planning Competition since 1998. The most recent version is PDDL 3.1 (Kovacs, 2011).
Planners in the early 1970s decomposed problems by computing a subplan for each subgoal and then stringing the subpla...

## IV Uncertain knowledge and reasoning



### 12 Quantifying Uncertainty



#### 12.1 Acting under Uncertainty




Artificial Intelligence: A Modern Approach














12.1Acting under Uncertainty
Agents in the real world need to handle uncertainty, whether due to partial observability, nondeterminism, or adversaries. An agent may never know for sure what state it is in now or where it will end up after a sequence of actions.

We have seen problem-solving and logical agents handle uncertainty by keeping track of a belief state—a representation of the set of all possible world states that it might be in—and generating a contingency plan that handles every possible eventuality that its sensors may report during execution. This approach works on simple problems, but it has drawbacks:

•The agent must consider every possible explanation for its sensor observations, no matter how unlikely. This leads to a large belief-state full of unlikely possibilities.
•A correct contingent plan that handles every eventuality can grow arbitrarily large and must consider arbitrarily unlikely contingencies.
•Som...

#### 12.2 Basic Probability Notation




Artificial Intelligence: A Modern Approach














12.2Basic Probability Notation
For our agent to represent and use probabilistic information, we need a formal language. The language of probability theory has traditionally been informal, written by human mathematicians for other human mathematicians. Appendix A includes a standard introduction to elementary probability theory; here, we take an approach more suited to the needs of AI and connect it with the concepts of formal logic.
12.2.1What probabilities are about
Like logical assertions, probabilistic assertions are about possible worlds. Whereas logical assertions say which possible worlds are strictly ruled out (all those in which the assertion is false), probabilistic assertions talk about how probable the various worlds are. In probability theory, the set of all possible worlds is called the sample space. The possible worlds are mutually exclusive and exhaustive—two possible worlds cannot both be the case, and one poss...

#### 12.3 Inference Using Full Joint Distributions




Artificial Intelligence: A Modern Approach














12.3Inference Using Full Joint Distributions
In this section we describe a simple method for probabilistic inference—that is, the computation of posterior probabilities for query propositions given observed evidence. We use the full joint distribution as the “knowledge base” from which answers to all questions may be derived. Along the way we also introduce several useful techniques for manipulating equations involving probabilities.


We begin with a simple example: a domain consisting of just the three Boolean variables Toothache, Cavity, and Catch (the dentist’s nasty steel probe catches in my tooth). The full joint distribution is a 2 × 2 × 2 table as shown in Figure 12.3.




×
Figure 12.3A full joint distribution for the Toothache, Cavity, Catch world.
Notice that the probabilities in the joint distribution sum to 1, as required by the axioms of probability. Notice also that Equation (12.2) gives us a direct way to calcu...

#### 12.4 Independence




Artificial Intelligence: A Modern Approach














12.4Independence
Let us expand the full joint distribution in Figure 12.3 by adding a fourth variable, Weather. The full joint distribution then becomes P(Toothache, Catch, Cavity, Weather), which has 2 × 2 × 2 × 4 = 32 entries. It contains four “editions” of the table shown in Figure 12.3, one for each kind of weather. What relationship do these editions have to each other and to the original three-variable table? How is the value of P(toothache, catch, cavity, cloud) related to the value of P(toothache, catch, cavity)? We can use the product rule (Equation (12.4)):







P(toothache, catch, cavity,  cloud)





    = P(cloud | toothache, catch, cavity)P(toothache, catch, cavity).





Now, unless one is in the deity business, one should not imagine that one’s dental problems influence the weather. And for indoor dentistry, at least, it seems safe to say that the weather does not influence the dental variables. Therefore, th...

#### 12.5 Bayes’ Rule and Its Use




Artificial Intelligence: A Modern Approach














12.5Bayes’ Rule and Its Use
On page 408, we defined the product rule (Equation (12.4)). It can actually be written in two forms:







P(a∧b)=P(a|b)P(b)



and



P(a∧b)=P(b|a)P(a).





Equating the two right-hand sides and dividing by P(a), we get







P(b|a) =

P(a|b)P(b)

P(a)

.



                 (12.12)





This equation is known as Bayes’ rule (also Bayes’ law or Bayes’ theorem). This simple equation underlies most modern AI systems for probabilistic inference.

The more general case of Bayes’ rule for multivalued variables can be written in the P notation as follows:



P(Y|X) =

P(X|Y) P(Y)

P(X)

.


As before, this is to be taken as representing a set of equations, each dealing with specific values of the variables. We will also have occasion to use a more general version conditionalized on some background evidence e:







P(Y|X,e) =

P(X|Y,e) P(Y|e)

P(X|e)

. 



           (12.13)





12.5.1Applying Baye...

#### 12.6 Naive Bayes Models




Artificial Intelligence: A Modern Approach














12.6Naive Bayes Models
The dentistry example illustrates a commonly occurring pattern in which a single cause directly influences a number of effects, all of which are conditionally independent, given the cause. The full joint distribution can be written as







P(Cause,Effec
t
1

,…,Effec
t
n

) = P(Cause)

∏
i


P(Effec
t
i

|Cause).




            (12.20)





Such a probability distribution is called a naive Bayes model—“naive” because it is often used (as a simplifying assumption) in cases where the “effect” variables are not strictly independent given the cause variable. (The naive Bayes model is sometimes called a Bayesian classifier, a somewhat careless usage that has prompted true Bayesians to call it the idiot Bayes model.) In practice, naive Bayes systems often work very well, even when the conditional independence assumption is not strictly true.

To use a naive Bayes model, we can apply Equation (12.20) to obta...

#### 12.7 The Wumpus World Revisited




Artificial Intelligence: A Modern Approach














12.7The Wumpus World Revisited
We can combine the ideas in this chapter to solve probabilistic reasoning problems in the wumpus world. (See Chapter 7 for a complete description of the wumpus world.) Uncertainty arises in the wumpus world because the agent’s sensors give only partial information about the world. For example, Figure 12.5 shows a situation in which each of the three unvisited but reachable squares—[1,3], [2,2], and [3,1]—might contain a pit. Pure logical inference can conclude nothing about which square is most likely to be safe, so a logical agent might have to choose randomly. We will see that a probabilistic agent can do much better than the logical agent.






Description

The grid is depicted by a 4 cross 4 matrix square. The squares are labeled as follows from the lower left until the upper right. (1, 1), (2, 1), (3, 1), (4, 1), (1, 2), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (2, 4)...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has suggested probability theory as a suitable foundation for uncertain reasoning and provided a gentle introduction to its use.

•Uncertainty arises because of both laziness and ignorance. It is inescapable in complex, nondeterministic, or partially observable environments.
•Probabilities express the agent’s inability to reach a definite decision regarding the truth of a sentence. Probabilities summarize the agent’s beliefs relative to the evidence.
•Decision theory combines the agent’s beliefs and desires, defining the best action as the one that maximizes expected utility.
•Basic probability statements include prior or unconditional probabilities and posterior or conditional probabilities over simple and complex propositions.
•The axioms of probability constrain the probabilities of logically related propositions. An agent that violates the axioms must behave irrationally in some cases.
•The full joint ...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Probability theory was invented as a way of analyzing games of chance. In about 850 CE the Indian mathematician Mahaviracarya described how to arrange a set of bets that can’t lose (what we now call a Dutch book). In Europe, the first significant systematic analyses were produced by Girolamo Cardano around 1565, although publication was posthumous (1663). By that time, probability had been established as a mathematical discipline due to a series of results from a famous correspondence between Blaise Pascal and Pierre de Fermat in 1654. The first published textbook on probability was De Ratiociniis in Ludo Aleae (On Reasoning in a Game of Chance) by Huygens (1657). The “laziness and ignorance” view of uncertainty was described by John Arbuthnot in the preface of his translation of Huygens (Arbuthnot, 1692): “It is impossible for a Die, with such determin’d force and direction, not to fall on...

### 13 Probabilistic Reasoning



#### 13.1 Representing Knowledge in an Uncertain Domain




Artificial Intelligence: A Modern Approach














13.1Representing Knowledge in an Uncertain Domain
In Chapter 12, we saw that the full joint probability distribution can answer any question about the domain, but can become intractably large as the number of variables grows. Furthermore, specifying probabilities for possible worlds one by one is unnatural and tedious.
We also saw that independence and conditional independence relationships among variables can greatly reduce the number of probabilities that need to be specified in order to define the full joint distribution. This section introduces a data structure called a Bayesian network1 to represent the dependencies among variables. Bayesian networks can represent essentially any full joint probability distribution and in many cases can do so very concisely.

A Bayesian network is a directed graph in which each node is annotated with quantitative probability information. The full specification is as follows:

1.Each node ...

#### 13.2 The Semantics of Bayesian Networks




Artificial Intelligence: A Modern Approach














13.2The Semantics of Bayesian Networks
The syntax of a Bayes net consists of a directed acyclic graph with some local probability information attached to each node. The semantics defines how the syntax corresponds to a joint distribution over the variables of the network.
Assume that the Bayes net contains n variables, X1,...,Xn. A generic entry in the joint distribution is then P(X1 = x1 ∧ ... ∧ Xn = x n), or P(x1,..., xn) for short. The semantics of Bayes nets defines each entry in the joint distribution as follows:







P(
x
1

,…,
x
n

)=

∏

i=1
n


θ(
x
i

|parents(
X
i

))
,



         (13.1)





where parents (Xi) denotes the values of Parents (Xi) that appear in x1,...,xn. Thus, each entry in the joint distribution is represented by the product of the appropriate elements of the local conditional distributions in the Bayes net.
To illustrate this, we can calculate the probability that the alarm has sounded, but ne...

#### 13.3 Exact Inference in Bayesian Networks




Artificial Intelligence: A Modern Approach














13.3Exact Inference in Bayesian Networks
The basic task for any probabilistic inference system is to compute the posterior probability distribution for a set of query variables, given some observed event—usually, some assignment of values to a set of evidence variables.5 To simplify the presentation, we will consider only one query variable at a time; the algorithms can easily be extended to queries with multiple variables. (For example, we can solve the query P(U, V | e) by multiplying P(V | e) and P(U | V, e).) We will use the notation from Chapter 12: X denotes the query variable; E denotes the set of evidence variables E1,..., Em, and e is a particular observed event; Y denotes the hidden (nonevidence, nonquery) variables Y1,...,Yℓ. Thus, the complete set of variables is {X}∪E∪Y. A typical query asks for the posterior probability distribution P(X | e).

In the burglary network, we might observe the event in which JohnCalls...

#### 13.4 Approximate Inference for Bayesian Networks




Artificial Intelligence: A Modern Approach














13.4Approximate Inference for Bayesian Networks
Given the intractability of exact inference in large networks, we will now consider approximate inference methods. This section describes randomized sampling algorithms, also called  Monte Carlo algorithms, that provide approximate answers whose accuracy depends on the number of samples generated. They work by generating random events based on the probabilities in the Bayes net and counting up the different answers found in those random events. With enough samples, we can get arbitrarily close to recovering the true probability distribution—provided the Bayes net has no deterministic conditional distributions.

Monte Carlo algorithms, of which simulated annealing (page 133) is an example, are used in many branches of science to estimate quantities that are difficult to calculate exactly. In this section, we are interested in sampling applied to the computation of posterior probab...

#### 13.5 Causal Networks




Artificial Intelligence: A Modern Approach














13.5Causal Networks
We have discussed several advantages of keeping node ordering in Bayes nets compatible with the direction of causation. In particular, we noted the ease with which conditional probabilities can be assessed if such ordering is maintained, as well as the compactness of the resultant network structure. We noted however that, in principle, any node ordering permits a consistent construction of the network to represent the joint distribution function. This was demonstrated in Figure 13.3, where changing the node ordering produced networks that were bushier and a lot less natural than the original network in Figure 13.2 but enabled us, nevertheless, to represent the same distribution on all variables.
This section describes causal networks, a restricted class of Bayesian networks that forbids all but causally compatible orderings. We will explore how to construct such networks, what is gained by such construction...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has described Bayesian networks, a well-developed representation for uncertain knowledge. Bayesian networks play a role roughly analogous to that of propositional logic for definite knowledge.

•A Bayesian network is a directed acyclic graph whose nodes correspond to random variables; each node has a conditional distribution for the node, given its parents.
•Bayesian networks provide a concise way to represent conditional independence relationships in the domain.
•A Bayesian network specifies a joint probability distribution over its variables. The probability of any given assignment to all the variables is defined as the product of the corresponding entries in the local conditional distributions. A Bayesian network is often exponentially smaller than an explicitly enumerated joint distribution.
•Many conditional distributions can be represented compactly by canonical families of distributions. Hybrid Baye...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The use of networks to represent probabilistic information began early in the 20th century, with the work of Sewall Wright on the probabilistic analysis of genetic inheritance and animal growth factors (Wright, 1921, 1934). I. J. Good (1961), in collaboration with Alan Turing, developed probabilistic representations and Bayesian inference methods that could be regarded as a forerunner of modern Bayesian networks—although the paper is not often cited in this context.7 The same paper is the original source for the noisy-OR model.
The influence diagram representation for decision problems, which incorporated a DAG representation for random variables, was used in decision analysis in the late 1970s (see Chapter 15), but only enumeration was used for evaluation. Judea Pearl developed the messagepassing method for inference in tree networks (Pearl, 1982a) and polytree networks (Kim and Pearl, 198...

### 14 Probabilistic Reasoning over Time



#### 14.1 Time and Uncertainty




Artificial Intelligence: A Modern Approach














14.1Time and Uncertainty
We have developed our techniques for probabilistic reasoning in the context of static worlds, in which each random variable has a single fixed value. For example, when repairing a car, we assume that whatever is broken remains broken during the process of diagnosis; our job is to infer the state of the car from observed evidence, which also remains fixed.
Now consider a slightly different problem: treating a diabetic patient. As in the case of car repair, we have evidence such as recent insulin doses, food intake, blood sugar measurements, and other physical signs. The task is to assess the current state of the patient, including the actual blood sugar level and insulin level. Given this information, we can make a decision about the patient’s food intake and insulin dose. Unlike the case of car repair, here the dynamic aspects of the problem are essential. Blood sugar levels and measurements thereof ca...

#### 14.2 Inference in Temporal Models




Artificial Intelligence: A Modern Approach














14.2Inference in Temporal Models
Having set up the structure of a generic temporal model, we can formulate the basic inference tasks that must be solved:

•Filtering2 or state estimation is the task of computing the belief state P(Xt | e1:t)—the posterior distribution over the most recent state given all evidence to date. In the umbrella example, this would mean computing the probability of rain today, given all the umbrella observations made so far. Filtering is what a rational agent does to keep track of the current state so that rational decisions can be made. It turns out that an almost identical calculation provides the likelihood of the evidence sequence, P(e1:t).



•Prediction: This is the task of computing the posterior distribution over the future state, given all evidence to date. That is, we wish to compute P(Xt+k | e1:t) for some k > 0. In the umbrella example, this might mean computing the probability of rain thr...

#### 14.3 Hidden Markov Models




Artificial Intelligence: A Modern Approach














14.3Hidden Markov Models
The preceding section developed algorithms for temporal probabilistic reasoning using a general framework that was independent of the specific form of the transition and sensor models and independent of the nature of the state and evidence variables. In this and the next two sections, we discuss more concrete models and applications that illustrate the power of the basic algorithms and in some cases allow further improvements.
We begin with the hidden Markov model, or HMM. An HMM is a temporal probabilistic model in which the state of the process is described by a single, discrete random variable. The possible values of the variable are the possible states of the world. The umbrella example described in the preceding section is therefore an HMM, since it has just one state variable: Raint. What happens if you have a model with two or more state variables? You can still fit it into the HMM framework by ...

#### 14.4 Kalman Filters




Artificial Intelligence: A Modern Approach














14.4Kalman Filters
Imagine watching a small bird flying through dense jungle foliage at dusk: you glimpse brief, intermittent flashes of motion; you try hard to guess where the bird is and where it will appear next so that you don’t lose it. Or imagine that you are a World War II radar operator peering at a faint, wandering blip that appears once every 10 seconds on the screen. Or, going back further still, imagine you are Kepler trying to reconstruct the motions of the planets from a collection of highly inaccurate angular observations taken at irregular and imprecisely measured intervals.
In all these cases, you are doing filtering: estimating state variables (here, the position and velocity of a moving object) from noisy observations over time. If the variables were discrete, we could model the system with a hidden Markov model. This section examines methods for handling continuous variables, using an algorithm called Kalma...

#### 14.5 Dynamic Bayesian Networks




Artificial Intelligence: A Modern Approach














14.5Dynamic Bayesian Networks
Dynamic Bayesian networks, or DBNs, extend the semantics of standard Bayesian networks to handle temporal probability models of the kind described in Section 14.1. We have already seen examples of DBNs: the umbrella network in Figure 14.2 and the Kalman filter network in Figure 14.9. In general, each slice of a DBN can have any number of state variables Xt and evidence variables Et. For simplicity, we assume that the variables, their links, and their conditional distributions are exactly replicated from slice to slice and that the DBN represents a first-order Markov process, so that each variable can have parents only in its own slice or the immediately preceding slice. In this way, the DBN corresponds to a Bayesian network with infinitely many variables.

It should be clear that every hidden Markov model can be represented as a DBN with a single state variable and a single evidence variable. It i...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has addressed the general problem of representing and reasoning about probabilistic temporal processes. The main points are as follows:

•The changing state of the world is handled by using a set of random variables to represent the state at each point in time.
•Representations can be designed to (roughly) satisfy the Markov property, so that the future is independent of the past given the present. Combined with the assumption that the process is time-homogeneous, this greatly simplifies the representation.
•A temporal probability model can be thought of as containing a transition model describing the state evolution and a sensor model describing the observation process.
•The principal inference tasks in temporal models are filtering (state estimation), prediction, smoothing, and computing the most likely explanation. Each of these tasks can be achieved using simple, recursive algorithms whose run time is ...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Many of the basic ideas for estimating the state of dynamical systems came from the mathematician C. F. Gauss (1809), who formulated a deterministic least-squares algorithm for the problem of estimating orbits from astronomical observations. A. A. Markov (1913) developed what was later called the Markov assumption in his analysis of stochastic processes; he estimated a first-order Markov chain on letters from the text of Eugene Onegin. The general theory of Markov chains and their mixing times is covered by Levin et al. (2008).
Significant classified work on filtering was done during World War II by Wiener (1942) for continuous-time processes and by Kolmogorov (1941) for discrete-time processes. Although this work led to important technological developments over the next 20 years, its use of a frequency-domain representation made many calculations quite cumbersome. Direct state-space modeli...

### 15 Making Simple Decisions



#### 15.1 Combining Beliefs and Desires under Uncertainty




Artificial Intelligence: A Modern Approach














15.1Combining Beliefs and Desires under Uncertainty
We begin with an agent that, like all agents, has to make a decision. It has available some actions a. There may be uncertainty about the current state, so we’ll assume that the agent assigns a probability P(s) to each possible current state s. There may also be uncertainty about the action outcomes; the transition model is given by P(s' | s, a), the probability that action a in state s reaches state s'. Because we’re primarily interested in the outcome s', we’ll also use the abbreviated notation P(RESULT(a) = s'), the probability of reaching s' by doing a in the current state, whatever that is. The two are related as follows:



P(RESULT(a)=s')=

∑
s


P(s)P(s'|s,a).



Decision theory, in its simplest form, deals with choosing among actions based on the desirability of their immediate outcomes; that is, the environment is assumed to be episodic in the sense defined on page ...

#### 15.2 The Basis of Utility Theory




Artificial Intelligence: A Modern Approach














15.2The Basis of Utility Theory
Intuitively, the principle of Maximum Expected Utility (MEU) seems like a reasonable way to make decisions, but it is by no means obvious that it is the only rational way. After all, why should maximizing the average utility be so special? What’s wrong with an agent that maximizes the weighted sum of the cubes of the possible utilities, or tries to minimize the worst possible loss? Could an agent act rationally just by expressing preferences between states, without giving them numeric values? Finally, why should a utility function with the required properties exist at all? We shall see.
15.2.1Constraints on rational preferences
These questions can be answered by writing down some constraints on the preferences that a rational agent should have and then showing that the MEU principle can be derived from the constraints. We use the following notation to describe an agent’s preferences:







A≻B
...

#### 15.3 Utility Functions




Artificial Intelligence: A Modern Approach














15.3Utility Functions
Utility functions map from lotteries to real numbers. We know they must obey the axioms of orderability, transitivity, continuity, substitutability, monotonicity, and decomposability. Is that all we can say about utility functions? Strictly speaking, that is it: an agent can have any preferences it likes. For example, an agent might prefer to have a prime number of dollars in its bank account; in which case, if it had $16 it would give away $3. This might be unusual, but we can’t call it irrational. An agent might prefer a dented 1973 Ford Pinto to a shiny new Mercedes. The agent might prefer prime numbers of dollars only when it owns the Pinto, but when it owns the Mercedes, it might prefer more dollars to fewer. Fortunately, the preferences of real agents are usually more systematic and thus easier to deal with.
15.3.1Utility assessment and utility scales
If we want to build a decision-theoretic system ...

#### 15.4 Multiattribute Utility Functions




Artificial Intelligence: A Modern Approach














15.4Multiattribute Utility Functions
Decision making in the field of public policy involves high stakes, in both money and lives. For example, in deciding what levels of harmful emissions to allow from a power plant, policy makers must weigh the prevention of death and disability against the benefit of the power and the economic burden of mitigating the emissions. Picking a site for a new airport requires consideration of the disruption caused by construction; the cost of land; the distance from centers of population; the noise of flight operations; safety issues arising from local topography and weather conditions; and so on. Problems like these, in which outcomes are characterized by two or more attributes, are handled by multiattribute utility theory. In essence, it’s the theory of comparing apples to oranges.

Let the attributes be X = X1,...,Xn and let x = 〈x1,...,xn〉 be a complete vector of assignments, where each xi is ...

#### 15.5 Decision Networks




Artificial Intelligence: A Modern Approach














15.5Decision Networks
In this section, we look at a general mechanism for making rational decisions. The notation is often called an influence diagram (Howard and Matheson, 1984), but we will use the more descriptive term decision network. Decision networks combine Bayesian networks with additional node types for actions and utilities. We use the problem of picking an airport site as an example.


15.5.1Representing a decision problem with a decision network
In its most general form, a decision network represents information about the agent’s current state, its possible actions, the state that will result from the agent’s action, and the utility of that state. It therefore provides a substrate for implementing utility-based agents of the type first introduced in Section 2.4.5. Figure 15.6 shows a decision network for the airport-siting problem. It illustrates the three types of nodes used:




×
Figure 15.6A decision network f...

#### 15.6 The Value of Information




Artificial Intelligence: A Modern Approach














15.6The Value of Information
In the preceding analysis, we have assumed that all relevant information, or at least all available information, is provided to the agent before it makes its decision. In practice, this is hardly ever the case. One of the most important parts of decision making is knowing what questions to ask. For example, a doctor cannot expect to be provided with the results of all possible diagnostic tests and questions at the time a patient first enters the consulting room. Tests are often expensive and sometimes hazardous (both directly and because of associated delays). Their importance depends on two factors: whether the test results would lead to a significantly better treatment plan, and how likely the various test results are.
This section describes information value theory, which enables an agent to choose what information to acquire. We assume that prior to selecting a “real” action represented by the ...

#### 15.7 Unknown Preferences




Artificial Intelligence: A Modern Approach














15.7Unknown Preferences
In this section we discuss what happens when there is uncertainty about the utility function whose expected value is to be optimized. There are two versions of this problem: one in which an agent (machine or human) is uncertain about its own utility function, and another in which a machine is supposed to help a human but is uncertain about what the human wants.
15.7.1Uncertainty about one’s own preferences
Imagine that you are at an ice-cream shop in Thailand and they have only two flavors left: vanilla and durian. Both cost $2. You know you have a moderate liking for vanilla and you’d be willing to pay up to $3 for a vanilla ice cream on such a hot day, so there is a net gain of $1 for choosing vanilla. On the other hand, you have no idea whether you like durian or not, but you’ve read on Wikipedia that the durian elicits different responses from different people: some find that “it surpasses in flavou...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter shows how to combine utility theory with probability to enable an agent to select actions that will maximize its expected performance.

•Probability theory describes what an agent should believe on the basis of evidence, utility theory describes what an agent wants, and decision theory puts the two together to describe what an agent should do.
•We can use decision theory to build a system that makes decisions by considering all possible actions and choosing the one that leads to the best expected outcome. Such a system is known as a rational agent.
•Utility theory shows that an agent whose preferences between lotteries are consistent with a set of simple axioms can be described as possessing a utility function; furthermore, the agent selects actions as if maximizing its expected utility.
•Multiattribute utility theory deals with utilities that depend on several distinct attributes of states. Stochastic dom...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
In the 17th century treatise L’art de Penser, or Port-Royal Logic, Arnauld (1662) states:

To judge what one must do to obtain a good or avoid an evil, it is necessary to consider not only the good and the evil in itself, but also the probability that it happens or does not happen; and to view geometrically the proportion that all these things have together.

Modern texts talk of utility rather than good and evil, but this statement correctly notes that one should multiply utility by probability (“view geometrically”) to give expected utility, and maximize that over all outcomes (“all these things”) to “judge what one must do.” It is remarkable how much Arnauld got right, more than 350 years ago, and only 8 years after Pascal and Fermat first showed how to use probability correctly.
Daniel Bernoulli (1738), investigating the St. Petersburg paradox (see Exercise 15.STPT), was the first to re...

### 16 Making Complex Decisions



#### 16.1 Sequential Decision Problems




Artificial Intelligence: A Modern Approach














16.1Sequential Decision Problems
Suppose that an agent is situated in the 4 × 3 environment shown in Figure 16.1 (a). Beginning in the start state, it must choose an action at each time step. The interaction with the environment terminates when the agent reaches one of the goal states, marked +1 or −1. Just as for search problems, the actions available to the agent in each state are given by ACTIONS(s), sometimes abbreviated to A (s); in the 4 × 3 environment, the actions in every state are Up, Down, Left, and Right. We assume for now that the environment is fully observable, so that the agent always knows where it is.






Description

Part (“a”): Three points labeled "A", B, and C are arranged in the form of a circle in the counterclockwise direction. An arrow in the clockwise direction labeled 1 cent connects every two points. Part (b) has two parts: top and bottom. Top part: Two lines from a point are labeled p and 1 minu...

#### 16.2 Algorithms for MDPs




Artificial Intelligence: A Modern Approach














16.2Algorithms for MDPs
In this section, we present four different algorithms for solving MDPs. The first three, value iteration, policy iteration, and linear programming, generate exact solutions offline. The fourth is a family of online approximate algorithms that includes Monte Carlo planning.

16.2.1Value Iteration
The Bellman equation (Equation (16.5)) is the basis of the value iteration algorithm for solving MDPs. If there are n possible states, then there are n Bellman equations, one for each state. The n equations contain n unknowns—the utilities of the states. So we would like to solve these simultaneous equations to find the utilities. There is one problem: the equations are nonlinear, because the “max” operator is not a linear operator. Whereas systems of linear equations can be solved quickly using linear algebra techniques, systems of nonlinear equations are more problematic. One thing to try is an iterative appro...

#### 16.3 Bandit Problems




Artificial Intelligence: A Modern Approach














16.3Bandit Problems
In Las Vegas, a one-armed bandit is a slot machine. A gambler can insert a coin, pull the lever, and collect the winnings (if any). An n-armed bandit has n levers. Behind each lever is a fixed but unknown probability distribution of winnings; each pull samples from that unknown distribution.

The gambler must choose which lever to play on each successive coin–the one that has paid off best, or maybe one that has not been tried yet? This is an example of the ubiquitous tradeoff between exploitation of the current best action to obtain rewards and exploration of previously unknown states and actions to gain information, which can in some cases be converted into a better policy and better long-term rewards. In the real world, one constantly has to decide between continuing in a comfortable existence, versus striking out into the unknown in the hopes of a better life.
The n-armed bandit problem is a formal mode...

#### 16.4 Partially Observable MDPs




Artificial Intelligence: A Modern Approach














16.4Partially Observable MDPs
The description of Markov decision processes in Section 16.1 assumed that the environment was fully observable. With this assumption, the agent always knows which state it is in. This, combined with the Markov assumption for the transition model, means that the optimal policy depends only on the current state.
When the environment is only partially observable, the situation is, one might say, much less clear. The agent does not necessarily know which state it is in, so it cannot execute the action π(s) recommended for that state. Furthermore, the utility of a state s and the optimal action in s depend not just on s, but also on how much the agent knows when it is in s. For these reasons, partially observable MDPs (or POMDPs–pronounced “pom–dee–pees”) are usually viewed as much more difficult than ordinary MDPs. We cannot avoid POMDPs, however, because the real world is one.

16.4.1Definition of PO...

#### 16.5 Algorithms for Solving POMDPs




Artificial Intelligence: A Modern Approach














16.5Algorithms for Solving POMDPs
We have shown how to reduce POMDPs to MDPs, but the MDPs we obtain have a continuous (and usually high–dimensional) state space. This means we will have to redesign the dynamic programming algorithms from Sections 16.2.1 and 16.2.2, which assumed a finite state space and a finite number of actions. Here we describe a value iteration algorithm designed specifically for POMDPs, followed by an online decision-making algorithm similar to those developed for games in Chapter 6.
16.5.1Value iteration for POMDPs
Section 16.2.1 described a value iteration algorithm that computed one utility value for each state. With infinitely many belief states, we need to be more creative. Consider an optimal policy π* and its application in a specific belief state b: the policy generates an action, then, for each subsequent percept, the belief state is updated and a new action is generated, and so on. For this spe...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter shows how to use knowledge about the world to make decisions even when the outcomes of an action are uncertain and the rewards for acting might not be reaped until many actions have passed. The main points are as follows:

•Sequential decision problems in stochastic environments, also called Markov decision processes, or MDPs, are defined by a transition model specifying the probabilistic outcomes of actions and a reward function specifying the reward in each state.
•The utility of a state sequence is the sum of all the rewards over the sequence, possibly discounted over time. The solution of an MDP is a policy that associates a decision with every state that the agent might reach. An optimal policy maximizes the utility of the state sequences encountered when it is executed.
•The utility of a state is the expected sum of rewards when an optimal policy is executed from that state. The value iteration algor...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Richard Bellman developed the ideas underlying the modern approach to sequential decision problems while working at the RAND Corporation beginning in 1949. According to his autobiography (Bellman, 1984), he coined the term “dynamic programming” to hide from a research-phobic Secretary of Defense, Charles Wilson, the fact that his group was doing mathematics. (This cannot be strictly true, because his first paper using the term (Bellman, 1952) appeared before Wilson became Secretary of Defense in 1953.) Bellman’s book, Dynamic Programming (1957), gave the new field a solid foundation and introduced the value iteration algorithm.
Shapley (1953b) actually described the value iteration algorithm independently of Bellman, but his results were not widely appreciated in the operations research community, perhaps because they were presented in the more general context of Markov games. Although the ...

### 17 Multiagent Decision Making



#### 17.1 Properties of Multiagent Environments




Artificial Intelligence: A Modern Approach














17.1Properties of Multiagent Environments
So far, we have largely assumed that only one agent has been doing the sensing, planning, and acting. But this represents a huge simplifying assumption, which fails to capture many real-world AI settings. In this chapter, therefore, we will consider the issues that arise when an agent must make decisions in environments that contain multiple actors. Such environments are called multiagent systems, and agents in such a system face a multiagent planning problem. However, as we will see, the precise nature of the multiagent planning problem—and the techniques that are appropriate for solving it—will depend on the relationships among the agents in the environment.


17.1.1One decision maker
The first possibility is that while the environment contains multiple actors, it contains only one decision maker. In such a case, the decision maker develops plans for the other agents, and tells them ...

#### 17.2 Non-Cooperative Game Theory




Artificial Intelligence: A Modern Approach














17.2Non-Cooperative Game Theory
We will now introduce the key concepts and analytical techniques of game theory—the theory that underpins decision making in multiagent environments. Our tour will start with noncooperative game theory.
17.2.1Games with a single move: Normal form games
The first game model we will look at is one in which all players take action simultaneously and the result of the game is based on the profile of actions that are selected in this way. (Actually, it is not crucial that the actions take place at the same time; what matters is that no player has knowledge of the other players’ choices.) These games are called normal form games. A normal form game is defined by three components:


•Players or agents who will be making decisions. Two-player games have received the most attention, although n-player games for n > 2 are also common. We give players capitalized names, like Ali and Bo or O and E.

•Actions...

#### 17.3 Cooperative Game Theory




Artificial Intelligence: A Modern Approach














17.3Cooperative Game Theory
Recall that cooperative games capture decision making scenarios in which agents can form binding agreements with one another to cooperate. They can then benefit from receiving extra value compared to what they would get by acting alone.
We start by introducing a model for a class of ooperative games. Formally, these games are called “cooperative games with transferable utility in characteristic function form.” The idea of the model is that when a group of agents cooperate, the group as a whole obtains some utility value, which can then be split among the group members. The model does not say what actions the agents will take, nor does the game structure itself specify how the value obtained will be split up (that will come later).
Formally, we use the formula G = (N, v) to say that a cooperative game, G, is defined by a set of players N = {1,...,n} and a characteristic function, v, which for every s...

#### 17.4 Making Collective Decisions




Artificial Intelligence: A Modern Approach














17.4Making Collective Decisions
We will now turn from agent design to mechanism design—the problem of designing the right game for a collection of agents to play. Formally, a mechanism consists of

1.A language for describing the set of allowable strategies that agents may adopt.
2.A distinguished agent, called the center, that collects reports of strategy choices from the agents in the game. (For example, the auctioneer is the center in an auction.)

3.An outcome rule, known to all agents, that the center uses to determine the payoffs to each agent, given their strategy choices.

This section discusses some of the most important mechanisms.
17.4.1Allocating tasks with the contract net
The contract net protocol is probably the oldest and most important multiagent problemsolving technique studied in AI. It is a high‑level protocol for task sharing. As the name suggests, the contract net was inspired from the way that companies ...

#### Summary




Artificial Intelligence: A Modern Approach














Summary

•Multiagent planning is necessary when there are other agents in the environment with which to cooperate or compete. Joint plans can be constructed, but must be augmented with some form of coordination if two agents are to agree on which joint plan to execute.
•Game theory describes rational behavior for agents in situations in which multiple agents interact. Game theory is to multiagent decision making as decision theory is to single-agent decision making.
•Solution concepts in game theory are intended to characterize rational outcomes of a game—outcomes that might occur if every agent acted rationally.
•Non-cooperative game theory assumes that agents must make their decisions independently. Nash equilibrium is the most important solution concept in non-cooperative game theory. A Nash equilibrium is a strategy profile in which no agent has an incentive to deviate from its specified strategy. We have techniques for de...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
It is a curiosity of the field that researchers in AI did not begin to seriously consider the issues surrounding interacting agents until the 1980s—and the multiagent systems field did not really become established as a distinctive subdiscipline of AI until a decade later. Nevertheless, ideas that hint at multiagent systems were present in the 1970s. For example, in his highly influential Society of Mind theory, Marvin Minsky (1986, 2007) proposed that human minds are constructed from an ensemble of agents. Doug Lenat had similar ideas in a framework he called BEINGS (Lenat, 1975). In the 1970s, building on his PhD work on the PLANNER system, Carl Hewitt proposed a model of computation as interacting agents called the actor model, which has become established as one of the fundamental models in concurrent computation (Hewitt, 1977; Agha, 1986).
The prehistory of the multiagent systems field...

### 18 Probabilistic Programming



#### 18.1 Relational Probability Models




Artificial Intelligence: A Modern Approach














18.1Relational Probability Models
Recall from Chapter 12 that a probability model defines a set Ω of possible worlds with a probability P(ω) for each world ω. For Bayesian networks, the possible worlds are assignments of values to variables; for the Boolean case in particular, the possible worlds are identical to those of propositional logic.
For a first-order probability model, then, it seems we need the possible worlds to be those of first-order logic—that is, a set of objects with relations among them and an interpretation that maps constant symbols to objects, predicate symbols to relations, and function symbols to functions on those objects. (See Section 8.2.) The model also needs to define a probability for each such possible world, just as a Bayesian network defines a probability for each assignment of values to variables.
Let us suppose, for a moment, that we have figured out how to do this. Then, as usual (see page 40...

#### 18.2 Open-Universe Probability Models




Artificial Intelligence: A Modern Approach














18.2Open-Universe Probability Models
We argued earlier that database semantics was appropriate for situations in which we know exactly the set of relevant objects that exist and can identify them unambiguously. (In particular, all observations about an object are correctly associated with the constant symbol that names it.) In many real-world settings, however, these assumptions are simply untenable. For example, a book retailer might use an ISBN (International Standard Book Number) as a constant symbol to name each book, even though a given “logical” book (e.g., “Gone With the Wind”) may have several ISBNs corresponding to hardcover, paperback, large print, reissues, and so on. It would make sense to aggregate recommendations across multiple ISBNs, but the retailer may not know for sure which ISBNs are really the same book. (Note that we are not reifying the individual copies of the book, which might be necessary for used-boo...

#### 18.3 Keeping Track of a Complex World




Artificial Intelligence: A Modern Approach














18.3Keeping Track of a Complex World
Chapter 14 considered the problem of keeping track of the state of the world, but covered only the case of atomic representations (HMMs) and factored representations (DBNs and Kalman filters). This makes sense for worlds with a single object—perhaps a single patient in the intensive care unit or a single bird flying through the forest. In this section, we see what happens when two or more objects generate the observations. What makes this case different from plain old state estimation is that there is now the possibility of uncertainty about which object generated which observation. This is the identity uncertainty problem of Section 18.2 (page 648), now viewed in a temporal context. In the control theory literature, this is the data association problem—that is, the problem of associating observation data with the objects that generated them. Although we could view this as yet another examp...

#### 18.4 Programs as Probability Models




Artificial Intelligence: A Modern Approach














18.4Programs as Probability Models
Many probabilistic programming languages have been built on the insight that probability models can be defined using executable code in any programming language that incorporates a source of randomness. For such models, the possible worlds are execution traces and the probability of any such trace is the probability of the random choices required for that trace to happen. PPLs created in this way inherit all of the expressive power of the underlying language, including complex data structures, recursion, and, in some cases, higher-order functions. Many PPLs are in fact computationally universal: they can represent any probability distribution that can be sampled from by a probabilistic Turing machine that halts.
18.4.1Example: Reading text
We illustrate this approach to probabilistic modeling and inference via the problem of writing a program that reads degraded text. These kinds of models ca...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has explored expressive representations for probability models based on both logic and programs.

• Relational probability models (RPMs) define probability models on worlds derived from the database semantics for first-order languages; they are appropriate when all the objects and their identities are known with certainty.
•Given an RPM, the objects in each possible world correspond to the constant symbols in the RPM, and the basic random variables are all possible instantiations of the predicate symbols with objects replacing each argument. Thus, the set of possible worlds is finite.
•RPMs provide very concise models for worlds with large numbers of objects and can handle relational uncertainty.
• Open-universe probability models (OUPMs) build on the full semantics of first-order logic, allowing for new kinds of uncertainty such as identity and existence uncertainty.
• Generative programs are representati...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Hailperin (1984) and Howson (2003) recount the long history of attempts to connect probability and logic, going back to Leibniz’s Nouveaux Essais in 1704. These attempts usually involved probabilities attached directly to logical sentences. The first rigorous treatment was Gaifman’s propositional probability logic (Gaifman, 1964b). The idea is that a probability assertion P(ф) ≥ p is a constraint on the distribution over possible worlds, just as an ordinary logical sentence is a constraint on the possible worlds themselves. Any distribution P that satisfies the constraint is a model, in the standard logical sense, of the probability assertion, and one probability assertion entails another just when the models of the first are a subset of the models of the second.

Within such a logic, one can prove, for example, that 

P(α∧β)≤P(α⇒β)
 Satisfiability of sets of probability assertions can be d...

## V Machine Learning



### 19 Learning from Examples



#### 19.1 Forms of Learning




Artificial Intelligence: A Modern Approach














19.1Forms of Learning
Any component of an agent program can be improved by machine learning. The improvements, and the techniques used to make them, depend on these factors:

•Which component is to be improved.
•What prior knowledge the agent has, which influences the model it builds.
•What data and feedback on that data is available.
Chapter 2 described several agent designs. The components of these agents include:

1.A direct mapping from conditions on the current state to actions.
2.A means to infer relevant properties of the world from the percept sequence.
3.Information about the way the world evolves and about the results of possible actions the agent can take.
4.Utility information indicating the desirability of world states.
5.Action-value information indicating the desirability of actions.
6.Goals that describe the most desirable states.
7.A problem generator, critic, and learning element that enable the system to imp...

#### 19.2 Supervised Learning




Artificial Intelligence: A Modern Approach














19.2Supervised Learning
More formally, the task of supervised learning is this:

Given a training set of N example input-output pairs



(
x
1

,
y
1

), (
x
2

,
y
2

),… (
x
N

,
y
N

).



where each pair was generated by an unknown function y = f (x), discover a function h that approximates the true function f.
The function h is called a hypothesis about the world. It is drawn from a hypothesis space  of possible functions. For example, the hypothesis space might be the set of polynomials of degree 3; or the set of Javascript functions; or the set of 3-SAT Boolean logic formulas.

With alternative vocabulary, we can say that h is a model of the data, drawn from a model class , or we can say a function drawn from a function class. We call the output yi the ground truth—the true answer we are asking our model to predict.


How do we choose a hypothesis space? We might have some prior knowledge about the process that generate...

#### 19.3 Learning Decision Trees




Artificial Intelligence: A Modern Approach














19.3Learning Decision Trees
A decision tree is a representation of a function that maps a vector of attribute values to a single output value—a “decision.” A decision tree reaches its decision by performing a sequence of tests, starting at the root and following the appropriate branch until a leaf is reached. Each internal node in the tree corresponds to a test of the value of one of the input attributes, the branches from the node are labeled with the possible values of the attribute, and the leaf nodes specify what value is to be returned by the function.

In general, the input and output values can be discrete or continuous, but for now we will consider only inputs consisting of discrete values and outputs that are either true (a positive example) or false (a negative example). We call this Boolean classification. We will use j to index the examples (xj is the input vector for the jth example and yj is the output), and xj,i...

#### 19.4 Model Selection and Optimization




Artificial Intelligence: A Modern Approach














19.4Model Selection and Optimization
Our goal in machine learning is to select a hypothesis that will optimally fit future examples. To make that precise we need to define “future example” and “optimal fit.”
First we will make the assumption that the future examples will be like the past. We call this the stationarity assumption; without it, all bets are off. We assume that each example Ej has the same prior probability distribution:




P(
E
j

) = P(
E

j+1

) = P(
E

j
+2) =⋯,


and is independent of the previous examples:



P(
E
j

) = P(
E
j

|
E

j−1

, 
E

j−2

,⋯).


Examples that satisfy these equations are independent and identically distributed or i.i.d..

The next step is to define “optimal fit.” For now, we will say that the optimal fit is the hypothesis that minimizes the error rate: the proportion of times that h(x) ≠ y for an (x, y) example. (Later we will expand on this to allow different errors to have diffe...

#### 19.5 The Theory of Learning




Artificial Intelligence: A Modern Approach














19.5The Theory of Learning
How can we be sure that our learned hypothesis will predict well for previously unseen inputs? That is, how do we know that the hypothesis h is close to the target function f if we don’t know what f is? These questions have been pondered for centuries, by Ockham, Hume, and others. In recent decades, other questions have emerged: how many examples do we need to get a good h? What hypothesis space should we use? If the hypothesis space is very complex, can we even find the best h, or do we have to settle for a local maximum? How complex should h be? How do we avoid overfitting? This section examines these questions.
We’ll start with the question of how many examples are needed for learning. We saw from the learning curve for decision tree learning on the restaurant problem (Figure 19.7 on page 679) that accuracy improves with more training data. Learning curves are useful, but they are specific to a pa...

#### 19.6 Linear Regression and Classification




Artificial Intelligence: A Modern Approach














19.6Linear Regression and Classification
Now it is time to move on from decision trees and lists to a different hypothesis space, one that has been used for hundreds of years: the class of linear functions of continuous-valued inputs. We’ll start with the simplest case: regression with a univariate linear function, otherwise known as “fitting a straight line.” Section 19.6.3 covers the multivariable case. Sections 19.6.4 and 19.6.5 show how to turn linear functions into classifiers by applying hard and soft thresholds.

19.6.1Univariate linear regression
A univariate linear function (a straight line) with input x and output y has the form y = w1x + w0, where w0 and w1 are real-valued coefficients to be learned. We use the letter w because we think of the coefficients as weights; the value of y is changed by changing the relative weight of one term or another. We’ll define w to be the vector 〈w0, w1 〉, and define the linear fun...

#### 19.7 Nonparametric Models




Artificial Intelligence: A Modern Approach














19.7Nonparametric Models
Linear regression uses the training data to estimate a fixed set of parameters w. That defines our hypothesis hw(x), and at that point we can throw away the training data, because they are all summarized by w. A learning model that summarizes data with a set of parameters of fixed size (independent of the number of training examples) is called a parametric model.

When data sets are small, it makes sense to have a strong restriction on the allowable hypotheses, to avoid overfitting. But when there are millions or billions of examples to learn from, it seems like a better idea to let the data speak for themselves rather than forcing them to speak through a tiny vector of parameters. If the data say that the correct answer is a very wiggly function, we shouldn’t restrict ourselves to linear or slightly wiggly functions.
A nonparametric model is one that cannot be characterized by a bounded set of paramet...

#### 19.8 Ensemble Learning




Artificial Intelligence: A Modern Approach














19.8Ensemble Learning
So far we have looked at learning methods in which a single hypothesis is used to make predictions. The idea of ensemble learning is to select a collection, or ensemble, of hypotheses, h1, h2,...,hn, and combine their predictions by averaging, voting, or by another level of machine learning. We call the individual hypotheses base models and their combination an ensemble model.



There are two reasons to do this. The first is to reduce bias. The hypothesis space of a base model may be too restrictive, imposing a strong bias (such as the bias of a linear decision boundary in logistic regression). An ensemble can be more expressive, and thus have less bias, than the base models. Figure 19.23 shows that an ensemble of three linear classifiers can represent a triangular region that could not be represented by a single linear classifier. An ensemble of n linear classifiers allows more functions to be realizabl...

#### 19.9 Developing Machine Learning Systems




Artificial Intelligence: A Modern Approach














19.9Developing Machine Learning Systems
In this chapter we have concentrated on explaining the theory of machine learning. The practice of using machine learning to solve practical problems is a separate discipline. Over the last 50 years, the software industry has evolved a software development methodology that makes it more likely that a (traditional) software project will be a success. But we are still in the early stages of defining a methodology for machine learning projects; the tools and techniques are not as well-developed. Here is a breakdown of typical steps in the process.
19.9.1Problem formulation
The first step is to Figure out what problem you want to solve. There are two parts to this. First ask, “what problem do I want to solve for my users?” An answer such as “make it easier for users to organize and access their photos” is too vague; “help a user find all photos that match a specific term, such as Paris” is b...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter introduced machine learning, and focused on supervised learning from examples. The main points were:

•Learning takes many forms, depending on the nature of the agent, the component to be improved, and the available feedback.
•If the available feedback provides the correct answer for example inputs, then the learning problem is called supervised learning. The task is to learn a function y = h(x). Learning a function whose output is a continuous or ordered value (like weight) is called regression; learning a function with a small number of possible output categories is called classification;
•We want to learn a function that not only agrees with the data but also is likely to agree with future data. We need to balance agreement with the data against simplicity of the hypothesis.
•Decision trees can represent all Boolean functions. The information-gain heuristic provides an efficient method for finding a sim...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Chapter 1 covered the history of philosophical investigations into the topic of inductive learning. William of Ockham (1280–1349), the most influential philosopher of his century and a major contributor to medieval epistemology, logic, and metaphysics, is credited with a statement called “Ockham’s Razor”—in Latin, Entia non sunt multiplicanda praeter necessitatem, and in English, “Entities are not to be multiplied beyond necessity.” Unfortunately, this laudable piece of advice is nowhere to be found in his writings in precisely these words (although he did say “Pluralitas non est ponenda sine necessitate,” or “Plurality shouldn’t be posited without necessity”). A similar sentiment was expressed by Aristotle in 350 BCE in Physics book I, chapter VI: “For the more limited, if adequate, is always preferable.”
David Hume (1711–1776) formulated the problem of induction, recognizing that generali...

### 20 Knowledge in Learning



#### 20.1 A Logical Formulation of Learning




Artificial Intelligence: A Modern Approach














20.1A Logical Formulation of Learning
Chapter 19 defined pure inductive learning as a process of finding a hypothesis that agrees with the observed examples. Here, we specialize this definition to the case where the hypothesis is represented by a set of logical sentences. Example descriptions and classifications will also be logical sentences, and a new example can be classified by inferring a classification sentence from the hypothesis and the example description. This approach allows for incremental construction of hypotheses, one sentence at a time. It also allows for prior knowledge, because sentences that are already known can assist in the classification of new examples. The logical formulation of learning may seem like a lot of extra work at first, but it turns out to clarify many of the issues in learning. It enables us to go well beyond the simple learning methods of Chapter 19 by using the full power of logical infer...

#### 20.2 Knowledge in Learning




Artificial Intelligence: A Modern Approach














20.2Knowledge in Learning
The preceding section described the simplest setting for inductive learning. To understand the role of prior knowledge, we need to talk about the logical relationships among hypotheses, example descriptions, and classifications. Let Descriptions denote the conjunction of all the example descriptions in the training set, and let Classifications denote the conjunction of all the example classifications. Then a Hypothesis that “explains the observations” must satisfy the following property (recall that ⊨ means “logically entails”):







Hypothesis∧Descriptions⊨Classifications .



       (20.3)





We call this kind of relationship an entailment constraint, in which Hypothesis is the “unknown.” Pure inductive learning means solving this constraint, where Hypothesis is drawn from some predefined hypothesis space. For example, if we consider a decision tree as a logical formula (see Equation (20.1) on p...

#### 20.3 Explanation-Based Learning




Artificial Intelligence: A Modern Approach














20.3Explanation-Based Learning
Explanation-based learning is a method for extracting general rules from individual observations. As an example, consider the problem of differentiating and simplifying algebraic expressions (Exercise 9.17). If we differentiate an expression such as X2 with respect to X, we obtain 2X. (We use a capital letter for the arithmetic unknown X, to distinguish it from the logical variable x.) In a logical reasoning system, the goal might be expressed as ASK(Derivative(X2, X) = d, KB), with solution d = 2X.
Anyone who knows differential calculus can see this solution “by inspection” as a result of practice in solving such problems. A student encountering such problems for the first time, or a program with no experience, will have a much more difficult job. Application of the standard rules of differentiation eventually yields the expression 1 × (2 × (X(2–1))), and eventually this simplifies to 2X. In the...

#### 20.4 Learning Using Relevance Information




Artificial Intelligence: A Modern Approach














20.4Learning Using Relevance Information
Our traveler in Brazil seems to be able to make a confident generalization concerning the language spoken by other Brazilians. The inference is sanctioned by her background knowledge, namely, that people in a given country (usually) speak the same language. We can express this in first-order logic as follows:2







Nationality(x,n)∧Nationality(y,n)∧Language(x,l)⇒Language(y,l).



              (20.6)





(Literal translation: “If x and y have the same nationality n and x speaks language l, then y also speaks it.”) It is not difficult to show that, from this sentence and the observation that



Nationality(Fernando,Brazil)∧Language(Fernando,Portuguese),


the following conclusion is entailed (see Exercise 20.1):



Nationality(x,Brazil) ⇒ Language (x,Portuguese).


Sentences such as (20.6) express a strict form of relevance: given nationality, language is fully determined. (Put anothe...

#### 20.5 Inductive Logic Programming




Artificial Intelligence: A Modern Approach














20.5Inductive Logic Programming
Inductive logic programming (ILP) combines inductive methods with the power of first-order representations, concentrating in particular on the representation of hypotheses as logic programs.3 It has gained popularity for three reasons. First, ILP offers a rigorous approach to the general knowledge-based inductive learning problem. Second, it offers complete algorithms for inducing general, first-order theories from examples, which can therefore learn successfully in domains where attribute-based algorithms are hard to apply. An example is in learning how protein structures fold (Figure 20.10). The three-dimensional configuration of a protein molecule cannot be represented reasonably by a set of attributes, because the configuration inherently refers to relationships between objects, not to attributes of a single object. First-order logic is an appropriate language for describing the relationship...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has investigated various ways in which prior knowledge can help an agent to learn from new experiences. Because much prior knowledge is expressed in terms of relational models rather than attribute-based models, we have also covered systems that allow learning of relational models. The important points are:

•The use of prior knowledge in learning leads to a picture of cumulative learning, in which learning agents improve their learning ability as they acquire more knowledge.
•Prior knowledge helps learning by eliminating otherwise consistent hypotheses and by “filling in” the explanation of examples, thereby allowing for shorter hypotheses. These contributions often result in faster learning from fewer examples.
•Understanding the different logical roles played by prior knowledge, as expressed by entailment constraints, helps to define a variety of learning techniques.
•Explanation-based learning (EBL) ex...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Although the use of prior knowledge in learning would seem to be a natural topic for philosophers of science, little formal work was done until quite recently. Fact, Fiction, and Forecast, by the philosopher Nelson Goodman (1954), refuted the earlier supposition that induction was simply a matter of seeing enough examples of some universally quantified proposition and then adopting it as a hypothesis. Consider, for example, the hypothesis “All emeralds are grue,” where grue means “green if observed before time t, but blue if observed thereafter.” At any time up to t, we might have observed millions of instances confirming the rule that emeralds are grue, and no disconfirming instances, and yet we are unwilling to adopt the rule. This can be explained only by appeal to the role of relevant prior knowledge in the induction process. Goodman proposes a variety of different kinds of prior knowle...

### 21 Learning Probabilistic Models



#### 21.1 Statistical Learning




Artificial Intelligence: A Modern Approach














21.1Statistical Learning
The key concepts in this chapter, just as in Chapter 19, are data and hypotheses. Here, the data are evidence—that is, instantiations of some or all of the random variables describing the domain. The hypotheses in this chapter are probabilistic theories of how the domain works, including logical theories as a special case.
Consider a simple example. Our favorite surprise candy comes in two flavors: cherry (yum) and lime (ugh). The manufacturer has a peculiar sense of humor and wraps each piece of candy in the same opaque wrapper, regardless of flavor. The candy is sold in very large bags, of which there are known to be five kinds—again, indistinguishable from the outside:








h
1

: 100% cherry,






h
2

: 75% cherry + 25% lime,






h
3

: 50% cherry + 50% lime,






h
4

: 25% cherry + 75% lime,






h
5

: 100% lime.





Given a new bag of candy, the random variable H (for hypothesis) deno...

#### 21.2 Learning with Complete Data




Artificial Intelligence: A Modern Approach














21.2Learning with Complete Data
The general task of learning a probability model, given data that are assumed to be generated from that model, is called density estimation. (The term applied originally to probability density functions for continuous variables, but it is used now for discrete distributions too.) Density estimation is a form of unsupervised learning. This section covers the simplest case, where we have complete data. Data are complete when each data point contains values for every variable in the probability model being learned. We focus on parameter learning—finding the numerical parameters for a probability model whose structure is fixed. For example, we might be interested in learning the conditional probabilities in a Bayesian network with a given structure. We will also look briefly at the problem of learning structure and at nonparametric density estimation.



21.2.1Maximum-likelihood parameter learning: ...

#### 21.3 Learning with Hidden Variables: The EM Algorithm




Artificial Intelligence: A Modern Approach














21.3Learning with Hidden Variables: The EM Algorithm
The preceding section dealt with the fully observable case. Many real-world problems have hidden variables (sometimes called latent variables), which are not observable in the data. For example, medical records often include the observed symptoms, the physician’s diagnosis, the treatment applied, and perhaps the outcome of the treatment, but they seldom contain a direct observation of the disease itself! (Note that the diagnosis is not the disease; it is a causal consequence of the observed symptoms, which are in turn caused by the disease.) One might ask, “If the disease is not observed, could we construct a model based only on the observed variables?” The answer appears in Figure 21.11, which shows a small, fictitious diagnostic model for heart disease. There are three observable predisposing factors and three observable symptoms (which are too depressing to name). Assume ...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
Statistical learning methods range from simple calculation of averages to the construction of complex models such as Bayesian networks. They have applications throughout computer science, engineering, computational biology, neuroscience, psychology, and physics. This chapter has presented some of the basic ideas and given a flavor of the mathematical underpinnings. The main points are as follows:

•Bayesian learning methods formulate learning as a form of probabilistic inference, using the observations to update a prior distribution over hypotheses. This approach provides a good way to implement Ockham’s razor, but quickly becomes intractable for complex hypothesis spaces.
•Maximum a posteriori (MAP) learning selects a single most likely hypothesis given the data. The hypothesis prior is still used and the method is often more tractable than full Bayesian learning.
•Maximum-likelihood learning simply selects the hypoth...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The application of statistical learning techniques in AI was an active area of research in the early years (see Duda and Hart, 1973) but became separated from mainstream AI as the latter field concentrated on symbolic methods. A resurgence of interest occurred shortly after the introduction of Bayesian network models in the late 1980s; at roughly the same time, a statistical view of neural network learning began to emerge. In the late 1990s, there was a noticeable convergence of interests in machine learning, statistics, and neural networks, centered on methods for creating large probabilistic models from data.
The naive Bayes model is one of the oldest and simplest forms of Bayesian network, dating back to the 1950s. Its origins were mentioned in Chapter 12. Its surprising success is partially explained by Domingos and Pazzani (1997). A boosted form of naive Bayes learning won the first KD...

### 22 Deep Learning



#### 22.1 Simple Feedforward Networks




Artificial Intelligence: A Modern Approach














22.1Simple Feedforward Networks
A feedforward network, as the name suggests, has connections only in one direction—that is, it forms a directed acyclic graph with designated input and output nodes. Each node computes a function of its inputs and passes the result to its successors in the network. Information flows through the network from the input nodes to the output nodes, and there are no loops. A recurrent network, on the other hand, feeds its intermediate or final outputs back into its own inputs. This means that the signal values within the network form a dynamical system that has internal state or memory. We will consider recurrent networks in Section 22.6.


Boolean circuits, which implement Boolean functions, are an example of feedforward networks. In a Boolean circuit, the inputs are limited to 0 and 1, and each node implements a simple Boolean function of its inputs, producing a 0 or a 1. In neural networks, input v...

#### 22.2 Computation Graphs for Deep Learning




Artificial Intelligence: A Modern Approach














22.2Computation Graphs for Deep Learning
We have established the basic ideas of deep learning: represent hypotheses as computation graphs with tunable weights and compute the gradient of the loss function with respect to those weights in order to fit the training data. Now we look at how to put together computation graphs. We begin with the input layer, which is where the training or test example x is encoded as values of the input nodes. Then we consider the output layer, where the outputs ŷ are compared with the true values y to derive a learning signal for tuning the weights. Finally, we look at the hidden layers of the network.
22.2.1Input encoding
The input and output nodes of a computational graph are the ones that connect directly to the input data x and the output data y. The encoding of input data is usually straightforward, at least for the case of factored data where each training example contains values for n input...

#### 22.3 Convolutional Networks




Artificial Intelligence: A Modern Approach














22.3Convolutional Networks
We mentioned in Section 22.2.1 that an image cannot be thought of as a simple vector of input pixel values, primarily because adjacency of pixels really matters. If we were to construct a network with fully connected layers and an image as input, we would get the same result whether we trained with unperturbed images or with images all of whose pixels had been randomly permuted. Furthermore, suppose there are n pixels and n units in the first hidden layer, to which the pixels provide input. If the input and the first hidden layer are fully connected, that means n2 weights; for a typical megapixel RGB image, that’s 9 trillion weights. Such a vast parameter space would require correspondingly vast numbers of training images and a huge computational budget to run the training algorithm.
These considerations suggest that we should construct the first hidden layer so that each hidden unit receives input f...

#### 22.4 Learning Algorithms




Artificial Intelligence: A Modern Approach














22.4Learning Algorithms
Training a neural network consists of modifying the network's parameters so as to minimize the loss function on the training set. In principle, any kind of optimization algorithm could be used. In practice, modern neural networks are almost always trained with some variant of stochastic gradient descent (SGD).
We covered standard gradient descent and its stochastic version in Section 19.6.2. Here, the goal is to minimize the loss L(w), where w represents all of the parameters of the network. Each update step in the gradient descent process looks like this:



w←w−α 
∇
w

L(w),


where α is the learning rate. For standard gradient descent, the loss L is defined with respect to the entire training set. For SGD, it is defined with respect to a minibatch of m examples chosen randomly at each step.
As noted in Section 4.2, the literature on optimization methods for high-dimensional continuous spaces includes...

#### 22.5 Generalization




Artificial Intelligence: A Modern Approach














22.5Generalization
So far we have described how to fit a neural network to its training set, but in machine learning the goal is to generalize to new data that has not been seen previously, as measured by performance on a test set. In this section, we focus on three approaches to improving generalization performance: choosing the right network architecture, penalizing large weights, and randomly perturbing the values passing through the network during training.
22.5.1Choosing a network architecture
A great deal of effort in deep learning research has gone into finding network architectures that generalize well. Indeed, for each particular kind of data—images, speech, text, video, and so on—a good deal of the progress in performance has come from exploring different kinds of network architectures and varying the number of layers, their connectivity, and the types of node in each layer.6
Some neural network architectures are exp...

#### 22.6 Recurrent Neural Networks




Artificial Intelligence: A Modern Approach














22.6Recurrent Neural Networks
Recurrent neural networks (RNNs) are distinct from feedforward networks in that they allow cycles in the computation graph. In all the cases we will consider, each cycle has a delay, so that units may take as input a value computed from their own output at an earlier step in the computation. (Without the delay, a cyclic circuit may reach an inconsistent state.) This allows the RNN to have internal state, or memory: inputs received at earlier time steps affect the RNN's response to the current input.

RNNs can also be used to perform more general computations—after all, ordinary computers are just Boolean circuits with memory—and to model real neural systems, many of which contain cyclic connections. Here we focus on the use of RNNs to analyze sequential data, where we assume that a new input vector xt arrives at each time step.
As tools for analyzing sequential data, RNNs can be compared to the hi...

#### 22.7 Unsupervised Learning and Transfer Learning




Artificial Intelligence: A Modern Approach














22.7Unsupervised Learning and Transfer Learning
The deep learning systems we have discussed so far are based on supervised learning, which requires each training example to be labeled with a value for the target function. Although such systems can reach a high level of test-set accuracy—as shown by the ImageNet competition results, for example—they often require far more labeled data than a human would for the same task. For example, a child needs to see only one picture of a giraffe, rather than thousands, in order to be able to recognize giraffes reliably in a wide range of settings and views. Clearly, something is missing in our deep learning story; indeed, it may be the case that our current approach to supervised deep learning renders some tasks completely unattainable because the requirements for labeled data would exceed what the human race (or the universe) can supply. Moreover, even in cases where the task is feasible...

#### 22.8 Applications




Artificial Intelligence: A Modern Approach














22.8Applications
Deep learning has been applied successfully to many important problem areas in AI. For indepth explanations, we refer the reader to the relevant chapters: Chapter 23 for the use of deep learning in reinforcement learning systems, Chapter 25 for natural language processing, Chapter 27 (particularly Section 27.4) for computer vision, and Chapter 26 for robotics.
22.8.1Vision
We begin with computer vision, which is the application area that has arguably had the biggest impact on deep learning, and vice versa. Although deep convolutional networks had been in use since the 1990s for tasks such as handwriting recognition, and neural networks had begun to surpass generative probability models for speech recognition by around 2010, it was the success of the AlexNet deep learning system in the 2012 ImageNet competition that propelled deep learning into the limelight.
The ImageNet competition was a supervised learning t...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter described methods for learning functions represented by deep computational graphs. The main points were:

•Neural networks represent complex nonlinear functions with a network of parameterized linear-threshold units.
•The back-propagation algorithm implements a gradient descent in parameter space to minimize the loss function.
•Deep learning works well for visual object recognition, speech recognition, natural language processing, and reinforcement learning in complex environments.
•Convolutional networks are particularly well suited for image processing and other tasks where the data have a grid topology.
•Recurrent networks are effective for sequence-processing tasks including language modeling and machine translation.


...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The literature on neural networks is vast. Cowan and Sharp (1988b, 1988a) survey the early history, beginning with the work of McCulloch and Pitts (1943). (As mentioned in Chapter 1, John McCarthy has pointed to the work of Nicolas Rashevsky (1936, 1938) as the earliest mathematical model of neural learning.) Norbert Wiener, a pioneer of cybernetics and control theory (Wiener, 1948), worked with McCulloch and Pitts and influenced a number of young researchers, including Marvin Minsky, who may have been the first to develop a working neural network in hardware, in 1951 (see Minsky and Papert, 1988, pp. ix–x). Alan Turing (1948) wrote a research report titled Intelligent Machinery that begins with the sentence “I propose to investigate the question as to whether it is possible for machinery to show intelligent behaviour” and goes on to describe a recurrent neural network architecture he calle...

### 23 Reinforcement Learning



#### 23.1 Learning from Rewards




Artificial Intelligence: A Modern Approach














23.1Learning from Rewards
Consider the problem of learning to play chess. Let’s imagine treating this as a supervised learning problem using the methods of Chapters 19, 21, and 22. The chess-playing agent function takes as input a board position and returns a move, so we train this function by supplying examples of chess positions, each labeled with the correct move. Now, it so happens that we have available databases of several million grandmaster games, each a sequence of positions and moves. The moves made by the winner are, with few exceptions, assumed to be good, if not always perfect. Thus, we have a promising training set. The problem is that there are relatively few examples (about 108) compared to the space of all possible chess positions (about 1040). In a new game, one soon encounters positions that are significantly different from those in the database, and the trained agent function is likely to fail miserably—not...

#### 23.2 Passive Reinforcement Learning




Artificial Intelligence: A Modern Approach














23.2Passive Reinforcement Learning
We start with the simple case of a fully observable environment with a small number of actions and states, in which an agent already has a fixed policy π(s) that determines its actions. The agent is trying to learn the utility function Uπ(s)—the expected total discounted reward if policy π is executed beginning in state s. We call this a passive learning agent.

The passive learning task is similar to the policy evaluation task, part of the policy iteration algorithm described in Section 16.2.2. The difference is that the passive learning agent does not know the transition model P(s' | s,a), which specifies the probability of reaching state s' from state s after doing action a; nor does it know the reward function R(s,a,s'), which specifies the reward for each transition.
We will use as our example the 4 × 3 world introduced in Chapter 16. Figure 23.1 shows the optimal policies for that world...

#### 23.3 Active Reinforcement Learning




Artificial Intelligence: A Modern Approach














23.3Active Reinforcement Learning
A passive learning agent has a fixed policy that determines its behavior. An active learning agent gets to decide what actions to take. Let us begin with the adaptive dynamic programming (ADP) agent and consider how it can be modified to take advantage of this new freedom.
First, the agent will need to learn a complete transition model with outcome probabilities for all actions, rather than just the model for the fixed policy. The learning mechanism used by PASSIVE-ADP-AGENT will do just fine for this. Next, we need to take into account the fact that the agent has a choice of actions. The utilities it needs to learn are those defined by the optimal policy; they obey the Bellman equations (which we repeat here):







U(s)=

max

a∈A(s)



∑

s'


P(s'|s,a)[R(s,a,s') + γ U(s')]
 .



     (23.4)





These equations can be solved to obtain the utility function U using the value iteration or po...

#### 23.4 Generalization in Reinforcement Learning




Artificial Intelligence: A Modern Approach














23.4Generalization in Reinforcement Learning
So far, we have assumed that utility functions and Q-functions are represented in tabular form with one output value for each state. This works for state spaces with up to about 106 states, which is more than enough for our toy two-dimensional grid environments. But in real-world environments with many more states, convergence will be too slow. Backgammon is simpler than most real-world applications, yet it has about 1020 states. We cannot easily visit them all in order to learn how to play the game.
Chapter 6 introduced the idea of an evaluation function as a compact measure of desirability for potentially vast state spaces. In the terminology of this chapter, the evaluation function is an approximate utility function; we use the term function approximation for the process of constructing a compact approximation of the true utility function or Q-function. For example, we might appr...

#### 23.5 Policy Search




Artificial Intelligence: A Modern Approach














23.5Policy Search
The final approach we will consider for reinforcement learning problems is called policy search. In some ways, policy search is the simplest of all the methods in this chapter: the idea is to keep twiddling the policy as long as its performance improves, then stop.

Let us begin with the policies themselves. Remember that a policy π is a function that maps states to actions. We are interested primarily in parameterized representations of π that have far fewer parameters than there are states in the state space (just as in the preceding section). For example, we could represent π by a collection of parameterized Q-functions, one for each action, and take the action with the highest predicted value:







π(s)=

argmax
a

 


Q
^

θ

(s,a).



                   (23.13)





Each Q-function could be a linear function, as in Equation (23.9), or it could be a nonlinear function such as a deep neural network. Pol...

#### 23.6 Apprenticeship and Inverse Reinforcement Learning




Artificial Intelligence: A Modern Approach














23.6Apprenticeship and Inverse Reinforcement Learning
Some domains are so complex that it is difficult to define a reward function for use in reinforcement learning. Exactly what do we want our self-driving car to do? Certainly it should not take too long to get to the destination, but it should not drive so fast as to incur undue risk or to get speeding tickets. It should conserve fuel/energy. It should avoid jostling or accelerating the passengers too much, but it can slam on the brakes in an emergency. And so on. Deciding how much weight to give to each of these factors is a difficult task. Worse still, there are almost certainly important factors we have forgotten, such as the obligation to behave with consideration for other drivers. Omitting a factor usually leads to behavior that assigns an extreme value to the omitted factor—in this case, extremely inconsiderate driving—in order to maximize the remaining factors.
One a...

#### 23.7 Applications of Reinforcement Learning




Artificial Intelligence: A Modern Approach














23.7Applications of Reinforcement Learning
We now turn to applications of reinforcement learning. These include game playing, where the transition model is known and the goal is to learn the utility function, and robotics, where the model is initially unknown.
23.7.1Applications in game playing
In Chapter 1 we described Arthur Samuel’s early work on reinforcement learning for checkers, which began in 1952. A few decades passed before the challenge was taken up again, this time by Gerry Tesauro in his work on backgammon. Tesauro’s first attempt (1990) was a system called NEUROGAMMON. The approach was an interesting variant on imitation learning. The input was a set of 400 games played by Tesauro against himself. Rather than learn a policy, NEUROGAMMON converted each move (s, a, s') into a set of training examples, each of which labeled s' as a better position than some other position s" reachable from s by a different move. The...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has examined the reinforcement learning problem: how an agent can become proficient in an unknown environment, given only its percepts and occasional rewards. Reinforcement learning is a very broadly applicable paradigm for creating intelligent systems. The major points of the chapter are as follows.

•The overall agent design dictates the kind of information that must be learned:

–A model-based reinforcement learning agent acquires (or is equipped with) a transition model P(s' | s, a) for the environment and learns a utility function U(s).
–A model-free reinforcement learning agent may learn an action-utility function Q(s, a) or a policy π(s).

•Utilities can be learned using several different approaches:

–Direct utility estimation uses the total observed reward-to-go for a given state as direct evidence for learning its utility.
–Adaptive dynamic programming (ADP) learns a model and a reward function f...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
It seems likely that the key idea of reinforcement learning—that animals do more of what they are rewarded for and less of what they are punished for—played a significant role in the domestication of dogs at least 15,000 years ago. The early foundations of our scientific understanding of reinforcement learning include the work of the Russian physiologist Ivan Pavlov, who won the Nobel Prize in 1904, and that of the American psychologist Edward Thorndike—particularly his book Animal Intelligence (1911). Hilgard and Bower (1975) provide a good survey.
Alan Turing (1948, 1950) proposed reinforcement learning as an approach for teaching computers; he considered it a partial solution, writing, “The use of punishments and rewards can at best be a part of the teaching process.” Arthur Samuel’s checkers program (1959, 1967) was the first successful use of machine learning of any kind. Samuel sugges...

## VI Communicating, perceiving, and acting



### 24 Natural Language Processing



#### 24.1 Language Models




Artificial Intelligence: A Modern Approach














24.1Language Models
Formal languages, such as first-order logic, are precisely defined, as we saw in Chapter 8. A grammar defines the syntax of legal sentences and semantic rules define the meaning.
Natural languages, such as English or Chinese, cannot be so neatly characterized:

•Language judgments vary from person to person and time to time. Everyone agrees that “Not to be invited is sad” is a grammatical sentence of English, but people disagree on the grammaticality of “To be not invited is sad.”
•Natural language is ambiguous (“He saw her duck” can mean either that she owns a waterfowl, or that she made a downwards evasive move) and vague (“That’s great!” does not specify precisely how great it is, nor what it is).
•The mapping from symbols to objects is not formally defined. In first-order logic, two uses of the symbol “Richard” must refer to the same person, but in natural language two occurrences of the same word or ph...

#### 24.2 Grammar




Artificial Intelligence: A Modern Approach














24.2Grammar
In Chapter 7 we used Backus–Naur Form (BNF) to write down a grammar for the language of first-order logic. A grammar is a set of rules that defines the tree structure of allowable phrases, and a language is the set of sentences that follow those rules.
Natural languages do not work exactly like the formal language of first-order logic—they do not have a hard boundary between allowable and unallowable sentences, nor do they have a single definitive tree structure for each sentence. However, hierarchical structure is important in natural language. The word “Stocks” in “Stocks rallied on Monday” is not just a word, nor is it just a noun; in this sentence it also comprises a noun phrase, which is the subject of the following verb phrase. Syntactic categories such as noun phrase or verb phrase help to constrain the probable words at each point within a sentence, and the phrase structure provides a framework for the mean...

#### 24.3 Parsing




Artificial Intelligence: A Modern Approach














24.3Parsing
Parsing is the process of analyzing a string of words to uncover its phrase structure, according to the rules of a grammar. We can think of it as a search for a valid parse tree whose leaves are the words of the string. Figure 24.4 shows that we can start with the S symbol and search top down, or we can start with the words and search bottom up. Pure top-down or bottom-up parsing strategies can be inefficient, however, because they can end up repeating effort in areas of the search space that lead to dead ends. Consider the following two sentences:






Description

An arrow labeled w subscript x, z from a node labeled x points to a node labeled z. An arrow labeled w subscript z, y from node z points to a node labeled y. A self-loop labeled w subscript z, z from node z points back to node z. A point on the self-loop is labeled delta.

×
Figure 24.4Parsing the string “The wumpus is dead” as a sentence, according to...

#### 24.4 Augmented Grammars




Artificial Intelligence: A Modern Approach














24.4Augmented Grammars
So far we have dealt with context-free grammars. But not every NP can appear in every context with equal probability. The sentence “I ate a banana” is fine, but “Me ate a banana” is ungrammatical, and “I ate a bandanna” is unlikely.
The issue is that our grammar is focused on lexical categories, like Pronoun, but while “I” and “me” are both pronouns, only “I” can be the subject of a sentence. Similarly, “banana” and “bandanna” are both nouns, but the former is much more likely to be object of “ate”. Linguists say that the pronoun “I” is in the subjective case (i.e., is the subject of a verb) and “me” is in the objective case3 (i.e., is the object of a verb). They also say that “I” is in the first person (“you” is second person, and “she” is third person) and is singular (“we” is plural). A category like Pronoun that has been augmented with features like “subjective case, first person singular” is called ...

#### 24.5 Complications of Real Natural Language




Artificial Intelligence: A Modern Approach














24.5Complications of Real Natural Language
The grammar of real English is endlessly complex (and other languages are equally complex). We will briefly mention some of the topics that contribute to this complexity.
Quantification: Consider the sentence “Every agent feels a breeze.” The sentence has only one syntactic parse under 


ξ
0


, but it is semantically ambiguous: is there one breeze that is felt by all the agents, or does each agent feel a separate personal breeze? The two interpretations can be represented as








∀a   a∈Agents⇒





              ∃b b∈Breezes∧Feel(a,b);





∃b   b∈Breezes∧∀a   a∈Agents⇒





              Feel(a,b).





One standard approach to quantification is for the grammar to define not an actual logical semantic sentence, but rather a quasi-logical form that is then turned into a logical sentence by algorithms outside of the parsing process. Those algorithms can have preference rules for ...

#### 24.6 Natural Language Tasks




Artificial Intelligence: A Modern Approach














24.6Natural Language Tasks
Natural language processing is a big field, deserving an entire textbook or two of its own (Goldberg, 2017; Jurafsky and Martin, 2020). In this section we briefly describe some of the main tasks; you can use the references to get more details.
Speech recognition is the task of transforming spoken sound into text. We can then perform further tasks (such as question answering) on the resulting text. Current systems have a word error rate of about 3% to 5% (depending on details of the test set), similar to human transcribers. The challenge for a system using speech recognition is to respond appropriately even when there are errors on individual words.

Top systems today use a combination of recurrent neural networks and hidden Markov models (Hinton et al., 2012; Yu and Deng, 2016; Deng, 2016; Chiu et al., 2017; Zhang et al.,2017). The introduction of deep neural nets for speech in 2011 led to an immedia...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
The main points of this chapter are as follows:

•Probabilistic language models based on n-grams recover a surprising amount of information about a language. They can perform well on such diverse tasks as language identification, spelling correction, sentiment analysis, genre classification, and named-entity recognition.
•These language models can have millions of features, so preprocessing and smoothing the data to reduce noise is important.
•In building a statistical language system, it is best to devise a model that can make good use of available data, even if the model seems overly simplistic.
•Word embeddings can give a richer representation of words and their similarities.
•To capture the hierarchical structure of language, phrase structure grammars (and in particular, context-free grammars) are useful. The probabilistic context-free grammar (PCFG) formalism is widely used, as is the dependency grammar formalism....

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
N-gram letter models for language modeling were proposed by Markov (1913). Claude Shannon (Shannon and Weaver, 1949) was the first to generate n-gram word models of English. The bag-of-words model gets its name from a passage from linguist Zellig Harris (1954), “language is not merely a bag of words but a tool with particular properties.” Norvig (2009) gives some examples of tasks that can be accomplished with n-gram models.
Chomsky (1956, 1957) pointed out the limitations of finite-state models compared with context-free models, concluding, “Probabilistic models give no particular insight into some of the basic problems of syntactic structure.” This is true, but probabilistic models do provide insight into some other basic problems—problems that context-free models ignore. Chomsky’s remarks had the unfortunate effect of scaring many people away from statistical models for two decades, unti...

### 25 Deep Learning for Natural Language Processing



#### 25.1 Word Embeddings




Artificial Intelligence: A Modern Approach














25.1Word Embeddings
We would like a representation of words that does not require manual feature engineering, but allows for generalization between related words—words that are related syntactically (“colorless” and “ideal” are both adjectives), semantically (“cat” and “kitten” are both felines), topically (“sunny” and “sleet” are both weather terms), in terms of sentiment (“awesome” has opposite sentiment to “cringeworthy”), or otherwise.
How should we encode a word into an input vector x for use in a neural network? As explained in Section 22.2.1 (page 807), we could use a one-hot vector—that is, we encode the ith word in the dictionary with a 1 bit in the ith input position and a 0 in all the other positions. But such a representation would not capture the similarity between words.
Following the linguist John R. Firth’s (1957) maxim, “You shall know a word by the company it keeps,” we could represent each word with a vector...

#### 25.2 Recurrent Neural Networks for NLP




Artificial Intelligence: A Modern Approach














25.2Recurrent Neural Networks for NLP
We now have a good representation for single words in isolation, but language consists of an ordered sequence of words in which the context of surrounding words is important. For simple tasks like part of speech tagging, a small, fixed-size window of perhaps five words usually provides enough context.
More complex tasks such as question answering or reference resolution may require dozens of words as context. For example, in the sentence “Eduardo told me that Miguel was very sick so I took him to the hospital,” knowing that him refers to Miguel and not Eduardo requires context that spans from the first to the last word of the 14-word sentence.
25.2.1Language models with recurrent neural networks
We’ll start with the problem of creating a language model with sufficient context. Recall that a language model is a probability distribution over sequences of words. It allows us to predict the ne...

#### 25.3 Sequence-to-Sequence Models




Artificial Intelligence: A Modern Approach














25.3Sequence-to-Sequence Models
One of the most widely studied tasks in NLP is machine translation (MT), where the goal is to translate a sentence from a source language to a target language—for example, from Spanish to English. We train an MT model with a large corpus of source/target sentence pairs. The goal is to then accurately translate new sentences that are not in our training data.



Can we use RNNs to create an MT system? We can certainly encode the source sentence with an RNN. If there were a one-to-one correspondence between source words and target words, then we could treat MT as a simple tagging task—given the source word “perro” in Spanish, we tag it as the corresponding English word “dog.” But in fact, words are not one-to-one: in Spanish the three words “caballo de mar” corresponds to the single English word “seahorse,” and the two words “perro grande” translate to “big dog,” with the word order reversed. Word...

#### 25.4 The Transformer Architecture




Artificial Intelligence: A Modern Approach














25.4The Transformer Architecture
The influential article “Attention is all you need” (Vaswani et al., 2018) introduced the transformer architecture, which uses a self-attention mechanism that can model long-distance context without a sequential dependency.


25.4.1Self-attention
Previously, in sequence-to-sequence models, attention was applied from the target RNN to the source RNN. Self-attention extends this mechanism so that each sequence of hidden states also attends to itself—the source to the source, and the target to the target. This allows the model to additionally capture long-distance (and nearby) context within each sequence.
The most straightforward way of applying self-attention is where the attention matrix is directly formed by the dot product of the input vectors. However, this is problematic. The dot product between a vector and itself will always be high, so each hidden state will be biased towards attending t...

#### 25.5 Pretraining and Transfer Learning




Artificial Intelligence: A Modern Approach














25.5Pretraining and Transfer Learning
Getting enough data to build a robust model can be a challenge. In computer vision (see Chapter 27), that challenge was addressed by assembling large collections of images (such as ImageNet) and hand-labeling them.
For natural language, it is more common to work with text that is unlabeled. The difference is in part due to the difficulty of labeling: an unskilled worker can easily label an image as “cat” or “sunset,” but it requires extensive training to annotate a sentence with part-of-speech tags or parse trees. The difference is also due to the abundance of text: the Internet adds over 100 billion words of text each day, including digitized books, curated resources such as Wikipedia, and uncurated social media posts.
Projects such as Common Crawl provide easy access to this data. Any running text can be used to build n-gram or word embedding models, and some text comes with structure th...

#### 25.6 State of the art




Artificial Intelligence: A Modern Approach














25.6State of the art
Deep learning and transfer learning have markedly advanced the state of the art for NLP—so much so that one commentator in 2018 declared that “NLP’s ImageNet moment has arrived” (Ruder, 2018). The implication is that just as a turning point occurred in 2012 for computer vision when deep learning systems produced surprising good results in the ImageNet competition, a turning point occurred in 2018 for NLP. The principal impetus for this turning point was the finding that transfer learning works well for natural language problems: a general language model can be downloaded and fine-tuned for a specific task.
It started with simple word embeddings from systems such as WORD2VEC in 2013 and GloVe in 2014. Researchers can download such a model or train their own relatively quickly without access to supercomputers. Pretrained contextual representations, on the other hand, are orders of magnitude more expensive to...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
The key points of this chapter are as follows:

•Continuous representations of words with word embeddings are more robust than discrete atomic representations, and can be pretrained using unlabeled text data.
•Recurrent neural networks can effectively model local and long-distance context by retaining relevant information in their hidden-state vectors.
•Sequence-to-sequence models can be used for machine translation and text generation problems.
•Transformer models use self-attention and can model long-distance context as well as local context. They can make effective use of hardware matrix multiplication.
•Transfer learning that includes pretrained contextual word embeddings allows models to be developed from very large unlabeled corpora and applied to a range of tasks. Models that are pretrained to predict missing words can handle other tasks such as question answering and textual entailment, after fine-tuning for th...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The distribution of words and phrases in natural language follow Zipf’s Law (Zipf, 1935, 1949): the frequency of the nth most popular word is roughly inversely proportional to n. That means we have a data sparsity problem: even with billions of words of training data, we are constantly running into novel words and phrases that were not seen before.
Generalization to novel words and phrases is aided by representations that capture the basic insight that words with similar meanings appear in similar contexts. Deerwester et al.(1990) projected words into low-dimensional vectors by decomposing the co-occurrence matrix formed by words and the documents the words appear in. Another possibility is to treat the surrounding words—say, a 5-word window—as context. Brown et al. (1992) grouped words into hierarchical clusters according to the bigram context of words; this has proven to be effective for ...

### 26 Robotics



#### 26.1 Robots




Artificial Intelligence: A Modern Approach














26.1Robots
Robots are physical agents that perform tasks by manipulating the physical world. To do so, they are equipped with effectors such as legs, wheels, joints, and grippers. Effectors are designed to assert physical forces on the environment. When they do this, a few things may happen: the robot’s state might change (e.g., a car spins its wheels and makes progress on the road as a result), the state of the environment might change (e.g., a robot arm uses its gripper to push a mug across the counter), and even the state of the people around the robot might change (e.g., an exoskeleton moves and that changes the configuration of a person’s leg; or a mobile robot makes progress toward the elevator doors, and a person notices and is nice enough to move out of the way, or even push the button for the robot).


Robots are also equipped with sensors, which enable them to perceive their environment. Present-day robotics employs ...

#### 26.2 Robot Hardware




Artificial Intelligence: A Modern Approach














26.2Robot Hardware
So far in this book, we have taken the agent architecture—sensors, effectors, and processors—as given, and have concentrated on the agent program. But the success of real robots depends at least as much on the design of sensors and effectors that are appropriate for the task.
26.2.1Types of robots from the hardware perspective
When you think of a robot, you might imagine something with a head and two arms, moving around on legs or wheels. Such anthropomorphic robots have been popularized in fiction such as the movie The Terminator and the cartoon The Jetsons. But real robots come in many shapes and sizes.

Manipulators are just robot arms. They do not necessarily have to be attached to a robot body; they might simply be bolted onto a table or a floor, as they are in factories (Figure 26.1 (a)). Some have a large payload, like those assembling cars, while others, like wheelchair-mountable arms that assist peo...

#### 26.3 What kind of problem is robotics solving?




Artificial Intelligence: A Modern Approach














26.3What kind of problem is robotics solving?
Now that we know what the robot hardware might be, we’re ready to consider the agent software that drives the hardware to achieve our goals. We first need to decide the computational framework for this agent. We have talked about search in deterministic environments, MDPs for stochastic but fully observable environments, POMDPs for partial observability, and games for situations in which the agent is not acting in isolation. Given a computational framework, we need to instantiate its ingredients: reward or utility functions, states, actions, observation spaces, etc.
We have already noted that robotics problems are nondeterministic, partially observable, and multiagent. Using the game-theoretic notions from Chapter 17, we can see that sometimes the agents are cooperative and sometimes they are competitive. In a narrow corridor where only one agent can go first, a robot and a person ...

#### 26.4 Robotic Perception




Artificial Intelligence: A Modern Approach














26.4Robotic Perception
Perception is the process by which robots map sensor measurements into internal representations of the environment. Much of it uses the computer vision techniques from the previous chapter. But perception for robotics must deal with additional sensors like lidar and tactile sensors.
Perception is difficult because sensors are noisy and the environment is partially observable, unpredictable, and often dynamic. In other words, robots have all the problems of state estimation (or filtering) that we discussed in Section 14.2. As a rule of thumb, good internal representations for robots have three properties:

1.They contain enough information for the robot to make good decisions.
2.They are structured so that they can be updated efficiently.
3.They are natural in the sense that internal variables correspond to natural state variables in the physical world.

In Chapter 14, we saw that Kalman filters, HMMs, an...

#### 26.5 Planning and Control




Artificial Intelligence: A Modern Approach














26.5Planning and Control
The robot’s deliberations ultimately come down to deciding how to move, from the abstract task level all the way down to the currents that are sent to its motors. In this section, we simplify by assuming that perception (and, where needed, prediction) are given, so the world is observable. We further assume deterministic transitions (dynamics) of the world.
We start by separating motion from control. We define a path as a sequence of points in geometric space that a robot (or a robot part, such as an arm) will follow. This is related to the notion of path in Chapter 3, but here we mean a sequence of points in space rather than a sequence of discrete actions. The task of finding a good path is called motion planning.

Once we have a path, the task of executing a sequence of actions to follow the path is called trajectory tracking control. A trajectory is a path that has a time associated with each point...

#### 26.6 Planning Uncertain Movements




Artificial Intelligence: A Modern Approach














26.6Planning Uncertain Movements
In robotics, uncertainty arises from partial observability of the environment and from the stochastic (or unmodeled) effects of the robot’s actions. Errors can also arise from the use of approximation algorithms such as particle filtering, which does not give the robot an exact belief state even if the environment is modeled perfectly.
The majority of today’s robots use deterministic algorithms for decision making, such as the path-planning algorithms of the previous section, or the search algorithms that were introduced in Chapter 3. These deterministic algorithms are adapted in two ways: first, they deal with the continuous state space by turning it into a discrete space (for example with visibility graphs or cell decomposition). Second, they deal with uncertainty in the current state by choosing the most likely state from the probability distribution produced by the state estimation algorith...

#### 26.7 Reinforcement Learning in Robotics




Artificial Intelligence: A Modern Approach














26.7Reinforcement Learning in Robotics
Thus far we have considered tasks in which the robot has access to the dynamics model of the world. In many tasks, it is very difficult to write down such a model, which puts us in the domain of reinforcement learning (RL).
One challenge of RL in robotics is the continuous nature of the state and action spaces, which we handle either through discretization, or, more commonly, through function approximation. Policies or value functions are represented as combinations of known useful features, or as deep neural networks. Neural nets can map from raw inputs directly to outputs, and thus largely avoid the need for feature engineering, but they do require more data.
A bigger challenge is that robots operate in the real world. We have seen how reinforcement learning can be used to learn to play chess or Go by playing simulated games. But when a real robot moves in the real world, we have to mak...

#### 26.8 Humans and Robots




Artificial Intelligence: A Modern Approach














26.8Humans and Robots
Thus far, we’ve focused on a robot planning and learning how to act in isolation. This is useful for some robots, like the rovers we send out to explore distant planets on our behalf. But, for the most part, we do not build robots to work in isolation. We build them to help us, and to work in human environments, around and with us.
This raises two complementary challenges. First is optimizing reward when there are people acting in the same environment as the robot. We call this the coordination problem (see Section 17.1). When the robot’s reward depends on not just its own actions, but also the actions that people take, the robot has to choose its actions in a way that meshes well with theirs. When the human and the robot are on the same team, this turns into collaboration.
Second is the challenge of optimizing for what people actually want. If a robot is to help people, its reward function needs to incen...

#### 26.9 Alternative Robotic Frameworks




Artificial Intelligence: A Modern Approach














26.9Alternative Robotic Frameworks
Thus far, we have taken a view of robotics based on the notion of defining or learning a reward function, and having the robot optimize that reward function (be it via planning or learning), sometimes in coordination or collaboration with humans. This is a deliberative view of robotics, to be contrasted with a reactive view.


26.9.1Reactive controllers
In some cases, it is easier to set up a good policy for a robot than to model the world and plan. Then, instead of a rational agent, we have a reflex agent.
For example, picture a legged robot that attempts to lift a leg over an obstacle. We could give this robot a rule that says lift the leg a small height h and move it forward, and if the leg encounters an obstacle, move it back and start again at a higher height. You could say that h is modeling an aspect of the world, but we can also think of h as an auxiliary variable of the robot control...

#### 26.10 Application Domains




Artificial Intelligence: A Modern Approach














26.10Application Domains
Robotic technology is already permeating our world, and has the potential to improve our independence, health, and productivity. Here are some example applications.
Home care: Robots have started to enter the home to care for older adults and people with motor impairments, assisting them with activities of daily living and enabling them to live more independently. These include wheelchairs and wheelchair-mounted arms like the Kinova arm from Figure 26.1(b). Even though they start off as being operated by a human directly, these robots are gaining more and more autonomy. On the horizon are robots operated by brain-machine interfaces, which have been shown to enable people with quadriplegia to use a robot arm to grasp objects and even feed themselves (Figure 26.33(a)). Related to these are prosthetic limbs that intelligently respond to our actions, and exoskeletons that give us superhuman strength or ena...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
Robotics is about physically embodied agents, which can change the state of the physical world. In this chapter, we have learned the following:

•The most common types of robots are manipulators (robot arms) and mobile robots. They have sensors for perceiving the world and actuators that produce motion, which then affects the world via effectors.
•The general robotics problem involves stochasticity (which can be handled by MDPs), partial observability (which can be handled by POMDPs), and acting with and around other agents (which can be handled with game theory). The problem is made even harder by the fact that most robots work in continuous and high-dimensional state and action spaces. They also operate in the real world, which refuses to run faster than real time and in which failures lead to real things being damaged, with no “undo” capability.
•Ideally, the robot would solve the entire problem in one go: observati...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The word robot was popularized by Czech playwright Karel Čapek in his 1920 play R.U.R.(Rossum’s Universal Robots). The robots, which were grown chemically rather than constructed mechanically, end up resenting their masters and decide to take over. It appears that it was Čapek’s brother, Josef, who first combined the Czech words “robota” (obligatory work) and “robotnik” (serf) to yield “robot” in his 1917 short story Opilec (Glanc, 1978). The term robotics was invented for a science fiction story (Asimov, 1950).
The idea of an autonomous machine predates the word “robot” by thousands of years. In 7th century BCE Greek mythology, a robot named Talos was built by Hephaistos, the Greek god of metallurgy, to protect the island of Crete. The legend is that the sorceress Medea defeated Talos by promising him immortality but then draining his life fluid. Thus, this is the first example of a robot ...

### 27 Computer Vision



#### 27.1 Introduction




Artificial Intelligence: A Modern Approach














27.1Introduction
Vision is a perceptual channel that accepts a stimulus and reports some representation of the world. Most agents that use vision use passive sensing—they do not need to send out light to see. In contrast, active sensing involves sending out a signal such as radar or ultrasound, and sensing a reflection. Examples of agents that use active sensing include bats (ultrasound), dolphins (sound), abyssal fishes (light), and some robots (light, sound, radar). To understand a perceptual channel, one must study both the physical and statistical phenomena that occur in sensing and what the perceptual process should produce. We concentrate on vision in this chapter, but robots in the real world use a variety of sensors to perceive sound, touch, distance, temperature, global position, and acceleration.

A feature is a number obtained by applying simple computations to an image. Very useful information can be obtained direc...

#### 27.2 Image Formation




Artificial Intelligence: A Modern Approach














27.2Image Formation
Imaging distorts the appearance of objects. A picture taken looking down a long straight set of railway tracks will suggest that the rails converge and meet. If you hold your hand in front of your eye, you can block out the moon, even though the moon is larger than your hand (this works with the sun too, but you could damage your eyes checking it). If you hold a book flat in front of your face and tilt it backward and forward, it will seem to shrink and grow in the image. This effect is known as foreshortening (Figure 27.1). Models of these effects are essential for building competent object recognition systems and also yield powerful cues for reconstructing geometry.




×
Figure 27.1Geometry in the scene appears distorted in images. Parallel lines appear to meet, like the railway tracks in a desolate town. Buildings that have right angles in the real world scene have distorted angles in the image.
27.2.1I...

#### 27.3 Simple Image Features




Artificial Intelligence: A Modern Approach














27.3Simple Image Features
Light reflects off objects in the scene to form an image consisting of, say, twelve million three-byte pixels. As with all sensors there will be noise in the image, and in any case there is a lot of data to deal with. The way to get started analyzing this data is to produce simplified representations that expose what’s important, but reduce detail. Much current practice learns these representations from data. But there are four properties of images and video that are particularly general: edges, texture, optical flow and segmentation into regions.
An edge occurs where there is a big difference in pixel intensity across part of an image. Building representations of edges involves local operations on an image—you need to compare a pixel value to some values nearby—and doesn’t require any knowledge about what is in the image. Thus, edge detection can come early in the pipeline of operations and we call i...

#### 27.4 Classifying Images




Artificial Intelligence: A Modern Approach














27.4Classifying Images
Image classification applies to two main cases. In one, the images are of objects, taken from a given taxonomy of classes, and there’s not much else of significance in the picture—for example, a catalog of clothing or furniture images, where the background doesn’t matter, and the output of the classifier is “cashmere sweater” or “desk chair.”
In the other case, each image shows a scene containing multiple objects. So in grassland you might see a giraffe and a lion, and in the living room you might see a couch and lamp, but you don’t expect a giraffe or a submarine in a living room. We now have methods for large-scale image classification that can accurately output “grassland” or “living room.”
Modern systems classify images using appearance (i.e., color and texture, as opposed to geometry). There are two difficulties. First, different instances of the same class could look different—some cats are black a...

#### 27.5 Detecting Objects




Artificial Intelligence: A Modern Approach














27.5Detecting Objects
Image classifiers predict what is in the image—they classify the whole image as belonging to one class. Object detectors find multiple objects in an image, report what class each object is, and also report where each object is by giving a bounding box around the object.1 The set of classes is fixed in advance. So we might try to detect all faces, all cars, or all cats.

We can build an object detector by looking at a small sliding window onto the larger image—a rectangle. At each spot, we classify what we see in the window, using a CNN classifier. We then take the high-scoring classifications—a cat over here and a dog over there—and ignore the other windows. After some work resolving conflicts, we have a final set of objects with their locations. There are still some details to work out:


•Decide on a window shape: The easiest choice by far is to use axis-aligned rectangles. (The alternative—some form of...

#### 27.6 The 3D World




Artificial Intelligence: A Modern Approach














27.6The 3D World
Images show a 2D picture of a 3D world. But this 2D picture is rich with cues about the 3D world. One kind of cue occurs when we have multiple pictures of the same world, and can match points between pictures. Another kind of cue is available within a single picture.
27.6.13D cues from multiple views
Two pictures of objects in a 3D world are better than one for several reasons:

•If you have two images of the same scene taken from different viewpoints and you know enough about the two cameras, you can construct a 3D model—a collection of points with their coordinates in 3 dimensions—by figuring out which point in the first view corresponds to which point in the second view and applying some geometry. This is true for almost all pairs of viewing directions and almost all kinds of camera.
•If you have two views of enough points, and you know which point in the first view corresponds to which point in the second ...

#### 27.7 Using Computer Vision




Artificial Intelligence: A Modern Approach














27.7Using Computer Vision
Here we survey a range of computer vision applications. There are now many reliable computer vision tools and toolkits, so the range of applications that are successful and useful is extraordinary. Many are developed at home by enthusiasts for special purposes, which is testimony to how usable the methods are and how much impact they have. (For example, an enthusiast created a great object-detection-based pet door that refuses entry to a cat if it is bringing in a dead mouse–a Web search will find it for you).
27.7.1Understanding what people are doing
If we could build systems that understood what people are doing by analyzing video, we could build human-computer interfaces that watch people and react to their behavior. With these interfaces, we could: design buildings and public places better, by collecting and using data about what people do in public; build more accurate and less intrusive security...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
Although perception appears to be an effortless activity for humans, it requires a significant amount of sophisticated computation. The goal of vision is to extract information needed for tasks such as manipulation, navigation, and object recognition.

•The geometry and optics of image formation is well understood. Given a description of a 3D scene, we can easily produce a picture of it from some arbitrary camera position—this is the graphics problem. The inverse problem, the computer vision problem—taking a picture and turning it into a 3D description—is more difficult.
•Representations of images capture edges, texture, optical flow, and regions. These yield cues to the boundaries of objects and to correspondence between images.
•Convolutional neural networks produce accurate image classifiers that use learned features. Rather roughly, the features are patterns of patterns of patterns... It is hard to predict when the...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
This chapter has concentrated on vision, but other perceptual channels have been studied and put to use in robotics. For auditory perception (hearing), we have already covered speech recognition, and there has also been considerable work on music perception (Koelsch and Siebel, 2005) and machine learning of music (Engel et al., 2017) as well as on machine learning for sounds in general (Sharan and Moir, 2016).
Tactile perception or touch (Luo et al., 2017) is important in robotics and is discussed in Chapter 26. Automated olfactory perception (smell) has seen less work, but it has been shown that deep learning models can learn to predict smells based on the structure of molecules (Sanchez-Lengeling et al., 2019).
Systematic attempts to understand human vision can be traced back to ancient times. Euclid (ca. 300 BCE) wrote about natural perspective—the mapping that associates, with each poin...

## VII Conclusions



### 28 Philosophy, Ethics, and Safety of AI



#### 28.1 The Limits of AI




Artificial Intelligence: A Modern Approach














28.1The Limits of AI
In 1980, philosopher John Searle introduced a distinction between weak AI—the idea that machines could act as if they were intelligent—and strong AI—the assertion that machines that do so are actually consciously thinking (not just simulating thinking). Over time the definition of strong AI shifted to refer to what is also called “human-level AI” or “general AI”—programs that can solve an arbitrarily wide variety of tasks, including novel ones, and do so as well as a human.


Critics of weak AI who objected to the very possibility of intelligent behavior in machines now appear as shortsighted as Simon Newcomb, who in October 1903 wrote “aerial flight is one of the great class of problems with which man can never cope”—just two months before the Wright brothers’ flight at Kitty Hawk. The rapid progress of recent years does not, however, prove that there can be no limits to what AI can achieve. Alan Turing (...

#### 28.2 Can Machines Really Think?




Artificial Intelligence: A Modern Approach














28.2Can Machines Really Think?
Some philosophers claim that a machine that acts intelligently would not be actually thinking, but would be only a simulation of thinking. But most AI researchers are not concerned with the distinction, and the computer scientist Edsger Dijkstra (1984) said that “The question of whether Machines Can Think ... is about as relevant as the question of whether Submarines Can Swim.” The American Heritage Dictionary’s first definition of swim is “To move through water by means of the limbs, fins, or tail,” and most people agree that submarines, being limbless, cannot swim. The dictionary also defines fly as “To move through the air by means of wings or winglike parts,” and most people agree that airplanes, having winglike parts, can fly. However, neither the questions nor the answers have any relevance to the design or capabilities of airplanes and submarines; rather they are about word usage in Englis...

#### 28.3 The Ethics of AI




Artificial Intelligence: A Modern Approach














28.3The Ethics of AI
Given that AI is a powerful technology, we have a moral obligation to use it well, to promote the positive aspects and avoid or mitigate the negative ones.
The positive aspects are many. For example, AI can save lives through improved medical diagnosis, new medical discoveries, better prediction of extreme weather events, and safer driving with driver assistance and (eventually) self-driving technologies. There are also many opportunities to improve lives. Microsoft’s AI for Humanitarian Action program applies AI to recovering from natural disasters, addressing the needs of children, protecting refugees, and promoting human rights. Google’s AI for Social Good program supports work on rainforest protection, human rights jurisprudence, pollution monitoring, measurement of fossil fuel emissions, crisis counseling, news fact checking, suicide prevention, recycling, and other issues. The University of Chicago’s...

#### Summary




Artificial Intelligence: A Modern Approach














Summary
This chapter has addressed the following issues:

•Philosophers use the term weak AI for the hypothesis that machines could possibly behave intelligently, and strong AI for the hypothesis that such machines would count as having actual minds (as opposed to simulated minds).
•Alan Turing rejected the question “Can machines think?” and replaced it with a behavioral test. He anticipated many objections to the possibility of thinking machines. Few AI researchers pay attention to the Turing test, preferring to concentrate on their systems’ performance on practical tasks, rather than the ability to imitate humans.
•Consciousness remains a mystery.
•AI is a powerful technology, and as such it poses potential dangers, through lethal autonomous weapons, security and privacy breaches, unintended side effects, unintentional errors, and malignant misuse. Those who work with AI technology have an ethical imperative to responsibly r...

#### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
Weak AI: When Alan Turing (1950) proposed the possibility of AI, he also posed many of the key philosophical questions, and provided possible replies. But various philosophers had raised similar issues long before AI was invented. Maurice Merleau-Ponty’s Phenomenology of Perception (1945) stressed the importance of the body and the subjective interpretation of reality afforded by our senses, and Martin Heidegger’s Being and Time (1927) asked what it means to actually be an agent. In the computer age, Alva Noe (2009) and Andy Clark (2015) propose that our brains form a rather minimal representation of the world, use the world itself on a just-in-time basis to maintain the illusion of a detailed internal model, and use props in the world (such as paper and pencil as well as computers) to increase the capabilities of the mind. Pfeifer et al. (2006) and Lakoff and Johnson (1999) present argumen...

### 29 The Future of AI



#### 29.1 AI Components




Artificial Intelligence: A Modern Approach














29.1AI Components
This section examines the components of AI systems and the extent to which each of them might accelerate or hinder future progress.
Sensors and actuators
For much of the history of AI, direct access to the world has been glaringly absent. With a few notable exceptions, AI systems were built in such a way that humans had to supply the inputs and interpret the outputs. Meanwhile, robotic systems focused on low-level tasks in which high-level reasoning and planning were largely ignored and the need for perception was minimized. This was partly due to the great expense and engineering effort required to get real robots to work at all, and partly because of the lack of sufficient processing power and sufficiently effective algorithms to handle high-bandwidth visual input.
The situation has changed rapidly in recent years with the availability of ready-made programmable robots. These, in turn, have benefited from c...

#### 29.2 AI Architectures




Artificial Intelligence: A Modern Approach














29.2AI Architectures
It is natural to ask, “Which of the agent architectures in Chapter 2 should an agent use?” The answer is, “All of them!” Reflex responses are needed for situations in which time is of the essence, whereas knowledge-based deliberation allows the agent to plan ahead. Learning is convenient when we have lots of data, and necessary when the environment is changing, or when human designers have insufficient knowledge of the domain.
AI has long had a split between symbolic systems (based on logical and probabilistic inference) and connectionist systems (based on loss minimization over a large number of uninterpreted parameters). A continuing challenge for AI is to bring these two together, to capture the best of both. Symbolic systems allow us to string together long chains of reasoning and to take advantage of the expressive power of structured representations, while connectionist systems can recognize patterns...

## A Mathematical Background



### A.1 Complexity Analysis and O() Notation




Artificial Intelligence: A Modern Approach














A.1Complexity Analysis and O() Notation
Computer scientists are often faced with the task of comparing algorithms to see how fast they run or how much memory they require. There are two approaches to this task. The first is benchmarking—running the algorithms on a computer and measuring speed in seconds and memory consumption in bytes. Ultimately, this is what really matters, but a benchmark can be unsatisfactory because it is so specific: it measures the performance of a particular program written in a particular language, running on a particular computer, with a particular compiler and particular input data. From the single result that the benchmark provides, it can be difficult to predict how well the algorithm would do on a different compiler, computer, or data set. The second approach relies on a mathematical analysis of algorithms, independent of the particular implementation and input, as discussed below.


A.1.1Asympto...

### A.2 Vectors, Matrices, and Linear Algebra




Artificial Intelligence: A Modern Approach














A.2Vectors, Matrices, and Linear Algebra
Mathematicians define a vector as a member of a vector space, but we will use a more concrete definition: a vector is an ordered sequence of values. For example, in two-dimensional space, we have vectors such as x = 〈3,4〉 and y = 〈0,2〉. We follow the convention of boldface characters for vector names, although some authors use arrows or bars over the names: 

x
→

 or 

y
¯

. The elements of a vector can be accessed using subscripts:  
z=〈
z
1

,
z
2

,… 
z
n

〉
. One confusing point: this book is synthesizing work from many subfields, which variously call their sequences vectors, lists, or tuples, and variously use the notations 〈1,2〉, [1, 2], or (1, 2).

The two fundamental operations on vectors are vector addition and scalar multiplication. The vector addition x + y is the elementwise sum: x + y = 〈3 + 0,4 + 2〉 = 〈3,6〉. Scalar multiplication multiplies each element by a constant: 5 ...

### A.3 Probability Distributions




Artificial Intelligence: A Modern Approach














A.3Probability Distributions
A probability is a measure over a set of events that satisfies three axioms:

1.The measure of each event is between 0 and 1. We write this as 0 ≤ P(X = xi) ≤ 1, where X is a random variable representing an event and xi are the possible values of X. In general, random variables are denoted by uppercase letters and their values by lowercase letters.
2.The measure of the whole set is 1; that is, 


∑

i=1
n

P(X=
x
i

)=1
.
3.The probability of a union of disjoint events is the sum of the probabilities of the individual events; that is, P(X = x1 ∨ X = x2) = P(X = x1) + P(X = x2), in the case where x1 and x2 are disjoint.

A probabilistic model consists of a sample space of mutually exclusive possible outcomes, together with a probability measure for each outcome. For example, in a model of the weather tomorrow, the outcomes might be sun, cloud, rain, and snow. A subset of these outcomes constitutes a...

### Bibliographical and Historical Notes




Artificial Intelligence: A Modern Approach














Bibliographical and Historical Notes
The O() notation so widely used in computer science today was first introduced in the context of number theory by the mathematician P. G. H. Bachmann (1894). The concept of NP-completeness was invented by Cook (1971), and the modern method for establishing a reduction from one problem to another is due to Karp (1972). Cook and Karp have both won the Turing award for their work.
Textbooks on the analysis and design of algorithms include Sedgewick and Wayne (2011) and Cormen, Leiserson, Rivest and Stein (2009). These books place an emphasis on designing and analyzing algorithms to solve tractable problems. For the theory of NP-completeness and other forms of intractability, see Garey and Johnson (1979) or Papadimitriou (1994). Good texts on probability include Chung (1979), Ross (2015), and Bertsekas and Tsitsiklis (2008).

...

## B Notes on Languages and Algorithms



### B.1 Defining Languages with Backus-Naur Form (BNF)




Artificial Intelligence: A Modern Approach














B.1Defining Languages with Backus-Naur Form (BNF)
In this book we define several languages, including the languages of propositional logic (235), first-order logic (276), and a subset of English (page 893). A formal language is defined as a set of strings where each string is a sequence of symbols. The languages we are interested in consist of an infinite set of strings, so we need a concise way to characterize the set. We do that with a grammar. The particular type of grammar we use is called a context-free grammar, because each expression has the same form in any context. We write our grammars in a formalism called Backus-Naur form (BNF). There are four components to a BNF grammar:


•A set of terminal symbols. These are the symbols or words that make up the strings of the language. They could be letters (A, B, C,...) or words (a, aardvark, abacus, ...), or whatever symbols are appropriate for the domain.

•A set of nontermi...

### B.2 Describing Algorithms with Pseudocode




Artificial Intelligence: A Modern Approach














B.2Describing Algorithms with Pseudocode
The algorithms in this book are described in pseudocode. Most of the pseudocode should be familiar to programmers who use languages like Java, C++, or especially Python. In some places we use mathematical formulas or ordinary English to describe parts that would otherwise be more cumbersome. A few idiosyncrasies should be noted:


•Persistent variables: We use the keyword persistent to say that a variable is given an initial value the first time a function is called and retains that value (or the value given to it by a subsequent assignment statement) on all subsequent calls to the function. Thus, persistent variables are like global variables in that they outlive a single call to their function; but they are accessible only within the function. The agent programs in the book use persistent variables for memory. Programs with persistent variables can be implemented as objects in object-...

### B.3 Online Supplemental Material




Artificial Intelligence: A Modern Approach














B.3Online Supplemental Material
The book has a Web site with supplemental material, instructions for sending suggestions, and opportunities for joining discussion lists:

•aima.cs.berkeley.edu

The algorithms in the book, and multiple additional programming exercises, have been implemented in Python and Java (and some in other languages) at the online code repository, accessible from the Web site and currently hosted at:

•github.com/aimacode


...

## Bibliography




Artificial Intelligence: A Modern Approach














Bibliography
The following abbreviations are used for frequently cited conferences and journals:


AAAI
Proceedings of the AAAI Conference on Artificial Intelligence


AAMAS
Proceedings of the International Conference on Autonomous Agents and Multi-agent Systems


ACL
Proceedings of the Annual Meeting of the Association for Computational Linguistics


AIJ
Artificial Intelligence
(Journal)


AIMag
AI Magazine


AIPS
Proceedings of the International Conference on AI Planning Systems


AISTATS
Proceedings of the International Conference on Artificial Intelligence and Statistics


BBS
Behavioral and Brain Sciences


CACM
Communications of the Association for Computing Machinery


COGSCI
Proceedings of the Annual Conference of the Cognitive Science Society


COLING
Proceedings of the International Conference on Computational Linguistics


COLT
Proceedings of the Annual ACM Workshop on Computational Learning Theory


CP
Proceedings ...

## Index




Artificial Intelligence: A Modern Approach














Index
Page numbers in bold refer to definitions of terms and algorithms.
Page numbers in italics refer to items in the bibliography.
Symbols
α (alpha) learning rate. 816
α (alpha) normalization constant. 418
∧ (and), 235
x2 (chi squared), 682
⊢ (derives), 234
|= (entailment), 232
ϵ (epsilon)-ball, 691
∃ (there exists), 280
∀ (for all), 279
γ (gamma) discount factor, 632
̺ (gap) in sentence. 897
| (given). 407
⇔ (if and only if). 235
⇒ (implies), 235
~ (indifferent), 520
λ (lambda)-expression, 277
∇ (nabla) gradient. 138
¬ (not), 235
∨ (or), 235
≻ (preferred), 520
σ (sigma) standard deviation, 1079
T (matrix transpose), 1077
A
A(s) (actions in a state), 552
A* search, 103–108
Aaronson, S., 1035, 1085
Aarts, E., 190, 1085
Aarup, M., 402, 1085
Abbas, A., 549, 550, 1085
Abbeel, P., 80, 516, 551, 638. 737, 841, 868, 872, 873, 985, 986, 1055, 1085, 1091, 1095, 1097, 1099, 1102, 1103, 1112
Abbott, L. F., 839, 873, 1092
ABC computer, ...

