
# Best Software Engineering Practices

How do you build good software? How do you not build bad software?

Unfortunately, there is no uncontroversial, authoritative, science-backed answer to this questions. The best you will find are opinions, which are hard to objectively assess. But some opinions are more fact-based than other, so I will try to sift through the pile of information to figure-out what's worth occupying mind-share.

I usually try to write only on things that are facts and evidence based, but for this topic I make an exception since I think that a tentative answer is better than no answer.

## Why Isn't There a Good Answer to this Question Yet?

It is shocking that science has not yet gotten around to answer the question given how much is at stake. I think the base of the problem is similar to the failure of economics to predict actual outcome before the advent of behavioral economics. Behavioral economy is a relatively new field, and the first to acknowledge that you cannot assume that all actors in an economic system are rational -- you have to acknowledge that humans do not always act in a rational way (see [cognitive biases](http://en.wikipedia.org/wiki/Cognitive_bias)) in order to predict crowd behavior and its economic impact.

An example of this is the failure of metric-based reward to promote good outcomes in software companies. Let's assume it is a fact that having a low bug count and lots of unit-tests are undeniably good for a software system (I am not saying that it is, but bear with me). It seems reasonable from a managerial perspective to reward employees that fix a lot of bugs and write a lot of unit tests. However, every time that I saw such system in software companies, there was an initial phase where it seemed to work, and then rampant gaming of the system by the employees who eventually figure out how to maximize their personal gains.

It seems reasonable to instigate metric systems in software companies, but because of the human factor it might be doomed from the beginning. Or there may be a good way to have metrics (hard to game? secret metrics?) without the bad side-effect, but I have yet to hear about one that worked well.

# TO write and order

- SOLID
- Joel's post: unit-tests, ...
- Code complete 2: ref & management
- Manage complexity [CC2], add functionality without adding complexity.
- Split into modules, micro-services & equivalence with small modules.
- The pragmatic programmer

