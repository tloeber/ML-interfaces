# High-Level Machine Learning Framework Project

The aim of this project is to develop a comprehensive machine learning framework, functioning as a versatile wrapper around the most popular ML libraries and frameworks. The intention isn't to supplant specific low-level frameworks but to foster greater uniformity among them. The intention is to facilitate interaction with any algorithm, regardless of the underlying ML framework, through the standardized interface.

The envisioned end state isn't a Python package that encapsulates all specific ML frameworks as dependencies and exposes a wrapper around them. Instead, the objective is a reverse dependency flow: Specific ML frameworks will incorporate this Python package as a lightweight dependency. The package will only include standardized interfaces and abstract classes, which the ML frameworks will then implement or subclass.

## The Problem

Traditional ML workflow inefficiencies are addressed as follows:

- **Tight coupling between different components:** Altering ML pipelines for a problem often requires extensive modifications due to the code being highly specific to each model type and library used. This project aims to streamline this process, enabling rapid swapping of components by simply providing a different class, without having to make changes elsewhere in the code.
 
- **Poor separation of abstraction layers:** A lack of clear division of labor among different abstraction levels often leads data scientists and ML engineers spending most of their time handling low-level implementation details. This takes resources away and distracts us from higher-level problems such as model interpretability, monitoring, and more sophisticated deployment techniques.

- **Hard to do automated testing:** Due to the presence of boilerplate code, writing automated tests is neither cost nor time-effective. The scarcity of automatic tests not just increases bugs, but also leads to a slow but steady decline in code quality, and thus maintainability (and thus development velocity) over time. Since deploying ML models to production demands more stringent standards on bug frequency and maintainability, enhancing this area could significantly ease the transition from ML experiments to production deployment.

## Project Goals

- **User-Friendliness:** This project aims to make it effortless for users to get started and promptly generate results. While facilitating quick wins, the project also aspires to allow for continuous workflow refinement without having to migrate to another framework down the line as more specific requirements arise.

- **Simplify Complexity:** This project strives to eliminate [*accidental complexity*](https://en.wikipedia.org/wiki/No_Silver_Bullet#Summary), enabling tackling problems of greater [*inherent complexity*](https://en.wikipedia.org/wiki/No_Silver_Bullet#Summary) (as well as providing faster and cheaper solutions to problems of a given complexity).

## The Solution

The foundation of this project's solution lies in leveraging good object-oriented design, such as [design patterns](https://en.wikipedia.org/wiki/Design_Patterns) or Uncle Bob's [SOLID design principles](https://en.wikipedia.org/wiki/SOLID). While these lessons have long been absorbed in some circles (such as the Java world), these old lessons are unfortunately much less widely followed in the Python world - particularly in the corners of that world where many practitioners have come in from scientific computing, machine learning, etc. 
For example, we can leverage the Liskov-substitution principle and the Strategy Pattern to achieve polymorphism (letting the precise behavior of a method call vary depending on the context). For example, we should be able to swap one estimator with another without making code modifications to other parts of the pipeline.

Note that this object-oriented solution gives us both flexibility and simplicity: The project's design allows the creation of a hierarchy of subclasses, with different behavior implementations per subclass. This approach balances code reuse and allows variations in behavior by subclasses. Additionally, it enables users to override behavior if needed, by providing a custom method implementation or class.

## Side Note

While many popular frameworks employ object-oriented programming, they often fail in implementing good object-oriented design. Python's simplicity is ideally suited for the iterative and experimental workflows characteristic of data analysis and ML. However, as projects grow larger and more complex, features that make other programming languages verbose also offer valuable tools to manage emerging complexity. 

Some argue that Python isn't suitable for production applications, but I contend that the issue isn't Python but the underutilization of Python's optional safeguards (in particular, type hints, static analysis, and one of the various way to mimick interfaces). With Python's combination of readability and the ability to create good application design, this project's way forward is to use (and enforce) of Python's optional safeguards diligently.
