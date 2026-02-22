# CustomFixture

CustomFixture : [Fixture](fixture.md)

A CustomFixture is simply a fixture that uses the same custom message for taking, moving, and putting. In many cases, it's useful to customize the message for a fixture, using the same custom message for all sorts of moving. Just override **cannotTakeMsg**, and the other messages will copy it.

We haven't yet reached the point in our game where we need a CustomFixture, but we'll eventually use one to represent the pillars in a [temple](lever.md#temple).

See also the similar but subtly different [CustomImmovable](customimmovable.md).
