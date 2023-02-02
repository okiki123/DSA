//Example 1 
const array1 = ['a', 'b', 'c', 'x'];
const array2 = ['z', 'y', 'x'];

function containsCommonItems(arr1, arr2) {
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) {
                return true;    
            }
        }
    }
    return false;
}

console.log(containsCommonItems(array1, array2));

function containsCommonItems2(arr1, arr2) {
    let map = {};
    for (let i = 0; i < arr1.length; i++) {
        if(!map[arr1[i]]) {
            const item = arr1[i];
            map[item] = true;
        }
    }

    for (let j = 0; j < arr2.length; j++) {
        if (map[arr2[j]]) {
            return true;
        }
    }
    return false;
}

console.log(containsCommonItems2(array1, array2));

// Arrays .................
const strings = ['a', 'b', 'c', 'd'];

//push
strings.push('e') // O(n)

//pop
strings.pop() //O(1)

//unshift
strings.unshift('x'); // 0(n)

//Classes in Javascript
class Player {
    constructor(name, type) {
        this.name = name;
        this.type = type;
    }
    introduce() {
        console.log(`Hi i am ${this.name}, i am a ${this.type}`)
    }
}

class Wizard extends Player {
    constructor(name, type) {
        super(name, type)
    }
    play() {
        console.log(`I am a ${this.type}`)
    }
}

const wizard1 = new Wizard('Shally', 'Healer');
const wizard2 = new Wizard('Shawn', 'Dark Magic');
console.log(wizard1.play())

//Implementing an Array
class myArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }
    get(index) {
        return this.data[index];
    }
    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }
    pop() {
        const lastItem = this.data[this.length - 1];
        delete this.data[this.length - 1];
        this.length--;
        return lastItem;
    }
    delete(index) {
        const item = this.data[index];
        this.shiftItems(index);
    }
    shiftItems(index) {
        for (let i = index; i < this.length -1; i++) {
            this.data[i] = this.data[i + 1];
        }
    } 
}

const newArray = new myArray;
newArray.push('1');
console.log(newArray);

//Create a function that Reverse a string

function reverse(str) {
    //check input
    if(!str || str.length < 2 || typeof str !== 'string') {
        return 'Not reversible'
    }
    const backwards = []
    return backwards.join();

}
function reverse(str) {
    //check input
    if(!str || str.length < 2 || typeof str !== 'string') {
        return 'Not reversible'
    }
    const backwards = []
    return backwards.join();

}





