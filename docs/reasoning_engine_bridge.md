Reasoning Engine Bridge — Finite Number Framework

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa

Copyright (c) 2026 Christopher Thomas Ronio and Jeremey James Grice-Rosa. All rights reserved.

Companion to README.md, C_of_S.md, All_Things.md, composition_bridge.md, decomposition_bridge.md, and transformation_bridge.md.

1. Purpose

The Reasoning Engine Bridge defines an interface between the Finite Number Framework (FNF) and a computational state-transition reasoning engine.

The Finite Number Framework provides mathematical representations for positive magnitudes, logarithmic relations, boundary-relative positions, classifications, and balance conditions.

The ReasoningEngine provides a computational mechanism for exploring states, applying actions, enforcing invariants, detecting duplicate states, and searching for goal conditions.

The bridge connects these systems without requiring every property of a state to be represented as a number.

Its objectives are to:

Represent selected state properties as positive magnitudes.
Evaluate logarithmic relations and boundary-relative positions.
Apply composition, transformation, and decomposition operations.
Validate candidate states against structural and mathematical constraints.
Preserve explicitly declared invariants across transitions.
Define state equivalence and canonicalization for search.
Support goal-directed reasoning through valid action sequences.
Keep mathematical correctness separate from heuristic search decisions.

The bridge uses a hybrid architecture: general state representations remain intact, while FNF operations apply to selected properties for which they are mathematically appropriate.

2. Mathematical and Computational Domains
2.1 State space

Let 
𝑆
 denote the set of representable computational states.

A state may contain:

Geometric coordinates.
Graph vertices and edges.
Physical or abstract relationships.
Discrete labels.
Positive magnitudes.
Derived classifications.
Metadata required for validation or reconstruction.

A state is not required to be a positive real number.

2.2 Magnitude measurements

For each selected property, define a measurement function

𝑚
𝑖
:
𝑆
→
𝑅
>
0
.

The index 
𝑖
 identifies the measured property.

Examples include:

A strictly positive bond length.
A positive scale factor.
A positive ratio between two compatible measurements.
A strictly positive model parameter.

Properties that may be zero, negative, vector-valued, or categorical require a suitable representation or an explicitly defined positive measurement before logarithmic operations can be applied.

2.3 Logarithmic coordinates

For every valid measurement,

𝑞
𝑖
(
𝑠
)
=
ln
⁡
𝑚
𝑖
(
𝑠
)
.

For a positive boundary 
𝐵
𝑖
, define

𝑃
𝐵
𝑖
(
𝑠
)
=
ln
⁡
𝑚
𝑖
(
𝑠
)
𝐵
𝑖
.

For two positive measurements 
𝑚
𝑖
(
𝑠
)
 and 
𝑚
𝑗
(
𝑠
)
, define

𝑅
𝑖
𝑗
(
𝑠
)
=
ln
⁡
𝑚
𝑖
(
𝑠
)
𝑚
𝑗
(
𝑠
)
.

These definitions provide the FNF representation of selected state properties.

They do not replace the underlying state representation.

3. Architecture

The integrated system consists of five logical components.

3.1 State model

The state model stores the system being reasoned about.

It defines the valid data structures, structural relationships, and operations required to clone or reconstruct a state.

3.2 Action model

An action is a state-transition operation

𝑇
:
𝑆
→
𝑆
.

An action may transform coordinates, remove a graph edge, combine components, or perform another domain-specific operation.

Actions should declare their preconditions and any invariants they are expected to preserve.

3.3 FNF measurement and relation layer

This layer evaluates:

𝑞
𝑖
(
𝑠
)
=
ln
⁡
𝑚
𝑖
(
𝑠
)
,
𝑃
𝐵
𝑖
(
𝑠
)
=
ln
⁡
𝑚
𝑖
(
𝑠
)
𝐵
𝑖
,

and

𝑅
𝑖
𝑗
(
𝑠
)
=
ln
⁡
𝑚
𝑖
(
𝑠
)
𝑚
𝑗
(
𝑠
)
.

It also supplies classification and balance calculations where the necessary measurements and assumptions are specified.

3.4 Validation gates

