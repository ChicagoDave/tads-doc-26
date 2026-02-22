# AllAction

*class* — defined in [action.t](../by-file/action.t.md) (line 3044)


"All" and "Default" are a pseudo-actions used for dobjFor(All), iobjFor(Default), and similar catch-all handlers. These are never executed as actual actions, but we define them so that dobjFor(All) and the like won't generate any warnings for undefined actions.


**Superclass chain:** `object` > **AllAction**
