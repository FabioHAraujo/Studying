console.log(Math.ceil(6.1));

const obj1 = {};
obj1.nome = "Pedro";
obj1["idade"] = 18;

console.log(obj1.nome);
console.log(obj1.idade);

function Obj(nome) {
    this.nome = nome;
    this.exec = function () {
        console.log("Exec...");
    };
}

const obj2 = new Obj("Cadeira");
const obj3 = new Obj("Mesa");
console.log(obj2);
console.log(obj3);
obj3.exec();