Validation gates evaluate whether a state satisfies its required conditions.

The gates may include:

Structural validity.
Magnitude-domain validity.
Transformation consistency.
Classification validity.
Relation preservation.
Balance requirements.
Domain-specific constraints.

Not every gate must apply to every model. The model configuration determines which conditions are mandatory.

3.5 Reasoning engine

The ReasoningEngine explores valid transitions from an initial state.

It evaluates goal predicates, tracks visited states, and returns a successful action sequence when a goal is found within the search limit.

The engine's search strategy is separate from the mathematical definitions used by the bridge.

4. State-Transition Contract

A candidate transition consists of an input state 
𝑠
, an action 
𝑇
, and a candidate output state

𝑠
′
=
𝑇
(
𝑠
)
.

The bridge evaluates the transition in the following order:

Confirm that the action's preconditions are satisfied.
Apply the action to an isolated copy of the input state.
Validate the output state's structural representation.
Validate all required positive measurements.
Evaluate the invariants required by the model.
Evaluate any transition-specific preservation conditions.
Canonicalize the state for duplicate detection.
Enqueue the state if it is admissible and has not already been visited.

If an action fails or produces an invalid state, that candidate transition is rejected.

An action that changes an explicitly preserved invariant is rejected. An action that changes a property not declared invariant may remain valid.

This distinction prevents the bridge from treating every change as a violation.

5. Transformation Bridge

For a valid action 
𝑇
, define the change in a positive measured property as

Δ
𝑖
(
𝑠
,
𝑇
)
=
ln
⁡
𝑚
𝑖
(
𝑇
(
𝑠
)
)
𝑚
𝑖
(
𝑠
)
.

This value measures the change in logarithmic magnitude.

5.1 Relation preservation

For two positive measurements 
𝑥
 and 
𝑦
, a transformation preserves their logarithmic relation when

ln
⁡
𝑇
(
𝑥
)
𝑇
(
𝑦
)
=
ln
⁡
𝑥
𝑦
.

For transformations acting on all positive magnitudes, this condition holds for every pair if and only if

𝑇
(
𝑥
)
=
𝑘
𝑥
,
𝑘
>
0.

Therefore, positive scaling preserves all pairwise logarithmic relations.

Other transformations may preserve specific relations or structural properties without preserving every logarithmic relation.

5.2 Geometric transformations

Rigid rotations and translations of Cartesian coordinates preserve Euclidean distances, assuming the coordinates are transformed consistently.

Consequently, positive bond-length measurements remain unchanged under a rigid transformation:

𝑚
𝑖
(
𝑇
(
𝑠
)
)
=
𝑚
𝑖
(
𝑠
)
.

Their logarithmic measurements are also unchanged:

𝑞
𝑖
(
𝑇
(
𝑠
)
)
=
𝑞
𝑖
(
𝑠
)
.

A uniform positive scaling by 
𝑘
 instead gives

𝑚
𝑖
(
𝑇
(
𝑠
)
)
=
𝑘
 
𝑚
𝑖
(
𝑠
)

for length measurements, and hence

𝑞
𝑖
(
𝑇
(
𝑠
)
)
=
𝑞
𝑖
(
𝑠
)
+
ln
⁡
𝑘
.

These are examples of domain-specific transformation guarantees that can be tested by the bridge.

6. Composition Bridge

Composition combines two or more compatible magnitudes or structures.

For positive magnitudes 
𝑥
,
𝑦
, define multiplicative composition by

𝑥
∘
𝑦
=
𝑥
𝑦
.

The logarithmic representation satisfies

𝑞
(
𝑥
𝑦
)
=
𝑞
(
𝑥
)
+
𝑞
(
𝑦
)
.

For a finite indexed collection,

𝑞
(
∏
𝑖
=
1
𝑛
𝑥
𝑖
)
=
∑
𝑖
=
1
𝑛
𝑞
(
𝑥
𝑖
)
.

In the computational state model, composition may also mean joining graph components or combining compatible structures.

Structural composition and numerical multiplication are distinct operations. The bridge must define the operation appropriate to each data type rather than assuming that every pair of states can be multiplied.

