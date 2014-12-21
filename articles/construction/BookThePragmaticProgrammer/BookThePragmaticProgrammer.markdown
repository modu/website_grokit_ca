
# Meta: Most Important Points

- Information in one and only one authoritative place.
- Orthogonality
- Reversibility
- ?Complexity?

# Book The Pragmatic Programmer

The book is a set of observations without real overarching theme (by design). This books was written in 2000, it is surprising how prescient that book was. Reading it in 2015 some of the information are now a  given (write unit-tests, use SCM, ...), but some of the items are still pearls of wisdom that are good to review periodically.

## Chapter 1: A Pragmatic Philosophy

**Chapter overview**: AAA.

### 1. Take Responsibility

When something goes bad, explain instead of giving excuses. Some things outside of your control might have happened, but there is rarely nothing you could have done to avoid the issue.

Work the conversation in your head before having it with your boss. Think about what will be asked.

Provide solutions, not excuses. Have a plan so that the problem does not happen again.

### 2. Software Entropy, Software Rot

The broken window theory: once you start neglecting the code-base, neglect becomes the expectation and propagates. The thing to fight is the _perception_ that the project does not deserve caring.

### 3. How to Get Projects Started

In some companies the process to get started is so brutal (approval from too many people, committees, process) it makes sure nothing novel ever gets done. A way to get people on board is to just do it, and show it off. People are likely to get on board on what seems like an ongoing success.

### 4. Good Enough Software

There is a cost to get software to be to a certain standard of quality. Like everything else, this quality has a cost opportunity. Consider the requirements, and define what quality you need.

### 5. Your Knowledge Portfolio

Your knowledge and experience are your most important assets. Because technology evolves quickly, your knowledge depreciates with time.

Think of your knowledge like a financial asset:

- Invest frequently: get a _habit_ of always learning. Daily, weekly, monthly, yearly.
- Diversify: have a safe base you can fall-back on, as well as learning some of the hot new stuff that you get you your next dream gig.
- Review: periodically review your knowledge portfolio. Invest in what is lacking.

Make use of every minute of free time. Carry books you are reading on your phone so that you can use the 10 minutes you are waiting for the desist to read a few pages. When on the bus, have a stack of problem to think about and solve them in your head.

Always seek out other enthusiasts. Associate with them. Learn from them. Especially people outside of your circle / company so that you can learn novel things.

### 6. Communicate

When you communicate, whether it is an important meeting, mail, specification document, plan it out. Write it. Iterate over it. Ask yourself if it conveys what it needs to convey. Only show up at the meeting / send the document when it conveys exactly what you want to trigger the outcome you want. Jot down the big picture of what you want to accomplish, and make sure the big thing conveys those principal points effectively.

Target your audience. Your communication is only effective if your target audience can understand it and is helped by it.

## Chapter 2: A Pragmatic Approach

**Chapter overview**: AAA.

### 7. The Evils of Duplication, DRY Principle: Don't Repeat Yourself

@@tag-main_point: Principle: information at one authoritative place, and one place only.

DRY (Don't Repeat Yourself) principle: "_every piece of knowledge must have a single, unambiguous, authoritative representation within a system_".

Information change. If it is not clear where that information belongs, it will be duplicated and someone seeking it will find one of the place, not necessarily the most recent one. Once you have information at more than one place, it becomes too much of a burden to update all the locations so things start failing apart (not being updated, ...).

Question: Where does information about x goes? Need to have a single unambiguous answer.

Code comments are often a needless duplication that eventually becomes out of sync. If code can express it, better to have no comment and expressive code. If the comment duplicates something that is in the code, better to erase the comment.

### 8. Orthogonality

Things are simpler when components are made to be orthogonal. Orthogonality means that components need to be isolated from each other. This way, if components X interacts with component Y, when Y change X does not have to change.

This is about complexity management: as the number of features grows, grow complexity as little as possible by not having the complexity

#### A Few Observations on Orthogonality

Orthogonality has the side-effect of allowing better re-use and unit-testing.

Inheritance breaks orthogonality more than composition. Think about class X and Y, if X inherit from Y, a change in Y's functions and data directly impacts X. It is also the case with composition, but with composition at least X has to respect Y's interface, making it easier to have the two classes change without breaking each other.

Applies to team with week defined responsibilities. But does not go over the fact that aligning becomes a nightmare.

Example of orthogonal systems: MVC.

### 9. Reversibility

When possible, select a course of action that preserve the most options for the longest.

It's hard to make good decision the first time around. Keep things flexible so that decision can be made once you have more information.

You know how to build the system well once you are done writing the first system that did not turn out so well. If re-writing the whole thing is not an option (wasn't a prototype), then if your picked reversible choices at least you can re-write the parts that are the worst.

### 10. Tracer Bullets

One way to hit target is to specify the system to death. Itemize every requirement and constrain the environment at the time where you know the least about how to build the system well.

The principle of tracer bullets is to do the opposite. Build an end to end system with minimum functionality cheaply and iterate fast. A fully built system that only implement a few requirements is used as a 'tracer', after which the stakeholders can adjust course.

#### Tracer Bullets and Agile Practices

Tracer Bullets foreshadows the [Agile Manifesto](http://agilemanifesto.org/), which was published two years after The Pragmatic Programmer. This is not a coincidence that both authors of the Pragmatic Programmer are signatories of The Agile Manifesto.

### 11. Prototypes and Post It Notes

Prototypes are meant to brainstorm new ideas and figure-out the possible issues with using risky new ideas and architectures.

Prototypes can be, but do _not_ have to be code. White-boards diagrams and UI mock-ups are also fine prototypes.

Prototypes have to be throw away code. Make sure that management understands that this code is not meant, cannot be used for production. If not, you are tracing bullets, you are not prototyping. And tracing bullets do not bring you the same exploratory benefits of prototyping.

### 13. Estimating

Give estimate in the largest possible word. If you think something will take 48 hours, say two days, if you think it will take 15 days, say a little over a week. This is because estimating has a fudge factor, and if you use big, precise numbers, people will naturally assume that the fudge factor is lower (e.g: you said 48 but took 52, how dare you! You said two days but took two and a half -- cool).

When estimating, use the following steps:
- Understand.
- Build a model.
- Break down into components.
- Evaluate risk.

Keep track of your estimates and how long the project really ended up taking. Having this data will help you train yourself to produce more and more accurate estimates. Do not waste a chance to learn by not keeping yourself accountable.

## Chapter 3: Resume

### 14. Use Plain Text

# Links and References

- http://blog.codinghorror.com/a-pragmatic-quick-reference/
