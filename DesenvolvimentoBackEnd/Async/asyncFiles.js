const $fs = require("fs"); // nao async
const $fspromise = require("fs/promises"); // async
const $path = require('path');
const filePath = $path.resolve(__dirname, '..', 'log.txt'); 

$fs.appendFile("log.txt", `Escrito em ${new Date()}\n`, "utf8", (err) => {
  if (err) throw err;
  console.log("Linha adicionada");
});

async function leitura() {
  try {
    const data = await $fspromise.readFile(filePath, { encoding: "utf8" });
    console.log(data);
  } catch (err) {
    console.log("Erro:", err);
  }
}

leitura();
