from .code_block import CodeBlock

async_example = CodeBlock(
    "Async Example",
    """
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}""",
    """
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}""",
)

array_manipulation = CodeBlock(
    "Array Manipulation",
    """
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
const sum = doubledNumbers.reduce((acc, curr) => acc + curr);
console.log('Doubled Numbers:', doubledNumbers);
console.log('Sum:', sum);
""",
    """
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
const sum = doubledNumbers.reduce((acc, curr) => acc + curr, 0);
console.log('Doubled Numbers:', doubledNumbers);
console.log('Sum:', sum);
""",
)

missing_semicolon = CodeBlock(
    "Missing Semicolon",
    """
function sayHello() {
    console.log('Hello, world!')
}
sayHello()
""",
    """
function sayHello() {
    console.log('Hello, world!');
}
sayHello();
""",
)

undefined_variable = CodeBlock(
    "Undefined Variable",
    """
const x = 10;
console.log(x + y);
""",
    """
const x = 10;
const y = 5;
console.log(x + y);
""",
)

dummy_data = {
    async_example.get_id(): async_example,
    array_manipulation.get_id(): array_manipulation,
    missing_semicolon.get_id(): missing_semicolon,
    undefined_variable.get_id(): undefined_variable,
}