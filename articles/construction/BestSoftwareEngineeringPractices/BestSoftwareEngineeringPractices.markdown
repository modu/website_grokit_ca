
# Best Software Engineering Practices

How do you build good software? How do you not build bad software?

Unfortunately, there is no uncontroversial, authoritative, science-backed answer to this questions. The best you will find are opinions, which are hard to objectively assess. But some opinions are more fact-based than other, so I will try to sift through the pile of information to figure-out what's worth occupying mind-share.

I usually try to write only on things that are facts and evidence based, but for this topic I make an exception since I think that a tentative answer is better than no answer.

# Goal: Quotable Things

For example, DRY principle. Want to have this page so that I can eventually point people here http://.../Endineering/#DRY for a rationale of a code comment or decision.

Make sure that all of those come with references and justifications.

# How to Stay on Top

- Always want to play at the limit of your ability: 6 pronged approach sharpen the saw, motivation and reason for all of those.

## Why Isn't There a Good Answer to this Question Yet?

It is shocking that science has not yet gotten around to answer the question given how much is at stake. I think the base of the problem is similar to the failure of economics to predict actual outcome before the advent of behavioral economics. Behavioral economy is a relatively new field, and the first to acknowledge that you cannot assume that all actors in an economic system are rational -- you have to acknowledge that humans do not always act in a rational way (see [cognitive biases](http://en.wikipedia.org/wiki/Cognitive_bias)) in order to predict crowd behavior and its economic impact.

An example of this is the failure of metric-based reward to promote good outcomes in software companies. Let's assume it is a fact that having a low bug count and lots of unit-tests are undeniably good for a software system (I am not saying that it is, but bear with me). It seems reasonable from a managerial perspective to reward employees that fix a lot of bugs and write a lot of unit tests. However, every time that I saw such system in software companies, there was an initial phase where it seemed to work, and then rampant gaming of the system by the employees who eventually figure out how to maximize their personal gains.

It seems reasonable to instigate metric systems in software companies, but because of the human factor it might be doomed from the beginning. Or there may be a good way to have metrics (hard to game? secret metrics?) without the bad side-effect, but I have yet to hear about one that worked well.

# TO write and order

- Expose your work to others, code in the wild. Github, post of reddit, ...
- SOLID
- Joel's post: unit-tests, ...
- Code complete 2: ref & management
- Manage complexity [CC2], add functionality without adding complexity.
- Split into modules, micro-services & equivalence with small modules.
- The pragmatic programmer
- Principle of least surprise.
- Python's PEP approach.
- best so: alert early on issues, never swallow
- best Eng logging in nanespace, can change at compilation or dynamically
- Concern about modules and dependencies
- logging: in a namespace, levels plus event name so that it can be aggregated
- big level thinking logic consistent at the details of the code
- management: when people own thing, do no micro manage. Reward for what they get done and the quality, not for impact since impact is out of their control and can lead to bad behavior (force things through to reap the rewards).
- Errors and scenarios should be easy to reproduce. Implication with a lot of small internal components. Post from dude.
- Use reversible path (pragmatic programmer).
- DP: total number of possible states.
- engineering principles: management, look at incentives, do not trust good human nature, it only goes so far
- ZULU time EVERYWHERE

- [Agile Manifesto](http://agilemanifesto.org/)
--> Robert C. Martin book about SOLID.
--> Other people.co

- Magic is not good --- LOOK AT THAT, ONLY A LINE OF CODE! Compromise complexity, obscurity, less flexibility.

- Dependency injection, micro-services : beware the buzzwords. Does it reduce complexity

# Logging

- Logs from ALL machines accessible / queryable in one place.
- Logging in a tree based structure log4js, dynamic enable disable part of tree.

# Principles

## DRY

Code comments < code that is understandable. Better to erase a comment that repeats information that is or can be expressed by clean code.

Reference(s):

- TPP section?

## SOLID - S: Liskov Substitution Principle

## Complexity Management

## Complexity Management 2: Have to Have A Mental Model that Maps to Code

Reference(s):

- None, this is conjecture on my part.

## Orthogonality

Reference:

- TPP section?

# Appendix: Quote

Let no youth have any anxiety about the upshot of his education, whatever the line of it may be. If he keep faithfully busy each hour of the working-day, he may safely leave the final result to itself. He can with perfect certainty count on waking up some fine morning, to find himself one of the competent ones of his generation, in whatever pursuit he may have singled out. Silently, between all the details of his business, the power of judging in all that class of matter will have built itself up within him as a possession that will never pass away. Young people should know this truth in advance. The ignorance of it has probably engendered more discouragement and faint-heartedness in youths embarking on arduous careers than all other causes put together.

It may be that 10,000 hours, not 10 years, is the magic number. Or it might be some other metric; Henri Cartier-Bresson (1908-2004) said Your first 10,000 photographs are your worst. True expertise may take a lifetime: Samuel Johnson (1709-1784) said Excellence in any department can be attained only by the labor of a lifetime; it is not to be purchased at a lesser price. And Chaucer (1340-1400) complained the lyf so short, the craft so long to lerne. Hippocrates (c. 400BC) is known for the excerpt ars longa, vita brevis, which is part of the longer quotation Ars longa, vita brevis, occasio praeceps, experimentum periculosum, iudicium difficile, which in English renders as Life is short, [the] craft long, opportunity fleeting, experiment treacherous, judgment difficult. Of course, no single number can be the final answer: it doesn't seem reasonable to assume that each of programming, chess playing, checkers playing, and music playing could all require exactly the same amount of time t ...
