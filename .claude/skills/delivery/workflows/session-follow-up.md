# Session follow-up

## Purpose

Turn the owner's notes from a session, meeting or job into a short recap email for the client with the actions agreed, and update the client's private file so the next session starts where this one ended.

## Use when

A session has just finished: "write up my session with Dana", "here are my notes from the Brightside meeting, send a recap", "turn this into actions for Leo", "log today's visit".

## Load first

- The session notes or transcript (pasted by the owner, or from a connected meeting tool)
- `departments/delivery/clients/<client-name>.md`
- `business/voice.md` (tone rules, samples)
- `business/tools.md` (inbox, calendar, meeting tool connected?)
- `departments/delivery/context.md` (the owner's recap format, if saved)

## Steps

1. **Get the notes.** If the owner hasn't pasted them, ask for them. Rough notes, bullet points or a voice-to-text dump are fine. If a meeting tool is connected and has a transcript, read that.
2. **Pull out what matters.** What was covered, any breakthroughs or decisions, what's still open, and every action agreed, on both sides, with a date if one was said. Don't add actions nobody agreed to. If something is unclear (who owns an action, a date), ask.
3. **Update the client file.** Add a dated entry to the Log (three to six lines), update Actions agreed (tick off finished ones, add new ones), and set Next date if it was agreed. Update Goals only if the goals changed.
4. **Draft the recap email.** In the owner's voice, short and warm:
   - one line on what you covered or the big takeaway
   - "What you're doing next" (the client's actions, with dates)
   - "What I'm doing next" (the owner's actions, if any)
   - the next session, meeting or appointment date

   Leave out anything private the owner wouldn't want written down, and anything the notes mark as for the owner only. If in doubt, ask.
5. **Remind the owner of their own actions.** List what the owner promised, so nothing slips.
6. **Spot a testimonial moment.** If the notes show a clear win or the client said something glowing, mention it in one line and offer to run `testimonial-request`. Don't ask in this email.

## Check before handing over

- Every action in the email was actually agreed. Nothing invented.
- The client would recognise the session from the recap.
- Nothing in the email that the owner noted as private.
- The client file has a new dated log entry and an up-to-date action list.

## Save to

Update `departments/delivery/clients/<client-name>.md`. Save the recap to `outputs/delivery/YYYY-MM-DD-recap-<client-name>.md`. Show the recap email in the chat.

## Needs a yes

Sending the recap email or message to the client, and sending a calendar invite for the next date. Show the final text, who it goes to and how it will be sent first. Client notes are private and never leave this folder.
