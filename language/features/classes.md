## Classes
Your programming language supports object-oriented programming with classes and objects.

Example:
```class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        print("Hello, my name is " + this.name);
    }
}

var person = new Person("Alice", 25);
person.greet();
