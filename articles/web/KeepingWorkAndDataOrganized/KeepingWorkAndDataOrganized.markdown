
# Keeping Work and Data Organized

*Goal*: defining a simple system that allows to keep my work and data organized.

Problem: people usually do not have a very good system to archive the work that they do for later retrieval. A hodgepodge system result in many ideas forgotten, project started but never picked-up for continuation later and countless hours wasted. Let's define the properties of a good information system, then describe and instantiation of such a system. 

## Properties of a Good Information System

**Very Important**

- Everything important should be organized in a way that is it easy to retrieve and to keep working on it at a later time.
- The question "Where should I store / retrieve X?" should have one, unambiguous answer.
- The effort for serendipitous ideas to be noted down and later reviewed should be really low.
- The data should be future proof so that at any point in the future, work can resume on a project that was shelved.

**Less Important**

- There should be a way to easily identify.
- The system should allow for "global search".


## The Three Stages of Information: Capture, Production And Archival

I believe that information has three phases: **capture**, **production** and **archival**.

The three phases are somewhat at odds with each other. Capture should be flexible and allow anything to be kept for later evaluation or storage. Unlike production and archival, it can be chaotic, primitive and disorganized but _available everywhere_. 

During  the **production** phase, you want a place when you can easily bump into the data and work on it. If there is too much stuff, too many files and things to look at, it becomes easy to never finish something or to make the barrier to spend some time on it so high that not much effort is done. In the production mode, you need focus and ease of modification. Also, ongoing work is hard to categorize (it may still be evolving), so it should not be categorized at this time.

The **archive** phase should allow for easy retrieval, but it does not matter if there is a lot of stuff as long as it is labeled and organized properly. This is where you evaluate work done in the production mode and put it somewhere where answering the question "Where is X?" has a unique and easy answer. It is also important to future-proof the data for the archive stage. Make it search-able as much as possible (add search-able metadata). In order of priority use: plain text, a non-proprietary modifiable format that is human-understandable, a proprietary format with an exported non-modifiable version if possible (for example, a proprietary document format + export as .pdf so that you can at least always read it).

## How I Implement Capture, Production And Archival

Any system that has the properties described above is good. If it works for you, share and keep using it. Here is how _I_ organized my things. It might now be perfect but it's pretty good :).

**Capture**. I use my phone to take picture of things that are important and mail it to myself. I use pen / paper a lot because it helps me be creative, but I never keep any paper around. As soon as I am done and I feel like I want to keep it, I take a picture and e-mail it to myself. I also e-mail myself reminders and have a command-line script so that the amount of effort to jolt down an idea is minimal. I also always keep pen and paper around my bed for those "wake-up-in-the-middle-of-the-night-with-an-idea" moments are not lost. For longer things that need to be drafted, I use an online editing suite (google docs or office 365).

Capture is the only mode where I allow the information to _not be all at the same single place_. This is because I do not always have access to my data repositories (my personal computer at home), and I never want to waste an idea because I cannot capture it.

Things never stay in capture mode for too long. A lot of the times, the next day I feel like it is not good and I just throw the ideas / notes away. If I think they are worth it, I transfer them in production. My capture "inbox" is never more than 15 items. If it is, I take some time to either delete and migrate to production.

**Production**. When things graduate from capture to production mode, I transfer them from disparate data repositories to my main an only data repository. This means under my "./data/" folder on my computer. This data is backed-up forever, cannot be lost / destructed and most importantly, _all the data is all at the same place_. I never allow important data to be solely in the cloud. This produce fragmentation that makes it impossible and complicated to keep track of everything. To keep at least some of the stuff accessible at all time, I use dropbox-onedrive-googledrive like services.

Data in production are kept in a format that is _forever modifiable_. I use plain text as much as possible, open formats that are simple and can be human-readable (I can write a scrip in the future to export my information if necessary).

Sometimes I get over-excited about a project, do some work on it and then lose interest. I eventually move those to the "archived/[year]/abandoned" folder, so that I can always go back to it eventually if I want but it does not clutter my "production" folder.

**Archive**. This is the most difficult part. Unfortunately, I have not archived universal search-ability yet. This is because it is simply not convenient to use plain-text for everything and some stuff is not text-based (art, pictures, ...). What I do is to keep everything under a single folder in my file-system:

    /data/archive
    /data/dev

/data/dev contains the data in _production_ phase, and archive in archival phase. The data in archive is either plain-text and indexable, or contains an "info.txt" file that describes it. All of my "info.txt" files are indexed, so I write-down as many relevant keywords that I can think of there. I also always try to have folders and filenames that are relatively long and descriptive. I have a relatively complex script system that allows me to retrieve my data but at the end of the day I should be able to retrieve things I care about by simply using an index of all folder / filenames. For example, if I want to know where my tax information is stored for 2012, I can do the simple:

    find > index
    grep -i taxes.*2012 index
    
(The answer is my taxes are under the /data/archive/taxes_2012/ folder.) I try to use dates (of course, in [ISO8601](http://en.wikipedia.org/wiki/ISO_8601) format because it is sortable alphabetically) in my file / folder names as much as I can.




