
# Meta: Most Important Points

- Information in one and only one authoritative place.

# Book The Pragmatic Programmer

## Chapter 1: A Pragmatic Philosophy

**Chapter overview**: this chapter contains miscellaneous tips related to the discipline of software engineering. IMHO this chapter is not too useful.

### Take Responsibility

When something goes bad, explain instead of giving excuses. Some things outside of your control might have happened, but there is rarely nothing you could have done to avoid the issue.

Work the conversation in your head before having it with your boss. Think about what will be asked.

Provide solutions, not excuses. Have a plan so that the problem does not happen again.

### Software Entropy, Software Rot

The broken window theory: once you start neglecting the code-base, neglect becomes the expectation and propagates. The thing to fight is the _perception_ that the project does not deserve caring.

### How to Get Projects Started

In some companies the process to get started is so brutal (approval from too many people, committees, process) it makes sure nothing novel ever gets done. A way to get people on board is to just do it, and show it off. People are likely to get on board on what seems like an ongoing success.

### Good Enough Software

There is a cost to get software to be to a certain standard of quality. Like everything else, this quality has a cost opportunity. Consider the requirements, and define what quality you need.

### Your Knowledge Portfolio

Your knowledge and experience are your most important assets. Because technology evolves quickly, your knowledge depreciates with time.

Think of your knowledge like a financial asset:

- Invest frequently: get a _habit_ of always learning. Daily, weekly, monthly, yearly.
- Diversify: have a safe base you can fall-back on, as well as learning some of the hot new stuff that you get you your next dream gig.
- Review: periodically review your knowledge portfolio. Invest in what is lacking.

Make use of every minute of free time. Carry books you are reading on your phone so that you can use the 10 minutes you are waiting for the desist to read a few pages. When on the bus, have a stack of problem to think about and solve them in your head.

Always seek out other enthusiasts. Associate with them. Learn from them. Especially people outside of your circle / company so that you can learn novel things.

### Communicate

When you communicate, whether it is an important meeting, mail, specification document, plan it out. Write it. Iterate over it. Ask yourself if it conveys what it needs to convey. Only show up at the meeting / send the document when it conveys exactly what you want to trigger the outcome you want. Jot down the big picture of what you want to accomplish, and make sure the big thing conveys those principal points effectively.

Target your audience. Your communication is only effective if your target audience can understand it and is helped by it.

## Chapter 2: A Pragmatic Approach

**Chapter overview**: AAA.

### The Evils of Duplication, DRY Principle

@@tag-main_point: Principle: information at one authoritative place, and one place only.

DRY (Don't Repeat Yourself) principle: "_every piece of knowledge must have a single, unambiguous, authoritative representation within a system_".

Information change. If it is not clear where that information belongs, it will be duplicated and someone seeking it will find one of the place, not necessarily the most recent one. Once you have information at more than one place, it becomes too much of a burden to update all the locations so things start failing apart (not being updated, ...).
