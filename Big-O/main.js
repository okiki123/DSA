// Big-O = O(n)
const nemo = ['nemo'];
const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat',
'nigel','squirt', 'darla', 'hank']
const large = new Array(1000).fill('nemo')
function findNemo (array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!!')
        }
    }
}

findNemo(large);

//Big-O = O(1)
const boxes = [0,1,2,3,4,5]
function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]);
    console.log(boxes[1]);
}


// Big-O rule
function comopressBoxesTwice(boxes, boxes2) {
    boxes.forEach(function(boxes) {
        console.log(boxes);
    })

    boxes2.forEach(function(boxes) {
        console.log(boxes);
    })
}

//Big-O = O(n^2)
const box = [1,2,3,4,5];

function logAllPairs(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            console.log(array[i], array[j])
        }
    }
}

logAllPairs(box)