When a composed state includes positive measurements, the FNF measurement layer can evaluate their logarithmic coordinates and relations.

7. Decomposition Bridge

Decomposition separates a state into smaller structures or classification classes.

For a graph-valued state

𝐺
=
(
𝑉
,
𝐸
)
,

removing an edge 
𝑒
∈
𝐸
 produces

𝐺
′
=
(
𝑉
,
𝐸
∖
{
𝑒
}
)
.

The resulting graph may contain more connected components than the original graph.

The decomposition operation should:

Validate that the requested edge exists.
Remove the edge.
Recompute connected components when required.
Preserve the remaining valid vertices and edges.
Apply any domain-specific geometric or structural updates.
Validate the resulting state.

For FNF classification, decomposition may also partition selected elements by their positive magnitudes relative to two boundaries.

Let 
𝐵
1
<
𝐵
2
. Define

𝑆
i
n
=
{
𝑥
:
𝑚
(
𝑥
)
<
𝐵
1
}
,
𝑆
m
i
d
=
{
𝑥
:
𝐵
1
≤
𝑚
(
𝑥
)
≤
𝐵
2
}
,
𝑆
o
u
t
=
{
𝑥
:
𝑚
(
𝑥
)
>
𝐵
2
}
.

These classes form a partition of the measured elements when all their magnitudes are valid and finite.

Graph decomposition and magnitude classification are different operations. A graph can be disconnected without its measurements changing classes, and a classification can change without the graph's connectivity changing.

8. Many & Few Classification Gate

The bridge may use the two-boundary classification function

𝐶
𝐵
1
,
𝐵
2
(
𝑆
)
=
(
𝑆
i
n
,
𝑆
m
i
d
,
𝑆
o
u
t
)
.

For each measured element, its class is determined by comparison with the two positive boundaries.

The gate must ensure that:

Both boundaries are finite and strictly positive.
The boundaries satisfy 
𝐵
1
<
𝐵
2
.
Each measured magnitude is finite and strictly positive.
Every element belongs to exactly one class.
Boundary equality is assigned to the middle class.

A change of coordinate frame preserves classification only when the boundary coordinates are transformed consistently with the measurements.

A transformation that changes measurements while leaving boundaries fixed may legitimately change the classification.

The bridge must not infer that class membership is invariant merely because a transformation is valid.

9. Balance Gate

A balance condition must specify the quantity being balanced, the domain over which it is evaluated, and any required closure or weighting assumptions.

For a finite indexed collection of positive magnitudes, define

𝐿
(
𝐴
)
=
∑
𝑖
=
1
𝑛
ln
⁡
𝑥
𝑖
.

Then

𝐿
(
𝐴
)
=
0
  
⟺
  
∏
𝑖
=
1
𝑛
𝑥
𝑖
=
1.

For a collection closed under reciprocal pairing, with each reciprocal contribution included with matching multiplicity,

ln
⁡
𝑥
+
ln
⁡
(
1
/
𝑥
)
=
0.

Thus the paired logarithmic sum is zero.

The bridge must distinguish this logarithmic balance from:

Equality of the numbers of elements in two classification classes.
Conservation of graph connectivity.
Conservation of physical energy or mass.
Other weighted or domain-specific conservation laws.

These properties are not automatically equivalent.

For infinite collections, the bridge must additionally specify convergence and summation conditions before evaluating a global sum.

10. Invariant and Goal Separation

The ReasoningEngine must distinguish admissibility conditions from goal conditions.

Invariants

An invariant is a property that must hold for every state admitted by the configured model or must be preserved by a specified class of actions.

Examples include:

Finite, valid coordinates.
Valid vertex indices.
No self-edges where prohibited.
Positive magnitudes for logarithmic measurements.
Preservation of a specified relation under a relation-preserving action.
Goals

A goal is a predicate identifying a desired state.

For example,

Goal
⁡
(
𝑠
)
  
⟺
  
(
3
,
4
)
∉
𝐸
(
𝑠
)
.

This predicate states that edge 
(
3
,
4
)
 is absent from the graph.

Removing an edge is a goal in this example, not a universal invariant.

