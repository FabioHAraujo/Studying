let num1 = 1;
let num2 = 2;

console.log(num1);
num1++;
console.log(num1);
--num1;
console.log(num1);
++num1;
console.log(num1);
num1--;
console.log(num1);

console.log(++num1 === num2--); // vai dizer que são iguais, mesmo sendo diferentes, pois na hora da comparação eles são iguais, já que o num1,
// é incrementado antes de ser comparado, mas o num2 só é decrementado depois.
console.log(num1 === num2);
