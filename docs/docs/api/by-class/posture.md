# Posture

*class* — defined in [actor.t](../by-file/actor.t.md) (line 103)


Postures. A posture describes how an actor is internally positioned: standing, lying, sitting. We represent postures with objects of class Posture to make it easier to add new game-specific postures.


**Superclass chain:** `object` > **PostureGlobal objects:** [lying](lying.md), [sitting](sitting.md), [standing](standing.md)


## Properties


### `msgVerbI`

Defined in en_us.t, line 2604

Intransitive and transitive forms of the verb, for use in library messages. Each of these methods simply calls one of the two corresponding fixed-tense properties, depending on the current tense.


### `// msgVerbIPast`

Defined in en_us.t, line 2616

our past-tense intransitive form ("he stood up")


### `// msgVerbIPresent`

Defined in en_us.t, line 2613

our present-tense intransitive form ("he stands up")


### `msgVerbT`

Defined in en_us.t, line 2605


### `// msgVerbTPast`

Defined in en_us.t, line 2622

our past-tense transitive form ("he stood on the chair")


### `// msgVerbTPresent`

Defined in en_us.t, line 2619

our present-tense transitive form ("he stands on the chair")


### `// participle`

Defined in en_us.t, line 2625

our participle form


## Methods


### `setActorToPosture(actor, loc)`

Defined in actor.t, line 111

put the actor into our posture via a nested action


### `tryMakingPosture(loc)`

Defined in actor.t, line 108

Try getting the current actor into this posture within the given location, by running an appropriate implied command.
