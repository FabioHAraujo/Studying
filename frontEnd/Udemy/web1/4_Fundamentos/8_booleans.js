let isAtivo = false;
console.log(isAtivo);

isAtivo = true;
console.log(isAtivo);

isAtivo = 1;
console.log(!!isAtivo);

isAtivo = 0;
console.log(!!isAtivo);

console.log("Os verdadeiros...");
console.log(!!3);
console.log(!!-1);
console.log(!!" ");
console.log(!![]);
console.log(!!{});
console.log(!!Infinity);
console.log(!!(isAtivo = true));
console.log(!!(isAtivo = Infinity));
console.log(!!(isAtivo = 1));

console.log("Os falsos...");
console.log(!!0);
console.log(!!"");
console.log(!!null);
console.log(!!NaN);
console.log(!!undefined);
console.log(!!(isAtivo = false));

console.log("pra finalizar...");
console.log(!!("" || undefined || 0 || false || NaN || 123));
console.log("" || undefined || 0 || false || NaN || 123);

let nome = "";
console.log(nome || "Desconhecido");

nome = "Fabio";
console.log(nome || "Desconhecido");
