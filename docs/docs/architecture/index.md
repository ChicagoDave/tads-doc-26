# Architecture

These documents explain how TADS 3 and the adv3 library are built — the layers, the patterns, and the practical knowledge you need to write and extend IF games.

## [Architecture Overview](overview.md)

The big picture. How the T3 VM, the system library, the adv3 library, and your game code fit together. Class hierarchy maps, the containment and sensory models, the turn cycle, and the build pipeline.

## [The Parser Pipeline](parser-pipeline.md)

How a line of text becomes a resolved action. The grammar matching, command ranking, noun resolution, and disambiguation systems — their class hierarchies, design patterns, and the hooks game authors can use to extend the parser.

## [Action Resolution](action-resolution.md)

How a parsed action becomes a change in the world. The action class hierarchy, scope, the verify/precondition/check/action execution cycle, the remapping system, and the practical intervention points where game authors can hook in.

## [Sense and Perception](sense-perception.md)

How the four senses — sight, sound, smell, and touch — propagate through the containment tree. Materials and transparency, brightness propagation, sense path calculation, SenseConnectors, sensory emanations, and how it all feeds into scope.

## [Containment Model](containment-model.md)

How the physical world is structured as a containment tree. The location/contents hierarchy, container types and their boundaries, reachability and touch paths, bulk and weight capacity, nested rooms and staging locations, and multi-location objects.

## [IF Development Guide](development-guide.md)

A conceptual roadmap for building adv3 games. Covers the minimal game skeleton, rooms and travel, the Thing hierarchy, actors and conversations, output formatting, timed events, scoring, and source organization.

## [Design Patterns](design-patterns.md)

The recurring code patterns in adv3 and how to use them. The dobjFor/iobjFor property set system, mix-in composition, state objects, modify vs. subclassing, scenery management, daemons and fuses, agenda-driven NPCs, and report accumulation.

## [Quick Reference](quick-reference.md)

A dense cheat sheet for active development. Class tables, action handler syntax, common properties, template syntax, string formatting, conversation setup, timed events, and debugging commands — all on one page.
