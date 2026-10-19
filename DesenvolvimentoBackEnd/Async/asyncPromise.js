const somar = async (a, b) => a + b;
const imprimir_soma = async (a, b) => {
  let valor = await somar(a, b);
  return "Executado soma. Valor: " + valor;
};

imprimir_soma(2, 2).then((retorno) => console.log(retorno));

const dividir = (a, b) => {
  const promise = new Promise((resolve, reject) => {
    if (b == 0) {
      reject("Divisão por zero");
    } else {
      resolve(a / b);
    }
  });
  return promise;
};

for (let i = 2; i >= -2; i--) {
  dividir(10, i)
    .then((x) => console.log(x))
    .catch((error) => console.log(error));
}
