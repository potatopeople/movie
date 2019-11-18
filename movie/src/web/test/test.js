var b = {
        name: 'wang',
        age: 20,
    }
let anchor = [];
let name = '';

let data = someFunction(b, 20);
function someFunction(obj, value) {
    for (let item in obj) {
        if (typeof (obj[item]) === 'object') {
            name += item+'.'
            someFunction(obj[item],value)
        } else if (typeof (value) === 'number') {
            if (obj[item] === value) {
              anchor.push(name+item)
            }
        } else if (typeof (value) === 'string' && typeof(obj[item]) === 'string') { 
            if (new RegExp(value).test(obj[item])) {
                anchor.push(name+item)
              }
          }
    }
    return anchor
}
console.log(data)