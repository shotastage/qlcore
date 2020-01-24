# CATP Environment Class



## Basic Flow



- **1. Initialize Environment**

  First. we create `CATPEnvironment` class instance to initialize environment.

- **2. Memory agent act flow**

  If the finished initializing environment, register agent action flow and memory.

- **3. Commit and build environment**

  A interval of agent actions has been acted or registred, you can commit environment by `commit()` method.

  This method caluclate environment differences of acted before and after and then, 
