import $fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.resolve(__dirname, "..", "log.txt");

const reader = $fs.createReadStream(filePath, {
  flag: "r",
  encoding: "utf8",
  // onde começa lendo, onde termina e o quanto fica em linha antes de quebrar
  start: 0,
  end: 500,
  highWaterMark: 10,
});

reader.on("data", (chunk) => {
  console.log(chunk);
});
