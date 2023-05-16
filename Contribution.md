   ______            __       _ __          __  _                 
  / ____/___  ____  / /______(_) /_  __  __/ /_(_)___  ____  _____
 / /   / __ \/ __ \/ __/ ___/ / __ \/ / / / __/ / __ \/ __ \/ ___/
/ /___/ /_/ / / / / /_/ /  / / /_/ / /_/ / /_/ / /_/ / / / (__  ) 
\____/\____/_/ /_/\__/_/  /_/_.___/\__,_/\__/_/\____/_/ /_/____/  
                                                                  


## [Git Commit Patterns](https://dev.to/hornet_daemon/git-commit-patterns-5dm7)

CRUD Operation Conventions??

**Type**: What are the types of commits

> The type is responsible for telling us what change or iteration is being made, from the convention rules, we have the following types:

    test: indicates any type of creation or alteration of test codes.

    update: updating the file structure not the code

    fix: used when correcting errors that are generating bugs in the system.
    Example: Apply a handling for a function that is not behaving as expected and returning an error.

    docs: used when there are changes in the project documentation.
    Example: add information in the API documentation, change the README, etc.

    revert: indicates the reversal of a previous commit.
