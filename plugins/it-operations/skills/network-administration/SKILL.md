---
name: network-administration
description: Designs and operates the corporate network — segmentation, remote access, wireless, DNS and addressing, and diagnosing network problems. Use this to segment a network, set up or fix remote access, diagnose intermittent connectivity, plan addressing or DNS, or assess whether the network's trust assumptions still hold.
---

# Network administration

The network is the substrate everything else assumes works. It gets attention when it fails and is
otherwise expected to be invisible, which is why its design debts persist for years.

## Segment by trust, and mean it

A flat network means one compromised laptop reaches the finance server. Segmentation is the highest-
value structural control available and the most commonly deferred.

Separate at minimum: user devices, servers, management interfaces, guest, and anything unmanaged —
printers, cameras, building systems, contractor equipment. That last category is the recurring entry
point, because it is rarely patched and rarely owned.

Default deny between segments, and permit specific flows. Rules that accumulate without review become
an allow-all with extra steps; review them on a cadence and remove what no longer has a reason.

## Remote access

The perimeter stopped being a perimeter when the workforce and the workloads left it. Treat network
location as weak evidence of trust: being on the corporate network should not by itself grant access
to anything sensitive.

Prefer per-application access over full network access. A remote user needing one internal
application does not need a route to the entire internal estate, which is what a traditional VPN
grants by default.

Authentication and authorization policy belongs to `security:access-and-identity`; this skill
implements the network path.

## DNS and addressing are load-bearing

DNS failure presents as everything being broken, which is why it is misdiagnosed for the first
twenty minutes of many incidents. Run it redundantly, monitor resolution from the client's
perspective rather than the server's, and keep records under change control.

Plan addressing with room to grow and document it. Overlapping private ranges is the problem that
surfaces years later during an acquisition or a site merge and is expensive at exactly that moment.

## Diagnose in layers

Work bottom-up and prove each layer before moving on: physical, then addressing, then routing, then
name resolution, then the application. Most misdiagnosis comes from starting at the application
because that is where the complaint originated.

Intermittent problems are the hard case and need data over time, not a test at the moment someone
complains. Capture continuously at the affected point; a test that passes while nobody is suffering
proves nothing.

## Multiple sites multiply the failure modes, not the work

A second location does not double the network; it introduces a class of problem the first site
never had. Traffic now crosses a link you do not own, and every service the remote site depends on
becomes a question of where it lives.

Decide deliberately what is central and what is local. Authentication, name resolution, and print
are the three that hurt most when a site link drops — a location that cannot log in because the
domain controller is elsewhere is offline for every purpose, not just the one that failed. Local
survivability for those three is usually worth the cost; centralizing everything else usually is.

**Site links fail partially more often than completely.** A circuit that is up but degraded is
harder than one that is down, because nothing alerts and everything is slow. Monitor the link from
both ends and on the path rather than trusting the provider's portal, which reports their view of
their equipment.

Where a software-defined WAN is in use, it makes the degraded case survivable by steering traffic
between circuits, and it makes the topology something you configure centrally rather than per site.
That is a real gain and a real concentration of risk: the controller becomes a thing whose failure
is everyone's failure, so treat it as production infrastructure rather than a management tool.

Small sites accumulate exceptions. A closet without cooling, a switch nobody has patched, an
address range someone reused. Budget for a periodic physical visit — remote management does not
show you the cable run someone added, and the sites without permanent IT staff are exactly the ones
that drift furthest from the standard.

## Never

- Run a flat network and rely on host controls alone.
- Grant full network access where application access would do.
- Treat network location as sufficient evidence of trust.
- Diagnose from the application layer down.