A valid state may fail the goal, and a candidate state may satisfy the goal while still violating another required invariant. The engine must check admissibility independently of goal satisfaction.

11. State Equivalence and Canonicalization

Search efficiency depends on detecting states that should count as equivalent.

Define an equivalence relation

𝑠
1
∼
𝑠
2

according to the semantics of the particular model.

For the equivalence relation to be mathematically well-defined, it must be reflexive, symmetric, and transitive.

The canonicalization function 
𝐾
 should satisfy

𝑠
1
∼
𝑠
2
  
⟹
  
𝐾
(
𝑠
1
)
=
𝐾
(
𝑠
2
)
.

Ideally, the converse should also hold if the canonical representation is intended to characterize equivalence exactly.

For a geometric graph, equivalence might permit a common rigid transformation while preserving graph structure and distances.

Coordinate rounding alone does not guarantee this property. It can merge distinct states or fail to recognize equivalent states represented in different coordinate frames.

If a tolerance-based equivalence is used, its limitations must be documented. Approximate equality is not automatically transitive.

The state key must also include every state property relevant to future actions, invariants, and goals. Otherwise, duplicate detection can incorrectly prune a path that would lead to a valid solution.

12. Search Strategy

The bridge supports breadth-first search as a baseline.

Given an initial state 
𝑠
0
, an action set 
𝐴
, and a goal predicate 
𝐺
, the engine searches for a sequence

𝑠
0
→
𝑇
1
𝑠
1
→
𝑇
2
⋯
→
𝑇
𝑛
𝑠
𝑛

such that every admitted state satisfies the required invariants and

𝐺
(
𝑠
𝑛
)
=
T
r
u
e
.

For a finite branching transition system, breadth-first search finds a shortest action sequence when a goal is reachable and duplicate detection is sound with respect to the chosen state equivalence.

A depth limit restricts the search to paths of bounded length.

The bridge may later support cost-based search, in which actions have nonnegative costs and the engine prioritizes paths by cumulative cost. Cost-based optimization is a search policy, not an FNF mathematical invariant.

13. Reference Adapter Interface

The following interface illustrates the proposed contract.

from typing import Any, Callable, Dict, Protocol


class FrameworkBridge(Protocol):
    def measure(self, state: Any) -> Dict[str, float]:
        """Return named, finite, positive magnitudes."""
        ...

    def validate(self, state: Any) -> bool:
        """Check structural and configured FNF constraints."""
        ...

    def transform(self, state: Any, action: Callable) -> Any:
        """Apply an action and return its candidate state."""
        ...

    def decompose(self, state: Any) -> Any:
        """Return the requested structural or classified decomposition."""
        ...

    def state_key(self, state: Any) -> Any:
        """Return a stable key consistent with state equivalence."""
        ...


The protocol is illustrative. A production implementation should use explicit state types, action contracts, typed measurement definitions, and structured validation results.

The adapter should not silently convert invalid magnitudes into valid ones or conceal failed actions.

14. Integration with the Existing ReasoningEngine

The existing ReasoningEngine already implements several required mechanisms:

A queue for breadth-first exploration.
Action application to cloned states.
An invariant predicate.
Duplicate-state detection.
A maximum search depth.
A goal predicate.
A result object containing the path and search statistics.

The bridge can integrate with these mechanisms by supplying:

A stronger invariant function combining structural validation and configured FNF gates.
A state-key function that follows the model's declared equivalence semantics.
Actions that implement composition, transformation, and decomposition.
Optional transition validators that check properties an action claims to preserve.
Measurement functions for logarithmic relations and classification.

The search engine need not implement the logarithmic mathematics directly. It can delegate these calculations to the bridge.

Likewise, the FNF measurement layer does not need to know how breadth-first search operates.

This separation keeps the mathematical rules independently testable and the search algorithm reusable across different state models.

15. DNA-Like Demonstration

Consider a graph with six vertices and five edges:

𝑉
=
{
0
,
1
,
2
,
3
,
4
,
5
}
,
𝐸
=
{
(
0
,
1
)
,
(
1
,
2
)
,
(
2
,
3
)
,
(
3
,
4
)
,
(
4
,
5
)
}
.

