---
name: telephony-and-conferencing
description: Runs voice and meeting infrastructure — phone systems and numbers, emergency calling obligations, conference rooms and their AV, call recording and its retention consequences, and the porting that makes provider changes go badly. Use this to replace a phone system, fix rooms nobody can start a meeting in, meet emergency-calling requirements, port numbers without losing service, or work out why voice quality degrades only sometimes.
---

# Telephony and conferencing

Voice is the service where failure is most visible and least tolerated. Nobody files a ticket when
email is slow; everyone notices a dead phone, and customers notice first. It is also the service
most likely to be nobody's stated job — inherited from a facilities vendor, half-migrated to a
collaboration suite, with the parts that still work unowned.

## Voice is an application on the network now, and behaves like one

A phone system is real-time traffic sharing a network built for everything else. That makes voice
the first service to expose problems the network was hiding: jitter, packet loss, and asymmetric
routing that a file transfer absorbs and a conversation does not.

Quality complaints are almost never about the phone system. Diagnose them as network problems on
the path, and prioritize voice traffic explicitly rather than assuming capacity is enough — a link
with headroom on average still queues at the moment someone is talking. See
`it-operations:network-administration` for the diagnosis order.

The corollary is that a network change can break voice without touching it, which is an argument
for including voice in the change review rather than discovering it afterward.

## Emergency calling is a legal obligation, not a feature

Emergency calls must reach the right dispatch center with a location accurate enough to send help
to, and in most jurisdictions this is regulated rather than optional. Two requirements that
routinely get missed: a caller must be able to dial emergency services directly without a prefix,
and someone on site should be notified when such a call is placed.

Remote and hybrid work is what makes this hard. A softphone carries its number, not its location,
so a home worker dialing for help may route to the office's dispatch center hundreds of miles away.
Provider features exist to handle this and they require configuration and user prompting to work.

Treat location records as data that goes stale. Desk moves, new floors, and new home addresses all
invalidate them, and nobody discovers the error at a good moment.

## Numbers are assets, and porting is the risky part

Phone numbers are contractually held by the losing provider until a port completes, which gives
that provider both the ability and the incentive to make leaving slow. Ports fail on trivial
mismatches — a service address that does not match the billing record exactly, an account PIN
nobody has, a number that was never actually on the account.

Get a current bill and a copy of the losing provider's records before scheduling anything, port a
small test group first, and never cancel the old service until the new one carries live traffic.
Canceling early does not accelerate the port; it strands the numbers.

Keep the number inventory somewhere permanent, with what each number is for. Main lines, fax lines
that still receive real documents, and numbers printed on physical material are all things that
cost more than they appear to when lost.

## Rooms fail on the last two feet

Conference rooms are where the technology is judged, and they fail in the mundane ways: the wrong
cable, a display on the wrong input, a control panel asleep, a camera pointed at a wall. A room
that takes five minutes to start a meeting is a room people stop booking.

Standardize aggressively — the same room build repeated is supportable, and eight bespoke rooms are
not. One-touch join is worth real money because it eliminates the entire class of failure. Monitor
rooms as infrastructure rather than waiting for complaints; most platforms report device health,
and a dead room found on Monday morning beats one found by an executive at nine o'clock.

## Recording creates records

Call and meeting recording is trivial to enable and produces material that is discoverable in
litigation, subject to privacy law, and subject to consent requirements that vary by jurisdiction —
some places require every party to consent, not just one.

Decide retention before switching it on, and default to short. Transcripts and AI-generated
summaries are records too, and they are increasingly produced automatically by the meeting platform
whether or not anyone chose it. `legal-risk:privacy-and-data-protection` owns the obligations; this
skill owns knowing the feature creates them.

## Never

- Deploy softphones without solving location for emergency calls.
- Cancel the losing provider before numbers have ported and carry traffic.
- Enable recording before deciding retention.
- Diagnose voice quality inside the phone system when the network is untested.
