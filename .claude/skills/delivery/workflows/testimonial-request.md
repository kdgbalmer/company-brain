# Testimonial request

## Purpose

Ask a happy client for a testimonial at the right moment, in a way that's easy for them to say yes to, and when one arrives, save it with their permission recorded so marketing can use it.

## Use when

- The owner wants a testimonial: "ask Rosa for a testimonial", "who should I ask for a review?", "I need some social proof for my sales page".
- A client has just had a win, or the work is ending (spotted in `session-follow-up` or `client-wrap-up`).
- A testimonial has arrived: "Ben sent me this lovely message, save it", "here's the review Ana left".

## Load first

- `departments/delivery/clients/<client-name>.md` (goals, log, wins)
- `departments/delivery/testimonials.md` (testimonials already saved)
- `business/voice.md` (tone rules, samples)
- `business/tools.md` (inbox connected? review site used?)
- `departments/delivery/context.md` (where the owner likes reviews posted, if noted)

## Steps

**Asking**

1. **Check the moment.** A good moment is right after a clear win the client would name themselves, when they've said something glowing, or near the end of the work. A bad moment is when something has gone wrong, they're behind, or an invoice is in dispute. If the owner asks "who should I ask?", read the client files and suggest up to three clients at a good moment, with the win for each.
2. **Name the win.** From the client file, write one line on what changed for them, in their words if possible. Don't exaggerate it.
3. **Draft the ask.** Short, personal, in the owner's voice. Mention the win, ask if they'd be happy to share a few lines about working together, and make it easy with two or three prompts (where were you before, what changed, what would you tell someone thinking about it). If the owner uses a review site, include the link from `tools.md` or `context.md`. Ask permission to use their words, and whether they'd like their full name, first name only, or anonymous.
4. **Note it.** Add a dated line to the client's Log that a testimonial was requested.

**Saving**

5. **Record exactly what they wrote.** Never tidy up, shorten or rewrite a client's words without their okay. If the owner wants a shorter version, draft it and mark it "needs the client's approval".
6. **Record permission.** Ask the owner what the client agreed to: where it can be used (website, social, sales pages), and how they want to be named. If permission isn't clear, save it as "permission not confirmed" so marketing doesn't use it.
7. **Save it.** Add an entry to `departments/delivery/testimonials.md` (create the file with a `# Testimonials` heading if it doesn't exist):

   ```
   ## <Client name or "Anonymous"> (YYYY-MM-DD)
   - Offer: <the offer they bought>
   - Permission: <e.g. yes, website and social, first name only | not confirmed>
   - Source: <email, review site, message>
   > <their exact words>
   ```

8. **Tell marketing.** Say in one line that it's saved and can be used in a post or on the website, if permission allows.

## Check before handing over

- The ask goes to a client at a good moment, and mentions a real win from their file.
- Saved testimonials are word for word, with permission and naming recorded.
- Nothing invented: no made-up quotes, results or numbers.

## Save to

The ask: `outputs/delivery/YYYY-MM-DD-testimonial-ask-<client-name>.md`, shown in the chat as well. Received testimonials: `departments/delivery/testimonials.md`. A dated note in `departments/delivery/clients/<client-name>.md`.

## Needs a yes

Sending the ask to the client by email or message, and publishing or posting the testimonial anywhere. Show the final text, who it goes to and how it will be sent first. A testimonial without confirmed permission is never used.