The vertices have Cartesian coordinates

𝑝
𝑖
=
(
𝑖
,
0
,
0
)
,
𝑖
=
0
,
…
,
5.

The target condition is

(
3
,
4
)
∉
𝐸
.

The action set contains:

A rigid rotation or other geometric transformation.
A bond-cleavage operation removing edge 
(
3
,
4
)
.

The structural gate checks coordinate validity and edge indices. The decomposition operation removes the target edge and recomputes connectivity.

Before cleavage, the graph has one connected component. After cleavage, it has two:

𝑉
1
=
{
0
,
1
,
2
,
3
}
,
𝑉
2
=
{
4
,
5
}
.

The graph decomposition is exact for this chain.

If bond lengths are also measured, each length is a positive magnitude and may be evaluated using

𝑞
(
𝑑
𝑖
)
=
ln
⁡
𝑑
𝑖
.

A rigid rotation preserves these measurements. Cleavage changes the edge set but does not, by itself, require the coordinates of the remaining vertices to change.

Any additional displacement introduced to simulate fragment separation is a separate geometric action and should be validated independently.

The engine can therefore search for the target graph state while the bridge verifies structural validity and evaluates the applicable FNF properties.

16. Testing Requirements

An integrated implementation should include tests for the following conditions.

Mathematical properties
𝑞
(
𝑥
𝑦
)
=
𝑞
(
𝑥
)
+
𝑞
(
𝑦
)
 for valid positive inputs.
𝑞
(
1
/
𝑥
)
=
−
𝑞
(
𝑥
)
.
𝑃
𝐵
(
𝑥
)
−
𝑃
𝐵
(
𝑦
)
=
ln
⁡
(
𝑥
/
𝑦
)
.
Positive scaling preserves pairwise logarithmic relations.
Reciprocal pairs cancel in a finite logarithmic sum.
Transformation properties
Rigid transformations preserve Euclidean distances within numerical tolerance.
Uniform scaling changes positive lengths by the expected factor.
A relation-preserving action satisfies its declared preservation conditions.
Invalid transformed magnitudes are rejected.
Classification properties
Every valid measurement belongs to exactly one class.
Boundary values belong to the middle class.
Invalid boundaries are rejected.
Consistent frame shifts preserve classification.
Fixed-boundary transformations may change classification when expected.
Reasoning properties
Invalid initial states are rejected.
Invalid candidate states are not enqueued.
Failed actions do not terminate the entire search.
The target bond-cleavage action reaches the specified goal.
Duplicate detection respects the configured state equivalence.
Search depth limits are respected.
Returned action sequences reproduce the reported final state.

Tests involving floating-point coordinates should use explicit tolerances and should not treat numerical agreement as a proof of exact mathematical equality.

17. Scope and Limitations

The Reasoning Engine Bridge defines an integration contract. It does not, by itself, establish that a particular physical or abstract model is correct.

In particular:

The framework does not automatically supply physical laws for molecular systems.
Positive magnitude measurements must be selected and justified for each domain.
Logarithmic balance is not automatically physical conservation.
Valid transformations need not preserve all measurements or relations.
Decomposition does not necessarily conserve every structural or numerical property.
Search completeness depends on the transition system, search strategy, equivalence rules, and resource limits.
Approximate numerical checks require documented tolerances.

Each implementation must declare its state model, allowed actions, required invariants, goal predicates, measurement functions, and state-equivalence rules.

18. Conclusion

The Reasoning Engine Bridge connects the Finite Number Framework's mathematical representations with a computational system for state-transition reasoning.

The Finite Number Framework supplies logarithmic measurements, relational invariants, boundary-relative classifications, and balance conditions.

The ReasoningEngine supplies action execution, invariant filtering, state exploration, duplicate detection, and goal-directed search.

The bridge makes these systems interoperable without collapsing their distinct responsibilities.

Its central principle is:

Represent each state in its natural domain, apply FNF mathematics to explicitly defined positive magnitudes and relations, and use validated state transitions to reason toward a goal.

Document: docs/reasoning_engine_bridge.md

Framework: Finite Number Framework

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa
